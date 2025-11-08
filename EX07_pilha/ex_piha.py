print("______________________")
print("MENU SANDUÍCHE")
print("1 - Adicionar ingrediente")
print("2 - Remover ingrediente (do topo)")
print("3 - Ver último ingrediente adicionado")
print("4 - Mostrar sanduíche")
print("5 - Finalizar pedido")
print("______________________")

# Criando a pilha
pilha = []

# Solicita a primeira opção do usuário
resposta = input("Digite um número para escolher uma opção: ")

while resposta != '5':
    
    # 1 - Adicionar ingrediente
    if resposta == '1':
        ingrediente = input("Digite (coloque) um ingrediente: ")
        pilha.append(ingrediente)
        print(f"Ingrediente '{ingrediente}' adicionado ao sanduíche! 🥪")
    
    # 2 - Remover ingrediente (do topo)
    elif resposta == '2':
        if len(pilha) == 0:
            print("O sanduíche está vazio! Nada para remover 👀")
        else:
            tira_ingrediente = pilha.pop()
            print(f"Ingrediente '{tira_ingrediente}' removido do topo do sanduíche.")
    
    # 3 - Ver último ingrediente adicionado
    elif resposta == '3':
        if len(pilha) == 0:
            print("O sanduíche está vazio! 😢")
        else:
            print(f"O último ingrediente adicionado foi: '{pilha[-1]}'")
    
    # 4 - Mostrar sanduíche completo
    elif resposta == '4':
        if len(pilha) == 0:
            print("O sanduíche está vazio! 🥖")
        else:
            print("\n--- Seu sanduíche ---")
            for i in range(len(pilha)):
                print(f"{i+1}. {pilha[i]}")
            print("---------------------\n")
    
    # Opção inválida
    else:
        print("Opção inválida! Tente novamente.")
    
    # Mostra novamente o menu e pede nova resposta
    print("______________________")
    print("1 - Adicionar ingrediente")
    print("2 - Remover ingrediente (do topo)")
    print("3 - Ver último ingrediente adicionado")
    print("4 - Mostrar sanduíche")
    print("5 - Finalizar pedido")
    print("______________________")
    resposta = input("Digite um número para escolher uma opção: ")

# Quando o usuário escolhe finalizar
print("\nPedido finalizado! 🍔 Bom apetite! 😋")
