class Televisao:
    def __init__(self, min, max):
        self.canal = 2
        self.ligada = False
        self.cmin = min
        self.cmax = max

        def muda_canal_para_baixo(self):
           # if self.canal - 1 >= self.cmin:
            self.canal -= 1

        def muda_canal_para_cima(self):
            # if self.canal + 1 <= self.cmax:
            self.canal += 1
        # criar um objeto a partir de uma classe
        # instanciar uma classe
# tv = televisao(1, 99)


tvDoQuarto = Televisao(1, 99)
tvDoQuarto.ligada = True
print(tvDoQuarto.ligada)
print(f'canal selecionado: {tvDoQuarto.canal}')
print(f'canal selecionado: {tvDoQuarto.ligada}')
tvDoQuarto.muda_canal_para_cima()
print(f'canal selecionado: {tvDoQuarto.canal}')
tvDoQuarto.muda_canal_para_cima()
tvDoQuarto.muda_canal_para_cima()
tvDoQuarto.muda_canal_para_cima()
print(f'Canal selecionado: {tvDoQuarto.canal}')
