# ### Importa a biblioteca
import streamlit as st

# ### Adiciona o Titulo
# st.title("Imune ao Conhecimento")
# ### Escreve
# st.write("Testando.....")
# ### Adiciona uma Barra Lateral com Titulo
# st.sidebar.title("Barra Lateral")

# # Adiciona uma Lista
# nomes = ["Breno", "Nicolas", "Matheus", "Lucas", "Henry"]

# st.sidebar.selectbox("Escolha um nome: ", nomes)

# SideBar

st.sidebar.title("Alugel de Carro")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha o carro ideal para você!")

carros = ["Ferrari 488 GTB", "Lamborghini Aventador", "Porsche Panamera", "Bentley Continental GT", "Rolls-Royce Phantom"]



opcao = st.sidebar.selectbox("Escolha o Carro que foi alugado", carros)

#Principal

st.title("🚗 Viva a experiência de dirigir um carro de luxo")
st.write("Na Mogger Car Rental, não alugamos apenas carros — oferecemos momentos inesquecíveis. Imagine-se ao volante de uma Ferrari, um Porsche ou um Rolls-Royce, sentindo a potência, o design impecável e o conforto que só os carros mais desejados do mundo podem proporcionar.")
st.write("✔️ Frota exclusiva de veículos premium")
st.write("✔️ Atendimento personalizado e discreto")
st.write("✔️ Planos sob medida para cada ocasião")
st.write("Seja para impressionar em um evento, celebrar uma conquista ou simplesmente realizar um sonho, nós entregamos o carro certo para você.")
st.write("👉 Reserve agora e transforme sua viagem em uma experiência única.")


st.title("Mogger Car Rental - Aluguel de Carros")

st.image(f"{opcao}.png", width=350)
st.markdown(f"## Você alugou o modelo: {opcao}")
st.markdown("---")

#------------Calcular------------
dias = st.number_input("Quantos dias você deseja alugar o carro?", min_value=1, step=1)
km = st.number_input("Quantos quilômetros você rodou?", min_value=0, step=1)

if opcao == "Ferrari 488 GTB":
    valor_diario = 6600
elif opcao == "Lamborghini Aventador":
    valor_diario = 6313
elif opcao == "Porsche Panamera":
    valor_diario = 4000 
elif opcao == "Bentley Continental GT":
    valor_diario = 2600
elif opcao == "Rolls-Royce Phantom":
    valor_diario =  7170

if st.button("Calcular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias * valor_diario
    total_km = km * 0.15
    valor_total = total_km + total_dias 

    st.warning(f"Você alugou {opcao} por {dias} e rodou {km}km. O valor total a pagar é R${valor_total:.2f}")