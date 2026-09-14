import streamlit as st
import pandas as pd

# Configuration du dashboard
st.set_page_config(
    page_title="Marketing SMD",
    layout="wide"
)

st.title("📊 Analyse Marketing SMD")

# Charger les données
customers = pd.read_csv(
    "data/raw/customers_data.csv"
)

sales = pd.read_csv(
    "data/raw/sales_data.csv"
)

marketing = pd.read_csv(
    "data/raw/marketing_data.csv"
)

# Calcul du revenu
sales["Revenue"] = (
    sales["Quantity"] *
    sales["Sale_Price"]
)

# KPI
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Clients",
    len(customers)
)

col2.metric(
    "Ventes",
    len(sales)
)

col3.metric(
    "Quantité vendue",
    sales["Quantity"].sum()
)

col4.metric(
    "Revenu",
    f"{sales['Revenue'].sum():.2f}"
)

st.divider()

# Afficher les campagnes
st.subheader("Performance des campagnes")

marketing["CTR"] = (
    marketing["Clicks"] /
    marketing["Impressions"]
) * 100

marketing["Conversion_Rate"] = (
    marketing["Conversions"] /
    marketing["Clicks"]
) * 100

st.dataframe(marketing)