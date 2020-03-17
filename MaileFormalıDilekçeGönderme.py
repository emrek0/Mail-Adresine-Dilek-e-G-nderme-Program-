class Karakter():
    def __init__(self, can, guc):
        self.can=can
        self.guc=guc


    def vur(self, rakip):
        rakip.can -= self.guc



x= Karakter(70, 40)
y= Karakter(100, 50)


print( "Birinci Durumda Canı : ",x.can)

y.vur(x)

print("İkinci Durumda Canı: ", x.can)
