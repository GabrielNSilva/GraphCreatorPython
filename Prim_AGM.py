from copy import deepcopy
# grafo={'a': ['b', 'e'], 'b': ['a', 'e', 'c', 'd'], 'c': ['b', 'd'], 'd': ['b', 'e', 'c'], 'e': ['d', 'a', 'b']}
# print(grafo)
grafo = dict()
grafo = {
    "0": {"1": 6, "2": 1, "3": 5},
    "1": {"0": 6, "2": 2, "4": 5},
    "2": {"0": 1, "1": 2, "3": 2, "4": 6, "5": 4},
    "3": {"0": 5, "2": 2, "5": 4},
    "4": {"1": 5, "2": 6, "5": 3},
    "5": {"2": 4, "3": 4, "4": 3}
}
agm = dict()


def ins_v(g, nome):
	g[nome] = dict()


def ins_e(g, n1, n2, p):
	if n1 in g and n2 in g:
		g[n1][n2] = p
		g[n2][n1] = p
	else:
		print('***Vertices inexistentes!!***')


def rem_v(g, v):
	if v in g:
		keys = list(g['n1'].keys())
		for k in keys:
			g[k].pop(v)

		g.pop(v)
		# print('Vertice removido com sucesso!')
	else:
		print('***Vertice inexistente!***')


def rem_e(g, v1, v2):
	if v1 in g and v2 in g:
		if v2 in g[v1] and v1 in g[v2]:
			g[v1].pop(v2)
			g[v2].pop(v1)
			# print('Aresta removida com sucesso!')
		else:
			print('**Não existe aresta entre os vertices na direção informada!**')
	else:
		print('***Vertices inexistentes!!***')


def mostra(g):
	if len(g) == 0:
		print('***Grafo vazio!***')
	else:
		for v, es in g.items():
			print()
			print('Vertice '+v+':')
			print('\tArestas:')
			if len(es) == 0:
				print('\t\tSem arestas')
			else:
				for viz, p in es.items():
					# print('\t\t'+v,'———',p,'———',viz)
					print('\t\t'+v,'---',p,'---',viz)


    # for v in g.keys():
    #     if v not in agm:
    #         agm[v] = dict()
def gerar_agm():
    print('GERANDO AGM....')
    g = deepcopy(grafo)
    agm = dict()
    mostra(agm)

    # selecionando um vertice qualquer para iniciar PRIM
    keys = list(g.keys())
    v = keys.pop()
    ins_v(agm, v)
    inseridos = [v]
    print('Comecou pelo',v)

    while len(agm) < len(g):
        print('Loop..............................................................................')
        menor = dict()

        # verifica aresta de menor peso entre os vertices inserido
        print('Inseridos',inseridos)
        for x in inseridos:
            for y, p in g[x].items():
                print('Verificando',x,'---',p,'---',y)
                if not menor or p < menor['peso']:
                    menor = {'viz': x, 'vertice': y, 'peso': p}
                print('\tMENOR: ',menor['viz'],'---',menor['peso'],'---',menor['vertice'])

        # Armazenando vertice na listagem dos inseridos
        inseridos.append(menor['vertice'])
        # Inserindo vertice e criando a aresta
        ins_v(agm, menor['vertice'])
        ins_e(agm, menor['vertice'], menor['viz'], menor['peso'])
        print('Selecionada aresta',menor['viz'],'---',menor['peso'],'---',menor['vertice'])

        # remove aresta do grafo base, para n re escolhe-la
        rem_e(g, menor['vertice'], menor['viz'])
        # break
    return agm


while True:
	print()
	print('1. Cadastrar/Editar Grafo')
	print('2. Visualizar Grafo')
	print('3. Calcular AGM (Árvore Gradora Mínima) do grafo')
	print('0. Sair')

	op = input()
	# print(op)

	if op == '1':
		while True:
			print()
			print('a) Inserir Vertices')
			print('b) Inserir Arestas')
			print('c) Remover Vertice')
			print('d) Remover Aresta')
			print('e) Sair')
			op1 = input()
			if op1 == 'a' or op1 == 'A':
				print()
				nomes = input(
					'Digite os nomes dos vertices separados por um espaço: ').split()
				for vert in nomes:
					ins_v(grafo, vert)
			elif op1 == 'b' or op1 == 'B':
				print()
				n1, n2 = input(
					'Digite (separados por um espaço) os vertices ligados por esta aresta: ').split()
				p = int(input('Digite um valor numerico para o peso desta ligação: '))
				ins_e(grafo, n1, n2, p)
			elif op1 == 'c' or op1 == 'C':
				print()
				v = input('Digite os nomes dos vertices separados por um espaço: ').split()
				for vert in v:
					rem_v(grafo, vert)
			elif op1 == 'd' or op1 == 'D':
				print()
				v1, v2 = input(
					'Digite (separados por um espaço) os vertices a serem desconectados: ').split()
				rem_e(grafo, v1, v2)
			elif op1 == 'e' or op1 == 'E':
				break
			else:
				print()
				print('***Opção Inválida***')

	elif op == '2':
		mostra(grafo)
	elif op == '3':
		agm = gerar_agm()
		print('\n----------ÁRVORE GERADORA MÍNIMA----------')
		mostra(agm)
	elif op == '0':
		break
	else:
		print()
		print('***Opção Inválida***')
