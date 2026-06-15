from jogo import iniciar_jogo

print("====================")
print("The Suelen's Garden")
print("1- iniciar jogo")
print("2- opções")
print("3- sair")

opcao = int(input("Escolher uma opção: "))

if opcao == 1:
    iniciar_jogo()

elif opcao == 2:
    print("Abrindo opções...")

else:
    print("Saindo...Até mais!")