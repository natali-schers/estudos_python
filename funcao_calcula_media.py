# python.exe ./funcao_calcula_media.py

def calcula_media(*notas):
    soma = 0
    
    for nota in notas:
        soma += nota

    media = soma / len(notas)

print(calcula_media(7, 9, 6))