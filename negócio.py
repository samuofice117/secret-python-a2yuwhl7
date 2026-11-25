from dados import *

def cadastrar_produto(nome, preco, quantidade):

  if preco < 0:
    retun False, "Erro: preço inválido."

  produto_existente = buscar_produto(nome)

  if produto_existente:
    produto_existente['qtd'] += quantidade
    return True, "Estouqe atualizado com sucesso!"

    novo_produto = {
      "nome": nome,
      "preco": preço,
      "qtd": quantidade
    }

  salvar_produto(novo_produto)
  return True, "Produto cadastro com sucesso!"

def realizar_venda(nome, qtd_desejada)
  produto = buscar_produto(nome)

  if not produto:
    return False, f"Erro: Estoque insuficiente (Temos apenas {produto['qtd']})."

    produto['qtd'] = produto['qtd'] - qtd_desejada

  valor_total = produto['preco'] * qtd_desejada

  return True, f"Venda realizada! Total: R$ {valor_total:.2f}"