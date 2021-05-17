from openpyxl import Workbook, load_workbook
from openpyxl.styles.borders import Border
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, Font, PatternFill, GradientFill, Side

from utils import database


def create_excel_file():
    thin = Side(border_style="thin", color="000000")
    double = Side(border_style="double", color="000000")

    wb = Workbook()
    ws = wb.active
    ws.title = "Investimentos_Realizados"

    # Cabeçalho Geral
    ws.merge_cells('A1:F1')
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
        # Estilizando a linha
        for col in range(1, 7):
            char = get_column_letter(col)
            ws[char+str(i)].font = Font(bold=False)
            ws[char+str(i)].fill = PatternFill("solid", fgColor="DAFFFF")
            ws[char+str(i)].border = Border(top=double,
                                            left=thin, right=thin,
                                            bottom=double)
            ws[char+str(i)].alignment = Alignment(horizontal="center",
                                                  vertical="center")
        i += 1

    # Estilizando as células
    # Cabeçalho principal
    for col in range(1, 7):
        char = get_column_letter(col)
        ws[char+'1'].font = Font(bold=True, color="FFFFFF")
        ws[char+'1'].fill = PatternFill("solid", fgColor="00558E")
        ws[char+'1'].border = Border(left=thin, right=thin)
        ws[char+'1'].alignment = Alignment(horizontal="center",
                                           vertical="center")
    # Cabeçalho secundário
    for col in range(1, 7):
        char = get_column_letter(col)
        ws[char+'2'].font = Font(bold=True, color="000000")
        ws[char+'2'].fill = PatternFill("solid", fgColor="95E9FF")
        ws[char+'2'].border = Border(left=thin, right=thin)
        ws[char+'2'].alignment = Alignment(horizontal="center",
                                           vertical="center")
    # Salvando alterações
    wb.save("/mnt/c/wsl/pythonRoadMap/myProjects/financialApp/Investimentos.xlsx")

    # cell.font = Font(b=True, color="FF0000")
    # cell.alignment = Alignment(horizontal="center", vertical="center")
