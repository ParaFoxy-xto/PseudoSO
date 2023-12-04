Eduardo Afonso da Silva Inácio, 221033920

# Introdução ao Projeto - Implementação de Pseudo-SO Multiprogramado

Este projeto, desenvolvido como parte da disciplina de Sistemas Operacionais (FSO), reúne um grupo de três colaboradores para criar um Pseudo-Sistema Operacional (Pseudo-SO) multiprogramado. Ao longo das distintas fases do trabalho, nosso objetivo é abordar os fundamentos teóricos do tema, apresentar soluções teóricas para os problemas propostos e, finalmente, implementar um sistema robusto que incorpora um Gerenciador de Processos, um Gerenciador de Memória, um Gerenciador de E/S e um Gerenciador de Arquivos.

A estrutura do gerenciador de processos busca a eficiência ao agrupar os processos em quatro níveis de prioridades. O gerenciador de memória é projetado para garantir a segurança, impedindo que um processo acesse as regiões de memória de outros. O gerenciador de E/S assume a responsabilidade de administrar a alocação e liberação de recursos, garantindo o uso exclusivo desses recursos. Por fim, o gerenciador de arquivos permite que os processos criem e deletam arquivos conforme um modelo de alocação determinado.



## **Modo de Uso - Pseudo-SO Multiprogramado em Python**

### Execução do Programa Principal

Para executar o Pseudo-SO multiprogramado em Python, utilize o seguinte comando no terminal:

```bash
python main.py processos.txt sistema_de_arquivos.txt
```
Certifique-se de substituir processos.txt pelo arquivo que contém as informações dos processos a serem gerenciados e sistema_de_arquivos.txt pelo arquivo com a descrição das operações do sistema de arquivos.

### Estrutura do Arquivo de Processos (processos.txt)
O arquivo de processos deve ter extensão .txt e seguir o formato descrito no documento:
```bash
<tempo_de_inicialização>, <prioridade>, <tempo_de_processador>, <blocos_em_memória>, <código_da_impressora>, <requisição_do_scanner>, <requisição_do_modem>, <código_do_disco>
```

Cada linha representa um processo, e a quantidade de linhas determina a quantidade de processos a serem disparados.

### Estrutura do Arquivo do Sistema de Arquivos (sistema_de_arquivos.txt)
O arquivo do sistema de arquivos também deve ter extensão .txt e seguir o formato especificado:
```bash
Linha 1: Quantidade_de_blocos_do_disco
Linha 2: Quantidade_de_segmentos_ocupados_no_disco (n)
A partir da Linha 3 até Linha n + 2: arquivo (identificado por uma letra), número_do_primeiro_bloco_gravado, quantidade_de_blocos_ocupados
A partir da linha n + 3: cada linha representa uma operação a ser efetivada pelo sistema de arquivos do Pseudo-SO:
<ID_Processo>, <Código_Operação>, <Nome_arquivo>, <se_operacaoCriar_numero_blocos>
```

Assim como o modelo:
```bash
10
3
X, 0, 2
Y, 3, 1
Z, 5, 3
0, 0, A, 5
0, 1, X
2, 0, B, 2
0, 0, D, 3
1, 0, E, 2
```

### Estrutura de filas 

A classe GerenciadorFilas possui métodos para adicionar processos à fila de processos de tempo real, usuários e bloqueados, além de métodos para obter o próximo processo a ser executado, envelhecer processos de usuário, verificar a necessidade de preempção entre processos e desbloquear processos previamente bloqueados. A função adicionar_processo aloca os processos nas filas apropriadas com base em sua prioridade e se são de tempo real. O método obter_proximo_processo retorna o próximo processo a ser executado, considerando as filas de tempo real e de usuário. O método envelhecer_processos reduz a prioridade dos processos de usuário, garantindo uma execução justa. A função preempcao_necessaria verifica se a preempção é necessária entre o processo atual e um novo processo com base em prioridades. Finalmente, desbloquear_processo move um processo previamente bloqueado de volta para a fila apropriada após desbloqueio. Este gerenciador de filas é crucial para a eficiente execução de processos no sistema operacional simulado, otimizando o uso de recursos e a priorização de processos.

### Gerenciamento de E/S

A classe gerenciadorES possui métodos para alocar, desalocar recursos e verificar se ocorrerá um overflow ao tentar alocar recursos. O dicionário recursos contém a quantidade global disponível de cada recurso. O método alocar_recursos verifica se há recursos suficientes para alocar com base nos recursos necessários para o processo, e em caso de insuficiência, reverte para o estado anterior. O método desalocar_recursos libera os recursos alocados anteriormente. A função overflow verifica se a alocação resultará em um overflow, indicando a indisponibilidade de recursos necessários. Esta classe é fundamental para garantir a correta utilização dos recursos de Entrada/Saída pelos processos do sistema operacional. 