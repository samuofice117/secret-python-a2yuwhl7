estoque=[]
  def salvar_produto(produto)
  estoque.append(produto)

  def listar_todos():
  return estoque  

  def buscar_produto(nome):
    for item in estoque
      if item['nome'] == nome
        return item
    return None 