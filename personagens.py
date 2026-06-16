class Personagem():
  def __init__(self, nome, dialogo):
    self.nome = nome
    self.dialogo = dialogo
    
  def falar(self):
    print(f"{self.nome}: {self.dialogo}")
  
class Jogador(Personagem):
  def __init__(self, nome, dialogo, local_atual):
    self.local_atual  = local_atual
    super().__init__(nome, dialogo)
    
  def mostrar_local(self):
    print(f"{self.nome} esta no {self.local_atual.nome}")
    
  def viajar(self, novo_local):
    self.local_atual.remover_personagens(self)
    self.local_atual = novo_local
    novo_local.adicionar_personagens(self)
      
      
    
class Norman(Personagem):
  pass
    
class Sapo(Personagem):
  pass

class Michael(Personagem):
  pass
    
class Local():
  def __init__(self, nome):
    self.nome = nome
    self.personagens= []
    
  def adicionar_personagens(self, personagem):
    self.personagens.append(personagem)
    
  def remover_personagens(self, personagem):
    self.personagens.remove(personagem)
  
  def mostrar_personagens(self):
    print(f"Local: {self.nome}")
    
    for personagem in self.personagens:
      print(f"- {personagem.nome}")
  

jardim = Local("jardim")
campo_d_flor = Local("Campo de Flores")

norman = Norman("Normando", "Miau!")
sapo = Sapo("Sapo", "Croax!")
michael = Michael("Michael Jackson", "Hee Hee!")
suelen = Jogador("Suelen", "Divou Mona!", jardim)
jardim.adicionar_personagens(suelen)


suelen.mostrar_local()

suelen.viajar(campo_d_flor)

suelen.mostrar_local()

campo_d_flor.mostrar_personagens()


