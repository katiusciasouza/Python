class Carro():
    def __init__(self):
        self.cor = "vermelho"
        self.velocidade = 100
        self.quantidadeDeRodas = 4
        self.quantidadeDePassageiros = 6
        self.tamanho = 3.0

    def andar(self):
        print("Está começando a andar!")

    def buzinar(self):
        print("Está Buzinando!")


tesla = Carro()
print(tesla.cor)
print(tesla.quantidadeDePassageiros)
print(tesla.velocidade)
print(tesla.quantidadeDeRodas)


class Carro():
    def __init__(self, marca, cor, velocidade, qtdDeRodas, qtdDePass, tamanho):
        self.marca = marca
        self.cor = cor
        self.velocidade = velocidade
        self.quantidadeDeRodas = qtdDeRodas
        self.quantidadeDePassageiros = qtdDePass
        self.tamanho = tamanho


tesla = Carro("Tesla", "Preto", 200.0, 4, 5, 3.5)
Fit = Carro("Honda", "Prata", 200, 4, 5, 3.2)
print("tesla")
print(tesla.marca)
print(Fit.marca)
print(tesla.cor)
print(tesla.quantidadeDePassageiros)
print(tesla.quantidadeDeRodas)
print(tesla.tamanho)
print(tesla.velocidade)
print("Fit")
print(Fit.velocidade)
print(Fit.cor)
print(Fit.quantidadeDePassageiros)
print(Fit.quantidadeDeRodas)
print('o carro' + tesla.marca + 'vai acender a luz')
print(f'o carro {Fit.marca} vai acender a luz')
