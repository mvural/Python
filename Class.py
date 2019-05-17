class Araba():
    def __init__(self,model,renk,beygir_gücü):
        print("init fonksiyonu çağrıldı")
        self.model = model
        self.renk = renk
        self.beygir_gücü = beygir_gücü
        
araba1 = Araba("BMW","white","260")
araba2 = Araba("Mercedes","white","290")
araba3 = Araba("Porsche","red","290")
print (araba1.model,araba1.renk,araba1.beygir_gücü)
print (araba2.model,araba2.renk,araba2.beygir_gücü)
print (araba3.model,araba3.renk,araba3.beygir_gücü)