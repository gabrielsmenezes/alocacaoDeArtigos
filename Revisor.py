#RGA: 201619040476 Nome: Victor Ezequiel Queiroz Alves
#RGA: 201619060051 Nome: Gabriel Menezes
#RGA: 201619040301 Nome: Matheus Henrique Fernandes Soares
class Revisor:
    def __init__(self, listaDeAfinidades, quantidadeMaximaDeArtigos):
        self.__listaDeAfinidades = listaDeAfinidades
        self.__quantidadeMaximaDeArtigos = quantidadeMaximaDeArtigos
    
    def getListaDeAfinidades(self):
        return self.__listaDeAfinidades
    
    def getQuantidadeMaximaDeArtigos(self):
        return self.__quantidadeMaximaDeArtigos
