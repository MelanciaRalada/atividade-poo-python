
class Joia ():
    def __init__ (self, valor, material, tipo):
        self.valor = valor
        self.material = material
        self.tipo = tipo

    def vender (self):
        return f"Você deseja vender seu {self.tipo} de {self.material} que é estimado em {self.valor}?"
    
    def comprar (self):
        return f"Você deseja comprar um(a) {self.tipo} de {self.material} que é estimado em {self.valor}?"
    
Joia1 = Joia("R$ 22.013,00", "ouro", "colar")
Joia2 = Joia("R$ 13.220,00", "esmeralda", "bracelete")

print(Joia1.vender())
print()
print(Joia2.comprar())
