#Alexandre Lanutti, Gabriela Garcia, Sofia Akemi

import os

def ler_produtos(nome_arquivo):
    produtos = {}
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(';')
            codigo = int(partes[0])
            estoque = int(partes[1])
            minimo = int(partes[2])
            produtos[codigo] = {'estoque': estoque, 'minimo': minimo}
    return produtos

def processar_vendas(arquivo_produtos, arquivo_vendas, pasta_saida='.'):
    produtos = ler_produtos(arquivo_produtos)
    vendas_confirmadas = {}
    divergencias = []
    totais_canais = {1: 0, 2: 0, 3: 0, 4: 0}

    with open(arquivo_vendas, 'r') as arquivo:
        for num_linha, linha in enumerate(arquivo, start=1):
            partes = linha.strip().split(';')
            cod_produto = int(partes[0])
            qt_vendida = int(partes[1])
            situacao = int(partes[2])
            canal = int(partes[3])

            if cod_produto not in produtos:
                divergencias.append(f"Linha {num_linha} – Código de Produto não encontrado {cod_produto}")
                continue

            if situacao == 135:
                divergencias.append(f"Linha {num_linha} – Venda cancelada")
                continue
            elif situacao == 190:
                divergencias.append(f"Linha {num_linha} – Venda não finalizada")
                continue
            elif situacao == 999:
                divergencias.append(f"Linha {num_linha} – Erro desconhecido. Acionar equipe de TI.")
                continue
            elif situacao in (100, 102):
                vendas_confirmadas[cod_produto] = vendas_confirmadas.get(cod_produto, 0) + qt_vendida
                totais_canais[canal] += qt_vendida

    with open(os.path.join(pasta_saida, 'TRANSFERE.TXT'), 'w') as transfere:
        transfere.write(f"{'Produto':<10}{'QtCO':>7}{'QtMin':>7}{'QtVendas':>10}{'Estq.após':>12}{'Necess.':>9}{'Transf.':>10}\n")
        for codigo in produtos:
            qtCO = produtos[codigo]['estoque']
            qtMin = produtos[codigo]['minimo']
            qtVend = vendas_confirmadas.get(codigo, 0)
            estq_apos = qtCO - qtVend
            necess = max(qtMin - estq_apos, 0)
            transf = necess if necess >= 10 else (10 if necess > 0 else 0)
            transfere.write(f"{codigo:<10}{qtCO:>7}{qtMin:>7}{qtVend:>10}{estq_apos:>12}{necess:>9}{transf:>10}\n")

    with open(os.path.join(pasta_saida, 'DIVERGENCIAS.TXT'), 'w') as diverg:
        for linha in divergencias:
            diverg.write(linha + '\n')

    with open(os.path.join(pasta_saida, 'TOTCANAL.TXT'), 'w') as totcanal:
        totcanal.write(f"Canal                   QtVendas\n")
        totcanal.write(f"1 - Representantes        {totais_canais[1]}\n")
        totcanal.write(f"2 - Website               {totais_canais[2]}\n")
        totcanal.write(f"3 - App móvel Android     {totais_canais[3]}\n")
        totcanal.write(f"4 - App móvel iPhone      {totais_canais[4]}\n")
