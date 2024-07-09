def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa para listar.")
    else:
        contador = 1
        for item in tarefas:
            print(f"{contador}. {item}")
            contador += 1
