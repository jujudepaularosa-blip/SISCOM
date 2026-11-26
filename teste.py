def entrarEvento (nome, idade):
    if idade <18:
         raise ValueError (f'{nome} tem {idade} anos e não pode entrar no evento')
    return f'Entrada liberada! {nome} entrou no evento'

try:
    num = int(input('Digite um número!'))
except ValueError:
    print('Por favor digite um número valido!')