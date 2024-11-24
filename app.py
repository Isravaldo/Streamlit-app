import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos
data = pd.read_csv('Employee_data.csv')

# 2. Preprocesar los datos para facilitar análisis
data['age'] = pd.to_datetime('today').year - pd.to_datetime(data['birth_date']).dt.year
data['hiring_year'] = pd.to_datetime(data['hiring_date']).dt.year

# 3. Configuración de la página
st.set_page_config(page_title="Análisis de Desempeño", layout="wide")

# 4. Título y descripción
st.title("Análisis de Desempeño de los Colaboradores")
st.write("Esta aplicación muestra el análisis de desempeño de los colaboradores de Socialize your Knowledge.")

# 5. Logotipo de la empresa
st.image("logo.png", caption="Socialize your Knowledge", width=200)

# 6. Filtros
st.sidebar.header("Filtros de empleados")

gender_filter = st.sidebar.selectbox("Selecciona el género:", options=["Todos"] + list(data['gender'].unique()))
score_range = st.sidebar.slider("Rango de puntaje de desempeño:", min_value=1, max_value=5, value=(1, 5))
marital_status_filter = st.sidebar.selectbox("Selecciona el estado civil:", options=["Todos"] + list(data['marital_status'].unique()))

# Filtrar datos según los controles
filtered_data = data.copy()
if gender_filter != "Todos":
    filtered_data = filtered_data[filtered_data['gender'] == gender_filter]
if marital_status_filter != "Todos":
    filtered_data = filtered_data[filtered_data['marital_status'] == marital_status_filter]
filtered_data = filtered_data[(filtered_data['performance_score'] >= score_range[0]) & (filtered_data['performance_score'] <= score_range[1])]

# 7. Visualización de gráficos
st.header("Visualización de datos")

# Gráfico 1: Distribución de puntajes de desempeño
st.subheader("Distribución de los puntajes de desempeño")
fig, ax = plt.subplots()
filtered_data['performance_score'].hist(bins=5, ax=ax, color='skyblue', edgecolor='black')
ax.set_title("Distribución de Puntajes de Desempeño")
ax.set_xlabel("Puntaje de desempeño")
ax.set_ylabel("Número de empleados")
st.pyplot(fig)

# Gráfico 2: Promedio de horas trabajadas por género
st.subheader("Promedio de horas trabajadas por género")
avg_hours_by_gender = filtered_data.groupby('gender')['average_work_hours'].mean()
fig, ax = plt.subplots()
avg_hours_by_gender.plot(kind='bar', ax=ax, color='orange', edgecolor='black')
ax.set_title("Promedio de Horas Trabajadas por Género")
ax.set_xlabel("Género")
ax.set_ylabel("Horas promedio")
st.pyplot(fig)

# Gráfico 3: Relación entre edad y salario
st.subheader("Relación entre edad y salario")
fig, ax = plt.subplots()
ax.scatter(filtered_data['age'], filtered_data['salary'], alpha=0.7, color='green')
ax.set_title("Relación Edad vs Salario")
ax.set_xlabel("Edad")
ax.set_ylabel("Salario")
st.pyplot(fig)

# Gráfico 4: Promedio de horas trabajadas vs. puntaje de desempeño
st.subheader("Promedio de horas trabajadas vs. Puntaje de desempeño")
fig, ax = plt.subplots()
ax.scatter(filtered_data['average_work_hours'], filtered_data['performance_score'], alpha=0.7, color='purple')
ax.set_title("Promedio de Horas Trabajadas vs. Puntaje de Desempeño")
ax.set_xlabel("Horas trabajadas (promedio)")
ax.set_ylabel("Puntaje de desempeño")
st.pyplot(fig)

# 8. Conclusiones
st.header("Conclusiones")
st.write("El análisis revela las fortalezas y áreas de oportunidad de los colaboradores.")
st.write("Por ejemplo, se observa una correlación entre las horas trabajadas y el desempeño en ciertos casos. Estos datos son clave para mejorar estrategias de capacitación y retención.")