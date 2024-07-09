import modadd
import modremove
import modlist
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
        print(f"Opção escolhida: {opcao}")        
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
