def remover(tarefas):
    if not tarefas:
        print("Nenhuma tarefa para remover.")
        return
    
    # Listar tarefas
    print("Tarefas:")
    for index, tarefa in enumerate(tarefas):
        print(f"{index + 1}. {tarefa}")
    
    # Solicitar ao usuário o número da tarefa a ser removida
    try:
        num_tarefa = int(input("Digite o número da tarefa a ser removida: "))
        if 1 <= num_tarefa <= len(tarefas):
            tarefa_removida = tarefas.pop(num_tarefa - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número inválido! Por favor, tente novamente.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
