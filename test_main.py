import pytest
import main, Revisor

########### variaveis ###############

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


########### testes ###############


def test_lerArquivoDeEntrada():
    #action
    matrizRetornado = main.lerArquivoDeEntrada("entrada.txt")
    #assert
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
    artigosAlterados = [4,4,4,4,4]
    valorRetornado = main.limiteArtigosParaCadaRevisor(revisores=revisores, artigos=artigosAlterados)
    
    assert valorEsperado == valorRetornado

def test_validarEstado_HappyDay():

    valorEsperado = True

    valorRetornado = main.validarEstado(artigos=[3,2,1,4,4], revisores=revisores)

    assert valorEsperado == valorRetornado

def test_validarEstado_ArtigoSemRevisor():

    valorEsperado = False

    valorRetornado = main.validarEstado(artigos=[3,2,1,4,-1], revisores=revisores)

    assert valorEsperado == valorRetornado

def test_validarEstado_ArtigoSemRevisor():

    valorEsperado = False

    valorRetornado = main.validarEstado(artigos=[3,2,1,4,-1], revisores=revisores)

    assert valorEsperado == valorRetornado

def test_validarEstado_ArtigoSemRevisor():

    valorEsperado = False

    valorRetornado = main.validarEstado(artigos=[1,1,1,1,1], revisores=revisores)

    assert valorEsperado == valorRetornado

def test_criarPopulacao():
    assert individuo.