import pandas as pd

# load the data
control = pd.read_csv('data/BarredecontroleKorea.csv')
df = control.rename(columns={'TradeValue in 1000 USD': 'Value'}).groupby(['ProductCode', 'PartnerISO3','PartnerName','Year']).Value.sum().reset_index()
df = df.fillna(0)
# create a list of countries
countries = df.PartnerName.unique()

# create a list of products
products = df.ProductCode.unique()

# create a list of years
years = df.Year.unique()