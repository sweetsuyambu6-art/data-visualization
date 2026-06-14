import streamlit as st
import pandas as pd


about_package = st.set_page_config(page_title="Dash Bord", page_icon="🏠",layout= "wide")
about_package = st.set_page_config(page_title="Summery", page_icon="🏠")
st.title("Volatile Stocks Analysis Dashboard")

#Select Filter
df1 = pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\_csv\combined2_data.csv")
filter_options = st.selectbox("Select Filter", df1['Ticker'].unique())
if filter_options:
    company_data = df1[df1['Ticker'] == filter_options]
    st.subheader(f"Data for {filter_options}")
    st.dataframe(company_data)


