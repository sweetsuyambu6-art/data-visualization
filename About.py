import streamlit as st
import pandas as pd
import plotly.express as px




about_package = st.set_page_config(page_title="stock value", page_icon="📈",layout="wide")

#data Previw
df2 = pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\_csv\combined01_data.csv")
df = pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\_csv\Sector_data - Sheet1.csv")

#per day return
st.header("per day return")
selected_company = st.selectbox("Select Company", df2['Ticker'])
filtered_df = df2[df2['Ticker'] == selected_company]
price_return=df2['close']-df2['close']/df2['close']
st.dataframe(filtered_df[['date', 'Ticker', 'open','close']])

#top_10_volatile_green_stocks 

st.subheader("Top 10 Volatile Green Stocks")    
close_price=df2['close'].sum()
price_return=df2['close']-df2['close']/df2['close']
max_close = df2.groupby("Ticker")[["open","high","close","date","volume"]].max().sort_values(by="close", ascending=False)
st.dataframe(max_close)

#top_10_volatile_green_stocks 

st.markdown("### Close Price Range for Top 3 Volatile Stocks")
MARUTI,BAJAJ_AUTO,ULTRACEMCO,BAJFINANCE,APOLLOHOSP = st.columns(5)
MARUTI.metric(label="MARUTI", value=df2[df2['Ticker']=="MARUTI"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_arrow="up")
BAJAJ_AUTO.metric(label="BAJAJ-AUTO", value=df2[df2['Ticker']=="BAJAJ-AUTO"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_arrow="up")
ULTRACEMCO.metric(label="ULTRACEMCO", value=df2[df2['Ticker']=="ULTRACEMCO"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_arrow="up")
BAJFINANCE.metric(label="BAJFINANCE", value=df2[df2['Ticker']=="BAJFINANCE"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_arrow="up")
APOLLOHOSP.metric(label="APOLLOHOSP", value=df2[df2['Ticker']=="APOLLOHOSP"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_color="off",delta_arrow="up")


#toppp_10_volatile_loss_stocks

st.subheader("Top 10 Volatile Loss Stocks")
close_price=df2['close'].sum() 
close_price_return = (df2['close'] - df2['close'].shift(1)) / df2['close'].shift(1)
min_close = df2.groupby("Ticker")[["open","high","close","date","volume"]].min().sort_values(by="close", ascending=True)
st.dataframe(min_close)


#top_10_volatile_loss_stocks

st.markdown("### Close Price Range for Top 3 Volatile Stocks")
TATASTEEL,BEL,BPCL,ONGC,POWERGRID = st.columns(5)  
TATASTEEL.metric(label="TATASTEEL", value=df2[df2['Ticker']=="TATASTEEL"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_color="inverse",delta_arrow="down")
BEL.metric(label="BEL", value=df2[df2['Ticker']=="BEL"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_color="inverse",delta_arrow="down")
BPCL.metric(label="BPCL", value=df2[df2['Ticker']=="BPCL"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_arrow="up")
ONGC.metric(label="ONGC", value=df2[df2['Ticker']=="ONGC"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_color="off",delta_arrow="up")
POWERGRID.metric(label="POWERGRID", value=df2[df2['Ticker']=="POWERGRID"]['close'].iloc[0],delta=df2['close'].max()-df2['close'].min(),delta_color="off",delta_arrow="up")

col1,col2=st.columns(2)
with col1:
#data vistualization
    MARUTI,BAJAJ_AUTO,ULTRACEMCO,BAJFINANCE,TRENT = st.columns(5)
    st.subheader("Top 5 Stock Price Trends")

    selected_company = st.selectbox("Select Company",["MARUTI",'BAJAJ-AUTO','ULTRACEMCO','BAJFINANCE','TRENT'])
    filtered_df = df2[df2['Ticker'] == selected_company]
    if selected_company in df2['Ticker'].unique():
        return_price = df2['close'] - df2['close'] / df2['close'] 
        fig = px.line(filtered_df, x='date', y='close', title=f'{selected_company} Stock Price Over Time')
        st.plotly_chart(fig)
    
with col2:  
#price range
    st.header("Price Range Of The Stocks")
    company = st.selectbox("Select Company",df2['Ticker'],key="company")
    filtered_df = df2[df2['Ticker'] == company]
    total_close_price = df2['close'].sum() 
    close_price = df2['close'].max() - df2['close'].min()
    st.dataframe(filtered_df[['date', 'Ticker', 'open','close']])




