import Revisor
def lerArquivoDeEntrada(nomeDoArquivo):
    arquivo = open(nomeDoArquivo)
    matriz = []
    for linha in arquivo:
        linha = linha.split(",")
        vetor = []
        for casa in linha:
            vetor.append(int(casa))
        matriz.append(vetor)
    return matriz


def criarRevisores(matriz):
    revisores = []
    for vetor in matriz:
        revisor = Revisor.Revisor(listaDeAfinidades=vetor[:len(vetor)-1], quantidadeMaximaDeArtigos=vetor[len(vetor)-1])
        revisores.append(revisor)
    return revisores

def todosArtigosComRevisor(artigos):
    return not -1 in artigos

# def validarEstado();
#     #nenhum artigo sem revisor
#     todosArtigosComRevisor(artigo)
#     #nenhum revisor com mais artigos que o maximo que ele pode