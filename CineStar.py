precos_das_sessoes = [] # Será usada, para armazenar os preços das sessões separadas, para poder auxiliar no cálculo das vendas da entrada
vendas_das_sessoes = [] # Onde será armazenado o lucro, por sessão #
nome_das_sessoes = [] # Será armazenado os nomes das sessões e seus respectivos filmes. #
numero_das_sessoes = [] # Será adicionado os números de cada sessão. #
cadeiras_disponiveis =[]
venda_total = float(0.0)
while True:
    a = int(0)
    sessoes = []
    cadeiras_vazias = []
    cadeiras_preenchidas = []
    opcao_entrada = ''
    valida_entrada = False
    print('-' * 91)
    print(' ' * 37, 'CINE STAR', ' ' * 37)
    print('-' * 91)
    
    def separar(linha, atributo): # Função para separar o elementos da linha por vírgula e transformar eles elementos de um array. #
        arrayDeValores = []
        aux = ''
        for i in range(len(linha)):
            if linha[i] != atributo:
                aux = aux + str(linha[i])
            else:
                arrayDeValores += [apagarEspaco(aux)]
                aux = ''
        arrayDeValores += [apagarEspaco(aux).replace("\n", "")]
        return arrayDeValores

    def tirarVirgula(palavra): # Essa função será necessária para formatação dos valores em R$, apenas para tirar a virgula das variáveis do tipo: float. #
        saida = ''
        for i in range(len(palavra)):
            if palavra[i] == '.': # Faz a verificação de cada elemento da palavra, pra quando encontrar um ".", substituir pela vírgula. #
                saida += ','
            else:
                saida+= palavra[i]
        return saida # Retorna a saida, que neste caso é palavra já substituida o ponto pela vírgula. #

    def apagarEspaco(palavra): # Essa função foi necessária, pois antes dos elementos do array foi observado que ficava um espaço. #
        tam = len(palavra)
        saida = ""
        for i in range(tam):
            if not((i == 0) and (palavra[i] == " ")):
                saida += palavra[i]   
        return saida

    def mudarParaFloat(valor): # Essa função será necessária para auxiliar o campo da variável do valor da entrada, para depois convertê-la em float. #
        saida = ''
        for i in range(len(valor)):
            if valor[i] == ',': # Faz a verificação de cada elemento da palavra, pra quando encontrar um ",", substituir pela ponto. #
                saida += '.'
            else:
                saida+= valor[i]
        saida = float(saida)
        return saida # Retorna a saida, que neste caso é palavra já substituida o ponto pela ponto. #

    def cadastrarSessoes(): #Função para cadastrar as sessões que serão apresentadas no dia. #
        cadeiras_vazias = int(0)
        continuar = ''
        contador = int(1)
        arquivo_sessoes = open('Sessões do dia.txt', 'w')
        while continuar != '1':
            print('-' * 24, '    Cadastrar Sessões do dia    ', '-' * 24)
            print()
            cadeiras_vazias = int(0)
            valor_entrada_valido = False
            continuar_valido = False
            cadeiras_vazias_valido = False
            nome_sessao = input('➢  Informe o nome do filme da sessão: ')
            horario = input('➢  Horário da sessão: ')
            print('➢  Informe o valor da entrada: ', end = '')
            while not(valor_entrada_valido): # Esse While servirá para um tratamento de erro, caso o usuário do sistema digite um valor inválido no campo "valor da entrada",. ele ficará perguntando até o usuário digitar um valor válido. #
                try:
                    valor_entrada = input()
                    valor_entrada = float(valor_entrada)
                    valor_entrada_valido = True
                except:
                    print('⚠ O valor da entrada é inválido, por favor, informe um valor válido: ', end = '')
            print()
            print('➢  Informe quantas cadeiras terão disponíveis para esta sessão: ', end= '')
            while not(cadeiras_vazias_valido):
                try:
                    cadeiras_vazias = int(input())
                    cadeiras_vazias_valido = True
                except:
                    print('⚠ Número de cadeiras vazias não válido, por favor, informe um valor válido: ', end = '')
            print('')
            print('-' * 87)
            valor_entrada_texto = tirarVirgula(str(f'{valor_entrada:.2f}'))
            valor_meia = valor_entrada / 2
            valor_meia_texto = tirarVirgula(str(f'{valor_meia:.2f}'))
            arquivo_sessoes = open('Sessões do dia.txt', 'a')
            arquivo_sessoes.write(f'{contador}º sessão: {nome_sessao} - Horário: {horario} - Valor da entrada inteira: R$ {valor_entrada_texto} - Valor entrada meia: R$ {valor_meia_texto} - {cadeiras_vazias} cadeiras disponíveis;\n')
            contador += 1
            print('➢  Digite 1 para encerrar, ou 2 para continuar...', end = '')
            while not(continuar_valido): # Esse While servirá para um tratamento de erro, caso o usuário do sistema digite uma opção inválida no campo "continuar",. ele ficará perguntando até o usuário digitar uma opção válida. #
                continuar = input('')
                if continuar == '1' or continuar == '2':
                    continuar_valido = True
                else:
                    print('⚠ A opção informada é inválida! Digite 1 para encerrar, ou 2 para continuar...', end = '')
            print('-' * 87)
            print()
        arquivo_sessoes.close()

    def adicionarSessao():
        contador = int(1)
        arquivo = open('Sessões do dia.txt', 'r')
        for linha in arquivo.readlines():
            contador += 1
        continuar = ''
        while continuar != '1':
            print('-' * 24, '    Adicionar sessões ao dia    ', '-' * 24)
            print()
            cadeiras_vazias = int(0)
            valor_entrada_valido = False
            continuar_valido = False
            cadeiras_vazias_valido = False
            nome_sessao = input('➢  Informe o nome do filme da sessão: ')
            horario = input('➢  Horário da sessão: ')
            print('➢  Informe o valor da entrada: ', end = '')
            while not(valor_entrada_valido): # Esse While servirá para um tratamento de erro, caso o usuário do sistema digite um valor inválido no campo "valor da entrada",. ele ficará perguntando até o usuário digitar um valor válido. #
                try:
                    valor_entrada = input()
                    valor_entrada = float(valor_entrada)
                    valor_entrada_valido = True
                except:
                    print('⚠ O valor da entrada é inválido, por favor, informe um valor válido: ', end = '')
            print()
            print()
            print('➢  Informe quantas cadeiras terão disponíveis para esta sessão: ', end= '')
            while not(cadeiras_vazias_valido):
                try:
                    cadeiras_vazias = int(input())
                    cadeiras_vazias_valido = True
                except:
                    print('⚠ Número de cadeiras vazias não válido, por favor, informe um valor válido: ', end = '')
            print('')
            print('-' * 87)
            valor_entrada_texto = tirarVirgula(str(f'{valor_entrada:.2f}'))
            valor_meia = valor_entrada / 2
            valor_meia_texto = tirarVirgula(str(f'{valor_meia:.2f}'))
            arquivo_sessoes = open('Sessões do dia.txt', 'a')
            arquivo_sessoes.write(f'{contador}º sessão: {nome_sessao} - Horário: {horario} - Valor da entrada inteira: R$ {valor_entrada_texto} - Valor entrada meia: R$ {valor_meia_texto} - {cadeiras_vazias} cadeiras disponíveis;\n')
            contador += 1
            print('➢  Digite 1 para encerrar, ou 2 para continuar...', end = '')
            while not(continuar_valido): # Esse While servirá para um tratamento de erro, caso o usuário do sistema digite uma opção inválida no campo "continuar",. ele ficará perguntando até o usuário digitar uma opção válida. #
                continuar = input('')
                if continuar == '1' or continuar == '2':
                    continuar_valido = True
                else:
                    print('⚠ A opção informada é inválida! Digite 1 para encerrar, ou 2 para continuar...', end = '')
            print('-' * 72)
            print()
        arquivo.close()        

    def mostrarSessoes():
        global cadeiras_disponiveis
        cont = int(0)
        arquivo = open('Sessões do dia.txt', 'r')
        for linha in arquivo.readlines(): #Esse laço servirá para captar os preços das sessões cadastradas, e irá acrascentálas em um Array, inicialmente chamado de: precos_das_sessoes. #
                verificacao = separar(linha, '-') # Aqui iremos separar a linha da sessão, pelo atributo "-". #
                separar_numero_cadeiras = separar(verificacao[4], ' ')
                disponiveis = (separar_numero_cadeiras[0])
                disponiveis = int(disponiveis)
                separar_numero_cadeiras[0] = disponiveis
                cadeiras_disponiveis += [disponiveis]
                parte_da_verificacao = verificacao[0:4]
                for k in range(len(parte_da_verificacao)):
                    print(parte_da_verificacao[k], end = ' - ')
                print(f'{cadeiras_disponiveis[cont]} Cadeiras disponiveis.')
                print()
                cont += 1
        
            
    def extrairDados():
        global precos_das_sessoes # Será usada, para armazenar os preços das sessões separadas, para poder auxiliar no cálculo das vendas da entrada
        global vendas_das_sessoes
        global nome_das_sessoes
        global numero_das_sessoes
        global cadeiras_disponiveis
        arquivo = open('Sessões do dia.txt', 'r')
        for linha in arquivo.readlines(): #Esse laço servirá para captar os preços das sessões cadastradas, e irá acrascentálas em um Array, inicialmente chamado de: precos_das_sessoes. #
                verificacao = separar(linha, '-') # Aqui iremos separar a linha da sessão, pelo atributo "-". #
                nome_dessa_sessao = verificacao[0] # Colhe o nome da sessão que esta na posição [0], do array verificação da linha do arquivo. #
                nome_dessa_sessao = str(nome_dessa_sessao) # Após colher o nome da sessão, a converte em uma variável do tipo String, para podermos adicionar a lista nomes_das_sessões, servirá mais a frente para podermos informar qual sessão obeteve melhor venda.#
                nome_das_sessoes += [nome_dessa_sessao]
                #pegaremos o 1º caraceter do nome da sessão, e a convertemos em um variável do tipo int, para em seguida adicionarmos o número dessa sessão a um array de valores correspondente. #
                numero_dessa_sessao = nome_dessa_sessao[0]
                numero_dessa_sessao = int(numero_dessa_sessao)
                numero_das_sessoes += [numero_dessa_sessao]
                campo_valor_entrada = verificacao[2] # O valor da sessão está no campo 3 (posição[2], da verificação)#
                campo_valor_entrada = separar(campo_valor_entrada, ' ') # O campo do valor da valor da entrada será "quabrado, para chegarmos ao valor desse ingresso. "#
                valor_da_entrada_float = mudarParaFloat(campo_valor_entrada[5]) # Aqui iremos tirar a virgula, para converterter o valor da variável, que até aqui é uma string, para uma variável do tipo float. para em seguida, jogar os preços da entrada em em array. #
                precos_das_sessoes += [valor_da_entrada_float] # Acrescentaremos os preços das entradas a um array, para mais a frente usarmos no lucro da sessão;
        for i in range(len(nome_das_sessoes)):
                a = int(0)
                vendas_das_sessoes += [a]

    def bilheteria():
        print('-' * 34, '    Bilheteria    ', '-' * 34)
        print()
        global numero_das_sessoes
        global vendas_das_sessoes
        global cadeiras_disponiveis
        tamanho_lista_nomes = int(len(nome_das_sessoes ))
        tamanho_lista_vendas = int(len(vendas_das_sessoes))
        venda = float(0.0)
        opcao = int(0)
        opcao_valida = False
        opcao_meia = int(0)
        opcao_meia_valida = False
        contador = int(0)
        mostrarSessoes() #Chamar a função para mostrar as seções disponíveis e suas respectivas informações. #
        arquivo = open('Sessões do dia.txt', 'r')
        for linha in arquivo.readlines(): # Servirá apenas para mais adiante fazermos uma verificação , para quando u úsuario digitar um valor maior ou diferente da quantidade de sessões, mostrarmos uma mensagem de erro. #
                contador += 1
        arquivo.close()
        
        print('➢  Dentre as opções acima, escolha a que você deseja comprar a entrada: ' ,end = '')
        while not(opcao_valida): # Esse While servirá para um tratamento de erro, caso o usuário do sistema digite um valor inválido no campo "valor da entrada",. ele ficará perguntando até o usuário digitar um valor válido. #
                try:
                        opcao = int(input())
                        if opcao > 0 and opcao <=contador: # Esse IF irá amarrar ainda mais o campo da ''opção", pois ele só permitirá que a sessão que o cliente deseja comprar o ingresso sseja apenas uma das opções (neste caso as sessões) disponíveis. #
                                opcao_valida = True
                        else:
                                print('⚠ O número da sessão é inválido, por favor, informe uma sessão válida: ', end = '')
                except:
                        print('⚠ O número da sessão é inválido, por favor, informe uma sessão válida: ', end = '')
        print()
        print('Esta entrada é do tipo inteira, ou meia?')
        print('➢  Digite 1 para entrada do tipo inteira, ou 2 para entrada do tipo meia: ', end = '')
        while not(opcao_meia_valida):
                try:
                        opcao_meia = int(input())
                        if (opcao_meia == 1) or (opcao_meia == 2):
                                opcao_meia_valida = True
                        else:
                                print('⚠ A opção informada é inválida, por favor, informe uma opção válida: ', end = '')
                except:
                        print('⚠ A opção informada é inválida, por favor, informe uma opção válida: ', end = '')
        print()
        if opcao_meia_valida:
                if opcao_meia == 1:
                        for j in range(tamanho_lista_vendas):
                                if opcao == numero_das_sessoes[j]:
                                        venda = precos_das_sessoes[j]
                                        temp = venda + vendas_das_sessoes[j]
                                        vendas_das_sessoes[j] = temp
                                        aux = cadeiras_disponiveis[j]
                                        cadeiras_disponiveis[j] = aux -1

                        print('-' *12, '  Venda realizada com sucesso, volte sempre no nosso cinema!  ', '-' * 12)
                else:
                        for j in range(tamanho_lista_vendas):
                                if opcao == numero_das_sessoes[j]:
                                        venda = precos_das_sessoes[j]
                                        venda = venda / 2
                                        temp = venda + vendas_das_sessoes[j]
                                        aux = cadeiras_disponiveis[j]
                                        cadeiras_disponiveis[j] = aux -1
                                        vendas_das_sessoes[j] = temp
                        print('-' *12, '  Venda realizada com sucesso, volte sempre no nosso cinema!  ', '-' * 12)
        print()

    def resumoDasVendas():
        print('-' * 27, '    Resumo das vendas    ', '-' * 27)
        print()
        global venda_total
        global vendas_das_sessoes
        global nome_das_sessoes

        for j in range(len(vendas_das_sessoes)):
            vendas = vendas_das_sessoes[j]
            venda_total += vendas
            vendas_txt = tirarVirgula(str(f'{vendas:.2f}'))
            print(f'{nome_das_sessoes[j]} R${vendas_txt}')
        venda_total_txt = tirarVirgula(str(f'{venda_total:.2f}'))
        print(f'➢ As vendam somam: R${venda_total_txt}')
        print()
        print('-' * 91)
        print()
   
    print('-' * 30, '     Menu principal    ', '-' * 30)
    print('-' * 87)
    print()
    print('Dentre as opções abaixo:',
          '\n\n0 - Encerrar o programa;',
          '\n1 - Cadastrar sessões do dia;',
          '\n2 - Adicionar sessões ao dia;',
          '\n3 - Mostrar sessões do dia;',
          '\n4 - Bilheteria;',
          '\n5 - Resumo das vendas;',
          '\n\nInfome qual você deseja seguir: ', end = '')
    while not(valida_entrada): # Esse While servirá para um tratamento de erro, caso o usuário do sistema digite uma opção inválida no campo "opções",. ele ficará perguntando até o usuário digitar uma opção válida. #
        opcao_entrada = input('')
        if  (opcao_entrada == '0') or (opcao_entrada == '1') or (opcao_entrada == '2') or (opcao_entrada == '3') or (opcao_entrada == '4') or (opcao_entrada == '5'):
            valida_entrada = True
            opcao_entrada = int(opcao_entrada)
        else:
            print('⚠ A opção informada é inválida, por favor, informe uma opção válida:', end = '')
    print()
    if valida_entrada:
        if (opcao_entrada == 0):
            print(cadeiras_disponiveis)
            print(precos_das_sessoes)
            print(vendas_das_sessoes)
            print(nome_das_sessoes)
            print(numero_das_sessoes)
            print(cadeiras_disponiveis)
            break
        if (opcao_entrada == 1):
            cadastrarSessoes()
        if (opcao_entrada == 2):
            adicionarSessao()
        if (opcao_entrada == 3):
            mostrarSessoes()
        if (opcao_entrada == 4):
            extrairDados() # Chamada da função extrairDados(), para atuar junto com a função bilheteria ().#
            continuar = int(0)
            while (continuar != '1'):
                bilheteria()
                continuar_valido = False
                print('➢  Digite 1 para encerrar, ou 2 para comprar outra entrada: ', end = '')
                while not(continuar_valido):
                        continuar = input('')
                        if continuar == '1' or continuar == '2':
                                continuar_valido = True
                        else:
                                print('⚠ A opção informada é inválida! Digite 1 para encerrar, ou 2 para continuar: ', end = '')
            print('-' * 113)
            print()
        if (opcao_entrada == 5):
            resumoDasVendas()
