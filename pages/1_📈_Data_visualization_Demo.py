import streamlit as st 
import pandas as pd
import plotly.express as px 
import numpy as np 

@st.cache_data
def load_data(file):
  return pd.read_csv(file)

file=st.file_uploader("Upload File",type=['csv'])

if file is not None:
    df=load_data(file)

    n_rows=st.slider("Choose number of rows to display",min_value=5,max_value=len(df))
    columns_show=st.multiselect("Select columns to show ",df.columns.to_frame(),default=df.columns.to_list())
    numerical_column=df.select_dtypes(include=np.number).columns.tolist()

    st.write(df[:n_rows][columns_show])

    tab1,tab2=st.tabs(["Scatter","histogram"])
    with tab1:
     col1,col2,col3=st.columns(3)
     with col1:
      x_columns=st.selectbox('Select Column on x axis:',numerical_column)

      with col2:
       y_columns=st.selectbox('Select Column on y axis:',numerical_column)

      with col3:
       color=st.selectbox('Select Column to be color:',numerical_column)
     fig_scatter=px.scatter(df,x=x_columns,y=y_columns,color=color)
     st.plotly_chart(fig_scatter)

    with tab2:
     hist_feature=st.selectbox('Select Feature to histogram:',numerical_column)
     fig_hist=px.histogram(df,x=hist_feature)
     st.plotly_chart(fig_hist)