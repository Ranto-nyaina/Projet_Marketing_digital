import pandas as pd

def test_customers_not_empty():
    # Vérifie que le fichier clients contient des données
    df = pd.read_csv("data/raw/customers_data.csv")
    assert len(df) > 0

def test_sales_columns():
    # Vérifie les colonnes importantes
    df = pd.read_csv("data/raw/sales_data.csv")
    assert "Customer_ID" in df.columns
    assert "Product_ID" in df.columns