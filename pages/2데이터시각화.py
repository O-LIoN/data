import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 웹앱 제목
st.sidebar.header('📈 데이터 시각화')
st.header("📈 데이터 시각화", divider='rainbow')

# 데이터 로드
df = pd.read_csv('Obesity Classification.csv')
  

# BMI 분포 히스토그램
st.subheader("BMI 분포 히스토그램")
st.markdown("""
    **BMI 분포 히스토그램**: 이 그래프는 데이터셋의 BMI 값 분포를 보여줍니다. 
    비만 여부(Label)에 따라 분포가 어떻게 다른지 확인할 수 있습니다.
""")
fig = plt.figure(figsize=(10, 5))
sns.histplot(df['BMI'], kde=True, color='blue')
st.pyplot(fig)

# 성별에 따른 비만 여부 박스플롯
st.subheader("성별에 따른 비만 여부 박스플롯")
st.markdown("""
    **성별에 따른 비만 여부**: 이 박스플롯은 성별에 따른 BMI 분포를 나타냅니다. 
    'Label' 값에 따라 비만 여부가 어떻게 구분되는지 확인할 수 있습니다.
""")
fig = plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='BMI', hue='Label', data=df)
st.pyplot(fig)

# 나이와 BMI 관계 스캐터플롯
st.subheader("나이와 BMI 관계 스캐터플롯")
st.markdown("""
    **나이와 BMI의 관계**: 이 스캐터플롯은 나이에 따른 BMI 값의 관계를 시각화한 것입니다. 
    'Label'에 따라 비만과 비만 아님 그룹이 어떻게 구분되는지 살펴볼 수 있습니다.
""")
fig = plt.figure(figsize=(10, 5))
sns.scatterplot(x='Age', y='BMI', hue='Label', data=df)
st.pyplot(fig)

# 비만 여부에 따른 나이 및 BMI 통계
st.subheader("비만 여부에 따른 나이 및 BMI 통계")
st.markdown("""
    비만 여부에 따른 나이, BMI 등의 통계를 아래에서 확인할 수 있습니다. 
    **Obese**, **Overweight**, **Normal Weight**, **Underweight**로 구분하여 각 그룹의 특성을 비교합니다.
""")
obesity_data = df[df['Label'] == 'Obese']
overweight_data = df[df['Label'] == 'Overweight']
normal_weight_data = df[df['Label'] == 'Normal Weight']
underweight_data = df[df['Label'] == 'Underweight']

st.write("**비만 데이터 통계 (Obese)**:")
st.write(obesity_data.describe())

st.write("**과체중 데이터 통계 (Overweight)**:")
st.write(overweight_data.describe())

st.write("**정상 체중 데이터 통계 (Normal Weight)**:")
st.write(normal_weight_data.describe())

st.write("**저체중 데이터 통계 (Underweight)**:")
st.write(underweight_data.describe())
