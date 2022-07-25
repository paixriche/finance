import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from stockHelper import *
from indicesHelper import *




st.write("# Norwegian Seafood Sector")

st.write("### Biggest company stock price dev - Mowi")
df_mowi_dev = get_stock_price_dev("MOWI.OL", period="ytd")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df_mowi_dev.index, y=df_mowi_dev.iloc[:, 0], name="Mowi", line_color="blue"))
fig.update_layout(
    title="Price Development of Mowi",
    xaxis_title="Date",
    yaxis_title="Stock Price",
    legend_title="Stock"
)

st.plotly_chart(fig, use_container_width=True)

st.write("### (Homemade) Indices for the Norwegian Seafood Sector")
st.write("Based on yFinance, however the data is somewhat incorrect.")

norway_seafood_tickers = ['AKBM.OL', 'ASA.OL', 'AUSS.OL', 'BAKKA.OL', 'GSF.OL', 'LSG.OL', 'MOWI.OL', 'NRS.OL']

df_index_price_weighted = create_price_weighted_index(norway_seafood_tickers, base=100, period='ytd')
df_index_market_weighted = create_market_weighted_index(norway_seafood_tickers, base=100, period='ytd')
df_index_equal_weighted = create_equal_weighted_index(norway_seafood_tickers, base=100, period='ytd')

fig = go.Figure()

fig.add_trace(go.Scatter(x=df_index_price_weighted.index, y=df_index_price_weighted.iloc[:, 0], name="Price Weighted", line_color="blue"))
fig.add_trace(go.Scatter(x=df_index_market_weighted.index, y=df_index_market_weighted.iloc[:, 0], name="Market Weighted", line_color="red"))
fig.add_trace(go.Scatter(x=df_index_equal_weighted.index, y=df_index_equal_weighted.iloc[:, 0], name="Equal Weighted", line_color="green"))

fig.update_layout(
    title="Indices for Norwegian Seafood Sector",
    xaxis_title="Date",
    yaxis_title="Value",
    legend_title="Index Type"
)

st.plotly_chart(fig, use_container_width=True)



