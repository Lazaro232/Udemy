from user.info import InfoUsuario

from fpdf import FPDF

import locale


class PDF(FPDF):
    def cabecalho(self):
        top = self.y
        # print(self.y)
        offset = self.x + 92 + 46
        # Logo
        self.image('logo01.png', 23, 12, 20)
        # Fonte
        self.set_font('helvetica', 'B', 10)
        # Caixas
        self.cell(46, 36, border=1)
        self.multi_cell(92, 6, 'HOME STUDIO MÓVEIS PLANEJADOS\nRua Júlio Siqueira 1008\nDionísio Torres, Fortaleza - CE\n@HOME.STUDIO21\nCONTATO@STUDIOUPINTERIORES.COM.BR\nContatos: 9.9775-7393 / 9.8694-1731 / 9.9198-7119',
                        border=1, align='C')
        self.y = top
        self.x = offset
        offset = self.x + 46
        self.multi_cell(
            46, 6, f'\n \nNº DO ORÇAMENTO\n{InfoUsuario.codigo}\n \n ', border=1, align='C')

        # ------- Caixa grande -------
        top = self.y
        self.x = 9.9999
        self.cell(184, 236, border=1)

        # Quebra de linha
        self.ln(2)
        # ------ Segunda Linha de Caixas -----------
        top = self.y
        self.x = 12
        offset = self.x + 83
        # Fonte
        self.set_font('helvetica', 'B', 8)
        # Caixas
        self.multi_cell(83, 6, 'Responsável pela venda\nLázaro', border=1)
        self.y = top
        self.x = offset
        offset = self.x + 34
        self.multi_cell(34, 6, 'Profissional\nLázaro', border=1)
        self.y = top
        self.x = offset
        offset = self.x + 32
        self.multi_cell(32, 6, 'Contato\n(85) 98872.3250', border=1)
        self.y = top
        self.x = offset
        self.multi_cell(31, 6, 'Data do Orçamento\n04/05/2021', border=1)

        # ------ Teceira Linha de Caixas -----------
        top = self.y
        self.x = 12
        offset = self.x + 180
        self.multi_cell(180, 6, 'Cliente\nLázaro', border=1)

        # ------ Quarta Linha de Caixas -----------
        top = self.y
        self.x = 12
        offset = self.x + 180
        self.multi_cell(180, 6, 'Endereço\nRua tal', border=1)

        # ------ Quinta Linha de Caixas -----------
        top = self.y
        self.x = 12
        offset = self.x + 58
        self.multi_cell(58, 6, 'Bairro\nBairro tal', border=1)
        self.y = top
        self.x = offset
        offset = self.x + 56
        self.multi_cell(56, 6, 'Cidade\nCidade tal', border=1)
        self.y = top
        self.x = offset
        offset = self.x + 22
        self.multi_cell(22, 6, 'UF\nCE', border=1)
        self.y = top
        self.x = offset
        offset = self.x + 44
        self.multi_cell(44, 6, 'CEP\n00000-000', border=1)

        # ------ Sexta Linha de Caixas -----------
        top = self.y
        self.x = 12
        offset = self.x + 58
        self.multi_cell(58, 6, 'Telefone\n85 999999999', border=1)
        self.y = top
        self.x = offset
        offset = self.x + 122
        self.multi_cell(122, 6, 'Email\nemailtal@gmail.com', border=1)

        # Quebra de linha
        self.ln(1.5)

    def ambiente(self):
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(128, 128, 128)
        top = self.y
        self.x = 12
        # print(self.y)
        offset = self.x + 9
        self.multi_cell(9, 6, 'AMB', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 9
        self.multi_cell(9, 6, 'QTD', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 51
        self.multi_cell(51, 6, 'AMBIENTE', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 43
        self.multi_cell(43, 6, 'FORNECEDOR', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 33
        self.multi_cell(33, 6, 'LINHA', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 12
        self.multi_cell(12, 6, 'PRAZO', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 23
        self.multi_cell(23, 6, 'VALOR', border=1, fill=1)

        # ---- Adicionando os dados ------
        self.set_font('helvetica', '', 8)
        self.set_fill_color(250, 250, 250)
        top = self.y
        self.x = 12
        offset = self.x + 9
        self.multi_cell(
            9, 6, f'{InfoUsuario.ambiente.upper()}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 9
        self.multi_cell(
            9, 6, f'{InfoUsuario.quantidade.upper()}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 51
        self.multi_cell(
            51, 6, f'{InfoUsuario.nome_ambiente.upper()}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 43
        self.multi_cell(
            43, 6, f'{InfoUsuario.fornecedor.upper()}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 33
        self.multi_cell(
            33, 6, f'{InfoUsuario.linha.upper()}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 12
        self.multi_cell(
            12, 6, f'{InfoUsuario.prazo.upper()}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 23
        locale.setlocale(locale.LC_ALL, '')
        self.multi_cell(
            23, 6, f'{locale.currency(float(InfoUsuario.valor), grouping=True)}', border=1, fill=1)

        # Quebra de linha
        self.ln(2.5)

        # ----- Segundo Grupo de Informações ------
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(220, 220, 220)
        top = self.y
        self.x = 12
        offset = self.x + 9
        self.multi_cell(9, 6, "AMB", border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 36
        self.multi_cell(36, 6, 'CORPO', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 32
        self.multi_cell(32, 6, 'PORTA', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 34
        self.multi_cell(34, 6, 'PUXADOR', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 34
        self.multi_cell(34, 6, 'COMPLEMENTO', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 35
        self.multi_cell(35, 6, 'MODELO', border=1, fill=1)

        # ----- Adicionando as Informações do segundo grupo ------
        self.set_font('helvetica', '', 8)
        self.set_fill_color(250, 250, 250)
        top = self.y
        self.x = 12
        offset = self.x + 9
        self.multi_cell(
            9, 6, f'{InfoUsuario.ambiente.upper()}\n ', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 36
        self.multi_cell(
            36, 6, f'{InfoUsuario.corpo_cor.upper()}\n ', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 32
        self.multi_cell(
            32, 6, f'{InfoUsuario.porta_cor.upper()}\n ', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 34
        self.multi_cell(
            34, 6, f'{InfoUsuario.puxador.upper()}\n ', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 34
        self.multi_cell(
            34, 6, f'{InfoUsuario.complemento.upper()}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 35
        self.multi_cell(
            35, 6, f'{InfoUsuario.modelo.upper()}\n ', border=1, fill=1)

        # Quebra de linha
        self.ln(1.5)

    def assinatura(self):
        self.y = 200
        self. x = 12
        top = self.y
        self.set_font('helvetica', 'B', 8)
        self.set_fill_color(200, 200, 200)
        self.y = top
        offset = self.x + 180
        self.multi_cell(
            180, 6, f'AMB OBSERVAÇÃO - {InfoUsuario.observacao.upper()}', border=1, fill=1)
        # Quebra de linha
        self.ln(3)
        self. x = 12
        locale.setlocale(locale.LC_ALL, '')
        self.multi_cell(
            180, 6, f'TOTAL DOS AMBIENTES - {locale.currency(float(InfoUsuario.total_ambientes), grouping=True)}', border=1, fill=1)
        # Quebra de linha
        self.ln(3)
        top = self.y
        self. x = 12
        offset = self.x + 60
        self.multi_cell(
            60, 6, 'CONDIÇÕES DE PAGAMENTO', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 52
        self.multi_cell(
            52, 6, 'PRAZO DE ENTREGA', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 68
        self.multi_cell(
            68, 6, 'VALIDADE DA PROPOSTA', border=1, fill=1)

        self.set_font('helvetica', '', 8)
        self.set_fill_color(250, 250, 250)
        top = self.y
        self. x = 12
        offset = self.x + 60
        self.multi_cell(
            60, 6, f'{InfoUsuario.condicoes_pagamento.upper()}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 52
        self.multi_cell(
            52, 6, f'{InfoUsuario.prazo_entrega}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 68
        self.multi_cell(
            68, 6, f'{InfoUsuario.validade_proposta.upper()}', border=1, fill=1)

        # Quebra de linha
        self.set_fill_color(200, 200, 200)
        self.ln(2.5)
        top = self.y
        self. x = 12
        offset = self.x + 8
        self.multi_cell(
            8, 6, 'PC', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 36
        self.multi_cell(
            36, 6, 'VALOR TOTAL', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 73
        self.multi_cell(
            73, 6, 'CONDIÇÕES DE PAGAMENTO COM DESCONTO', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 63
        self.multi_cell(
            63, 6, 'FORMA DE PAGAMENTO', border=1, fill=1)

        self.set_font('helvetica', '', 8)
        self.set_fill_color(250, 250, 250)
        top = self.y
        self. x = 12
        offset = self.x + 8
        self.multi_cell(
            8, 6, f'{InfoUsuario.pc}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 36
        self.multi_cell(
            36, 6, f'{locale.currency(float(InfoUsuario.valor_total), grouping=True)}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 73
        self.multi_cell(
            73, 6, f'{InfoUsuario.condicoes_pagamento_desconto.upper()}', border=1, fill=1)
        self.y = top
        self.x = offset
        offset = self.x + 63
        locale.setlocale(locale.LC_ALL, '')
        self.multi_cell(
            63, 6, f'{InfoUsuario.forma_pagamento}', border=1, fill=1)

        # Quebra de linha
        self.set_font('helvetica', '', 8)
        self.set_fill_color(250, 250, 250)
        self.ln(25)
        self.x = 41 + 12
        self.multi_cell(
            106, 6, 'RESPONSÁVEL PELA VENDA', border='T', fill=1, align='C')
