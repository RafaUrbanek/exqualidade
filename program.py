# Calculadora de IMC simples
print("--- Calculadora de Saúde ---")

# Entrada de dados (convertendo o texto para números decimais)
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibindo o resultado com duas casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Estrutura de decisão
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal (Saudável)")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
