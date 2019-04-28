import pytest
import Individuo
import Revisor

matrizEsperada = [
        [0,0,3,4,4,1], #revisor 0
        [3,3,0,0,1,2], #revisor 1
        [4,0,0,1,0,1], #revisor 2
        [2,2,2,3,2,2] #revisor 3
    ]

artigos = [0, 1, 3, 1, 3]

revisores = []
for vetor in matrizEsperada:
    revisor = Revisor.Revisor(listaDeAfinidades= vetor[:len(vetor)-1], quantidadeMaximaDeArtigos=vetor[len(vetor)-1])
    revisores.append(revisor)

def test_valorDeFitness():
    individuo = Individuo.Individuo(artigos)
    valorEsperado = 7

    valorRetornado = individuo.valorDeFitness(revisores)

    assert valorEsperado == valorRetornado