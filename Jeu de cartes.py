class abstraite_Carte:
    def __init__(self,coutmana,nom,desc):
        self._coutm = coutmana
        self._name= nom
        self._description = desc            #creation de la classe de la carte et init de ses vars
    def renvoiecarte(self):
        return True     
    def returncoutmana(self):       #creation de ses def
        return self._coutm  
    

class Mage:
    def __init__(self,nom,pointdevie,manatotal,valeurmana,main):
        self._name=nom
        self._pv=pointdevie
        self._manat=manatotal
        self._valactuelmana=valeurmana              #creation de la classe mage avec ses vars
        self._mainm=main        
        self._def=[]
        self._zonegame=[]
    def recupmana(self):        
        self._valactuelmana=self._manat         #fonction de remise a zero du mana a chaque fin de tour
    def jouercarte(self,cartes):
        print(self._mainm)
        cartes = int(input("choisissez la carte que vous voulez jouer"))+1          #fonction pour jouer une carte qui va se placer sur le terrain de jeu
        self._zonegame=self._mainm[cartes]
        self._valactuelmana=self._valactuelmana-self._mainm[cartes].returncoutmana()
        self.AfficheGame()
    def attaquerC(self,cartesj):
        if (cartesj==self._zonegame):           #fonction pour attaquer ennemies
            "degatcartesennemies"
        self.AfficheGame()
    def AfficheGame(self):
        print(self._zonegame)           #fonction pour afficher la zone de jeu
    def VerifRenvoie(self,cartes):
        if (abstraite_Carte.renvoiecarte==True):            #fonction pour renvoyé une carte dans la defausse
            self._def=self._mainm[cartes]          
        
class Cristal(abstraite_Carte):
    def __init__(self, val,coutmana):
        self._valeur=val
        abstraite_Carte.__init__(self,coutmana,"cristal","permet de recuperer x mana quand joué")               #creation de la class cristal avec son heredité a la classe carte

class Creature(abstraite_Carte):
    def __init__(self, pointdevie, score_attaque,coutmana):
        self._pv=pointdevie
        self._attack=score_attaque
        abstraite_Carte.__init__(self,coutmana,"Creature","la creature peu attaqué et se faire attaqué")        #creation de la class creature avec son hérédité a la classe carte
    def attaquer(self,cible):   
        cible.pv=cible.pv-self._attack      #fonction de l'attaque de la creature
    def degatrecu(self,attaquantdegat):
        self._pv=self._pv-attaquantdegat            #fonction de l'attaque recu de la creature
        print(self._pv)
    def verifpv(self):
        if(self._pv<=0):            #verif de ses pv, si pv>=0 alors defausse
            Creature.renvoiecarte()

class Blast(abstraite_Carte):
    def __init__(self, val,coutmana):
        self._valeur=val                                    #creation de la carte blast avec son heredité a la classe carte
        abstraite_Carte.__init__(self,coutmana,"blast","inflige x degat a la cible, se detruit quand joué")
    
Mage1=Mage("Pierre",50,30,30,[abstraite_Carte(20,"murlock","creature agressif vivant dans les marais"),Cristal(10,0),Creature(10,5,5),Blast(5,0),Blast(10,0)])
Mage2=Mage("Caillou",30,50,50,[abstraite_Carte(25,"Tarzan","humain je n'ai pas d'inspi"),Creature(5,10,5),Creature(10,5,5),Blast(5,0)])         #creation des deux mages et de leurs deck


while(Mage1._pv>0 or Mage2._pv>0):
    Mage1.jouercarte(None)                  #deroulement de partie
    Mage1.attaquerC(None)
    Mage1.recupmana()
    Mage2.jouercarte(None)
    Mage2.attaquerC(None)
    Mage2.recupmana()