peso = input("Digite seu peso corporal: ")
altura = input("Digite sua altura(Exemplo: 1.77 pra 1 metro e 77cm): ")


def calculadora_imc(peso, altura):
    imc = (int(peso)) / (float(altura) ** (float(altura))) #pra conseguir o imc, é necessario fazer peso dividido pela altura elevado ao quadrado
    if imc <= 18.5:
        print("seu nível de imc é 'Magreza' ")
        print(imc)
    elif imc > 18.5 and imc < 25:
        print("seu nível de imc é 'normal' ")
        print(imc)
    elif imc > 25:
        print("seu nível de imc é 'sobrepeso'")

calculadora_imc(peso, altura)
