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
        print(individuo.valorDeFitness(revisores))
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
	somatoriaDasFF = calculaSomatoria(populacaoDeIndividuos, revisores)
	calculaGrauDaRoleta(populacaoDeIndividuos, somatoriaDasFF, revisores)
	numeroRandomico = random.randrange(1, 361)
	return escolheIndividuoDaRoleta(numeroRandomico, populacaoDeIndividuos)

def reproduzir(individuo1, individuo2, crossoverrate):
    numeroRandomico = random.random()

    if not (numeroRandomico < crossoverrate):
        return individuo1
    
    tamanhoDoIndividuo = len(individuo1.getArtigos())
    pontoDeDivisaoDoIndividuo = random.randrange(0, tamanhoDoIndividuo)
    novoIndividuo = Individuo.Individuo(individuo1.getArtigos()[0:pontoDeDivisaoDoIndividuo] + individuo2.getArtigos()[pontoDeDivisaoDoIndividuo:tamanhoDoIndividuo] )
    while(not validarEstado(artigos=novoIndividuo.getArtigos() ) ):
        pontoDeDivisaoDoIndividuo = random.randrange(0, tamanhoDoIndividuo)
        novoIndividuo = Individuo.Individuo(individuo1.getArtigos()[0:pontoDeDivisaoDoIndividuo] + individuo2.getArtigos()[pontoDeDivisaoDoIndividuo:tamanhoDoIndividuo])
    return novoIndividuo

def mutar(individuo, mutationrate, numeroDeRevisores):
	numeroRandomico = random.random()
	for posicao in range(0,len(individuo.getArtigos())):
		if(numeroRandomico < mutationrate):
			individuo.artigos[posicao] = random.randrange(numeroDeRevisores)

# def algoritmoGenetico(populacao, crossoverrate, mutationrate, maxgen):
# 	valorDeFitnessObjetivo = calculaValorDeFitnessObjetivo()
# 	geracao = 0
# 	while maxgen > 0:
# 		geracao = geracao + 1
# 		print("Geracao ", geracao)

# 		novaPopulacao = list()
# 		for x in range(1,(len(populacao))+1):
			
# 			#selecao
# 			individuo1 = selecaoRandomicaDoIndividuoParaReproduzir(populacao)
# 			individuo2 = selecaoRandomicaDoIndividuoParaReproduzir(populacao)
			
# 			#reproducao
# 			filho = reproduzir(individuo1, individuo2, crossoverrate)
# 			#mutacao
# 			mutar(filho, mutationrate)
			
# 			novaPopulacao.append(filho)

# 		populacao = novaPopulacao

# 		for individuo in populacao:
# 			print(individuo.cromossomos)

# 		maxgen = maxgen - 1
# 		melhor = escolheMelhorIndividuo(populacao)

# 		if objetivo == melhor.cromossomos:
# 			return melhor

# 	return escolheMelhorIndividuo(populacao)

def main():
    matrizEsperada = [
        [0,0,3,4,4,1],
        [3,3,0,0,1,2],
        [4,0,0,1,0,1],
        [2,2,2,3,2,2]
    ]

    artigos = [3,2,1,4,4]

    revisores = []
    for vetor in matrizEsperada:
        revisor = Revisor.Revisor(listaDeAfinidades= vetor[:len(vetor)-1], quantidadeMaximaDeArtigos=vetor[len(vetor)-1])
        revisores.append(revisor)


    populacao = [
        [1, 2, 1, 0, 3] ,#3+0+0+4+2=9 9
        [0, 3, 1, 1, 2], #0+2+0+0+0=2 2
        [3, 2, 1, 3, 0], #2+0+0+3+4=9 9
        [3, 1, 0, 3, 1], #2+3+3+3+1=12 12
        [0, 1, 3, 1, 3], #0+3+2+4+2=11 7
        [1, 3, 0, 1, 2], #3+2+3+0+0=8 8 
        [3, 0, 1, 3, 2], #2+0+0+3+0=5 5
        [1, 0, 3, 3, 1]] #3+0+2+3+1=9 9

    populacaoDeIndividuos = transformaPopulacaoEmIndividuos(populacao)

    calculaSomatoria(populacaoDeIndividuos, revisores)

# main()