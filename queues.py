from process import Processo
from io import gerenciadorES

es = gerenciadorES()

class GerenciadorFilas:
    def __init__(self):
        self.fila_tempo_real = []
        self.filas_usuario = [[], [], []]
        self.fila_bloqueados = []
        self.num_processos = 0
        self.quantum_tempo_real = 1  # Quantum para processos de tempo real
        self.quantum_usuario = 1  # Quantum para processos de usuário

    def adicionar_processo(self, processo: Processo):
        if processo.eh_tempo_real:
            self.fila_tempo_real.append(processo)
        else:
            #Caso a linha abaixo for true, significa que foi possivel alocar recursos e/s para o processo, entao ele nao é bloqueado.
            if es.alocar_recursos(processo):
                self.filas_usuario[processo.prioridade].append(processo)
            else:
                self.fila_bloqueados.append(processo)

    def obter_proximo_processo(self):
        for fila in [self.fila_tempo_real] + self.filas_usuario:
            if fila:
                return fila.pop(0)
        return None

    def envelhecer_processos(self):
        for fila in self.filas_usuario[1:]:
            for processo in fila:
                processo.prioridade -= 1  # diminui a prioridade
                if processo.prioridade < 0:
                    processo.prioridade = 0  # Garante que a prioridade não seja negativa

    def preempcao_necessaria(self, processo_atual: Processo, novo_processo: Processo):
        # Verifica se é necessário preemptar o processo atual para o novo
        if novo_processo.eh_tempo_real:
            return True
        elif processo_atual is not None and novo_processo.prioridade < processo_atual.prioridade:
            return True
        return False

    def desbloquear_processo(self, processo: Processo):
        self.fila_bloqueados.remove(processo)
        self.adicionar_processo(processo)
        