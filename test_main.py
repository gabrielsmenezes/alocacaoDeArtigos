import pytest
import main, Revisor

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


populacao = main.criarPopulacao(revisores)

########### testes ###########


def test_lerArquivoDeEntrada():
    
    matrizRetornado = main.lerArquivoDeEntrada("entrada.txt")
    
    assert matrizEsperada == matrizRetornado

def test_criarRevisores():
    revisores = []
    for vetor in matrizEsperada:
        revisor = Revisor.Revisor(listaDeAfinidades= vetor[:len(vetor)-1], quantidadeMaximaDeArtigos=vetor[len(vetor)-1])
        revisores.append(revisor)

    revisoresRetornados = main.criarRevisores(matrizEsperada)

    for revisorEsperado, revisorRetornado in zip(revisores, revisoresRetornados):
        assert revisorEsperado.getListaDeAfinidades() == revisorRetornado.getListaDeAfinidades()

def test_todosArtigosComRevisorTrue():
    
    valorEsperado = True

    valorRetornado = main.todosArtigosComRevisor(artigos)

    assert valorEsperado == valorRetornado
    
def test_todosArtigosComRevisorFalse():
    artigosAlterados = [3,2,1,4,-1]
    valorEsperado = False

    valorRetornado = main.todosArtigosComRevisor(artigosAlterados)

    assert valorEsperado == valorRetornado

def test_limiteArtigosParaCadaRevisorTrue():
    valorEsperado = True

    valorRetornado = main.limiteArtigosParaCadaRevisor(revisores=revisores, artigos=artigos)
    
    assert valorEsperado == valorRetornado

def test_limiteArtigosParaCadaRevisorFalse():
    valorEsperado = False
    artigosAlterados = [3,3,3,3,3]
    valorRetornado = main.limiteArtigosParaCadaRevisor(revisores=revisores, artigos=artigosAlterados)
    
    assert valorEsperado == valorRetornado

def test_validarEstado_HappyDay():

    valorEsperado = True

    valorRetornado = main.validarEstado(artigos=[2,1,0,3,3], revisores=revisores)

    assert valorEsperado == valorRetornado

def test_validarEstado_ArtigoSemRevisor():

    valorEsperado = False

    valorRetornado = main.validarEstado(artigos=[3,2,1,4,-1], revisores=revisores)

    assert valorEsperado == valorRetornado

def test_validarEstado_UltrapassandoLimiteDeUmRevisor():

    valorEsperado = False

    valorRetornado = main.validarEstado(artigos=[1,1,1,1,1], revisores=revisores)

    assert valorEsperado == valorRetornado

def test_criarPopulacao():
    valorEsperado = 8
    
    valorRetornado = populacao
    valorRetornado = len(valorRetornado)

    assert valorEsperado == valorRetornado

def test_transformaPopulacaoEmIndividuos():
    valorEsperado = 8

    valorRetornado = len(main.transformaPopulacaoEmIndividuos(populacao))

    assert valorEsperado == valorRetornado