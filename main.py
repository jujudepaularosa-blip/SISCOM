from models import Categoria, Produto, Fornecedor,MovimentoEstoque

categoria1 = Categoria("Eletrônicos", "Produtos eletronicos e gadgets")
categoria2 = Categoria("Papelaria", "Materiais Escolares")
categoria3 = Categoria("Informatica", "Acessórios e Equipamentos")

fornecedor1 = Fornecedor("Fornecedor A", "(27) 3253-2222", 'fornecedor1@gmail.com' )
fornecedor2 = Fornecedor("Fornecedor B", "(27) 3253-3212", 'fornecedor2@gmail.com' )

produto1 = Produto("Notebook", 5000.00, 10, categoria1, fornecedor2)
produto2 = Produto("Caneta", 2.50, 100, categoria2, fornecedor1)
produto3 = Produto("Teclado", 150.00, 20, categoria3, fornecedor2)

print(produto1.apresentar())
print(produto2.apresentar())
print(produto3.apresentar())

movimento1 = MovimentoEstoque('entrada', 5, '26/11/2026', produto1)
movimento1.executar()

movimento2 = MovimentoEstoque('saida', 4, '26/11/2026', produto2)
movimento2.executar()

movimento3 = MovimentoEstoque('saida', 5, '26/11/2026', produto1)
movimento3.executar()


print(produto1.apresentar())
print(produto2.apresentar())
print(produto3.apresentar())