import streamlit as st
import time


st.header("Shapes Calculations")
st.sidebar.title("Configuration")


with st.sidebar:
  shape=st.selectbox("Choose shape:",['Circle','Rectangle'])
if shape=='Circle':
    radius=st.number_input('Radius:',min_value=0.0,max_value=100.0,step=0.01)
    area=radius * radius *3.14
    perimeter=2 * 3.14 * radius

if shape=='Rectangle':
    width=st.number_input('Width',0,step=1)
    height=st.number_input('Height',0,step=1)
    area=width * height
    perimeter=2 * (width*height)

compute_btn=st.button("Compute Area and Perimeter")
if compute_btn:
    with st.spinner("Cpmputing...."):
      time.sleep(1)
      st.write("Area:",area)
      st.write("perimeter:",perimeter)