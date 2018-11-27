from copy import deepcopy
# grafo={'a': ['b', 'e'], 'b': ['a', 'e', 'c', 'd'], 'c': ['b', 'd'], 'd': ['b', 'e', 'c'], 'e': ['d', 'a', 'b']}
# print(grafo)
grafo = dict()
agm = dict()


def ins_v(nome):
	grafo[nome] = dict()


def ins_e(n1, n2, p):
	if n1 in grafo and n2 in grafo:
		grafo[n1][n2] = p
		grafo[n2][n1] = p
	else:
		print('***Vertices inexistentes!!***')


def rem_v(v):
	if v in grafo:
		keys = list(grafo['n1'].keys())
		for k in keys:
			grafo[k].pop(v)

		grafo.pop(v)
		print('Vertice removido com sucesso!')
	else:
		print('***Vertice inexistente!***')


def rem_e(v1, v2):
	if v1 in grafo and v2 in grafo:
		if v2 in grafo[v1] and v1 in grafo[v2]:
			grafo[v1].pop(v2)
			grafo[v2].pop(v1)
			print('Aresta removida com sucesso!')
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
				for viz, p in es:
					print('\t\t'+v,'———',p,'———',viz)


def vizinhos(v):
	if v in grafo:
		print('Adjacentes à '+v)
		for viz, p in grafo[v]:
			print('\t'+v,'———',p,'———',viz)
	else:
		print('***Vertice inexistente!***')


def ligados(v1, v2):
	if v1 in grafo and v2 in grafo:
		if v2 in grafo[v1] or v1 in grafo[v2]:
			print('Os vertices informados estão ligados da seguinte forma:')
			print('\t'+v1,'———',grafo[v1][v2],'———',v2)
		else:
			print('**Não existe aresta entre os vertices informados!**')
	else:
		print('***Vertices inexistentes!!***')


def grau(v):
	if v in grafo:
		print('Grau de '+v+':',len(grafo[v]))
	else:
		print('***Vertice inexistente!***')


def gerar_agm():
	agm = deepcopy(grafo)
	


while True:
	print()
	print('1. Cadastrar/Editar Grafo')
	print('2. Visualizar Grafo')
	print('3. Buscar Vertices Adjacentes')
	print('4. Buscar Aresta entre dois Vertices')
	print('5. Calcular Grau de um Vertice')
	print('6. Calcular AGM (Árvore Gradora Mínima) do grafo')
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
					ins_v(vert)
			elif op1 == 'b' or op1 == 'B':
				print()
				n1, n2 = input(
					'Digite (separados por um espaço) os vertices ligados por esta aresta: ').split()
				p = int(input('Digite um valor numerico para o peso desta ligação: '))
				ins_e(n1, n2, p)
			elif op1 == 'c' or op1 == 'C':
				print()
				v = input('Digite os nomes dos vertices separados por um espaço: ').split()
				for vert in v:
					rem_v(vert)
			elif op1 == 'd' or op1 == 'D':
				print()
				v1, v2 = input(
					'Digite (separados por um espaço) os vertices a serem desconectados: ').split()
				rem_e(v1, v2)
			elif op1 == 'e' or op1 == 'E':
				break
			else:
				print()
				print('***Opção Inválida***')

	elif op == '2':
		mostra(grafo)
	elif op == '3':
		print()
		v = input('Informe o Vertice: ')
		vizinhos(v)
	elif op == '4':
		print()
		v1, v2 = input('Informe os dois vertices separados por um espaço: ').split()
		ligados(v1, v2)
	elif op == '5':
		print()
		v = input('Informe o Vertice: ')
		grau(v)
	elif op == '6':
		gerar_agm()
		mostra(agm)
	elif op == '0':
		break
	else:
		print()
		print('***Opção Inválida***')