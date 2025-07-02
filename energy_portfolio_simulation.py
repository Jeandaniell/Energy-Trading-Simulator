
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Charger les données horaires de charge (proxy pour la demande)
load_df = pd.read_csv("monthly_hourly_load_values_2025.csv")

# Nettoyage
load_df["DateTime"] = pd.to_datetime(load_df["DateUTC"], format="%d-%m-%Y %H:%M")
load_df = load_df[["DateTime", "CountryCode", "Value"]]
load_df = load_df[load_df["CountryCode"] == "FR"]  # Focus sur la France
load_df = load_df.sort_values("DateTime").reset_index(drop=True)

# 2. Générer des prix spot simulés (corrélés à la demande avec du bruit)
np.random.seed(42)
base_price = 50  # €/MWh
load_df["Price"] = base_price + 0.05 * load_df["Value"] + np.random.normal(0, 5, size=len(load_df))

# 3. Simuler un portefeuille d'achat de 10 MWh toutes les heures
load_df["Position_MWh"] = 10  # Achat de 10 MWh toutes les heures
load_df["PnL"] = load_df["Position_MWh"] * (load_df["Price"].diff().fillna(0))  # Variation de prix x position

# 4. Calcul de la VAR historique (rolling window)
window_size = 24 * 7  # une semaine glissante
load_df["VAR_95"] = load_df["PnL"].rolling(window=window_size).quantile(0.05)
load_df["VAR_99"] = load_df["PnL"].rolling(window=window_size).quantile(0.01)

# 5. Stress test : choc +30% sur les prix
load_df["Stress_Price"] = load_df["Price"] * 1.3
load_df["Stress_PnL"] = load_df["Position_MWh"] * (load_df["Stress_Price"] - load_df["Price"])

# 6. Exporter les résultats
output_dir = "energy_trading_output"
os.makedirs(output_dir, exist_ok=True)
load_df.to_csv(f"{output_dir}/simulated_portfolio.csv", index=False)

# Affichage graphique
plt.figure(figsize=(12, 5))
plt.plot(load_df["DateTime"], load_df["PnL"], label="PnL")
plt.plot(load_df["DateTime"], load_df["VAR_95"], label="VaR 95%", linestyle='--')
plt.plot(load_df["DateTime"], load_df["VAR_99"], label="VaR 99%", linestyle='--')
plt.title("PnL et VAR Historique")
plt.xlabel("Date")
plt.ylabel("€")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{output_dir}/pnl_var_plot.png")
