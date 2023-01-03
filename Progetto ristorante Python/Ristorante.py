'''
Si deve realizzare un sistema per un ristorante per gestire i clienti e i tavoli
con il relativo numero di posti , le prenotazioni (effettuate dai clienti per un certo giorno e ora,
e per un certo numero di persone).
Alle prenotazioni vengono assegnati uno o più tavoli (divisi in fumatori/non fumatori) ,
i camerieri che servono i clienti al tavolo e il conto,
composto dalle singole portate ordinate.
Dei clienti interessano il nome e numero di telefono ,
mentre dei camerieri interessano il nome e gli anni di servizio.
Ogni portata ha un costo unitario previsto dal listino e al cliente
viene presentato il conto dove vengono indicate le singole portate con il nome,
il prezzo unitario e la quantità ordinata che permette di calcolare
il totale per portate e il conto totale per gruppo.
'''
#-------------------------------------****Inizio programma****-----------------------------------------------------------------------------------------------------------
class Ristorante:#Classe Padre
    def __init__(self,n_posti,prenotazioni):# Metodo costruttore
        self.n_posti = n_posti #Attributo
        self.prenotazioni = prenotazioni #Attributo
#--------------------------------------****Prenotazioni****-------------------------------------------------------------------------------------------------------------
    def Prenotazioni_clienti(self):
        print("inserisci il giorno")
        gg = int(input())
        print("inserisci l'ora")
        hh = float(input())
        print("inserisci il numero di persone")
        per = int(input())
        if (per <= 4):
            print("1 tavolo assegnato")
        elif(per > 4):
            print("più tavoli assegnati")

    def Tavoli_divisi(self):
        if (self.prenotazioni == "fumatori"):
            self.prenotazioni = "non fumatori"
            print("tavolo/i assegnato/i ai non fumatori")
        elif(self.prenotazioni == "non fumatori"):
            self.prenotazioni = "fumatori"
            print("tavolo/i assegnato/i ai fumatori")

#--------------------------------------****Classe Portata****------------------------------------------------------------------------------
class Portata(Ristorante):
    def __init__(self,n_posti,prenotazioni,somma,hummus,gamberi,risotto,carbonara,grigliata,cotoletta,tiramisù,sorbetto):
        super().__init__(n_posti,prenotazioni)
        self.somma = 0 #Attributo
        self.hummus = 3
        self.gamberi = 6
        self.risotto = 10
        self.carbonara = 5
        self.grigliata = 15
        self.cotoletta = 7
        self.tiramisù = 8
        self.sorbetto = 4

    def Listino(self):
        print("Scegli una portata:\n1)Hummus\n2)Gamberi\n3)Risotto\n4)Carbonara\n5)Grigliata\n6)Cotoletta\n7)Tiramisù\n8)Sorbetto")
        scelta = input()
        if (scelta == "1"):
            print("Hai scelto l'antipasto hummus")
            print("Inserisci la quantità")
            Q = int(input())
            L1 = ["Hummus",Q,self.hummus]
            print(L1)
            self.somma = (self.somma + 3) * Q
        elif(scelta == "2"):
            print("Hai scelto il secondo antipasto,cocktail di gamberi")
            print("Inserisci la quantità")
            Q1 = int(input())
            L2 = ["Cocktail di gamberi",Q1,self.gamberi]
            print(L2)
            self.somma = (self.somma + 6) * Q1
        elif(scelta == "3"):
            print("Hai scelto la prima portata,il risotto")
            print("Inserisci la quantità")
            Q2 = int(input())
            L3 = ["Risotto",Q2,self.risotto]
            print(L3)
            self.somma = (self.somma + 10) * Q2
        elif(scelta == "4"):
            print("Hai scelto la prima portata,la carbonara")
            print("Inserisci la quantità")
            Q3 = int(input())
            L4 = ["Carbonara",Q3,self.carbonara]
            print(L4)
            self.somma = (self.somma + 5) * Q3
        elif(scelta == "5"):
            print("Hai scelto la seconda portata, la grigliata mista")
            print("Inserisci la quantità")
            Q4 = int(input())
            L5 = ["Grigliata mista",Q4,self.grigliata]
            print(L5)
            self.somma = (self.somma + 15) * Q4
        elif(scelta == "6"):
            print("Hai scelto la seconda portata, la cotoletta")
            print("Inserisci la quantità")
            Q5 = int(input())
            L6 = ["Cotoletta",Q5,self.cotoletta]
            print(L6)
            self.somma = (self.somma + 7) * Q5
        elif(scelta == "7"):
            print("Hai scelto il primo dolce,il tiramisù")
            print("Inserisci la quantità")
            Q6 = int(input())
            L7 = ["Tiramisù",Q6,self.tiramisù]
            print(L7)
            self.somma = (self.somma + 8) * Q6
        elif(scelta == "8"):
            print("Hai scelto il secondo dolce, il sorbetto")
            print("Inserisci la quantità")
            Q7 = int(input())
            L8 = ["Sorbetto",Q7,self.sorbetto]
            print(L8)
            self.somma = (self.somma + 4) * Q7

    def Conto(self):
        print("IL CONTO É DI : ", self.somma,"€")
            
            
            
        
#--------------------------------------****Classe Cliente****-----------------------------------------------------------------------------
class Cliente(Ristorante):
    def __init__(self,n_posti,prenotazioni,somma,nome_cliente,n_telefono):
        super().__init__(n_posti,prenotazioni)
        self.nome_cliente = nome_cliente
        self.n_telefono = n_telefono
    def nomi_clienti(self):
        L_Cli = ["Claudio",3456778921,"Andrea",3698754422,"Gianmaria",3295643214]
        print(L_Cli)
            
        
#-----------------------------------****Classe Cameriere****------------------------------------------------------------------------------
class Cameriere(Ristorante):
    def __init__(self,n_posti,prenotazioni,somma,nome_cameriere,anni_servizio):
        super().__init__(n_posti,prenotazioni)
        self.nome_cameriere = nome_cameriere
        self.anni_servizio = anni_servizio
    def nomi_camerieri(self):
        L_Cam = ["Pasquale",2,"Giorgio",1,"Mario",5,"Laura",3]
        print(L_Cam)


#-------------------------------------------****MAIN****----------------------------------------------------------------------------------
R = Ristorante(2,"fumatori")
P = Portata(3,"non fumatori",18,3,6,10,5,15,7,8,4)
Cli = Cliente(4,"fumatori",20,"Andrea",3698754422)
Cam = Cameriere(5,"non fumatori",19,"Pasquale",2)
opzione = 19
while(opzione != 0):
    print("""
    Benvenuto/i nel nostro ristorante.Che cosa desidera?:

             ** 1 Prenotazione
             ** 2 Tavolo diviso
             ** 3 Menù
             ** 4 Nomi clienti
             ** 5 Conto
             ** 6 Nomi camerieri
             ** 0 ----> EXIT
    """)

    opzione = int(input())
        
    if(opzione == 1):
        R.Prenotazioni_clienti()
    elif(opzione == 2):
        R.Tavoli_divisi()
    elif(opzione == 3):
        P.Listino()
    elif(opzione == 4):
        Cli.nomi_clienti()
    elif(opzione == 5):
        P.Conto()
    elif(opzione == 6):
        Cam.nomi_camerieri()
    elif(opzione == 0):
        exit("Uscita")
    
    else:
        print("l'opzione che hai inserito non è valida")

    
     
    

