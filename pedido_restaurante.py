#Crie uma classe Pedido que represente um pedido em um restaurante, 
# contendo os itens pedidos e um método para calcular o valor total da conta.

#Entrada
#Lista de itens e seus respectivos preços.
#Saída
#O valor total da conta.


class Pedido:
    def __init__(self):
        self.itens = []  
    
    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    
        # TODO: Adicione o preço do item à lista:
    def adicionar_item(self, preco):
        self.itens.append(preco)      

    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:
    
        # TODO: Retorne a soma de todos os preços
    def calcular_total(self):
        return sum(self.itens)
        

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    #TODO: Chame o método adicionar_item corretamente: 
    pedido.adicionar_item(float(preco)) 

# TODO: Exiba o total formatado com duas casas decimais:
print(f"{pedido.calcular_total():.2f}")