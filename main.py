import Revisor
import random
import Individuo

#####variaveis#####
revisores = []

def lerArquivoDeEntrada(nomeDoArquivo):
    arquivo = open(nomeDoArquivo)
    matriz = []
    for linha in arquivo:
        linha = linha.split(",")
        vetor = []
        for casa in linha:
            vetor.append(int(casa))
        matriz.append(vetor)
    return matriz

def criarRevisores(matriz):
    for vetor in matriz:
        revisor = Revisor.Revisor(listaDeAfinidades=vetor[:len(vetor)-1], quantidadeMaximaDeArtigos=vetor[len(vetor)-1])
        revisores.append(revisor)

def todosArtigosComRevisor(artigos):
    return not -1 in artigos

def limiteArtigosParaCadaRevisor(artigos):
    numeroDeArtigosParaCadaRevisor = [0] * len(revisores)
    for i in range (len(artigos)):
        numeroDeArtigosParaCadaRevisor[artigos[i]] = numeroDeArtigosParaCadaRevisor[artigos[i]] + 1
    for i in range (len(revisores)):
        if (revisores[i].getQuantidadeMaximaDeArtigos() < numeroDeArtigosParaCadaRevisor[i]):
            return False
    return True

def validarEstado(artigos):
    return todosArtigosComRevisor(artigos) and limiteArtigosParaCadaRevisor(artigos)

def criarPopulacao():
    populacao = []
    for j in range(1, 9):
        while True:
            artigos = []
            numeroDeArtigos = len(revisores[0].getListaDeAfinidades())
            while (numeroDeArtigos > 0):
                artigos.append(random.randrange(len(revisores)))
                numeroDeArtigos = numeroDeArtigos - 1
            if (validarEstado(artigos)):
                break
        populacao.append(artigos)
    return populacao

def transformaPopulacaoEmIndividuos(populacao):
    populacaoDeIndividuos = []
    for individuo in populacao:
        populacaoDeIndividuos.append(Individuo.Individuo(artigos=individuo))
    return populacaoDeIndividuos

def escolheMelhorIndividuo(populacaoDeIndividuos):
	melhorIndividuo = populacaoDeIndividuos[0]
	for individuo in populacaoDeIndividuos:
		if melhorIndividuo.valorDeFitness(revisores) < individuo.valorDeFitness(revisores):
			melhorIndividuo = individuo
	return melhorIndividuo

def calculaSomatoria(populacaoDeIndividuos):
    somatoriaDasFF = 0
    for individuo in populacaoDeIndividuos:
        somatoriaDasFF = somatoriaDasFF + individuo.valorDeFitness(revisores)
    return somatoriaDasFF

def calculaGrauDaRoleta(populacaoDeIndividuos, somatoriaDasFF):
    for individuo in populacaoDeIndividuos:
        grau = (individuo.valorDeFitness(revisores) * 360) / somatoriaDasFF
        individuo.__grausDaRoleta = grau
    return populacaoDeIndividuos

def escolheIndividuoDaRoleta(numeroRandomico, populacaoDeIndividuos):
	anterior = 0
	for individuo in populacaoDeIndividuos:
		if anterior < numeroRandomico and numeroRandomico <= individuo.__grausDaRoleta+anterior:
			return individuo
		anterior = individuo.__grausDaRoleta + anterior

def selecaoRandomicaDoIndividuoParaReproduzir(populacaoDeIndividuos):
	somatoriaDasFF = calculaSomatoria(populacaoDeIndividuos)
	calculaGrauDaRoleta(populacaoDeIndividuos, somatoriaDasFF)
	numeroRandomico = random.randrange(1, 360)
	return escolheIndividuoDaRoleta(numeroRandomico, populacaoDeIndividuos)

def reproduzir(individuo1, individuo2, crossoverrate):
    numeroRandomico = random.random()

    if not (numeroRandomico < crossoverrate):
        return individuo1
    
    tamanhoDoIndividuo = len(individuo1.getArtigos())
    pontoDeDivisaoDoIndividuo = random.randrange(0, tamanhoDoIndividuo)
    novoIndividuo = Individuo.Individuo(individuo1.getArtigos()[0:pontoDeDivisaoDoIndividuo] + individuo2.getArtigos()[pontoDeDivisaoDoIndividuo:tamanhoDoIndividuo] )
    
    while(not validarEstado(novoIndividuo.getArtigos())):
        pontoDeDivisaoDoIndividuo = random.randrange(0, tamanhoDoIndividuo)
        novoIndividuo = Individuo.Individuo(individuo1.getArtigos()[0:pontoDeDivisaoDoIndividuo] + individuo2.getArtigos()[pontoDeDivisaoDoIndividuo:tamanhoDoIndividuo] )
    
    return novoIndividuo

def mutar(individuo, mutationrate, numeroDeRevisores):
	numeroRandomico = random.random()
	for posicao in range(0,len(individuo.getArtigos())):
		if(numeroRandomico < mutationrate):
			individuo.artigos[posicao] = random.randrange(numeroDeRevisores)
	
	while( not validarEstado(individuo.artigos)):
		numeroRandomico = random.random()
		for posicao in range(0,len(individuo.getArtigos())):
			if(numeroRandomico < mutationrate):
				individuo.artigos[posicao] = random.randrange(numeroDeRevisores)
	
def calculaValorDeFitnessObjetivo():
    fitnessObjetivo = 0
    for coluna in range (0,len(revisores[0].getListaDeAfinidades())):
        maior = -1
        for linha in range (0, len(revisores)):
            if maior < revisores[linha].getListaDeAfinidades()[coluna]:
                maior = revisores[linha].getListaDeAfinidades()[coluna]
        fitnessObjetivo = fitnessObjetivo + maior
    return fitnessObjetivo

def algoritmoGenetico(populacao, crossoverrate, mutationrate, maxgen):
	valorDeFitnessObjetivo = calculaValorDeFitnessObjetivo()
	geracao = 0
	print("Populacao inicial")
	for individuo in populacao:
		print(individuo.getArtigos())
	while maxgen > 0:
		geracao = geracao + 1
		print("geracao", geracao)
		novaPopulacao = list()
		for x in range(1,(len(populacao))+1):
			#selecao
			individuo1 = selecaoRandomicaDoIndividuoParaReproduzir(populacao)
			individuo2 = selecaoRandomicaDoIndividuoParaReproduzir(populacao)
			#reproducao
			filho = reproduzir(individuo1, individuo2, crossoverrate)
			#mutacao
			mutar(filho, mutationrate, len(revisores))
			
			novaPopulacao.append(filho)

		populacao = novaPopulacao
		for individuo in populacao:
			print(individuo.getArtigos())

		maxgen = maxgen - 1
		melhor = escolheMelhorIndividuo(populacao)

		if valorDeFitnessObjetivo == melhor.valorDeFitness(revisores):
			return melhor

	return escolheMelhorIndividuo(populacao)

#variaveis para testes
arquivoDeEntrada = lerArquivoDeEntrada("entrada.txt")

criarRevisores(arquivoDeEntrada)

populacao = criarPopulacao()

populacaoDeIndividuos = transformaPopulacaoEmIndividuos(populacao)
melhor = algoritmoGenetico(populacaoDeIndividuos, 0.70, 0.1, 100000)
print ("O melhor individuo eh: ", melhor.getArtigos(), "com funcao fitness de ", melhor.valorDeFitness(revisores))