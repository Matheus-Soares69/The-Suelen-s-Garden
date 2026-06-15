def iniciar_jogo():
    print("===========================")
    print("Casa da Suelen")
    print("===========================")

    print("Você acorda.")
    print("Norman está olhando pela janela.")

    print("1 - Conversar com Norman")
    print("2 - Olhar oela janela")
    print("3 - Ouvir a vitrola")
    print("4 - Sair para o jardim")
    
    acao = int(input("Escolha oq fazer: "))
    if acao == 1:
      print("====================")
      print("Normando: Miauu")
      print("Norman quer ir ao Jardim")
    elif acao == 2:
      print("Você olha pela janela, observa seus jardim de flores, as capivarinhas, os sapinhos, e seu vizinho Michael Jackson.....MICHAEL JACKSON!?!?!?")
    elif acao == 3:
      print("Você toca a vitrola...mas está sem disco.")
      print("Talvez haja algum disco em algum lugar da casa.")
    else:
      print("Você decide não fazer nada ainda.")