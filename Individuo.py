#RGA: 201619040476 Nome: Victor Ezequiel Queiroz Alves
#RGA: 201619060051 Nome: Gabriel Menezes
#RGA: 201619040301 Nome: Matheus Henrique Fernandes Soares
class Individuo():
	def __init__(self, artigos):
		self.artigos = artigos
		self.__grausDaRoleta= 0
	
	def getArtigos(self):
		return self.artigos

	def valorDeFitness(self, revisores):
		soma = 0
		for i in range(len (self.artigos)):
			artigo = self.artigos[i]
			soma = soma + revisores[artigo].getListaDeAfinidades()[i]
		return soma
