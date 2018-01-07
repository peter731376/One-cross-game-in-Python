'''
Created on Nov 29, 2017

@author: AnDong Mac
'''
class Ristinolla:
    PELAAJA1 = 1
    PELAAJA2 = 2
    RATKAISEMATON = 3
    MERKKI1 = 1
    MERKKI2 = -1
    TYHJA = 0
    EI_LOYDY = 0
    KESKEN = 0
    KOKO = 4
    MERKIT = ['_', 'X', '0']
    def  __init__(self, nimi1, nimi2):
        self.nimi1=nimi1
        self.nimi2=nimi2
        self.lista=[["_","_","_","_"],["_","_","_","_"],["_","_","_","_"],["_","_","_","_"]]
        
    def  kerro_pelaaja1(self):
        return self.nimi1
    def kerro_pelaaja2(self):
        return self.nimi2
    def lisaa_merkki(self, x_koord, y_koord, pelaaja):
      if (x_koord>3 or x_koord<0 or y_koord>3 or y_koord<0):
          return False
      else:
        if self.lista[3-y_koord][x_koord]=="_":
            if pelaaja==1:
                self.lista[3-y_koord][x_koord]="X"
                return True
            else:
                self.lista[3-y_koord][x_koord]="0"
                return True
        else:
            return False
    def peli_paattynyt(self):
        
        list=[]
        for i in range(4):
            l=[]
            for j in range(4):
                l.append(self.lista[j][i])
            list.append(l)
        for i in range(4):
            list.append(self.lista[i])
        l1=[]
        for i in range(4):
            l1.append(self.lista[i][3-i])
        l2=[]
        for i in range (4):
            l2.append(self.lista[i][i])
        list.append(l1)
        list.append(l2)
        for l in list:
            if l[0]=="X" and l[1]=="X"and l[2]=="X" and l[3]=="X":
                return Ristinolla.PELAAJA1
            elif l[0]=="0" and l[1]=="0"and l[2]=="0" and l[3]=="0":
                return Ristinolla.PELAAJA2
        check_list=[]
        for i in range(4):
            for j in range(4):
                check_list.append(self.lista[i][j])
        for x in check_list:
            if x=="_":
                return Ristinolla.KESKEN
        return Ristinolla.RATKAISEMATON
    def __str__(self):
        string=""
        for i in range(3):
           for j in range(4):
               string+=self.lista[i][j]
           string+="\n"
        for i in range(4):
            string+=self.lista[3][i]
        return string
            
            
        