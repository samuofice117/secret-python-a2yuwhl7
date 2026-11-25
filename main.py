from negocio import cadastrar_produto, realizar_venda
from dados import listar_todos

def menu():
  while True:
    print("\n--- MERCADINHO DEV ---")
    print("1. Cadastrar Produto (Entrada)")
    print("2. Vender Produto (Saída)")
    print("3. Ver Estoque")
    print("4. Sair")
    opcao = input("Escolha: ")

    if opcao == '1':
      nome = input("Nome do produto")
      preco = float(input("Preço unitário: "))
      qtd = int(input("quantidade: "))

      sucesso, mensagem = cadastrar_produto(nome ,preco , qtd)
      print(mensagem)

    elif opcao == '2':
      nome = input ("Nome do produto para vneder: ")
      qtd = int(input("Quantidade desejada: "))

      sucesso, mensagem = realizar_venda(nome, qtd)
      print(mensagem)

    elif opcao == '3':
      lista = listar_todos()
      print("\n--- RELATÓRIO DE ESTOQUE ---")
      for item in lista:
          print(f"Produto: {item['nome']} | R$ {item['preco']} | Qtd: {item['qtd']})

    elif opcao == '4':
      print("Fechando sistema...")
      break
    else:
      print("opção inválida!")

menu()
