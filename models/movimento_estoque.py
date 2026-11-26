class MovimentoEstoque:
    def __init__(self, tipo, quantidade, data, produto):
        self.tipo = tipo
        self.quantidade = quantidade
        self.data = data
        self.produto = produto

    def apresentar(self):
        return (
            f'Tipo: {self.tipo}'
            f'Quantidade: {self.quantidade}'
            f'Data: {self.data}'
            f'Produto: {self.produto.nome}'
        )
    
        