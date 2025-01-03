import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 웹앱 제목
st.write("# 비만 분류 데이터 웹앱 🏋️‍♀️")

st.header("비만 데이터 개요", divider='rainbow')

# 데이터 개요 설명
st.markdown('''
    이 웹앱은 비만 분류 데이터를 분석합니다. 데이터셋은 BMI(체질량지수) 기반의 비만 여부를 분류합니다.
    이 데이터셋은 연령, 성별, BMI 등 여러 특성을 사용하여 비만 여부를 예측합니다.
    데이터셋의 주요 항목은 다음과 같습니다:
    
    - **Age**: 나이
    - **Gender**: 성별 (Male, Female)
    - **Height**: 키 (cm)
    - **Weight**: 몸무게 (kg)
    - **BMI**: 체질량지수
    - **Label**: 비만 여부 (Normal Weight, Overweight, Obese, Underweight)
''')