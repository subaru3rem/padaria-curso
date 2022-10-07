def cadastro(produtos):
    Existe = True
    while Existe == True:
        import caixa
        codigo = input("cod do produto: ")
        Existe = caixa.BuscaEmListaDeListas(produtos,codigo)
        if Existe == True:
            produto = caixa.RetornarListaEmListaDeListas2(produtos,codigo)
            print("código já cadastrado como: {}. Favor cadastrar outro código diferente".format(produto[1]))
    
    nome = input("nome do produto: ")
    valor = float(input("valor do produto: "))
    quantidade = int(input("quantidade do produto: "))
    return [codigo, nome, valor, quantidade]
def exibir(produtos):
    for i in produtos:
        print("="*10)
        print("codigo:\t\t", i[0])
        print("nome:\t\t", i[1])
        print("valor:\t\t", i[2])
        print("quantidade:\t", i[3])
def adicionar(produtos):
    while True:
        x = input("qual item você deseja alterar? ")
        for i in produtos:
            if i[0] == x:
                y = int(input("atualizar quantidade: "))
                i[3] += y
                print("Quantidade atualizada com sucesso")
                return i
        print("item não encontrado")
def Alarme(produtos):
    for i in produtos:
        if i[3] < 10:
            print("*** ATENÇÃO, {} TEM MENOS DE 10 UNIDADES EM ESTOQUE. REPOR O QUANTO ANTES ***".format(i[1]))

def MenosDeDez (produtos):
    a = []
    for i in produtos:
        if i[3] < 10:
            a.append(i)
    return a

