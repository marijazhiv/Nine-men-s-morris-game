import traceback
from min_max_pretraga import Min_max_pretraga
from stanje import Stanje
from tabla import Tabla
import time
import datetime


def protivnikov_potez(tabla):
    while True:
        try:
            potez = input("unesite potez")
            potez = int(potez)
            
            if tabla.provera_pozicija(potez) == False:
                continue
            return potez
        except:
            print("Neispravna pozicija. Unesite broj ponovo: ")
def pomeri(stanje):
    while True:
        try:
            figura = input("unesite figuru koju zelite da pomerite")
            figura = int(figura)

            print('unet broj')

            if stanje.tabla.provera_bele_figure(figura)== False:
                print("nije vasa figura")
                continue

            pomeraj = input("unesite gde zelite da je pomerite")
            pomeraj = int(pomeraj)

            if stanje.tabla.provera_pozicija(pomeraj) == False:
                print('nije prazno polje')
                continue
            if stanje.tabla.provera_figura_pomeraj(figura, pomeraj) == False:
                print('nisu susedi')
                continue
            stanje.tabla.mapa_cvorova.__getitem__(pomeraj).vrednost = 'B'
            stanje.tabla.mapa_cvorova.__getitem__(figura).vrednost = None
            return pomeraj

        except:
            traceback.print_exc()
            print("Pogresan unos")

def uklanjanje (stanje):
    tabla = stanje.tabla
    while True:
        try: 
            ukloni = input("unesite poziciju protivnikove figure koju želite da uklonite: ")
            ukloni = int(ukloni)
            cvor = tabla.mapa_cvorova.__getitem__(ukloni)

            if tabla.provera_protivnikove_figure(ukloni):
                if stanje.da_li_su_svi_crni_u_morisu():
                    return ukloni
                if not stanje.trenutni_potez_moris(ukloni):
                    return ukloni

        except:
            print("Neispravan unos. Unesite poziciju ponovo: ")

if __name__ == '__main__':
    na_redu = 'beli'
    tabla = Tabla()
    stanje = Stanje(tabla)
    faza="Faza1"
    pretraga = Min_max_pretraga()
    iter=0
    while iter<9:
        if na_redu == 'beli':
            stanje.tabla.print_table()
            potez = protivnikov_potez(stanje.tabla)
            stanje.tabla.set_vrednost('B', potez)
            if stanje.trenutni_potez_moris(potez):
                stanje.tabla.print_table() 
                print("Sklopili ste micu")
                potez = uklanjanje(stanje)
                stanje.tabla.set_vrednost(None, potez)
                stanje.tabla.print_table()
            na_redu = 'crni'
            print('korisnik (beli igrac) je odigrao potez ', potez)                                   
        else:
            start = time.time()
            a = datetime.datetime.now()
            stanje.tabla.print_table()
            stanjaMoguca = stanje.next_states('C', pretraga.mapaVecPronadjenih, 'Faza1')
            if len(stanjaMoguca) < 7:
                stanje = pretraga.next_move(stanje, 4, faza)    
            elif len(stanjaMoguca) < 15:
                stanje = pretraga.next_move(stanje, 3, faza)
            else:
                stanje = pretraga.next_move(stanje, 2, faza)

            end = time.time()
            b = datetime.datetime.now()
            print('Evaluation time: {}s'.format(round(end - start, 9)))
            na_redu = 'beli'
            iter+=1
            print(iter)
    faza = "Faza 2"
    pretraga = Min_max_pretraga()
    while True:
        if stanje.da_li_je_kraj_igre():
            stanje.tabla.print_table()
            obrnuto='crni'
            if na_redu== 'crni':
                obrnuto='beli'
            print("Igra je zavrsena")
            print("Pobednik je", obrnuto, "igrac")
            break
        if na_redu == 'beli':
            stanje.tabla.print_table()
            pomeraj = pomeri(stanje)
            if stanje.trenutni_potez_moris(pomeraj):
                stanje.tabla.print_table() 
                print("Sklopili ste micu")
                pomeraj = uklanjanje(stanje)
                stanje.tabla.set_vrednost(None, pomeraj)
                stanje.tabla.print_table()
            na_redu = 'crni'                                  
        else:
            start = time.time()
            a = datetime.datetime.now()
            stanje.tabla.print_table()
            stanjaMoguca = stanje.next_states('C', pretraga.mapaVecPronadjenih, 'Faza1')
            if len(stanjaMoguca) < 10:
                stanje = pretraga.next_move(stanje, 4, faza)      
            elif len(stanjaMoguca) < 20:
                stanje = pretraga.next_move(stanje, 3, faza) 
            else:
                stanje = pretraga.next_move(stanje, 2, faza)       
            end = time.time()
            b = datetime.datetime.now()
            print('Evaluation time: {}s'.format(round(end - start, 9)))
            na_redu = 'beli'
            

    


