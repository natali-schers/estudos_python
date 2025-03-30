# python.exe .\escolha_numero.py

numero = ""

while not numero.isnumeric():
    numero = input("Informe um número inteiro positivo: ")

    if not numero.isnumeric():
        print(f"{numero} não é um número inteiro e positivo!")

print(f"Ótima escolha! {numero} era exatamente o que eu queria ;)")