from pdf import pdf


USER_CHOICE = ''' Escolha uma opção a seguir

- 'a' para adicionar um ambiente
- 'p' para gerar o PDF
- 'q' para sair sem gerar o PDF

Entre com sua escolha: '''

user_choices = {
    'a': pdf.ambiente,
    'p': pdf.output,
}

MAX_AMBIENTES_PAG_1 = 5  # Nmr máximo de ambientes na 1 pagina
MAX_AMBIENTES_PAG_2 = 8  # nmr máximo de ambites a partir da 2 pagina


def menu():
    page = 0  # Flag para controloar se está na primeira página (page=0)
    page_count = 0  # Flag para controlar a contagem de ambientes
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('a', 'p'):
            if user_input == 'p':
                pdf.add_page()
                pdf.assinatura()
                user_choices[user_input]('pdf_1.pdf')
                break
            else:
                user_choices[user_input]()
                page_count += 1
                # Se estiver na Primeira página
                if page_count >= MAX_AMBIENTES_PAG_1 and page == 0:
                    pdf.add_page()
                    page = 1
                    page_count = 0
                # Se estiver a partir da Segunda página
                elif page_count >= MAX_AMBIENTES_PAG_2 and page == 1:
                    pdf.add_page()
                    page_count = 0
        else:
            print('\nCOMANDO INVÁLIDO!!!\n')
        user_input = input(USER_CHOICE)


pdf.cabecalho()
menu()
