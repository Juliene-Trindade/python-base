#!/usr/bin/python3


email_tmpl = """
    Olá, %(nome)s!

    Tem interesse em comprar nossa %(produto)s?

    Este produto é ótimo para resolver %(texto)s!

    Clique agora em %(link)s

    APENAS %(quantidade)d UNIDADES DISPONÍVEIS!!!!

    Preço promocional %(preco).2f
    """

clientes = ["Maria", "João", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "um problema complexo demais para ser digitado",
            "link": "https://hackeeivoce.com.br",
            "quantidade": 30,
            "preco": 99.9     
        }
    )   
