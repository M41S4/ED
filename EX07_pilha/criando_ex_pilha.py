# Programa: Simulador de Desfazer (Ctrl+Z)
# Estrutura: Pilha (LIFO)

print("===================================")
print("  SIMULADOR DE DESFAZER (Ctrl+Z)")
print("===================================")


pilha_acoes = []

# Menu
def mostrar_menu():
    print("\nMENU")
    print("1 - Realizar uma ação")
    print("2 - Desfazer última ação (Ctrl+Z)")
    print("3 - Ver histórico de ações")
    print("4 - Sair do programa")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")


    if opcao == '1':
        acao = input("Descreva a ação realizada: ")
        pilha_acoes.append(acao)
        print(f"Ação '{acao}' realizada e adicionada ao histórico.")
    
 
    elif opcao == '2':
        if len(pilha_acoes) == 0:
            print("Nenhuma ação para desfazer! 🫤")
        else:
            desfazer = pilha_acoes.pop()
            print(f"Ação desfeita: '{desfazer}' ❌")
    
 
    elif opcao == '3':
        if len(pilha_acoes) == 0:
            print("Histórico vazio. Nenhuma ação registrada.")
        else:
            print("\nHistórico de ações (da primeira à última):")
            for i, a in enumerate(pilha_acoes, start=1):
                print(f"{i}. {a}")
    

    elif opcao == '4':
        print("\nPrograma encerrado! 👋")
        break
    

    else:
        print("Opção inválida! Tente novamente.")
