# Programa: Fila de Atendimento Bancário
# Estrutura: Fila (FIFO - First In, First Out)

from collections import deque

print("===================================")
print("      SIMULADOR DE FILA DO BANCO 🏦")
print("===================================")

# Criando a fila
fila = deque()

# Função para mostrar menu
def mostrar_menu():
    print("\nMENU")
    print("1 - Adicionar cliente à fila")
    print("2 - Atender próximo cliente")
    print("3 - Ver quem está na fila")
    print("4 - Quantidade de pessoas na fila")
    print("5 - Sair do programa")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    # 1 - Adicionar cliente
    if opcao == '1':
        nome = input("Digite o nome do cliente: ")
        fila.append(nome)
        print(f"Cliente '{nome}' entrou na fila. 🧍‍♂️")
    
    # 2 - Atender cliente (remove do início)
    elif opcao == '2':
        if len(fila) == 0:
            print("A fila está vazia! Nenhum cliente para atender.")
        else:
            atendido = fila.popleft()
            print(f"Cliente '{atendido}' foi atendido. ✅")
    
    # 3 - Mostrar quem está na fila
    elif opcao == '3':
        if len(fila) == 0:
            print("A fila está vazia no momento. 👀")
        else:
            print("\nClientes na fila:")
            for i, cliente in enumerate(fila, start=1):
                print(f"{i}. {cliente}")
    
    # 4 - Mostrar quantidade de pessoas na fila
    elif opcao == '4':
        print(f"Há {len(fila)} cliente(s) na fila.")
    
    # 5 - Sair do programa
    elif opcao == '5':
        print("\nEncerrando o atendimento. Tenha um bom dia! 👋")
        break
    
    # Opção inválida
    else:
        print("Opção inválida! Tente novamente.")
