class Veiculo():
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante

    def acelerar(self): 
        print(f"Vrummm! {self.modelo} na estrada!")

class Carro(Veiculo):
    pass

class Barco(Veiculo):
    def acelerar(self): 
        print(f"Splashhh! {self.modelo} na água!")

class Aviao(Veiculo):
    def acelerar(self): 
        print(f"Fwoooosh! {self.modelo} nos ares!")

meu_carro = Carro("Opala", "Chevrolet")
meu_barco = Barco("Lancha 360", "Azimut")
meu_aviao = Aviao("737 MAX", "Boeing")

print(f"Fabricante: {meu_carro.fabricante} | Carro: {meu_carro.modelo}.")
print(f"Fabricante: {meu_barco.fabricante} | Carro: {meu_barco.modelo}.")
print(f"Fabricante: {meu_aviao.fabricante} | Carro: {meu_aviao.modelo}.")

meu_carro.acelerar()
meu_barco.acelerar()
meu_aviao.acelerar()