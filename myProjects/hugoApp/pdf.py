from layout.layout import PDF

import locale


# Criando objeto PDF
pdf = PDF('P', 'mm', 'A4')
# Estabelecendo quebra automática de página
pdf.set_auto_page_break(auto=True, margin=15)  #

pdf.add_page()
