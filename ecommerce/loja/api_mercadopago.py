import mercadopago

public_key = "APP_USR-f7b9d816-56f4-4743-9dcd-236826dcf675"
token = "APP_USR-6587556615183950-042416-92b1d55702c386ed4ac1b531b8e72194-2408205438"

# Configure as credenciais
sdk = mercadopago.SDK(token)
# Crie um item na preferência

# itens que ele está comprando no formato de dicionário
# valor total
preference_data = {
    "items": [
        {
            "title": "My Item",
            "quantity": 1,
            "unit_price": 75.76,
        }
    ],
    "back_urls": {
        "success": link,
        "pending": link,
        "failure": link,
    }
}
# Crie a preferência de pagamento
resposta = sdk.preference().create(preference_data)
link = resposta["response"]["init_point"]
id_pagamento = resposta["response"]["id"]
print(link)
