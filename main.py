from process import Processo
from read_files import LeitorArquivo
from memory_manager import Memoria
from file_system import SistemaArquivos

def principal():
    CAMINHO_PROCESSOS = "input_files/processes.txt"
    CAMINHO_ARQUIVOS = "input_files/files.txt"

    # lê os inputs
    dados_processos = LeitorArquivo.ler_arquivo_processos(CAMINHO_PROCESSOS)
    dados_arquivos = LeitorArquivo.ler_arquivo_arquivos(CAMINHO_ARQUIVOS)
    processos = [Processo(*dados) for dados in dados_processos]

    # sistema de arquivos
    tamanho_disco = dados_arquivos['total_blocos']
    gerenciador_arquivos = SistemaArquivos(tamanho_disco, processos)
    gerenciador_arquivos.processar_operacoes(dados_arquivos)

    # gerenciador memoria
    memoria = Memoria(tamanho_total=1024, blocos_tempo_real=64)


    # testes:
    # print(dados_processos)
    # print(dados_arquivos)
    # print(*processos, sep="\n")

    # for processo in processos:
    #     memoria.alocar_memoria(processo)
    # print(memoria.memoria_ocupada)
    # print()

    # memoria.liberar_memoria(processos[0])
    # print(memoria.memoria_ocupada)

    # print(*processos, sep="\n")

if __name__ == "__main__":
    principal()
