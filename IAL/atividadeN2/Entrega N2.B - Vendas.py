arquivo = open('vendas.txt', "r")
produtos = (arquivo.read()).split('\n')
for i in range(len(produtos)):
    produtos[i] = {
        "codigo": int(produtos[i].split(';')[0]),
        "quantidade": int(produtos[i].split(';')[1]),
        "preco": float(produtos[i].split(';')[2]),
    }


arquivo.close()