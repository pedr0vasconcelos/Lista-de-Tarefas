import modadd
import modremove
import modlist
from datetime import datetime
import os

tarefas = []

def menu():
    while True:
        print("**********************")
        print("*  LISTA DE TAREFAS  *")
        print("* 1 - Adicionar      *")
        print("* 2 - Remover        *")
        print("* 3 - Listar         *")
        print("* 4 - Sair           *")
        print("**********************")
        opcao = int(input("Opção: "))
        #print(f"Opção escolhida: {opcao}")        
        match(opcao):
            case 1:
                modadd.adicionar(tarefas)
            case 2:
                modremove.remover(tarefas)
            case 3:
                print("Listando tarefas...")
                modlist.listar(tarefas)
            case 4:
                print("Saindo...")
                break      
menu()

with open(f'Lista de Tarefas({datetime.now().strftime('%H.%M.%S - %d.%m.%Y')}).txt', 'w') as gravar:
    for item in tarefas:
        gravar.write(f"{item}\n")
print("Lista Armazenada com sucesso...")

