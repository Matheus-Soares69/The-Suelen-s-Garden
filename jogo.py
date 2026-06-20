from personagens import *
def iniciar_jogo():
    #suelen.viajar(casa)
    print("===========================")
    print("Casa da Suelen")
    print("===========================")

    print("Você acorda.")
    print("Norman está olhando pela janela.")
    
    while True:
      try: 
        print("1 - Conversar com Norman")
        print("2 - Olhar pela janela")
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
        elif acao == 4:
           print("Você decide ir ao jardim")
           suelen.viajar(jardim)
           break
      except ValueError:
        print("O dia está lindo, pq ficar de bobeira quando se pode curtir o jardim, abraçar o norman ou entt explorar a vizinhança?")

    print("====================")
    print("JARDIM")
    print("====================")
    while True:
      try: 
        print("1 - Observar as flores")
        print("2 - Conversar com os sapinhos")
        print("3 - Olhar o caminhão de mudanças")
        print("4 - Voltar para casa")
        print("5 - Ir ao lago das capivarinhas")
        acao = int(input("Escolha oq fazer: "))
        if acao == 1:
            print("====================")
            print("As flores estão lindas e cheirosas hoje")
        elif acao == 2:
            print("Olá sapinhos!")
        elif acao == 3:
            print("Vou dar um averiguada nesse caminhão aqui!")
        elif acao == 4:
           print("Voce decide voltar para dentro de casa")
           suelen.viajar(casa)
           break
        elif acao == 5:
           print("Você decide ir ao lago")
           suelen.viajar(lago)
           break
      except ValueError:
        print("O dia está lindo, pq ficar de bobeira quando se pode curtir o jardim, abraçar o norman ou entt explorar a vizinhança?")
    
    print("====================")
    print("LAGO DAS CAPIVARINHAS")
    print("====================")
    while True:
       try:
        print("1 - Tentar pescar")
        print("2 - Dar um mergulho")
        print("3 - Dar comida as capivaras")
        print("4 - Voltar para o jardim")
        acao = int(input("Escolha oq fazer: "))
        if acao == 1:
            print("====================")
            print("Você esta sem a sua vara de pesca")
        elif acao == 2:
            print("Você esta sem a sua roupa de nadar")
        elif acao == 3:
            print("Vamo cume capivarinhas???")
        elif acao == 4:
           print("Você decide voltar ao jardim")
           suelen.viajar(jardim)
           break
       except ValueError:
        print("O dia está lindo, pq ficar de bobeira quando se pode curtir o jardim, abraçar o norman ou entt explorar a vizinhança?")
          
    
       

