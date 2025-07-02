# Energy-Trading-Simulator
# ⚡ Simulation d’un Portefeuille de Trading Énergie (Électricité - France)

Ce projet simule la gestion d’un portefeuille de trading sur le marché de l’électricité en France à partir de données horaires réelles de charge (proxy pour la demande). Il inclut les calculs de PnL, VAR, stress tests et une visualisation des risques de marché.

## 📊 Objectif

- Simuler une position constante sur le marché de l’électricité (achat de 10 MWh/heure)
- Générer des prix spot simulés à partir des données de charge
- Calculer les profits et pertes (PnL) horaires
- Estimer la Value at Risk (VaR) historique à 95% et 99%
- Réaliser un stress test sur un choc de +30% des prix

## 🗂 Données utilisées

- `monthly_hourly_load_values_2025.csv` : données horaires de charge en France (extrait de données ENTSO-E)

## 🧮 Méthodologie

1. Génération de prix spot simulés : `Price = 50 + 0.05 × Load + bruit`
2. Calcul du PnL horaire : `PnL = Position × ΔPrice`
3. Estimation de la VaR (rolling window de 7 jours)
4. Stress test : augmentation de 30% des prix simulés
5. Export CSV des résultats et graphique PnL/VAR

## 📦 Structure du projet

```
energy_portfolio_simulation.py        # Script principal
monthly_hourly_load_values_2025.csv  # Données de charge (à placer dans le même dossier)
energy_trading_output/
├── simulated_portfolio.csv          # Résultats complets
├── pnl_var_plot.png                 # Visualisation PnL / VaR
```

## 📌 Résultats

- Visualisation de la performance (PnL) et du risque (VAR)
- Capacité à simuler et surveiller un portefeuille électrique simple
- Projet facilement étendable à d'autres produits (futures, options) ou marchés (gaz, émissions)

## 🛠️ Technologies utilisées

- Python 3
- pandas, numpy
- matplotlib
- scikit-learn (pour usage futur éventuel de modèles prédictifs)

## 👨‍💻 Auteur

Jean Daniel HOUSSOU  
[LinkedIn](https://www.linkedin.com/in/jean-daniel-houssou-b56961208/)  
[GitHub](https://github.com/Jeandaniell)

---
