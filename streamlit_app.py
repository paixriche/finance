import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from stockHelper import *




st.write("# Norwegian Seafood Sector")

st.write("### Biggest company stock price dev - Mowi")
df_mowi_dev = get_stock_price_dev("MOWI.OL", period="ytd")

# fig = go.Figure()
# fig.add_trace(go.Scatter(x=df_mowi_dev.index, y=df_mowi_dev.iloc[:, 0], name="Mowi", line_color="blue"))
# fig.update_layout(
#     title="Price Development Mowi",
#     xaxis_title="Date",
#     yaxis_title="Stock Price",
#     legend_title="Stock"
# )
# fig.show()
st.line_chart(df_mowi_dev)





