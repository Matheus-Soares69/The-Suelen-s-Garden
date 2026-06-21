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
  

jardim_local = Local("jardim")
campo_d_flor_local = Local("Campo de Flores")
lago_local = Local("Lago das capivaras")
casa_local = Local("Casa da Suelen")
casa_michael_local = Local("Casa M.Jackson")

norman = Norman("Normando", "Miau!")
sapo = Sapo("Sapo", "Croax!")
michael = Michael("Michael Jackson", "Hee Hee!")
suelen = Jogador("Suelen", "Divou Mona!", jardim_local)
jardim_local.adicionar_personagens(suelen)





