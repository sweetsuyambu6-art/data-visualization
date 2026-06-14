import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt




filter_package = st.set_page_config(page_title="stock value", page_icon="📈",layout="wide")
df= pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\_csv\unique_tickers.csv")
df1 = pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\_csv\Sector_data - Sheet1.csv")
df2 = pd.read_csv(r"C:\Users\velku\Downloads\New folder\DS\project\_csv\combined2_data.csv")

#green stock*red stock
st.subheader("Top & Downfalling Stocks ")    
col1,col2=st.columns(2)
with col1:
  st.title('Top gaining')
  top= df2.groupby(['Ticker',"month"])[["open","high","volume","close"]].max().sort_values(by="close", ascending=False)
  close_price=df2['close'].sum()
  price_return=df2['close']-df2['close']/df2['close']
  st.dataframe(top)
with col2:
  st.title('Downfall Lossing')
  close_price=df2['close'].sum()
  price_return=df2['close']-df2['close']/df2['close']
  downfall = df2.groupby(['Ticker',"month"])[["open","high","volume","close"]].min().sort_values(by="close", ascending=True)
  st.dataframe(downfall)

#sector select
st.header("Sector Wise Company")
selected_sector = st.selectbox("Select Sector", ["ALUMINIUM", "AUTOMOBILES", "BANKING", 
                                                 'CEMENT', 'DEFENCE', 'ENERGY',
                                                 'ENGINEERING', 'FINANCE', 'FMCG', 'FOOD & TOBACCO',
                                                 'INSURANCE', 'MINING', 'MISCELLANEOUS',
                                                 'PAINTS', 'PHARMACEUTICALS', 'POWER', 'RETAILING',
                                                  'SOFTWARE', 'STEEL', 'TELECOM','TEXTILES'])
if selected_sector:
  filtered_df = df1[df1['sector'].isin([selected_sector])]
  st.subheader(f"Data for {selected_sector} Sector")
  st.dataframe(filtered_df) 
  st.subheader(f"Stock Price Trends for {selected_sector} Sector")
 
#name replace it of ticker for mapping 
col1, col2 = st.columns(2)
with col1:
  return_price = (df2['close'].max() - df2['close'].min())
  selected = df[df['Ticker'].isin(filtered_df['COMPANY'])]
  fig = px.bar(selected, x='date', y='close', color='Ticker', title=f'{selected_sector} Sector Stock Price Trends')
  st.plotly_chart(fig)

with col2:
  return_price = (df['close'].max() - df['close'].min())
  selected = df[df['Ticker'].isin(filtered_df['COMPANY'])]
  fig = px.scatter(selected, y='close', x='date',color="close",color_continuous_scale="reds",title=f'{selected_sector} Sector Stock Price Trends')
  st.plotly_chart(fig)


#dataframe table
st.columns(2)
column1, column2 = st.columns(2)
#corr
with column1:
    st.title('Define a custom')
    df2=pd.DataFrame.corr(df2,numeric_only=True)
    plt=sns.heatmap(df2,cmap="coolwarm",annot=True,fmt=".2f",linewidths=.5)
    st.pyplot()
#return_price   
with column2:
  filtered_df2 = df[df['Ticker'].isin(filtered_df['COMPANY'])]
  filtered_df2['return_price'] = (filtered_df2['close'] - filtered_df2['close'].shift(1)) / filtered_df2['close'].shift(1)
  st.dataframe(filtered_df2[['Ticker','close','date', 'return_price']])


# # monthly
# st.title('monthly')
# df2=pd.DataFrame(df2)
# group_frame=df2.groupby(['Ticker','month','close']).agg({'close':['max','count',"sum"],'Ticker':['max','count','sum']})
# group_frame


# import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly.express as xp

# columns1,column2=st.columns(2)
# with column1:
#   st.title('heatmap')
#   df2=pd.DataFrame.corr(df2,numeric_only=True)
#   plt=sns.heatmap(df2,cmap="coolwarm",annot=True,fmt=".2f",linewidths=.5)
#   st.pyplot()
# with column2:
#   st.subheader("Define a custom colorscale")
#   df2=pd.DataFrame.corr(df2,numeric_only=True)
#   # fig, ax = plt.subplots()
#   df2 = df2.reset_index()
#   fig = px.scatter(df2,x="close",y="Ticker",color="close",color_continuous_scale="reds")
#   st.plotly_chart(fig)

#dataframe table
 # st.subheader(f"Selected Companies in {selected_sector} Sector")
 # return_price = sum((df['close'] - df['close'].shift(1)) / df['close'].shift(1))
 # st.write(f"Total Return for {selected_sector}")
 # df1['Sector_Return'] = f"{return_price:.2f}%"
 # st.dataframe(df1[df1['sector'] == selected_sector][['COMPANY', 'Sector_Return']])
  
#correlation coefficient 


# selected_company = st.selectbox("Select Company for Correlation Heatmap", df['Ticker'].unique())
# if selected_company:
#     filtered_df = df2[df2['Ticker'] == selected_company]
#     pearson_corr = df2.corr(method='pearson')
#     print(pearson_corr)
#     #sns.heatmap(pearson_corr, annot=True, cmap='coolwarm')
#     plt.title("Pearson Correlation Heatmap")
#     df=pd.DataFrame(pearson_corr, columns=[f"{selected_company}"])
#     st.subheader(f"Correlation Heatmap of Closing Prices for {selected_company}")
#     plt = sns.heatmap(pearson_corr, annot=True, cmap='coolwarm', 
#                             title=f'Correlation Heatmap of Closing Prices for {selected_company}')
#     st.pyplot(plt)



    #df=pd.DataFrame(df2['close'],columns=[f"{selected_company}"])
    #t.subheader(f"Correlation Heatmap of Closing Prices for {selected_company}")
    #fig = px.density_heatmap(closing_prices, x=closing_prices, y=closing_prices, 
     #                       color_continuous_scale='Viridis',
      #                      title=f'Correlation Heatmap of Closing Prices for {selected_company}')
    #st.plotly_chart(fig)

    
#closing_prices = pd.DataFrame.corr(df2[['close']])
#st.subheader("Correlation Heatmap of Closing Prices")
#fig = px.imshow(closing_prices, x=selected_company.columns, y=closing_prices.columns, color_continuous_scale='Viridis', title='Correlation Heatmap of Closing Prices')
#st.plotly_chart(fig)  
#df=px.density_heatmap(df,x="close",y="Ticker",title="Correlation Heatmap")
#st.plotly_chart(df)


#df['close'].corr(df['Ticker'])