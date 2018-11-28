from copy import deepcopy
# grafo={'a': ['b', 'e'], 'b': ['a', 'e', 'c', 'd'], 'c': ['b', 'd'], 'd': ['b', 'e', 'c'], 'e': ['d', 'a', 'b']}
# print(grafo)
grafo = dict()
grafo = {
	"A": {"B": 1, "C": 3, "D": 2},
	"B": {"A": 1, "D": 3, "F": 1},
	"C": {"A": 3, "D": 4, "E": 1},
	"D": {"A": 2, "B": 3, "C": 4, "E": 3, "F": 1, "G": 4},
	"E": {"C": 1, "D": 3, "E": 2},
	"F": {"B": 1, "D": 1, "G": 2},
	"G": {"E": 2, "D": 4, "F": 2}
}


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
					print('\t\t'+v, '---', p, '---', viz)


def print_tabela(t):
	print('-','------'*len(t),sep='')
	print('|',end='')
	for v in t.keys():
		print('  '+v+'  |',end='')

	print('\n\t\tDistancia')
	print('|',end='')
	for dados in t.values():
		# print(dados)
		dist = ' ∞' if dados['dist']==None else dados['dist']
		print(' {:2}  |'.format(dist),end='')

	print('\n\t\tAnterior')
	print('|',end='')
	for dados in t.values():
		# print(dados)
		ant = ' ' if not dados['ant'] else dados['ant']
		print('  {}  |'.format(ant),end='')

	print('\n\t\tFechado')
	print('|',end='')
	for dados in t.values():
		# print(dados)
		fechado = 'X' if dados['fechado'] else ' '
		print('  {}  |'.format(fechado),end='')

	print('\n-','------'*len(t),sep='')
	print()


def dijkstra(g, ini, fim):
	print('Calculando menor caminho....\n')
	caminho = list()
	tabela = dict()
	nodes = list(g.keys())
	for no in nodes:
		tabela[no] = {'dist': None, 'ant': None, 'fechado': False}
	tabela[ini]['dist'] = 0

	atual = ini
	while(atual != fim):
		print('ATUAL:',atual)
		for viz in g[atual].keys():
			d = tabela[atual]['dist'] + g[atual][viz]
			print('\t',viz,'=',d)
			if tabela[viz]['dist']==None or d < tabela[viz]['dist']:
				tabela[viz]['dist'] = d
				tabela[viz]['ant'] = atual
		nodes.remove(atual)
		tabela[atual]['fechado'] = True
		
		print_tabela(tabela)

		menor = dict()
		for no in nodes:
			d = tabela[no]['dist']
			if d != None and (not menor or d < menor['dist']):
				menor = {'node': no, 'dist': d}
		atual = menor['node']

	while atual != ini:
		caminho.append(atual)
		atual = tabela[atual]['ant']
	caminho.append(atual)
	# caminho.reverse()

	return caminho


while True:
	print()
	print('1. Cadastrar/Editar Grafo')
	print('2. Visualizar Grafo')
	print('3. Calcular Menor Caminho (Dijkstra) entre dois vertices no grafo')
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
		caminho = dijkstra(grafo, "A", "G")
		print('\n----------MENOR CAMINHO (Dijkstra)----------')
		print('\t',end='')
		while len(caminho):
			print(caminho.pop(),end='')
			if len(caminho):
				print(' -> ',end='')
		print('\n')
	elif op == '0':
		break
	else:
		print()
		print('***Opção Inválida***')
