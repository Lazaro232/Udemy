# Classe responsável por obter as informações para preencher o PDF
class InfoUsuario():

    # CABEÇALHO
    codigo = 1037  # Número do Orçamento

    # AMBIENTE - PRIMEIRA LINHA
    ambiente = 'aa'
    quantidade = '01'
    nome_ambiente = 'sala de estar'
    fornecedor = 'home studio'
    linha = 'fabrica'
    prazo = '45'
    valor = '11200'
    # AMBIENTE - SEGUNDA LINHA
    corpo_cor = 'verde real'
    porta_cor = 'verde real'
    puxador = 'puxadores 45'
    complemento = 'tampo carvalho trevisso'
    modelo = 'móvel'

    # ASSINATURA - PRIMEIRA LINHA
    observacao = 'Alguma obs'
    # ASSINATURA - SEGUNDA LINHA
    total_ambientes = '140750'
    # ASSINATURA - TERCEIRA LINHA
    condicoes_pagamento = 'A VISTA 10% / PARCELADO'
    prazo_entrega = 'Em dias úteis conforme ambientes'
    validade_proposta = '05 dias úteis'
    # ASSINATURA - QUARTA LINHA
    pc = '01'
    valor_total = '140750'
    condicoes_pagamento_desconto = 'A VISTA 10% 126.675,00'
    forma_pagamento = '50%+50%'
