#n python.exe .\lista_pessoas.py

pessoas = []
id_grupo = 0

while len(pessoas) < 6:
    pessoa = input(f"Informe o {len(pessoas) + 1}º nome: ")
    pessoas.append(pessoa)

while len(pessoas) > 0:
    proximos_atendimentos = pessoas[0:3]
    restante_na_fila = len(pessoas) - len(proximos_atendimentos)
    id_grupo += 1

    print(f"\nAtendimento do {id_grupo}º grupo: ")

    for pessoa in proximos_atendimentos:
        print(f" - {pessoa}")
        pessoas.remove(pessoa)

    if restante_na_fila > 0:
        print(f"Pacientes restantes: {restante_na_fila}")
    else:
        print("Atendimentos finalizados, bom descanso!")