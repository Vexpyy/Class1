# sınıflar -> Fabrikaya benzer
# nesneler -> ürün

class Ogrenci():
    "Bu sınıf öğrenciyi tanımlar."
    def __init__(self): 
        "bu method otomatik çalışır"
        self.name = "Çağlar"
        self.age = 14
        self.coding_lesson = "Python"

ogr1 = Ogrenci()
print(ogr1.name)

ogr2 = Ogrenci()
print(ogr2.name, ogr2.age, ogr2.coding_lesson)

class Ogrenci2():
    counter = 0 # sınıfa ait bir değişken
    def __init__(self, name, age, coding_lesson):
        self.name = name
        self.age = age
        self.coding_lesson = coding_lesson
        Ogrenci2.counter += 1

    def get_info(self): # nesne metodlarına daima self yazılır!
        print("isim =",self.name, "yaş =",self.age, "ders =",self.coding_lesson)

    def update_info(self,name,age,coding_lesson):
        self.name = name
        self.age = age
        self.coding_lesson = coding_lesson
        self.get_info()

    def __str__(self):
        return self.name


ogr3 = Ogrenci2("Selman", 14, "Python")
ogr4 = Ogrenci2("İhsan", 14, "Javascript")
print(ogr3.name, ogr4.name) # Selman İhsan

ogr4.get_info() # isim = İhsan yaş = 14 ders = Javascript
ogr4.update_info(age=14,name="Çağlar",coding_lesson="ileri seviye python")

print(f"toplam öğrenci sayısı ={Ogrenci2.counter}")

print(ogr4) # <__main__.Ogrenci2 object at 0x0000021F20564C10>



