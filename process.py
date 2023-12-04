class Processo:
    contador_processos = 0

    def __init__(self, tempo_inicial, prioridade, tempo, blocos_de_memoria, impressora, scanner, modem, drive):
        self.pid = Processo.contador_processos 
        Processo.contador_processos += 1 
        self.offset = None 
        self.tempo_inicial = tempo_inicial
        self.prioridade = prioridade 
        self.tempo = tempo
        self.blocos_de_memoria = blocos_de_memoria
        self.impressora = impressora
        self.scanner = scanner
        self.modem = modem
        self.drive = drive
        self.eh_tempo_real = prioridade == 0

    @staticmethod
    def se_existe_processo_com_esse_id(codigo_processo, lista_processos):
        for processo in lista_processos:
            if processo.pid == codigo_processo:
                return True
        return False 
    
    @staticmethod
    def verificar_tempo_real(codigo_processo, lista_processos):
        for processo in lista_processos:
            if processo.pid == codigo_processo:
                return processo.eh_tempo_real
        return None  # Retorna None se o processo não for encontrado

    def __str__(self):
        return (
            f"   PID: {self.pid}\n"
            f"   Offset: {self.offset}\n"
            f"   Blocos de Memória: {self.blocos_de_memoria}\n"
            f"   Prioridade: {self.prioridade}\n"
            f"   Tempo: {self.tempo}\n"
            f"   Impressora: {self.impressora}\n"
            f"   Scanner: {self.scanner}\n"
            f"   Modem: {self.modem}\n"
            f"   Drive: {self.drive}\n"
        )

