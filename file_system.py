class SistemaArquivos:
    def __init__(self, tamanho_disco, processos):
        self.tamanho_disco = tamanho_disco
        self.mapa_ocupacao = [0] * tamanho_disco
        self.arquivos = {}
        self.num_operacao = 0
        self.processos = processos

    def criar_arquivo(self, processo_id, nome_arquivo, blocos_necessarios):
        self.num_operacao += 1
        inicio_regiao = self.encontrar_inicio_contigua(blocos_necessarios)
        if inicio_regiao is not None:
            self.arquivos[nome_arquivo] = {"processo_id": processo_id, "inicio_regiao": inicio_regiao, "blocos": blocos_necessarios}
            for i in range(inicio_regiao, inicio_regiao + blocos_necessarios):
                self.mapa_ocupacao[i] = nome_arquivo
            return f"Operação {self.num_operacao} => Sucesso: O processo {processo_id} criou o arquivo {nome_arquivo} (blocos {inicio_regiao} a {inicio_regiao + blocos_necessarios - 1})."
        return f"Operação {self.num_operacao} => Falha: O processo {processo_id} não pode criar o arquivo {nome_arquivo} (falta de espaço)."

    def deletar_arquivo(self, processo_id, nome_arquivo, is_tempo_real):
        self.num_operacao += 1
        if nome_arquivo in self.arquivos:
            if is_tempo_real or self.arquivos[nome_arquivo]["processo_id"] == processo_id:
                inicio_regiao = self.arquivos[nome_arquivo]["inicio_regiao"]
                blocos_ocupados = self.arquivos[nome_arquivo]["blocos"]
                del self.arquivos[nome_arquivo]
                for i in range(inicio_regiao, inicio_regiao + blocos_ocupados):
                    self.mapa_ocupacao[i] = 0
                return f"Operação {self.num_operacao} => Sucesso: O processo {processo_id} deletou o arquivo {nome_arquivo}."
            else:
                return f"Operação {self.num_operacao} => Falha: O processo {processo_id} não tem permissão para deletar o arquivo {nome_arquivo}."
        else:
            return f"Operação {self.num_operacao} => Falha: O processo {processo_id} não pode deletar o arquivo {nome_arquivo} porque ele não existe"

    # first-fit
    def encontrar_inicio_contigua(self, blocos_necessarios):
        contagem_blocos = 0
        for i in range(self.tamanho_disco):
            if self.mapa_ocupacao[i] == 0:
                contagem_blocos += 1
                if contagem_blocos == blocos_necessarios:
                    return i - blocos_necessarios + 1
            else:
                contagem_blocos = 0
        return None

    def exibir_mapa_ocupacao(self):
        print("Mapa de Ocupação do Disco:")
        for i in range(self.tamanho_disco):
            print(f"Bloco {i}: {self.mapa_ocupacao[i] if self.mapa_ocupacao[i] != 0 else 'Vazio'}")


# # Exemplo de uso:
# from read_files import LeitorArquivo
# from process import Processo
# CAMINHO_PROCESSOS = "input_files/processes.txt"
# dados_processos = LeitorArquivo.ler_arquivo_processos(CAMINHO_PROCESSOS)
# processos = [Processo(*dados) for dados in dados_processos]

# sistema_arquivos = SistemaArquivos(tamanho_disco=10, processos=processos)

# print(sistema_arquivos.criar_arquivo(processo_id=0, nome_arquivo="A", blocos_necessarios=5))
# print(sistema_arquivos.criar_arquivo(processo_id=0, nome_arquivo="X", blocos_necessarios=5))
# print(sistema_arquivos.deletar_arquivo(processo_id=3, nome_arquivo="X", is_tempo_real=False))
# print(sistema_arquivos.deletar_arquivo(processo_id=2, nome_arquivo="Y", is_tempo_real=True))
# print(sistema_arquivos.criar_arquivo(processo_id=0, nome_arquivo="D", blocos_necessarios=3))
# print(sistema_arquivos.deletar_arquivo(processo_id=1, nome_arquivo="E", is_tempo_real=False))

# sistema_arquivos.exibir_mapa_ocupacao()
