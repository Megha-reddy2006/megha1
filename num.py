import numpy as np
import pandas as pd
import streamlit as st
st.title("Welcome to python programming")
st.write("Python requires practice!!!")
data=pd.DataFrame({'c1':['A','B','C','D'],'c2':[10,20,30,40]})
st.write("Below is the given table for data")
st.write(data)
chart_data=pd.DataFrame(np.random.randn(20,4),columns=['A','B','C','D'])
st.bar_chart(chart_data)
st.area_chart(chart_data)