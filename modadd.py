import os
def adicionar(tarefas):
    while True:
        item = input("Digite a tarefa (ou pressione Enter para sair): ").strip()
        if not item:  # Se a entrada estiver vazia, sai do loop
            break
        tarefas.append(item)