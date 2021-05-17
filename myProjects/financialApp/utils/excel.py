from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, Font

import database

wb = Workbook()
ws = wb.active
ws.title = "Investimentos_Realizados"

# Cabeçalho Geral
ws.merge_cells('A1:F1')
cell = ws['A1']
ws['A1'].value = 'Compras de Ativos'

# Cabeçalho secundário
header = ['ATIVO', 'Nº COTAS', 'VALOR/COTA', 'TOTAL', 'DATA']
ws.append(header)
ws.merge_cells('C2:D2')
ws.merge_cells('E2:F2')


# Adicionando os investimentos armazenados no banco de dados
investments = database.get_all_investments()
i = 3
for invest in investments:
    investment_data = [invest['ativo'], invest['numero_cotas'],
                       invest['valor_cota'], invest['numero_cotas'] *
                       invest['valor_cota'],
                       invest['data']]
    ws.append(investment_data)
    ws.merge_cells(f"{'C'+str(i)}:{'D'+str(i)}")
    ws.merge_cells(f"{'E'+str(i)}:{'F'+str(i)}")
    i += 1

# Salvando alterações
wb.save("/mnt/c/wsl/pythonRoadMap/myProjects/financialApp/Investimentos.xlsx")


# cell.font = Font(b=True, color="FF0000")
# cell.alignment = Alignment(horizontal="center", vertical="center")
