# 📊 Analyse et Optimisation Marketing basée sur la Segmentation Client

> Projet pédagogique — **Stratégie Marketing Digital (SMD)**

## 🎯 Présentation

Ce projet vise à exploiter les données **clients, produits, ventes et campagnes marketing** afin de mieux comprendre les comportements d'achat, segmenter les clients et proposer une stratégie marketing personnalisée.

Le projet combine **Data Science, Machine Learning et visualisation interactive**.

## 🎯 Objectifs

* Explorer et nettoyer les données.
* Analyser les comportements d'achat.
* Segmenter les clients avec **K-Means**.
* Visualiser les segments avec **PCA**.
* Construire des profils clients.
* Analyser les performances des campagnes marketing.
* Calculer les principaux KPI.
* Proposer une stratégie marketing personnalisée.
* Développer un dashboard interactif avec **Streamlit**.
* Étudier la faisabilité d'une prédiction du churn ou de la CLV.

## 🛠️ Technologies

| Domaine                  | Outils                                |
| ------------------------ | ------------------------------------- |
| Langage                  | Python 3                              |
| Analyse                  | Pandas, NumPy                         |
| Visualisation            | Matplotlib, Seaborn                   |
| Machine Learning         | Scikit-learn                          |
| Segmentation             | K-Means                               |
| Réduction dimensionnelle | PCA                                   |
| Dashboard                | Streamlit                             |
| Environnement            | Jupyter Notebook, Virtual Environment |
| Versionnement            | Git, GitHub                           |

## 📁 Structure

```text
marketing-smd/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_customer_segmentation.ipynb
│   ├── 03_marketing_analysis.ipynb
│   └── 04_ml_prediction.ipynb
│
├── src/
├── dashboard/
│   └── app.py
├── models/
├── reports/
├── presentation/
├── tests/
│   └── test_data.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone <URL_DU_REPOSITORY>
cd marketing-smd
```

### 2. Créer l'environnement virtuel

```bash
python3 -m venv .venv
```

### 3. Activer l'environnement

```bash
source .venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5. Vérifier l'installation

```bash
python -c "import pandas, numpy, sklearn, streamlit; print('Environnement OK')"
```

Résultat attendu :

```text
Environnement OK
```

## 🚀 Utilisation

### Analyse exploratoire

Ouvrir :

```text
notebooks/01_data_exploration.ipynb
```

Cette étape permet de :

* charger les datasets ;
* vérifier les données ;
* rechercher les valeurs manquantes ;
* rechercher les doublons ;
* nettoyer les données ;
* créer les premières visualisations.

### Segmentation client

Ouvrir :

```text
notebooks/02_customer_segmentation.ipynb
```

Méthodes utilisées :

```text
StandardScaler
K-Means
PCA
```

Résultats :

```text
data/processed/customer_features.csv
data/processed/customer_segments.csv
```

### Analyse marketing

Ouvrir :

```text
notebooks/03_marketing_analysis.ipynb
```

KPI calculés :

```text
CTR
Conversion Rate
CPC
CPA
```

Résultat :

```text
data/processed/marketing_kpis.csv
```

### Machine Learning

Ouvrir :

```text
notebooks/04_ml_prediction.ipynb
```

Cette partie étudie la faisabilité d'un modèle de **churn / CLV**.

> ⚠️ Les données fournies sont très petites et ne contiennent pas de variable `Churn`. Une prédiction supervisée fiable ne peut donc pas être évaluée correctement avec ce dataset.

## 📊 Dashboard

Lancer :

```bash
streamlit run dashboard/app.py
```

Le dashboard présente notamment :

* nombre de clients ;
* nombre de ventes ;
* quantité vendue ;
* revenu calculé ;
* performances des campagnes ;
* KPI marketing ;
* segmentation client.

## 🧪 Tests

Installer pytest si nécessaire :

```bash
pip install pytest
```

Lancer les tests :

```bash
python -m pytest
```

## 📈 Résultats

Le projet produit :

* une segmentation des clients ;
* un profil des segments ;
* une analyse des campagnes ;
* des KPI marketing ;
* une stratégie marketing personnalisée ;
* un dashboard interactif.

## ⚠️ Limites

Les principales limites sont :

* très petit nombre de clients ;
* nombre limité de transactions ;
* absence de variable `Churn` ;
* absence de revenu directement attribué aux campagnes ;
* ROI financier non calculable correctement ;
* segmentation K-Means principalement démonstrative.

Ces limites sont prises en compte dans l'interprétation des résultats.

## 🔮 Perspectives

Pour une version plus avancée :

* utiliser un dataset plus important ;
* ajouter l'historique des achats ;
* ajouter les interactions digitales ;
* ajouter les revenus par campagne ;
* construire une vraie variable `Churn` ;
* entraîner plusieurs modèles ML ;
* utiliser MLflow ;
* conteneuriser avec Docker ;
* automatiser avec GitHub Actions.

## 🔄 Workflow

```text
Données
   ↓
Exploration
   ↓
Nettoyage
   ↓
Fusion
   ↓
Feature Engineering
   ↓
Segmentation
   ↓
Profilage
   ↓
Analyse Marketing
   ↓
Stratégie
   ↓
Dashboard
   ↓
Tests
   ↓
Rapport + Présentation
```

## 📦 Livrables

* Rapport final Word/PDF
* Présentation PowerPoint
* Code source
* Notebooks
* Dashboard Streamlit
* README
* Résultats de segmentation
* Analyse des campagnes
* Repository GitHub
