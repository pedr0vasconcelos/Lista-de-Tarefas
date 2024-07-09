import os
def adicionar(tarefas):
    while True:
        item = input("Digite a tarefa: ")
        tarefas.append(item)
        continuar = input("Deseja continuar? S/N: ")
        if continuar.lower() == "n":
            
            break
        elif continuar.lower() == "s":
            continue
        else:
            print("Opção inválida! Tente novamente: ")
