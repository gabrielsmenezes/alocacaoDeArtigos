#RGA: 201619040476 Nome: Victor Ezequiel Queiroz Alves
#RGA: 201619060051 Nome: Gabriel Menezes
#RGA: 201619040301 Nome: Matheus Henrique Fernandes Soares
import pytest
import alocacaoArtigos, Revisor

########### variaveis ###########

matrizEsperada = [
        [0,0,3,4,4,1], #revisor 0
        [3,3,0,0,1,2], #revisor 1
        [4,0,0,1,0,1], #revisor 2
        [2,2,2,3,2,2] #revisor 3
    ]

artigos = [2,1,0,3,3]

revisores = []
for vetor in matrizEsperada:
    revisor = Revisor.Revisor(listaDeAfinidades= vetor[:len(vetor)-1], quantidadeMaximaDeArtigos=vetor[len(vetor)-1])
    revisores.append(revisor)


populacao = [
    [1, 2, 1, 0, 3] ,#3+0+0+4+2=9 
    [0, 3, 1, 1, 2], #0+2+0+0+0=2
    [3, 2, 1, 3, 0], #2+0+0+3+4=9
    [3, 1, 0, 3, 1], #2+3+3+3+1=12
    [0, 1, 3, 1, 3], #0+3+2+4+2=7
    [1, 3, 0, 1, 2], #3+2+3+0+0=8
    [3, 0, 1, 3, 2], #2+0+0+3+0=5
    [1, 0, 3, 3, 1]] #3+0+2+3+1=9

populacaoDeIndividuos = alocacaoArtigos.transformaPopulacaoEmIndividuos(populacao)

########### testes ###########


def test_lerArquivoDeEntrada():
    
    matrizRetornado = alocacaoArtigos.lerArquivoDeEntrada("entrada.txt")
    
    assert matrizEsperada == matrizRetornado

def test_criarRevisores():
    revisores = []
    for vetor in matrizEsperada:
        revisor = Revisor.Revisor(listaDeAfinidades= vetor[:len(vetor)-1], quantidadeMaximaDeArtigos=vetor[len(vetor)-1])
        revisores.append(revisor)
    alocacaoArtigos.criarRevisores(matrizEsperada)
    revisoresRetornados = alocacaoArtigos.revisores

    for revisorEsperado, revisorRetornado in zip(revisores, revisoresRetornados):
        assert revisorEsperado.getListaDeAfinidades() == revisorRetornado.getListaDeAfinidades()

def test_todosArtigosComRevisorTrue():
    
    valorEsperado = True

    valorRetornado = alocacaoArtigos.todosArtigosComRevisor(artigos)

    assert valorEsperado == valorRetornado
    
def test_todosArtigosComRevisorFalse():
    artigosAlterados = [3,2,1,4,-1]
    valorEsperado = False

    valorRetornado = alocacaoArtigos.todosArtigosComRevisor(artigosAlterados)

    assert valorEsperado == valorRetornado

def test_limiteArtigosParaCadaRevisorTrue():
    valorEsperado = True

    valorRetornado = alocacaoArtigos.limiteArtigosParaCadaRevisor(artigos=artigos)
    
    assert valorEsperado == valorRetornado

def test_limiteArtigosParaCadaRevisorFalse():
    valorEsperado = False
    artigosAlterados = [3,3,3,3,3]
    valorRetornado = alocacaoArtigos.limiteArtigosParaCadaRevisor(artigos=artigosAlterados)
    
    assert valorEsperado == valorRetornado

def test_validarEstado_HappyDay():

    valorEsperado = True

    valorRetornado = alocacaoArtigos.validarEstado(artigos=[2,1,0,3,3])

    assert valorEsperado == valorRetornado

def test_validarEstado_ArtigoSemRevisor():

    valorEsperado = False

    valorRetornado = alocacaoArtigos.validarEstado(artigos=[3,2,1,4,-1])
    assert valorEsperado == valorRetornado

def test_validarEstado_UltrapassandoLimiteDeUmRevisor():

    valorEsperado = False

    valorRetornado = alocacaoArtigos.validarEstado(artigos=[1,1,1,1,1]) 
    assert valorEsperado == valorRetornado

def test_criarPopulacao():
    valorEsperado = 8
    
    valorRetornado = alocacaoArtigos.criarPopulacao()
    valorRetornado = len(valorRetornado)

    assert valorEsperado == valorRetornado

def test_transformaPopulacaoEmIndividuos():
    valorEsperado = 8

    valorRetornado = len(populacaoDeIndividuos)

    assert valorEsperado == valorRetornado

def test_escolheMelhorIndividuo():

	valorEsperado = [3, 1, 0, 3, 1]

	valorRetornado = alocacaoArtigos.escolheMelhorIndividuo(populacaoDeIndividuos=populacaoDeIndividuos).getArtigos()

	assert valorEsperado == valorRetornado

def test_calculaSomatoria():

	valorEsperado = 61

	valorRetornado = alocacaoArtigos.calculaSomatoria(populacaoDeIndividuos=populacaoDeIndividuos)
	assert valorEsperado == valorRetornado

def test_calculaGrauDaRoleta():
	#arrange
	valorEsperado = 53
	#action
	alocacaoArtigos.calculaGrauDaRoleta(populacaoDeIndividuos=populacaoDeIndividuos, somatoriaDasFF=61)
	valorRetornado = populacaoDeIndividuos[0].__grausDaRoleta
	
	assert valorEsperado == valorRetornado

def test_escolheIndividuoDaRoletaParaOPrimeiroIndividuo():
	#arrange
	valorEsperado = [1, 2, 1, 0, 3]
	somatoriaDasFF = 61

	alocacaoArtigos.calculaGrauDaRoleta(somatoriaDasFF=somatoriaDasFF, populacaoDeIndividuos=populacaoDeIndividuos)
	valorRetornado = alocacaoArtigos.escolheIndividuoDaRoleta(numeroRandomico=50, populacaoDeIndividuos=populacaoDeIndividuos).getArtigos()

	assert valorEsperado == valorRetornado

def test_reproduzir():
	valorEsperado = 5
	
	valorRetornado = len(alocacaoArtigos.reproduzir(populacaoDeIndividuos[0], populacaoDeIndividuos[1], crossoverrate=1).getArtigos())
	
	assert valorEsperado == valorRetornado

def test_mutar():
	
	valorEsperado = False
	
	alocacaoArtigos.mutar(individuo=populacaoDeIndividuos[0], mutationrate=1, numeroDeRevisores=len(revisores))
	valorRetornado = populacaoDeIndividuos[0].getArtigos() == [1, 2, 1, 0, 3]
	
	assert valorEsperado == valorRetornado

def test_calculaValorDeFitnessObjetivo():
    valorEsperado = 18

    valorRetornado = alocacaoArtigos.calculaValorDeFitnessObjetivo()

    assert valorEsperado == valorRetornado
