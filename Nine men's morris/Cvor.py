class Cvor(object):
    def __init__(self, pozicija, vrednost):
        self.pozicija = pozicija
        self.vrednost = vrednost
        self.levi = None
        self.desni = None
        self.gore = None
        self.dole = None
    
    def ubaci_levi(self, levi):
        self.levi = levi

    def ubaci_desno(self, desni):
        self.desni = desni

    def ubaci_gore(self, gore):
        self.gore = gore
    
    def ubaci_dole(self, dole):
        self.dole = dole

    def __str__(self):
        if self.vrednost == None:  
            return "  "
        return str(self.vrednost) + ' '
