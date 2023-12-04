class LeitorArquivo:
    @staticmethod
    def ler_arquivo_processos(caminho_arquivo):
        processos = []

        with open(caminho_arquivo, 'r') as arquivo:
            # Lê todas as linhas do arquivo
            linhas = arquivo.readlines()

        # Processa cada linha do arquivo
        for linha in linhas:
            dados_processo = list(map(int, linha.strip().split(',')))
            # Adiciona os dados do processo à lista de processos
            processos.append(dados_processo)
        return processos

    @staticmethod
    def ler_arquivo_arquivos(caminho_arquivo):
        # Dicionário para armazenar os dados do arquivo
        dados_arquivo = {"total_blocos": 0, "alocacao_arquivo": {}, "operacoes": []}

        with open(caminho_arquivo, 'r') as arquivo:
            # Lê todas as linhas do arquivo
            linhas = arquivo.readlines()

        # Obtém o número total de blocos a partir da primeira linha do arquivo
        dados_arquivo["total_blocos"] = int(linhas[0].strip())
        # Obtém o número de segmentos ocupados a partir da segunda linha do arquivo
        segmentos_ocupados = int(linhas[1].strip())

        # Processa as linhas correspondentes à alocação de arquivos
        for i in range(2, segmentos_ocupados + 2):
            linha = linhas[i].strip().split(',')
            nome_arquivo, bloco_inicial, contagem_blocos = map(str.strip, linha)
            # Adiciona a alocação de arquivo ao dicionário
            dados_arquivo["alocacao_arquivo"][nome_arquivo] = list(
                range(int(bloco_inicial), int(bloco_inicial) + int(contagem_blocos))
            )

        # Processa as linhas correspondentes às operações no arquivo
        for i in range(segmentos_ocupados + 2, len(linhas)):
            linha = linhas[i].strip().split(',')
            id_processo, codigo_operacao, nome_arquivo = map(str.strip, linha[:3])
            if codigo_operacao == '0':
                # Se a operação for de criar, adiciona o número de blocos à operação
                contagem_blocos = int(linha[3])
                dados_arquivo["operacoes"].append((int(id_processo), int(codigo_operacao), nome_arquivo, contagem_blocos))
            else:
                # Se a operação for de deletar, não há contagem_blocos
                dados_arquivo["operacoes"].append((int(id_processo), int(codigo_operacao), nome_arquivo))

        # Retorna os dados do arquivo
        return dados_arquivo
