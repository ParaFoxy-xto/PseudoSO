from process import Processo

class SistemaArquivos:
    def __init__(self, tamanho_disco, processos):
        self.tamanho_disco = tamanho_disco
        self.mapa_ocupacao = [0] * tamanho_disco  # Representa a ocupação de blocos no disco
        self.arquivos = {}  # Dicionário para armazenar informações sobre os arquivos
        self.num_operacao = 0  # Contador para o número da operação
        self.processos = processos  # Lista de processos no sistema

    def criar_arquivo(self, processo_id, nome_arquivo, blocos_necessarios):
        inicio_regiao = self.encontrar_inicio_contigua(blocos_necessarios)
        if inicio_regiao is not None:
            # Espaço contíguo encontrado, cria o arquivo e atualiza o mapa de ocupação
            self.arquivos[nome_arquivo] = {"processo_id": processo_id, "inicio_regiao": inicio_regiao, "blocos": blocos_necessarios}
            for i in range(inicio_regiao, inicio_regiao + blocos_necessarios):
                self.mapa_ocupacao[i] = nome_arquivo
            return f"Operação {self.num_operacao} => Sucesso: O processo {processo_id} criou o arquivo {nome_arquivo} (blocos {inicio_regiao} a {inicio_regiao + blocos_necessarios - 1})."
        return f"Operação {self.num_operacao} => Falha: O processo {processo_id} não pode criar o arquivo {nome_arquivo} (falta de espaço)."

    def deletar_arquivo(self, processo_id, nome_arquivo, is_tempo_real):
        if nome_arquivo in self.arquivos:
            if is_tempo_real or self.arquivos[nome_arquivo]["processo_id"] == processo_id:
                # Verifica permissões e deleta o arquivo atualizando o mapa de ocupação
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

    # Algoritmo first-fit para encontrar espaço contíguo no disco
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
        print()
        print("Mapa de Ocupação do Disco:")
        for i in range(self.tamanho_disco):
            print(f"Bloco {i}: {self.mapa_ocupacao[i] if self.mapa_ocupacao[i] != 0 else 'Vazio'}")

    # Método para preencher os blocos iniciais com base nas alocações de arquivo iniciais
    def preencher_blocos_iniciais(self, dados_operacoes):
        alocacao_arquivo = dados_operacoes['alocacao_arquivo']
        for nome_arquivo, blocos_ocupados in alocacao_arquivo.items():
            primeiro_bloco = blocos_ocupados[0]
            quantidade_blocos = len(blocos_ocupados)
            self.arquivos[nome_arquivo] = {"inicio_regiao": primeiro_bloco, "blocos": quantidade_blocos}
            for bloco_ocupado in blocos_ocupados:
                self.mapa_ocupacao[bloco_ocupado] = nome_arquivo

    # Método para processar as operações do sistema de arquivos
    def processar_operacoes(self, dados_operacoes):
        print()
        print("Sistema de arquivos =>")
        self.preencher_blocos_iniciais(dados_operacoes)
        for operacao in dados_operacoes['operacoes']:
            self.num_operacao += 1
            id_processo, codigo_operacao, *params = operacao
            nome_arquivo = params[0]

            if (Processo.se_existe_processo_com_esse_id(int(id_processo), self.processos)):
                if codigo_operacao == 0:  # Criar arquivo
                    blocos = params[1]
                    print(self.criar_arquivo(int(id_processo), nome_arquivo, int(blocos)))
                elif codigo_operacao == 1:  # Deletar arquivo
                    eh_tempo_real = Processo.verificar_tempo_real(int(id_processo), self.processos)
                    print(self.deletar_arquivo(int(id_processo), nome_arquivo, eh_tempo_real))
            else:
                print(f"Operação {self.num_operacao} => Falha: O processo {id_processo} não existe.")
        self.exibir_mapa_ocupacao()

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
# print(sistema_arquivos.deletar_arquivo(processo_id=1, nome_arquivo="X", is_tempo_real=True))

# sistema_arquivos.exibir_mapa_ocupacao()
