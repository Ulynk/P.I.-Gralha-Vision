import json

produtos_json = open("produtos.json", "r")
produtos = json.load(produtos_json)
produtos_json.close()
opcao = ""
volta = ""
resposta = "S"


def linha():
    print(96 * "-")


def nomes_produto():
    with open("produtos.json", "r") as categorias_produtos:
        catprodutos = json.load(categorias_produtos)
    categorias = set(produto["categoria"] for produto in catprodutos)
    for categoria in categorias:
        print(f"{categoria}")
    categoria = input("Escolha a categoria de produto: ").upper()
    while categoria not in categorias:
        print("Categoria de produto inválida.")
        return categoria
    produtos_da_categoria = []
    for produto in produtos:
        if produto["categoria"] == categoria:
            produtos_da_categoria.append(produto)
    for produto in produtos_da_categoria:
        linha()
        print(f"Nome: {produto['nome']}\nDescrição: {produto['descricao']}\nPreço: R${produto['preco']}\n")


def cadastrar_usuario():
    global usuarios
    with open("usuarios.json", "r") as usuarios_json:
        usuarios = json.load(usuarios_json)
    nome = input("Nome: ")
    if nome in usuarios:
        print("Usuário já cadastrado.")
        return
    e_mail = input("E-mail: ")
    if e_mail in usuarios:
        print("E-mail já cadastrado.")
        return
    senha = input("Digite uma SENHA com 8 caracteres: ")
    if not senha or len(senha) < 8:
        print("Senha inválida")
        return
    usuario = {
        "nome": nome,
        "e-mail": e_mail,
        "senha": senha
    }
    usuarios.append(usuario)
    with open("usuarios.json", "w") as usuarios_json:
        json.dump(usuarios, usuarios_json)
        usuarios_json.close()
    print("Usúario cadastrado!")


def login():
    with open("usuarios.json", "r") as login_json:
        usuarioslogin = json.load(login_json)
    cadastrosnome = {cad["nome"] for cad in usuarioslogin}
    cadastrossenha = {cadsenha["senha"] for cadsenha in usuarioslogin}
    volta = 0
    while volta != 1:
        nome_usuario = input("Nome de usuário: ")
        senha_usuario = input("Senha de usuário: ")
        if nome_usuario in cadastrosnome:
            if senha_usuario in cadastrossenha:
                print(f"Log in efetuado")
                volta = 1
            else:
                print("Senha incorreta")
        else:
            print("Nome incorreto")
            print("Aperte enter para voltar")
            input()


def compra():
    with open("produtos.json", "r") as venda_produtos:
        vendas = json.load(venda_produtos)
    produto_selecionado = input("Qual o produto selecionado: ").upper()
    nomes_produtos = [venda["nome"] for venda in vendas]
    precos_produtos = [venda["preco"] for venda in vendas]

    if produto_selecionado in nomes_produtos:
        indice_produto = nomes_produtos.index(produto_selecionado)
        preco = int(precos_produtos[indice_produto])
        quantidade = int(input("Quantidade: "))
        preco_compra = preco * quantidade
        metodo_pagamento = input("Método de pagamento:[PIX, CARTÃO, BOLETO] ").upper()
        if metodo_pagamento == "CARTAO":
            metodo_pagamento2 = int(input("Deseja dividir em quantas vezes: "))
            preco_compra = preco_compra / metodo_pagamento2
            print(
                "O Pedido do produto {} {} foi realizado no valor de {}x de R${:.2f} pagamento via {}".format(quantidade,
                                                                                                             produto_selecionado,
                                                                                                             metodo_pagamento2,
                                                                                                             preco_compra,
                                                                                                             metodo_pagamento))
        elif metodo_pagamento == "BOLETO" or "PIX":
            print("O Pedido do produto {} {} foi realizado no valor de R${},00 pagamento via {}".format(quantidade,
                                                                                                        produto_selecionado,
                                                                                                        preco_compra,
                                                                                                        metodo_pagamento))
    else:
        print("Produto não encontrado na lista de vendas.")


linha()
print(15 * "-" + "Bem Vindo a Gralha Esporte, a loja número 1 em materias esportivos" + "-" * 15)
while resposta == "S":
    while opcao != "3":
        linha()
        print(46 * "-" + "Menu" + 46 * "-")
        print("1. Cadastrar usuário")
        print("2. Comprar produto")
        print("3. Sair")
        opcao = input("Opção: ")
        linha()
        if opcao == "1":
            print(39 * "-" + "Menu para Cadastro" + 39 * "-")
            cadastrar_usuario()
        elif opcao == "2":
            print(28 * "-" + "Digite a categoria de materiais desejada" + "-" * 28)
            nomes_produto()
            login()
            compra()
        else:
            print()
            resposta = "N"
resposta = input("Deseja comprar outro produto: [S/N]").upper()
print("Espero que tenha conseguido achar o produto querido, Agradecemos pela preferência!")
linha()
