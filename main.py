import produtos,caixa,json

f = open("testeprodutos.txt", "r")
lista = json.loads(f.read())
f.close()
certeza = ""

while certeza != "s":
  produtos.Alarme(lista)
  print("=== Padaria Python ===")
  print("Menu")
  print("1 - Cadastra Produtos")
  print("2 - Exibir Produtos")
  print("3 - Alterar Produtos")
  print("4 - Venda")
  print("5 - Produtos com menos de 10 unidades")
  print("0 - Sair")
  
  escolha=int(input("Escolha uma opção: "))
  if escolha == 1:
    lista.append(produtos.cadastro(lista))
  if escolha== 2:
    print("Exibindo produtos...")
    produtos.exibir(lista)
    print ("Total de produtos cadastrados na loja: {}".format(len(lista)))
  if escolha== 3:
    produtos.adicionar(lista)
  if escolha == 4:
    caixa.caixa(lista)
  if escolha == 5:
    menosdedez = produtos.MenosDeDez(lista)
    produtos.exibir(menosdedez)
  if escolha == 0:
    certeza = input("Tem certeza que quer sair? (s - sim | Qualquer tecla - não)")
    if certeza == "s":
      print("volte sempre")
      xport = json.dumps(lista)
      f = open("testeprodutos.txt", "w")
      f.write(xport)
      f.close()
      