import streamlit as st

st.title("Calculadora de Impressão 3D")

materials = {"PLA": 60.0, "ABS": 80.0, "PETG": 100.0}

# Seção à esquerda
with st.sidebar:
    selected_material = st.selectbox("Escolha o material", list(materials.keys()))
    price_per_kg = materials[selected_material]
    st.write(f"Preço por quilo ({selected_material}): R$ {price_per_kg:.2f}")
    
    energy_rate = st.number_input(
        "Custo da eletricidade (kWh/R$)", min_value=0.0, value=1.0, step=0.1
    )
    st.write(f"Preço do kWh, em salvador valor é R$ 1,00")

    printer_power = st.number_input(
        "Consumo médio da impressora 3D (em watts)", min_value=0, value=110, step=10
    )
    st.write(f"Ender 3 - 110W // Prusa i3 MK3 - 180W")

    profit_margin = st.number_input(
        "Margem de lucro (%)", min_value=0.0, value=100.0, step=10.0
    )


weight = st.number_input(
    "Peso da peça (gramas)", min_value=0.0, value=100.0, step=1.0
)
printing_time = st.number_input(
    "Tempo de impressão (horas)", min_value=0.0, value=2.0, step=0.1
)

electricity_cost = (printer_power / 1000) * energy_rate * printing_time
st.write(f"Custo de eletricidade: R$ {electricity_cost:.2f}")

# Cálculo do custo total
material_cost = (price_per_kg / 1000) * weight
electricity_expense = electricity_cost
total_cost = material_cost + electricity_expense 
final_price = total_cost * (1 + profit_margin / 100)
st.subheader("Custo total (sem lucro): R$ {:.2f}".format(total_cost))
st.subheader("Preço final com lucro: R$ {:.2f}".format(final_price))
