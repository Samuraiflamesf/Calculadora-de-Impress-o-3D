import streamlit as st

# Título
st.title("Calculadora de Valor Justo de Impressão 3D")

# Entrada dos dados
filament_cost = st.number_input("Custo do filamento (por kilo)", min_value=0.0, value=0.05, step=0.01)
weight = st.number_input("Peso da peça (gramas)", min_value=0.0, value=100.0, step=1.0)
printing_time = st.number_input("Tempo de impressão (horas)", min_value=0.0, value=2.0, step=0.1)
electricity_cost = st.number_input("Custo da eletricidade por hora", min_value=0.0, value=0.5, step=0.1)
depreciation_cost = st.number_input("Depreciação da impressora por hora", min_value=0.0, value=1.0, step=0.1)
profit_margin = st.number_input("Margem de lucro (%)", min_value=0.0, value=20.0, step=0.1)

# Cálculo do custo total
material_cost = filament_cost * weight
electricity_expense = electricity_cost * printing_time
depreciation_expense = depreciation_cost * printing_time
total_cost = material_cost + electricity_expense + depreciation_expense

# Adicionando a margem de lucro
final_price = total_cost * (1 + profit_margin / 100)

# Exibição do resultado
st.subheader("Custo total (sem lucro): R$ {:.2f}".format(total_cost))
st.subheader("Preço final com lucro: R$ {:.2f}".format(final_price))
