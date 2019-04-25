class Individuo():
	def __init__(self, cromossomos):
		self.cromossomos = cromossomos
		self.grausDaRoleta= 0
	
	def funcaoDeFitness(self):
		soma = 1
		for cromossomo in self.cromossomos:
			soma =soma + int(cromossomo)
		return soma

	def insereGrauDaRoleta(self, somatoriaDasFF):
		self.grausDaRoleta = (360*self.funcaoDeFitness())/somatoriaDasFF