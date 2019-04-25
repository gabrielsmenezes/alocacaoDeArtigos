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

def limiteArtigosParaCadaRevisor(revisores, artigos):
    numeroDeArtigosParaCadaRevisor = [0] * len(revisores)
    for i in range (len(artigos)):
        print(artigos[i])
        numeroDeArtigosParaCadaRevisor[artigos[i]-1] = numeroDeArtigosParaCadaRevisor[artigos[i]-1] + 1
    print(numeroDeArtigosParaCadaRevisor)
    for i in range (len(revisores)):
        if (revisores[i].getQuantidadeMaximaDeArtigos() < numeroDeArtigosParaCadaRevisor[i]):
            return False
    return True

def validarEstado(revisores, artigos):
    return todosArtigosComRevisor(artigos) and limiteArtigosParaCadaRevisor(revisores, artigos)