import pytest
import Individuo

def test_insereGrauDaRoleta():
	valorEsperado = 45
	individuo = Individuo.Individuo([0,0,0,0])

	individuo.insereGrauDaRoleta(8)
	

	valorRetornado = individuo.grausDaRoleta
	assert valorEsperado == valorRetornado

def test_funcaoDeFitness():
	valorEsperado = 1

	individuo = Individuo.Individuo([0,0,0,0])
	valorRetornado = individuo.funcaoDeFitness()

	assert valorEsperado == valorRetornado