import copy
from Cvor import Cvor
from hashmap import HashMap


class Tabla(object):
    def __init__(self):

        cvor1 = Cvor(1, None)
        cvor2 = Cvor(2, None)
        cvor3 = Cvor(3, None)
        cvor4 = Cvor(4, None)
        cvor5 = Cvor(5, None)
        cvor6 = Cvor(6, None)
        cvor7 = Cvor(7, None)
        cvor8 = Cvor(8, None)
        cvor9 = Cvor(9, None)
        cvor10 = Cvor(10, None)
        cvor11 = Cvor(11, None)
        cvor12 = Cvor(12, None)
        cvor13 = Cvor(13, None)
        cvor14 = Cvor(14, None)
        cvor15 = Cvor(15, None)
        cvor16 = Cvor(16, None)
        cvor17 = Cvor(17, None)
        cvor18 = Cvor(18, None)
        cvor19 = Cvor(19, None)
        cvor20 = Cvor(20, None)
        cvor21 = Cvor(21, None)
        cvor22 = Cvor(22, None)
        cvor23 = Cvor(23, None)
        cvor24 = Cvor(24, None)

        cvor1.ubaci_desno(cvor2)        
        cvor1.ubaci_dole(cvor10)
        cvor2.ubaci_desno(cvor3)
        cvor2.ubaci_levi(cvor1)
        cvor2.ubaci_dole(cvor5)
        cvor3.ubaci_levi(cvor2)
        cvor3.ubaci_dole(cvor15)
        cvor4.ubaci_desno(cvor5)
        cvor4.ubaci_dole(cvor11)
        cvor5.ubaci_desno(cvor6)
        cvor5.ubaci_levi(cvor4)
        cvor5.ubaci_dole(cvor8)
        cvor5.ubaci_gore(cvor2)
        cvor6.ubaci_levi(cvor5)
        cvor6.ubaci_dole(cvor14)
        cvor7.ubaci_desno(cvor8)
        cvor7.ubaci_dole(cvor12)
        cvor8.ubaci_desno(cvor9)
        cvor8.ubaci_levi(cvor7)
        cvor8.ubaci_gore(cvor5)
        cvor9.ubaci_levi(cvor8)
        cvor9.ubaci_dole(cvor13)
        cvor10.ubaci_desno(cvor11)
        cvor10.ubaci_dole(cvor22)
        cvor10.ubaci_gore(cvor1)
        cvor11.ubaci_desno(cvor12)
        cvor11.ubaci_dole(cvor19)
        cvor11.ubaci_gore(cvor4)
        cvor11.ubaci_levi(cvor10)
        cvor12.ubaci_dole(cvor16)
        cvor12.ubaci_gore(cvor7)
        cvor12.ubaci_levi(cvor11)
        cvor13.ubaci_desno(cvor14)
        cvor13.ubaci_gore(cvor9)
        cvor13.ubaci_dole(cvor18)
        cvor14.ubaci_desno(cvor15)
        cvor14.ubaci_dole(cvor21)
        cvor14.ubaci_gore(cvor6)
        cvor14.ubaci_levi(cvor13)
        cvor15.ubaci_dole(cvor24)
        cvor15.ubaci_gore(cvor3)
        cvor15.ubaci_levi(cvor14)
        cvor16.ubaci_desno(cvor17)
        cvor16.ubaci_gore(cvor12)
        cvor17.ubaci_desno(cvor18)
        cvor17.ubaci_dole(cvor20)
        cvor17.ubaci_levi(cvor16)
        cvor18.ubaci_gore(cvor13)
        cvor18.ubaci_levi(cvor17)
        cvor19.ubaci_desno(cvor20)
        cvor19.ubaci_gore(cvor11)
        cvor20.ubaci_desno(cvor21)
        cvor20.ubaci_dole(cvor23)
        cvor20.ubaci_gore(cvor17)
        cvor20.ubaci_levi(cvor19)
        cvor21.ubaci_gore(cvor14)
        cvor21.ubaci_levi(cvor20)
        cvor22.ubaci_desno(cvor23)
        cvor22.ubaci_gore(cvor10)
        cvor23.ubaci_desno(cvor24)
        cvor23.ubaci_gore(cvor20)
        cvor23.ubaci_levi(cvor22)
        cvor24.ubaci_gore(cvor15)
        cvor24.ubaci_levi(cvor23)


        self.mapa_cvorova = HashMap(24)
        self.mapa_cvorova.__setitem__(1, cvor1)
        self.mapa_cvorova.__setitem__(2, cvor2)
        self.mapa_cvorova.__setitem__(3, cvor3)
        self.mapa_cvorova.__setitem__(4, cvor4)
        self.mapa_cvorova.__setitem__(5, cvor5)
        self.mapa_cvorova.__setitem__(6, cvor6)
        self.mapa_cvorova.__setitem__(7, cvor7)
        self.mapa_cvorova.__setitem__(8, cvor8)
        self.mapa_cvorova.__setitem__(9, cvor9)
        self.mapa_cvorova.__setitem__(10, cvor10)
        self.mapa_cvorova.__setitem__(11, cvor11)
        self.mapa_cvorova.__setitem__(12, cvor12)
        self.mapa_cvorova.__setitem__(13, cvor13)
        self.mapa_cvorova.__setitem__(14, cvor14)
        self.mapa_cvorova.__setitem__(15, cvor15)
        self.mapa_cvorova.__setitem__(16, cvor16)
        self.mapa_cvorova.__setitem__(17, cvor17)
        self.mapa_cvorova.__setitem__(18, cvor18)
        self.mapa_cvorova.__setitem__(19, cvor19)
        self.mapa_cvorova.__setitem__(20, cvor20)
        self.mapa_cvorova.__setitem__(21, cvor21)
        self.mapa_cvorova.__setitem__(22, cvor22)
        self.mapa_cvorova.__setitem__(23, cvor23)
        self.mapa_cvorova.__setitem__(24, cvor24)

        

    def print_table(self):
        print('                                                                                                              Raspored polja na tabli\n'
            '                     {}--------------{}---------------{}                                                  1 --------------2 ---------------3\n'
            '                     |               |                |                                                   |               |                |\n'
            '                     |    {}---------{}----------{}   |                                                   |    4 ---------5 ----------6    |\n'
            '                     |    |          |           |    |                                                   |    |          |           |    |\n'
            '                     |    |    {}----{}-----{}   |    |                                                   |    |    7 ----8 -----9    |    |\n'
            '                     |    |    |            |    |    |                                                   |    |    |            |    |    |\n'
            '                     {}---{}---{}           {}---{}---{}                                                 10 ---11---12           13---14---15\n'
            '                     |    |    |            |    |    |                                                   |    |    |            |    |    |\n'
            '                     |    |    {}----{}-----{}   |    |                                                   |    |    16----17----18    |    |\n'
            '                     |    |          |           |    |                                                   |    |          |           |    |\n'
            '                     |    {}---------{}----------{}   |                                                   |    19---------20---------21    |\n'
            '                     |               |                |                                                   |               |                |\n'
            '                     {}--------------{}---------------{}                                                 22--------------23---------------24\n'.format(
            self.mapa_cvorova.__getitem__(1), 
            self.mapa_cvorova.__getitem__(2), 
            self.mapa_cvorova.__getitem__(3), 
            self.mapa_cvorova.__getitem__(4), 
            self.mapa_cvorova.__getitem__(5), 
            self.mapa_cvorova.__getitem__(6), 
            self.mapa_cvorova.__getitem__(7), 
            self.mapa_cvorova.__getitem__(8), 
            self.mapa_cvorova.__getitem__(9), 
            self.mapa_cvorova.__getitem__(10), 
            self.mapa_cvorova.__getitem__(11), 
            self.mapa_cvorova.__getitem__(12), 
            self.mapa_cvorova.__getitem__(13), 
            self.mapa_cvorova.__getitem__(14), 
            self.mapa_cvorova.__getitem__(15), 
            self.mapa_cvorova.__getitem__(16), 
            self.mapa_cvorova.__getitem__(17), 
            self.mapa_cvorova.__getitem__(18), 
            self.mapa_cvorova.__getitem__(19), 
            self.mapa_cvorova.__getitem__(20), 
            self.mapa_cvorova.__getitem__(21), 
            self.mapa_cvorova.__getitem__(22), 
            self.mapa_cvorova.__getitem__(23), 
            self.mapa_cvorova.__getitem__(24), 

           ))
        print()

    def provera_figura_pomeraj(self, figura, pomeraj):    
        cvorf= self.mapa_cvorova.__getitem__(figura)
        cvorp= self.mapa_cvorova.__getitem__(pomeraj)
        if cvorf.desni!=None and cvorf.desni.pozicija==cvorp.pozicija:
            return True
        elif cvorf.levi!=None and cvorf.levi.pozicija==cvorp.pozicija:         #da li su figura i pomeraj jedno do drugog
            return True
        elif cvorf.gore!=None and cvorf.gore.pozicija==cvorp.pozicija:
            return True
        elif cvorf.dole!=None and cvorf.dole.pozicija==cvorp.pozicija:
            return True
        return False

    def provera_pozicija(self, pozicija):
        if pozicija < 1 or pozicija > 24:
            return False
        if self.mapa_cvorova.__getitem__(pozicija).vrednost != None:
            return False
        return True

    def provera_protivnikove_figure(self, pozicija):
        if pozicija < 1 or pozicija > 24:
            return False
        if self.mapa_cvorova.__getitem__(pozicija).vrednost == "C":
            return True
        return False

    def provera_bele_figure(self, pozicija):
        if pozicija < 1 or pozicija > 24:
            return False
        if self.mapa_cvorova.__getitem__(pozicija).vrednost == "B":
            return True
        return False
        
    def set_vrednost(self, vrednost, pozicija):
        self.mapa_cvorova.__getitem__(pozicija).vrednost = vrednost

    def moguci_cvorovi(self):
        moguci_cvorovi = []
        for i in range(1, 25):
            if self.mapa_cvorova.__getitem__(i).vrednost == None:
                moguci_cvorovi.append(i)
        return moguci_cvorovi

    def kopiraj_tablu(self):
        tabla_nova = copy.deepcopy(self)
        return tabla_nova

    def broj_figura(self):
        crniB=0
        beliB=0
        for i in range(1, 25):
            if self.mapa_cvorova.__getitem__(i).vrednost == 'C':
                crniB+=1
            elif self.mapa_cvorova.__getitem__(i).vrednost == 'B':
                beliB+=1
        return [crniB, beliB]     
    
    def hash_code(self):
        hash = ''
        for i in range(1, 25):
            hash += str(self.mapa_cvorova.__getitem__(i).vrednost)
        return hash

    def svi_elementi(self):
        lista = []
        for i in range(1, 25):
            lista.append(self.mapa_cvorova.__getitem__(i).vrednost)
        return lista
    def pronadji_sve_figure(self, figura):
        lista = []
        for i in range(1, 25):
            if self.mapa_cvorova.__getitem__(i).vrednost == figura:
                lista.append(i)
        return lista
                           
    
