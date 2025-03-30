# python.exe .\calculo_media.py

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2
situacao = "pendente"

print(f"A média final é: {media}.")

if media >= 6:
    situacao = "aprovado"
elif media >= 4:
    fez_trabalho = input("Informe se o aluno fez o trabalho de recuperação (s/n): ")
    
    if fez_trabalho == "s":
        situacao = "aprovado com recuperação"
    else:
        situacao = "reprovado"
else:
    situacao = "reprovado"

match situacao:
    case "aprovado":
        print("O aluno foi aprovado com sucesso!")
    case "aprovado com recuperação":
        print("O aluno foi aprovado após a conclusão do trabalho de recuperação!")
    case "reprovado":
        print("O aluno foi reprovado e deverá repetir o módulo!")
    case _:
        print("A situação do aluno não foi mapeada corretamente!")