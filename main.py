import Revisor
import random
import Individuo

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
    revisores = []
    for vetor in matriz:
        revisor = Revisor.Revisor(listaDeAfinidades=vetor[:len(vetor)-1], quantidadeMaximaDeArtigos=vetor[len(vetor)-1])
        revisores.append(revisor)
    return revisores

def todosArtigosComRevisor(artigos):
    return not -1 in artigos

def limiteArtigosParaCadaRevisor(revisores, artigos):
    numeroDeArtigosParaCadaRevisor = [0] * len(revisores)
    for i in range (len(artigos)):
        numeroDeArtigosParaCadaRevisor[artigos[i]] = numeroDeArtigosParaCadaRevisor[artigos[i]] + 1
    for i in range (len(revisores)):
        if (revisores[i].getQuantidadeMaximaDeArtigos() < numeroDeArtigosParaCadaRevisor[i]):
            return False
    return True

def validarEstado(revisores, artigos):
    return todosArtigosComRevisor(artigos) and limiteArtigosParaCadaRevisor(revisores, artigos)

def criarPopulacao(revisores):
    populacao = []
    for j in range(1, 9):
        while True:
            artigos = []
            numeroDeArtigos = len(revisores[0].getListaDeAfinidades())
            while (numeroDeArtigos > 0):
                artigos.append(random.randrange(len(revisores)))
                numeroDeArtigos = numeroDeArtigos - 1
            if (validarEstado(revisores, artigos)):
                break
        populacao.append(artigos)
    return populacao

def transformaPopulacaoEmIndividuos(populacao):
    populacaoDeIndividuos = []
    for individuo in populacao:
        populacaoDeIndividuos.append(Individuo.Individuo(artigos=individuo))
    return populacaoDeIndividuos

def escolheMelhorIndividuo(populacaoDeIndividuos, revisores):
	melhorIndividuo = populacaoDeIndividuos[0]
	for individuo in populacaoDeIndividuos:
		if melhorIndividuo.valorDeFitness(revisores) < individuo.valorDeFitness(revisores):
			melhorIndividuo = individuo
	return melhorIndividuo

def calculaSomatoria(populacaoDeIndividuos, revisores):
    somatoriaDasFF = 0
    for individuo in populacaoDeIndividuos:
        somatoriaDasFF = somatoriaDasFF + individuo.valorDeFitness(revisores)
        print(individuo.valorDeFitness(revisores))
    return somatoriaDasFF

def calculaGrauDaRoleta(populacaoDeIndividuos, somatoriaDasFF, revisores):
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