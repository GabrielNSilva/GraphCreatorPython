# grafo={'a': ['b', 'e'], 'b': ['a', 'e', 'c', 'd'], 'c': ['b', 'd'], 'd': ['b', 'e', 'c'], 'e': ['d', 'a', 'b']}
# print(grafo)
grafo = dict()


def ins_v(nome):
	grafo[nome] = {'sai': [], 'entra': []}


def ins_e(n1, n2):
	if n1 in grafo and n2 in grafo:
		grafo[n1]['sai'].append(n2)
		grafo[n2]['entra'].append(n1)
		# grafo[n2].append(n1)
	else:
		print('***Vertices inexistentes!!***')


def rem_v(v):
	if v in grafo:
		while len(grafo[v]['sai']):
			p = grafo[v]['sai'].pop()
			grafo[p]['entra'].remove(v)
		while len(grafo[v]['entra']):
			p = grafo[v]['entra'].pop()
			grafo[p]['sai'].remove(v)

		grafo.pop(v)
		print('Vertice removido com sucesso!')
	else:
		print('***Vertice inexistente!***')


def rem_e(v1, v2):
	if v1 in grafo and v2 in grafo:
		if v2 in grafo[v1]['sai'] and v1 in grafo[v2]['entra']:
			grafo[v1]['sai'].remove(v2)
			grafo[v2]['entra'].remove(v1)
			# grafo[v2].remove(v1)
			print('Aresta removida com sucesso!')
		else:
			print('**Não existe aresta entre os vertices na direção informada!**')
	else:
		print('***Vertices inexistentes!!***')


def mostra():
	if len(grafo) == 0:
		print('***Grafo vazio!***')
	else:
		for v, es in grafo.items():
			print()
			print('Vertice '+v+':')
			print('\tArestas de saida(diverge):')
			if len(es['sai']) == 0:
				print('\t\tSem arestas')
			else:
				for e in es['sai']:
					print('\t\t'+v+'----->'+e)
			print('\tArestas de entrada(converge):')
			if len(es['entra']) == 0:
				print('\t\tSem arestas')
			else:
				for e in es['entra']:
					print('\t\t'+v+'<-----'+e)


def vizinhos(v):
	if v in grafo:
		print('Adjacentes à '+v)
		for viz in grafo[v]['sai']:
			#print('\t'+v+'—————>'+viz)
			print('\t'+v+'----->'+viz)
		for viz in grafo[v]['entra']:
			#print('\t'+v+'—————>'+viz)
			print('\t'+v+'<-----'+viz)
		#for vert,es in grafo.items():
		 #if v in es:
			#    #print('\t'+vert+'—————>'+v)
		 #   print('\t'+vert+'----->'+v)
	else:
		print('***Vertice inexistente!***')


def ligados(v1, v2):
	if v1 in grafo and v2 in grafo:
		if v2 in grafo[v1]['sai'] or v1 in grafo[v2]['sai']:
			print('Os vertices informados estão ligados da seguinte forma!')
			if v2 in grafo[v1]['sai']:
				print('\t' + v1 + '----->' + v2)
			if v1 in grafo[v2]['sai']:
				print('\t' + v2 + '----->' + v1)
		else:
			print('**Não existe aresta entre os vertices informados!**')
	else:
		print('***Vertices inexistentes!!***')


def grau(v):
	if v in grafo:
		print('Grau de saida: '+str(len(grafo[v]['sai'])))
		print('Grau de entrada: '+str(len(grafo[v]['entra'])))
	else:
		print('***Vertice inexistente!***')


while True:
	print()
	print('1. Cadastrar/Editar Grafo')
	print('2. Visualizar Grafo')
	print('3. Buscar Vertices Adjacentes')
	print('4. Buscar Aresta entre dois Vertices')
	print('5. Calcular Grau de um Vertice')
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
				ins_e(n1, n2)
			elif op1 == 'c' or op1 == 'C':
				print()
				v = input('Digite os nomes dos vertices separados por um espaço: ').split()
				for vert in v:
					rem_v(vert)
			elif op1 == 'd' or op1 == 'D':
				print()
				v1, v2 = input(
					'Digite (separados por um espaço) os vertices a separados: ').split()
				rem_e(v1, v2)
			elif op1 == 'e' or op1 == 'E':
				break
			else:
				print()
				print('***Opção Inválida***')

	elif op == '2':
		mostra()
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
	elif op == '0':
		break
	else:
		print()
		print('***Opção Inválida***')