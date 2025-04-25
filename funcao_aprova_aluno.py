def aprova_aluno(nome, **informacoes_adicionais):
    print(f"Olá, {nome}.")

    if "nota_atvdd" not in informacoes_adicionais:
        print("A atividade não foi encontrada. ")
        return
    
    if informacoes_adicionais.get("nota_atvdd") > 7:
        print("Parabéns, você foi aprovado(a)!")
    else: 
        print("Infelizmente, você foi reprovado(a)!")

aprova_aluno("Natali", nota_atvdd = 8)
aprova_aluno("João")