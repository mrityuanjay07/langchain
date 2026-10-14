# import streamlit as st

# st.title("welcome to the programming language shop")
# language = st.selectbox("choose your favourite programing language:", ["java","python","c++","R","c#","javascripts"])
# st.write(f"you choose the {language} excellent choice")

import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
st.table(dataframe)
st.line_chart(dataframe)


dataframe1 = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.6,-133.4],
    columns=['lat', 'lon']
)
st.map(dataframe1)


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
