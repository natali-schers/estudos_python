# python.exe .\lista_nomes.py

nomes = [
    "Natali",
    "Leonardo",
    "Priscila",
    "Nicole",
    "Wagner",
    "Rosa"
]

for nome in nomes:
    print(f"\n {nome}")

    for letra in nome:
        print(f"- {letra.upper()}")