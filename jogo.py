from personagens import *
def casa_suelen():
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
           suelen.viajar(jardim_local)
           jardim()
           return
      except ValueError:
        print("O dia está lindo, pq ficar de bobeira quando se pode curtir o jardim, abraçar o norman ou entt explorar a vizinhança?")
        
def jardim():      
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
            suelen.viajar(casa_michael_local)
            casa_vizinho()
            return
        elif acao == 4:
           print("Voce decide voltar para dentro de casa")
           suelen.viajar(casa_local)
           casa_suelen()
           return
        elif acao == 5:
           print("Você decide ir ao lago")
           suelen.viajar(lago_local)
           lago()
           return
      except ValueError:
        print("O dia está lindo, pq ficar de bobeira quando se pode curtir o jardim, abraçar o norman ou entt explorar a vizinhança?")

def lago():
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
           suelen.viajar(jardim_local)
           jardim()
           return
       except ValueError:
        print("O dia está lindo, pq ficar de bobeira quando se pode curtir o jardim, abraçar o norman ou entt explorar a vizinhança?")
          
def casa_vizinho():
   print("====================")
   print("CASA DO VIZINHO MISTERIOSO")
   print("====================")
   print("Voce observa alguns trabalhadores descarregando o caminhão, que é grande por sinal")
   print("Tem algumas caixas no chão, e tbm alguns animais ja dentro da casa")
   print("Derrepente vc sente uma forte curiosidade pra descobrir quem se mudou")
   while True:
       try:
        print("1 - Pegar a caixa que caiu")
        print("2 - Dar uma espiada dentro da casa pelo portão")
        print("3 - Entrar e dar para dar as boas vindas e descobrir quem é o vizinho")
        print("4 - Voltar para o jardim")
        acao = int(input("Escolha oq fazer: "))
        if acao == 1:
            print("====================")
            print("A caixa tem duas iniciais... M.J eu ja vi isso em algum lugar.")
        elif acao == 2:
            print("Espiadinha rapidaa.")
        elif acao == 3:
            print("Vamo descobrir quem é o novo vizinho..ele tem um casarão em, caramba.")
            suelen.viajar(casa_michael_local)
            casa_vizinho_dentro()
            return
        elif acao == 4:
           print("Você decide voltar ao jardim.")
           suelen.viajar(jardim_local)
           jardim()
           return
       except ValueError:
        print("O dia está lindo, pq ficar de bobeira quando se pode curtir o jardim, abraçar o norman ou entt explorar a vizinhança?")

def casa_vizinho_dentro():
   print("====================")
   print("DENTRO DA CASA DO VIZINHO")
   print("====================")
   print("Você respira fundo e decide se aproximar.")
   print("Um dos trabalhadores aponta para dentro da casa.")
   print('"O senhor Jackson está lá dentro."')
   print("Jackson?")
   print("Não pode ser...")
   print("Dentro da casa vc encontra uma caixa com uma luva brilhante em cima")
   print("Voce escuta uma voz acima de você...")
   print("Olá, girl, como posso te help?")
   print("Você se vira em choque pois reconhece aquela voz")
   print("Lá esta ele, u homi")
   print("em toda a sua magnificiencia")
   print("HI HI")

       

