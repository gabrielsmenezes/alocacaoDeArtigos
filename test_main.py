import pytest
import main

def test_lerArquivoDeEntrada():
    #arrange
    vetorEsperado = [
        [0,0,3,4,4,1],
        [3,3,0,0,1,2],
        [4,0,0,1,0,1],
        [2,2,2,3,2,2]
    ]

    #action
    vetorRetornado = main.lerArquivoDeEntrada("entrada.txt")
    #assert
    assert vetorEsperado == vetorRetornado