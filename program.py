import datetime

def salvar_historico(imc, classificacao):
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("historico_saude.txt", "a") as arquivo:
        arquivo.write(f"[{data_atual}] IMC: {imc:.2f} - {classificacao}\n")
    print("\n✓ Resultado salvo com sucesso em 'historico_saude.txt'!")

print("--- Calculadora de Saúde Pro ---")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = "Abaixo do peso"
elif 18.5 <= imc < 25:
    status = "Peso normal"
elif 25 <= imc < 30:
    status = "Sobrepeso"
else:
    status = "Obesidade"

print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {status}")

# Nova Funcionalidade: Salvar os dados
salvar_historico(imc, status)
