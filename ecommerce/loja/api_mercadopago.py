import mercadopago

public_key = "APP_USR-f7b9d816-56f4-4743-9dcd-236826dcf675"
token = "APP_USR-6587556615183950-042416-92b1d55702c386ed4ac1b531b8e72194-2408205438"

def criar_pagamento(itens_pedido, link):
    # Configure as credenciais
    sdk = mercadopago.SDK(token)
    # Crie um item na preferência

    # itens que ele está comprando no formato de dicionário
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            "title": nome_produto,
            "quantity": quantidade,
            "unit_price": preco_unitario,
        })

    # valor total
    preference_data = {
        "items": itens,
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link,
        }
    }
    # Crie a preferência de pagamento
    resposta = sdk.preference().create(preference_data)
    link_pagamento= resposta["response"]["init_point"]
    id_pagamento = resposta["response"]["id"]
    return link_pagamento, id_pagamento
