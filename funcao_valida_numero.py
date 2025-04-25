#python.exe ./funcao.py
def input_numero(mensagem): 
    input_usuario = ""

    while not input_usuario.isnumeric():
        input_usuario = input(mensagem)

        if not input_usuario.isnumeric():
            print("Ops... A entrada informada não é um número.")
    
    return float(input_usuario)

a = input_numero("Informe o primeiro valor: ")
b = input_numero("Informe o segundo valor: ")

resultado = a + b

print(f"O resultado é: {resultado}")