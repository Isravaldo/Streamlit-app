{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import matplotlib.pyplot as plt\
\
# 1. Cargar los datos\
data = pd.read_csv('Employee_data.csv')\
\
# 2. Preprocesar los datos para facilitar an\'e1lisis\
data['age'] = pd.to_datetime('today').year - pd.to_datetime(data['birth_date']).dt.year\
data['hiring_year'] = pd.to_datetime(data['hiring_date']).dt.year\
\
# 3. Configuraci\'f3n de la p\'e1gina\
st.set_page_config(page_title="An\'e1lisis de Desempe\'f1o", layout="wide")\
\
# 4. T\'edtulo y descripci\'f3n\
st.title("An\'e1lisis de Desempe\'f1o de los Colaboradores")\
st.write("Esta aplicaci\'f3n muestra el an\'e1lisis de desempe\'f1o de los colaboradores de Socialize your Knowledge.")\
\
# 5. Logotipo de la empresa\
st.image("logo.png", caption="Socialize your Knowledge", width=200)\
\
# 6. Filtros\
st.sidebar.header("Filtros de empleados")\
\
gender_filter = st.sidebar.selectbox("Selecciona el g\'e9nero:", options=["Todos"] + list(data['gender'].unique()))\
score_range = st.sidebar.slider("Rango de puntaje de desempe\'f1o:", min_value=1, max_value=5, value=(1, 5))\
marital_status_filter = st.sidebar.selectbox("Selecciona el estado civil:", options=["Todos"] + list(data['marital_status'].unique()))\
\
# Filtrar datos seg\'fan los controles\
filtered_data = data.copy()\
if gender_filter != "Todos":\
    filtered_data = filtered_data[filtered_data['gender'] == gender_filter]\
if marital_status_filter != "Todos":\
    filtered_data = filtered_data[filtered_data['marital_status'] == marital_status_filter]\
filtered_data = filtered_data[(filtered_data['performance_score'] >= score_range[0]) & (filtered_data['performance_score'] <= score_range[1])]\
\
# 7. Visualizaci\'f3n de gr\'e1ficos\
st.header("Visualizaci\'f3n de datos")\
\
# Gr\'e1fico 1: Distribuci\'f3n de puntajes de desempe\'f1o\
st.subheader("Distribuci\'f3n de los puntajes de desempe\'f1o")\
fig, ax = plt.subplots()\
filtered_data['performance_score'].hist(bins=5, ax=ax, color='skyblue', edgecolor='black')\
ax.set_title("Distribuci\'f3n de Puntajes de Desempe\'f1o")\
ax.set_xlabel("Puntaje de desempe\'f1o")\
ax.set_ylabel("N\'famero de empleados")\
st.pyplot(fig)\
\
# Gr\'e1fico 2: Promedio de horas trabajadas por g\'e9nero\
st.subheader("Promedio de horas trabajadas por g\'e9nero")\
avg_hours_by_gender = filtered_data.groupby('gender')['average_work_hours'].mean()\
fig, ax = plt.subplots()\
avg_hours_by_gender.plot(kind='bar', ax=ax, color='orange', edgecolor='black')\
ax.set_title("Promedio de Horas Trabajadas por G\'e9nero")\
ax.set_xlabel("G\'e9nero")\
ax.set_ylabel("Horas promedio")\
st.pyplot(fig)\
\
# Gr\'e1fico 3: Relaci\'f3n entre edad y salario\
st.subheader("Relaci\'f3n entre edad y salario")\
fig, ax = plt.subplots()\
ax.scatter(filtered_data['age'], filtered_data['salary'], alpha=0.7, color='green')\
ax.set_title("Relaci\'f3n Edad vs Salario")\
ax.set_xlabel("Edad")\
ax.set_ylabel("Salario")\
st.pyplot(fig)\
\
# Gr\'e1fico 4: Promedio de horas trabajadas vs. puntaje de desempe\'f1o\
st.subheader("Promedio de horas trabajadas vs. Puntaje de desempe\'f1o")\
fig, ax = plt.subplots()\
ax.scatter(filtered_data['average_work_hours'], filtered_data['performance_score'], alpha=0.7, color='purple')\
ax.set_title("Promedio de Horas Trabajadas vs. Puntaje de Desempe\'f1o")\
ax.set_xlabel("Horas trabajadas (promedio)")\
ax.set_ylabel("Puntaje de desempe\'f1o")\
st.pyplot(fig)\
\
# 8. Conclusiones\
st.header("Conclusiones")\
st.write("El an\'e1lisis revela las fortalezas y \'e1reas de oportunidad de los colaboradores.")\
st.write("Por ejemplo, se observa una correlaci\'f3n entre las horas trabajadas y el desempe\'f1o en ciertos casos. Estos datos son clave para mejorar estrategias de capacitaci\'f3n y retenci\'f3n.")}