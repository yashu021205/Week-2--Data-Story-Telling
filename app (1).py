import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Titanic Data Storytelling App")

df = pd.read_csv("Titanic-Dataset.csv")

st.header("Dataset Introduction")

st.write("""
The Titanic dataset contains passenger information such as age,
gender, ticket class and survival status.
""")

st.header("Exploratory Data Analysis (EDA)")

st.write(df.head())

st.write(df.describe())

st.header("Visualizations")

fig1 = px.histogram(df, x="Age")
st.plotly_chart(fig1)

fig2 = px.pie(df, names="Sex")
st.plotly_chart(fig2)

fig3 = px.bar(df, x="Pclass")
st.plotly_chart(fig3)

st.header("Insights and Findings")

st.write("""
1. Female passengers had a higher survival rate.
2. First-class passengers survived more often.
3. Age had some influence on survival.
""")

st.header("Conclusion")

st.success(
    "Passenger class and gender were important factors affecting survival."
)