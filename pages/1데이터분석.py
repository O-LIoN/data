import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.header(' 📊 데이터 분석')
st.header("📊 데이터 분석", divider='rainbow')

# 데이터 로드
df = pd.read_csv('Obesity Classification.csv')


# 데이터 파악
st.subheader('데이터 파악')
st.write(df.head(10))  # 처음 10개 데이터 보기

st.subheader('데이터 통계')
st.write('데이터셋의 기본적인 통계 정보를 확인해보세요:')
st.dataframe(df.describe())  # 기본적인 통계 정보 보기

# 데이터 추출 (사용자가 선택한 컬럼만 보여주기)
st.subheader('데이터 추출')
st.markdown("분석할 컬럼을 선택하여 해당 데이터만 출력할 수 있습니다.")
col = st.multiselect('분석할 컬럼을 선택하세요', df.columns)
new_df = df.loc[:, col]
st.write(new_df)  # 선택된 컬럼만 출력
