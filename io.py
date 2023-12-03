recursos = {   # Dicionário que guarda a qtd. global de cada recurso
    "impressora": 2,
    "scanner": 1,
    "modem": 1,
    "drive": 2
}

class gerenciadorES:
    def __init__(self, processo: Processo):
        # Cria uma cópia do dicionário recursos
        self.recursos_necessarios = recursos.copy()

    def alocar_recursos(self):
        # Armazena o estado anterior do dicionário recursos
        recursos_anterior = recursos.copy()
        for recurso, quantidade in self.recursos_necessarios.items():
            if recursos[recurso] < quantidade:
                # Recurso insuficiente, restaura o estado anterior
                recursos = recursos_anterior
                return False
            recursos[recurso] -= quantidade
        return True

    def desalocar_recursos(self):
        for recurso, quantidade in self.recursos_necessarios.items():
            recursos[recurso] += quantidade

    def overflow(self):
        for recurso, quantidade in self.recursos_necessarios.items():
            if recursos[recurso] < quantidade:
                return True
        return False