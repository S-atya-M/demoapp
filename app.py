import yfinance as yf
import streamlit as st
import pandas as pd
from PIL import Image

st.write(""" # Stock Market Web App	
Shown are the stocks **closing price** and **volume**    \n
**Visually** show data on a stock!	
""")

# need a cool image
image = Image.open("stockIMG.jpg")
st.image(image, use_column_width=True)


#create a sidebar header
st.sidebar.header('User Input')

#create a funtion to get the user Input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2010-01-02")
    end_date = st.sidebar.text_input("End Date", "2020-08-04")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AAPL")  # Default symbol is AAPL (Apple Inc.)
    return start_date, end_date, stock_symbol

# Get the user's input
startDate, endDate, symbol = get_input()

try:
    # Get data on the ticker
    tickerData = yf.Ticker(symbol)
    
    # Get the historical prices for the ticker
    tickerDf = tickerData.history(period='1d', start=startDate, end=endDate)
    
    # Display the closing price and volume in line charts
    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
    
except Exception as e:
    st.error(f"An error occurred: {e}")