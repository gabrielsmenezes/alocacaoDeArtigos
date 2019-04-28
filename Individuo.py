class Individuo():
	def __init__(self, artigos):
		self.__artigos = artigos
		self.__grausDaRoleta= 0
	
	def getArtigos(self):
		return self.__artigos

	def valorDeFitness(self, revisores):
		soma = 0
		for i in range(len (self.__artigos)):
			artigo = self.__artigos[i]
			soma = soma + revisores[artigo].getListaDeAfinidades()[i]
		return soma