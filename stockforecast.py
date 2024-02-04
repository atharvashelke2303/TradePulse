import streamlit as st
from datetime import date
import subprocess
subprocess.run(["pip", "install", "yfinance==0.2.31"])
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")
stocks = ("RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","SBIN.NS","ICICIBANK.NS","LT.NS","ADANIPORTS.NS","BAJFINANCE.NS",
          "M&M.NS","ASIANPAINT.NS","BAJAJ-AUTO.NS","TITAN.NS","KOTAKBANK.NS","BHARTIARTL.NS","ITC.NS","SUNPHARMA.NS","HINDUNILVR.NS","TATAMOTORS.NS","TATAPOWER.NS")
selected_stocks = st.selectbox("Select dataset for prediction",stocks)

n_years = st.slider("Years of prediction:",1,6)
period = n_years * 365

@st.cache_data

def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data...")
data = load_data(selected_stocks)
data_load_state.text("Loading data...done!")

st.subheader("Raw data")
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'], name = 'stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'], name = 'stock_open'))
    fig.layout.update(title_text="Time Series Data",xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    
plot_raw_data()

#Forecasting by using Facebook prophet
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date":"ds","Close":"y"})
