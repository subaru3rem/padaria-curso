from xmlrpc.client import boolean

def ExibirCompras (listadedicionarios):
    pos = 0
    print("Item\tCód\tNome\tQtd\tVl Un.\tValor")
    for i in listadedicionarios:
        pos += 1
        codigo=i["codigo"]
        nome = i["nome"]
        valor_unit = i["valor"]
        qtd_venda = i["qtd_venda"]
        receita = i["receita"]
        print("{}\t{}\t{}\t{}\t{:.2f}\t{:.2f}".format(pos,codigo,nome[:6],qtd_venda,valor_unit,receita))

def BuscaEmListaDeListas(listadelistas,x):
    for i in listadelistas:
        if i[0] == x:
            return True

def RetornarListaEmListaDeListas2(listadelistas,x):
    for i in listadelistas:
        if i[0] == x:
            return i

def CalculaTotal(listadedicionarios):
    total = 0
    for x in listadedicionarios:
        total += x["receita"]
    return total

def Verificar(minimo,maximo,valoraverificar):
    return False if valoraverificar < minimo or valoraverificar > maximo else True

def AtualizarEstoque(ListaEstoque,Carrinho):
    for i in Carrinho:
        for x in ListaEstoque:
            if i["codigo"] == x[0]:
                x[3] -= i["qtd_venda"]
    return ListaEstoque

def CancelarItem(listadedicionarios):
    while True:
        QualItem = int(input("Qual item será cancelado?"))
        Ok = Verificar(1,len(listadedicionarios),QualItem)
        if Ok == False:
            print("opção inválida. Escolha entre 1 e {}".format(len(listadedicionarios)))
        else:
            ItemDoCarrinho = listadedicionarios[QualItem-1] #ItemDoCarrinho é um dicionário
            break

    while True:
        Quantos = int(input("Quantos itens de {} serão cancelados?".format(ItemDoCarrinho["nome"])))
        Ok = Verificar(1,ItemDoCarrinho["qtd_venda"],Quantos)
        if Ok == False:
            print("opção inválida. Escolha entre 1 e {}".format(ItemDoCarrinho["qtd_venda"]))
        else:
            ItemDoCarrinho["qtd_venda"] -= Quantos
            ItemDoCarrinho["receita"] = ItemDoCarrinho["qtd_venda"] * ItemDoCarrinho["valor"]
            listadedicionarios[QualItem-1] = ItemDoCarrinho
            break
    return listadedicionarios

def Comprar(listadelistas):
    while True:
        Codigo = (input  ("Insira o codigo do produto: ")) #100
        Ok = BuscaEmListaDeListas(listadelistas,Codigo)
        if Ok == True:
            ProdutoList = RetornarListaEmListaDeListas2(listadelistas,Codigo)
            if ProdutoList[3] == 0:
                print("não temos mais esse produto em estoque")
            Indice = listadelistas.index(ProdutoList)
            return [ProdutoList,Indice]
        else:
            print("Produto não encontrado")

def Quantidade(produto): #o produto é uma lista do tipo [nome,codigo,valor,qtd]
    while True:
        qtd = int(input("insira a qtd: "))
        if produto[3] >= qtd:
            ItemDoCarrinho = {
                "codigo":produto[0],
                "nome":produto[1],
                "valor":produto[2],
                "qtd_estoque":produto[3],
                "receita":(qtd*produto[2]),
                "qtd_venda":qtd
            }
            return ItemDoCarrinho
        else:
            print("Quantidade insuficiente em estoque. insira um valor <= {}".format(produto[3]))

def Cancela(listadedicionarios):
    Cancela = int(input("1 - Continuar comprando\n2 - cancelar item\n3 - cancelar compra\n"))
    Ok = Verificar(1,3,Cancela)
    if Ok == True:
        if Cancela == 1: return 1
        if Cancela == 2:
            listadedicionarios = CancelarItem(listadedicionarios)
            return 2
        if Cancela == 3: return 3

def caixa (produtos): #produtos é uma lista de listas
    p = produtos.copy()
    Carrinho = []
    print("=== Caixa ===")
    Fim = "s"
    while Fim == "s":
        Lista1 = Comprar(p) #Lista1 = ["produto","indice de produto em produtos"]
        ItemDoCarrinho = Quantidade(Lista1[0]) #ItemDoCarrinho é um dicionário
        Carrinho.append(ItemDoCarrinho) #Carrinho é uma lista de dicionários
        #p[Lista1[1]][3] -= ItemDoCarrinho["qtd_venda"] #Atualização da cópia da lista principal(produtos)
        OutroProduto = input("Outro produto? (s - sim | qualquer tecla - não)").strip().lower()
        while OutroProduto != "s":
            ExibirCompras(Carrinho)
            Confirma = input("Valor Total = {:.2f}\nConfirma compra? (s - sim | qualquer tecla - não)".format(CalculaTotal(Carrinho))).strip().lower()
            if Confirma == "s":
                produtos = AtualizarEstoque(produtos,Carrinho)
                ValorRecebido = float(input("Valor recebido: "))
                Troco = ValorRecebido - CalculaTotal(Carrinho)
                print("Troco : {}\nVolte Sempre!".format(Troco))
                return produtos
            else:
                DecisaoCancela = int(Cancela(Carrinho))
                if DecisaoCancela == 1: #continuar comprando
                    OutroProduto = "s"
                if DecisaoCancela == 2: #cancela item e volta na parte Exibir compras (line 113)
                    continue
                if DecisaoCancela == 3: #não faz nada e sai da função caixa devolvendo a lista como veio
                    return produtos