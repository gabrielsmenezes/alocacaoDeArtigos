class Revisor:
    def __init__(self, listaDeAfinidades, quantidadeMaximaDeArtigos):
        self.__listaDeAfinidades = listaDeAfinidades
        self.__quantidadeMaximaDeArtigos = quantidadeMaximaDeArtigos
    
    def getListaDeAfinidades(self):
        return self.__listaDeAfinidades
    
    def getQuantidadeMaximaDeArtigos(self):
        return self.__quantidadeMaximaDeArtigos