from utils import database


def prompt_add_investment(ativo, numero_cotas, valor_cota, data):
    #ativo = input('Nome do ativo: ')
    #numero_cotas = input('Número de cotas compradas: ')
    #valor_cota = input('Valor pago por cota: ')
    #data = input('Data da compra: ')
    database.add_investment(ativo, numero_cotas, valor_cota, data)


def list_investments():
    investments = database.get_all_investments()
    print(investments)


database.create_investment_table()
prompt_add_investment('BCFF11', 10, 100, '2021-01-01')
list_investments()
