class Stanje(object):
    def __init__(self, tabla):
        self.tabla = tabla
        self.deca = []      #ako ubaci morisa deca mogu biti drugacija od stanja pre
        self.faza = 'postavljanje_figura'
        self.pokupljen_moris = False

    def ko_je_na_redu(self, na_potezu):
        if na_potezu == 'C':
            protivnik = 'B'
            protivnik_ceo_u_morisu = self.da_li_su_svi_beli_u_morisu()
        else:
            protivnik = 'C'
            protivnik_ceo_u_morisu = self.da_li_su_svi_crni_u_morisu()
        lista_indexa = self.tabla.pronadji_sve_figure(protivnik)

        lista_pojedenih = []
        for index in lista_indexa:
            if self.trenutni_potez_moris(index) and not protivnik_ceo_u_morisu:
                continue
            tabla_kopija = self.tabla.kopiraj_tablu()
            stanje = Stanje(tabla_kopija)
            tabla_kopija.set_vrednost(None, index)
            lista_pojedenih.append(stanje)
        return lista_pojedenih

    def pomeranje (self,ciji_potez):
        lista_sl_pomeranja = []          #lista svih stanja gde figura moze da se pomeri
        for i in range(1, 25):
            cvor = self.tabla.mapa_cvorova.__getitem__(i)
            if cvor.vrednost == ciji_potez:
                lista_pomeranja = self.kretanje(cvor)
                if len(lista_pomeranja) == 0:
                    continue
                for elem in lista_pomeranja:
                    tabla_kopija = self.tabla.kopiraj_tablu()          
                    stanje = Stanje(tabla_kopija)
                    if elem == 'desno':
                        tabla_kopija.set_vrednost(None, i)
                        tabla_kopija.mapa_cvorova.__getitem__(i).desni.vrednost = ciji_potez
                        if stanje.trenutni_potez_moris(tabla_kopija.mapa_cvorova.__getitem__(i).desni.pozicija):
                            lista_sl_pomeranja.extend(stanje.ko_je_na_redu(ciji_potez))
                            stanje.pokupljen_morisf = ciji_potez
                        else:
                            lista_sl_pomeranja.append(stanje)
                    if elem == 'levo':
                        tabla_kopija.set_vrednost(None, i)
                        tabla_kopija.mapa_cvorova.__getitem__(i).levi.vrednost = ciji_potez
                        if stanje.trenutni_potez_moris(tabla_kopija.mapa_cvorova.__getitem__(i).levi.pozicija):
                            lista_sl_pomeranja.extend(stanje.ko_je_na_redu(ciji_potez))
                            stanje.pokupljen_morisf = ciji_potez
                        else:
                            lista_sl_pomeranja.append(stanje)
                    if elem == 'gore':
                        tabla_kopija.set_vrednost(None, i)
                        tabla_kopija.mapa_cvorova.__getitem__(i).gore.vrednost = ciji_potez
                        if stanje.trenutni_potez_moris(tabla_kopija.mapa_cvorova.__getitem__(i).gore.pozicija):
                            lista_sl_pomeranja.extend(stanje.ko_je_na_redu(ciji_potez))
                            stanje.pokupljen_morisf = ciji_potez
                        else:
                            lista_sl_pomeranja.append(stanje)
                    if elem == 'dole':
                        tabla_kopija.set_vrednost(None, i)
                        tabla_kopija.mapa_cvorova.__getitem__(i).dole.vrednost = ciji_potez
                        if stanje.trenutni_potez_moris(tabla_kopija.mapa_cvorova.__getitem__(i).dole.pozicija):
                            lista_sl_pomeranja.extend(stanje.ko_je_na_redu(ciji_potez))
                            stanje.pokupljen_morisf = ciji_potez
                        else:
                            lista_sl_pomeranja.append(stanje)

        self.deca = lista_sl_pomeranja
        return lista_sl_pomeranja

    def pokupljen_morisf(self):
        if self.pokupljen_moris=="C":
            return 1
        if self.pokupljen_moris=="B":
            return -1
        return 0

    def next_states(self, ciji_potez, mapa_postojecih, faza):
        try:
            stanje = mapa_postojecih.__getitem__(self.hash_code(faza))      #brisanje polja hash se menja, dodati ko je na redu
            return stanje.deca
        except:
            mapa_postojecih.__setitem__(self.hash_code(faza), self)
        if faza=="Faza1":
            cvorovi = self.tabla.moguci_cvorovi()
            self.deca.clear()
            for i in range(len(cvorovi)):
                tabla_kopija = self.tabla.kopiraj_tablu()
                stanje = Stanje(tabla_kopija)
                tabla_kopija.set_vrednost(ciji_potez, cvorovi[i])
                if stanje.trenutni_potez_moris(cvorovi[i]):
                    stanje.pokupljen_morisf = ciji_potez   #
                    self.deca.extend(stanje.ko_je_na_redu(ciji_potez))
                else:
                    self.deca.append(stanje)
            
            return self.deca
        else:
            lista = self.pomeranje(ciji_potez)   
            if len(lista) == 0:
                return []
            return lista

    def heuristika4(self):
        brojFigura = self.tabla.broj_figura()
        return brojFigura[0]- brojFigura[1]

    def broj_morisa_pomoc(self, cvor):
        brojac = 0
        if cvor.desni != None and cvor.desni.vrednost == cvor.vrednost:
            if cvor.levi != None and cvor.levi.vrednost == cvor.vrednost:
                brojac += 1
        if cvor.gore != None and cvor.gore.vrednost == cvor.vrednost:
            if cvor.dole != None and cvor.dole.vrednost == cvor.vrednost:
                brojac += 1
        return brojac

    def broj_morisa2(self):
        broj_crnih_morisa = 0
        broj_belih_morisa = 0
        for i in range(1, 25):
            retVal = self.broj_morisa_pomoc(self.tabla.mapa_cvorova.__getitem__(i))
            if self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'C':
                broj_crnih_morisa += retVal
            elif self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'B':
                broj_belih_morisa += retVal
            
        return broj_crnih_morisa - broj_belih_morisa

    def broj_blokiranih_pomoc(self, cvor):
        obrnuta_vrednost = 'C'
        if cvor.vrednost == 'C':
            obrnuta_vrednost = 'B'
        blokiraniBrojac=0
        brojPuteva=0
        if cvor.desni != None:
            brojPuteva+=1
        if cvor.levi != None:
            brojPuteva+=1
        if cvor.gore != None:
            brojPuteva+=1
        if cvor.dole != None:
            brojPuteva+=1

        if cvor.desni != None and cvor.desni.vrednost==obrnuta_vrednost:
            blokiraniBrojac+=1
        if cvor.levi != None and cvor.levi.vrednost==obrnuta_vrednost:
            blokiraniBrojac+=1
        if cvor.gore != None and cvor.gore.vrednost==obrnuta_vrednost:
            blokiraniBrojac+=1
        if cvor.dole != None and cvor.dole.vrednost==obrnuta_vrednost:
            blokiraniBrojac+=1

        if blokiraniBrojac==brojPuteva:
            return True
        else:
            return False

    def broj_blokiranih3(self):
        broj_blokiranih_crnih = 0 #naši
        broj_blokiranih_belih = 0  #protivnikovi
        for i in range(1, 25):
            retVal = self.broj_blokiranih_pomoc(self.tabla.mapa_cvorova.__getitem__(i))
            if retVal and self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'C':
                broj_blokiranih_crnih += 1
            elif retVal and self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'B':
                 broj_blokiranih_belih += 1
            
        return broj_blokiranih_belih - broj_blokiranih_crnih

    def broj_dvoniza_pomoc(self, cvor):
        brojacDvoniza=0
        if cvor.desni != None and cvor.desni.vrednost == cvor.vrednost:
            if cvor.desni.desni != None and cvor.desni.desni.vrednost == None: 
                brojacDvoniza+=1
        if cvor.levi != None and cvor.levi.vrednost == cvor.vrednost:
            if cvor.levi.levi != None and cvor.levi.levi.vrednost== None:
                brojacDvoniza+=1
        if cvor.dole != None and cvor.dole.vrednost == cvor.vrednost:
            if cvor.dole.dole != None and cvor.dole.dole.vrednost== None:
                brojacDvoniza+=1
        if cvor.gore != None and cvor.gore.vrednost == cvor.vrednost:
            if cvor.gore.gore != None and cvor.gore.gore.vrednost== None:
                brojacDvoniza+=1
        return brojacDvoniza

    def broj_dvoniza5(self):
        broj_dvoniza_crnih = 0 #naši
        broj_dvoniza_belih = 0  #protivnikovi
        for i in range(1, 25):
            retVal = self.broj_dvoniza_pomoc(self.tabla.mapa_cvorova.__getitem__(i))
            if self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'C':
                broj_dvoniza_crnih += retVal
            elif self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'B':
                broj_dvoniza_belih += retVal
            
        return broj_dvoniza_crnih - broj_dvoniza_belih

    def tri_konfiguracija_pomocni(self, cvor):
        brojacTriKonfiguracije=0
        if cvor.gore != None and cvor.gore.vrednost == cvor.vrednost:
            if cvor.gore.gore != None:
                if cvor.gore.gore.vrednost == None:
                    brojacTriKonfiguracije+=1
            elif cvor.dole.vrednost == None:
                    brojacTriKonfiguracije += 1
        if cvor.desni != None and cvor.desni.vrednost == cvor.vrednost:
            if cvor.desni.desni != None:
                if cvor.desni.desni.vrednost == None:
                    brojacTriKonfiguracije+=1
            elif cvor.levi.vrednost == None:
                    brojacTriKonfiguracije += 1
        if cvor.levi != None and cvor.levi.vrednost == cvor.vrednost:
            if cvor.levi.levi != None:
                if cvor.levi.levi.vrednost == None:
                    brojacTriKonfiguracije+=1
            elif cvor.desni.vrednost == None:
                    brojacTriKonfiguracije += 1
        if cvor.dole != None and cvor.dole.vrednost == cvor.vrednost:
            if cvor.dole.dole != None:
                if cvor.dole.dole.vrednost == None:
                    brojacTriKonfiguracije+=1
            elif cvor.gore.vrednost == None:
                    brojacTriKonfiguracije += 1

        if brojacTriKonfiguracije==2:
            return True

    def tri_konfiguracija6(self):
        broj_tri_konfiguracija_crnih = 0 #naši
        broj_tri_konfiguracija_belih = 0  #protivnikovi
        for i in range(1, 25):
            retVal = self.tri_konfiguracija_pomocni(self.tabla.mapa_cvorova.__getitem__(i))
            if retVal and self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'C':
                broj_tri_konfiguracija_crnih +=1
            elif retVal and self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'B':
                broj_tri_konfiguracija_belih += 1
            
        return broj_tri_konfiguracija_crnih - broj_tri_konfiguracija_belih

    def double_morris_pomocni(self, cvor):
        doubleMorrisBrojac=0
        if cvor.gore != None and cvor.gore.vrednost == cvor.vrednost:
            if cvor.gore.gore != None:
                if cvor.gore.gore.vrednost == cvor.vrednost:
                    doubleMorrisBrojac+=1
            elif cvor.dole.vrednost == cvor.vrednost:
                    doubleMorrisBrojac += 1
        if cvor.desni != None and cvor.desni.vrednost == cvor.vrednost:
            if cvor.desni.desni != None:
                if cvor.desni.desni.vrednost == cvor.vrednost:
                    doubleMorrisBrojac+=1
            elif cvor.levi.vrednost == cvor.vrednost:
                    doubleMorrisBrojac += 1
        if cvor.levi != None and cvor.levi.vrednost == cvor.vrednost:
            if cvor.levi.levi != None:
                if cvor.levi.levi.vrednost == cvor.vrednost:
                    doubleMorrisBrojac+=1
           
        if cvor.dole != None and cvor.dole.vrednost == cvor.vrednost:
            if cvor.dole.dole != None:
                if cvor.dole.dole.vrednost == cvor.vrednost:
                    doubleMorrisBrojac+=1
        return doubleMorrisBrojac == 2

    def double_morris7(self):
        broj_double_morris_crnih = 0 #naši
        broj_double_morris_belih = 0  #protivnikovi
        for i in range(1, 25):
            retVal = self.double_morris_pomocni(self.tabla.mapa_cvorova.__getitem__(i))
            if retVal and self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'C':
                broj_double_morris_crnih +=1
            elif retVal and self.tabla.mapa_cvorova.__getitem__(i).vrednost == 'B':
                broj_double_morris_belih += 1
            
        return broj_double_morris_crnih - broj_double_morris_belih

    def broj_blokiranih(self, cvor):   ## cvor je blokiran
        blokiraniBrojac=0
        brojPuteva=0
        if cvor.desni != None:
            brojPuteva+=1
        if cvor.levi != None:
            brojPuteva+=1
        if cvor.gore != None:
            brojPuteva+=1
        if cvor.dole != None:
            brojPuteva+=1

        if cvor.desni != None and cvor.desni.vrednost!=None:
            blokiraniBrojac+=1
        if cvor.levi != None and cvor.levi.vrednost!=None:
            blokiraniBrojac+=1
        if cvor.gore != None and cvor.gore.vrednost!=None:
            blokiraniBrojac+=1
        if cvor.dole != None and cvor.dole.vrednost!=None:
            blokiraniBrojac+=1

        if blokiraniBrojac==brojPuteva:
            return True
        else:
            return False

    def neblokirane_figure(self):
        lista_neblokiranih_crnih=[]
        lista_neblokiranih_belih=[]

        for i in range(1, 25):
            cvor = self.tabla.mapa_cvorova.__getitem__(i)

            if cvor.vrednost=="C":
                if not self.broj_blokiranih(cvor):
                    lista_neblokiranih_crnih.append(cvor)
            elif cvor.vrednost=="B":
                if not self.broj_blokiranih(cvor):
                    lista_neblokiranih_belih.append(cvor)
        return [lista_neblokiranih_crnih, lista_neblokiranih_belih]


    def da_li_je_kraj_igre(self):
        liste = self.neblokirane_figure()
        lista_neblokiranih_crnih = liste[0]
        lista_neblokiranih_belih = liste[1]
        tabla=self.tabla
        brojFigura = tabla.broj_figura()
        if brojFigura[0] < 3 or len(lista_neblokiranih_crnih) ==0:  #proveri da li je crni igrac skroz blokiran
            return True
        if brojFigura[1] < 3 or len(lista_neblokiranih_belih)==0 :   #proveri da li je beli skroz blokiran
            return True
        return False


    def heuristika(self):
        return self.pokupljen_morisf() * 18 + self.broj_morisa2() * 26 + self.broj_blokiranih3() * 1 + self.heuristika4() * 9 + self.broj_dvoniza5() * 10+ self.tri_konfiguracija6() * 7


#Evaluation function for Phase 1 = 18 * (1) + 26 * (2) + 1 * (3) + 9 * (4) + 10 * (5) + 7 * (6)

#Evaluation function for Phase 2 = 14 * (1) + 43 * (2) + 10 * (3) + 11 * (4) + 8 * (7) + 1086 * (8)
    def heuristika_faza2(self):
        return 14* self.pokupljen_morisf()+self.broj_morisa2() * 43 + self.broj_blokiranih3() * 10 + self.heuristika4() * 11 + self.double_morris7() * 8 +  1086 * self.da_li_je_kraj_igre()

    def hash_code(self, faza):
        return self.tabla.hash_code() + str(self.pokupljen_moris) + faza


    def trenutni_potez_moris(self, potez):
        cvor = self.tabla.mapa_cvorova.__getitem__(potez)
        if cvor.desni != None and cvor.desni.vrednost == cvor.vrednost:
            if cvor.desni.desni != None and cvor.desni.desni.vrednost == cvor.vrednost:
                return True

        if cvor.levi != None and cvor.levi.vrednost == cvor.vrednost:
            if cvor.levi.levi != None and cvor.levi.levi.vrednost == cvor.vrednost:
                return True

        if cvor.gore != None and cvor.gore.vrednost == cvor.vrednost:
            if cvor.gore.gore != None and cvor.gore.gore.vrednost == cvor.vrednost:
                return True
        
        if cvor.dole != None and cvor.dole.vrednost == cvor.vrednost:
            if cvor.dole.dole != None and cvor.dole.dole.vrednost == cvor.vrednost:
                return True

        if cvor.desni != None and cvor.desni.vrednost == cvor.vrednost:
            if cvor.levi != None and cvor.levi.vrednost == cvor.vrednost:
                return True
        
        if cvor.gore != None and cvor.gore.vrednost == cvor.vrednost:
            if cvor.dole != None and cvor.dole.vrednost == cvor.vrednost:
                return True
        return False
    
    def kretanje(self, cvor):
        lista_pomeranja=[]  #gde moze

        if cvor.desni != None and cvor.desni.vrednost == None:
           lista_pomeranja.append('desno')
        if cvor.levi != None and cvor.levi.vrednost == None:
            lista_pomeranja.append('levo')
        if cvor.dole != None and cvor.dole.vrednost == None:
            lista_pomeranja.append('dole')
        if cvor.gore != None and cvor.gore.vrednost == None:
            lista_pomeranja.append('gore')
        return lista_pomeranja
        
    def da_li_je_cvor_u_morisu(self):
        crni_cvorovi_u_morisu=[]
        beli_cvorovi_u_morisu=[]
        for i in range(1, 25):
            cvor = self.tabla.mapa_cvorova.__getitem__(i)
            if cvor.desni != None and cvor.desni.vrednost == cvor.vrednost:
                if cvor.desni.desni != None and cvor.desni.desni.vrednost == cvor.vrednost:
                    if cvor.vrednost=="C":
                        if cvor not in crni_cvorovi_u_morisu:
                            crni_cvorovi_u_morisu.append(cvor)
                    if cvor.vrednost=="B":
                        if cvor not in beli_cvorovi_u_morisu:
                            beli_cvorovi_u_morisu.append(cvor)
        
            if cvor.levi != None and cvor.levi.vrednost ==cvor.vrednost:
                if cvor.levi.levi != None and cvor.levi.levi.vrednost == cvor.vrednost:
                    if cvor.vrednost=="C":
                        if cvor not in crni_cvorovi_u_morisu:
                            crni_cvorovi_u_morisu.append(cvor)
                    if cvor.vrednost=="B":
                        if cvor not in beli_cvorovi_u_morisu:
                            beli_cvorovi_u_morisu.append(cvor)
                    

            if cvor.gore != None and cvor.gore.vrednost ==cvor.vrednost:
                if cvor.gore.gore != None and cvor.gore.gore.vrednost == cvor.vrednost:
                    if cvor.vrednost=="C":
                        if cvor not in crni_cvorovi_u_morisu:
                            crni_cvorovi_u_morisu.append(cvor)
                    if cvor.vrednost=="B":
                        if cvor not in beli_cvorovi_u_morisu:
                            beli_cvorovi_u_morisu.append(cvor)
            
            if cvor.dole != None and cvor.dole.vrednost == cvor.vrednost:
                if cvor.dole.dole != None and cvor.dole.dole.vrednost ==cvor.vrednost:
                    if cvor.vrednost=="C":
                        if cvor not in crni_cvorovi_u_morisu:
                            crni_cvorovi_u_morisu.append(cvor)
                    if cvor.vrednost=="B":
                        if cvor not in beli_cvorovi_u_morisu:
                            beli_cvorovi_u_morisu.append(cvor)

            if cvor.desni != None and cvor.desni.vrednost ==cvor.vrednost:
                if cvor.levi != None and cvor.levi.vrednost == cvor.vrednost:
                    if cvor.vrednost=="C":
                        if cvor not in crni_cvorovi_u_morisu:
                            crni_cvorovi_u_morisu.append(cvor)
                    if cvor.vrednost=="B":
                        if cvor not in beli_cvorovi_u_morisu:
                            beli_cvorovi_u_morisu.append(cvor)
            
            if cvor.gore != None and cvor.gore.vrednost == cvor.vrednost:
                if cvor.dole != None and cvor.dole.vrednost == cvor.vrednost:
                    if cvor.vrednost=="C":
                        if cvor not in crni_cvorovi_u_morisu:
                            crni_cvorovi_u_morisu.append(cvor)
                    if cvor.vrednost=="B":
                        if cvor not in beli_cvorovi_u_morisu:
                            beli_cvorovi_u_morisu.append(cvor)
        return [crni_cvorovi_u_morisu, beli_cvorovi_u_morisu]
    def da_li_su_svi_beli_u_morisu(self):
        tabla=self.tabla
        brojFigura = tabla.broj_figura()
        liste=self.da_li_je_cvor_u_morisu()
        lista_belih_u_morisu=liste[1]
        if brojFigura[1]==len(lista_belih_u_morisu):
            return True
        return False

    def da_li_su_svi_crni_u_morisu(self):
        tabla=self.tabla
        brojFigura = tabla.broj_figura()
        liste=self.da_li_je_cvor_u_morisu()
        lista_crnih_u_morisu=liste[0]
        if brojFigura[0]==len(lista_crnih_u_morisu):
            return True
        return False
