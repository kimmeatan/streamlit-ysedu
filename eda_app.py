# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils


def run_eda_app():
    st.subheader('탐색적 자료 분석')

    iris = pd.read_csv('data/iris.csv')
    st.markdown('## IRIS 데이터 확인')
    st.write(iris) # print()

    #메뉴지정
    submenu = st.sidebar.selectbox('하위메뉴', ['기술통계량', '그래프분석', '통계분석'])
    if submenu == '기술통계량':
        st.dataframe(iris)

        with st.expander('데이터타입'):
            result1 = pd.DataFrame(iris.dtypes)
            st.write(result1)
        with st.expander('기술통계량'):
            result2 = pd.DataFrame(iris.dtypes)
            st.write(result2)

        with st.expander('타겟 빈도 수 확인'):
            st.dataframe(iris['species'].value_counts())
    elif submenu == '그래프분석':
        st.title('Title')
        with st.expander('산점도'):
            fig = px.scatter(iris,
                             x ='sepal_width',
                             y ='sepal_length',
                             color ='species',
                             size = 'petal_width',
                             hover_data =['petal_length'])
            st.plotly_chart(fig)

        #layouts
        col1,col2 =  st.columns(2)
        with col1:
            st.title('Seaborn')
            fig1, ax = plt.subplots()
            fig1 = sns.histplot(iris,x ='sepal_width',
                                y = 'sepal_length')
            fig.show(fig1)

        with col2:
            st.title('Matplotlib')
    elif submenu == '통계분석':
        pass
    else:
        st.warning('뭔가 없어요')
