class Memoria:
    def __init__(self, tamanho_total, blocos_tempo_real):
        self.tamanho_total = tamanho_total
        self.blocos_tempo_real = blocos_tempo_real
        self.blocos_disponiveis_tempo_real = blocos_tempo_real
        self.blocos_disponiveis_usuario = tamanho_total - blocos_tempo_real
        self.memoria_ocupada = [-1] * tamanho_total

    def alocar_memoria(self, processo):
        if processo.eh_tempo_real:
            blocos_disponiveis = self.blocos_disponiveis_tempo_real
            inicio_base = 0  
        else:
            blocos_disponiveis = self.blocos_disponiveis_usuario
            inicio_base = self.blocos_tempo_real-1

        if processo.blocos_de_memoria <= blocos_disponiveis:
            inicio = self.encontrar_inicio_regiao_contigua(inicio_base, processo.blocos_de_memoria, processo.eh_tempo_real)
            if inicio is not None:
                for i in range(inicio, inicio + processo.blocos_de_memoria):
                    self.memoria_ocupada[i] = processo.pid
                if processo.eh_tempo_real:
                    self.blocos_disponiveis_tempo_real -= processo.blocos_de_memoria
                else:
                    self.blocos_disponiveis_usuario -= processo.blocos_de_memoria
                processo.offset = inicio
                return inicio
        print(f"Processo {processo.pid} não foi alocado por falta de espaço na memória")
        return None

    def encontrar_inicio_regiao_contigua(self, inicio_base, blocos_necessarios, is_tempo_real):
        contagem_blocos = 0
        limite_superior = self.tamanho_total if not is_tempo_real else inicio_base + self.blocos_tempo_real
        for i in range(inicio_base, limite_superior):
            if self.memoria_ocupada[i] == -1:
                contagem_blocos += 1
                if contagem_blocos == blocos_necessarios:
                    return i - blocos_necessarios + 1
            else:
                contagem_blocos = 0
        return None

    
    def liberar_memoria(self, processo):
        inicio_regiao_liberada = processo.offset
        blocos_liberados = processo.blocos_de_memoria
        for i in range(inicio_regiao_liberada, inicio_regiao_liberada + blocos_liberados):
            self.memoria_ocupada[i] = -1
        if processo.eh_tempo_real:
            self.blocos_disponiveis_tempo_real += blocos_liberados
        else:
            self.blocos_disponiveis_usuario += blocos_liberados

