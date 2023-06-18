
class Animal():
    """virtual animal"""
    total_amount_animals = 0

    def __init__(self, name):
        print("Urodził się jakiś nowy zwirzak.")
        self.name = name    # czy to inicjalizacja atrybutu ???
        Animal.total_amount_animals += 1

    def __repr__(self):
        return f'Jestem egzemplarzem klasy zwierzak i nazywam się {self.name}'

    def __str__(self):
        rep = f'Obiekt klasy Animal o imieniu {self.name}'
        return rep

    def die(self):
        print("zwierzątko umarło")
        Animal.total_amount_animals -= 1

    def talk(self):
        print("Cześć, jestem egzemplarzem klasy zwierzak")

    @staticmethod
    def breeding_status():
        print(f'ilość zwierząt w hodowli = {Animal.total_amount_animals}')

    def eat(self, food):
        print("Coś zeżarło roślinkę") # zrobić tak, żeby podąło imię zjadającego
        food.die()


class Wombat(Animal):
    def __init__(self):
        super(Wombat,self).__init__(name="Torbacz")
        print("Działa super, jestem Wombat")

    def make_wombat_sound(self):
        print("grrrrgghhhhyyy")


class Cat(Animal):
    def __init(self,name):
        super(Cat,self).__init__()
        print("Działa super z namem")

    def miau(self):
        print("miiaaaaauuuuu")


class Plant():
    """virtual pant"""
    total_amount_plants = 0

    def __init__(self, name):
        print("Wyrosła roślinka")
        self.name = name
        Plant.total_amount_plants += 1

    def __str__(self):
        rep = f'Obiekt klasy Plant o imieniu {self.name}'
        return rep

    def die(self):
        print("roślinka umarła")
        Plant.total_amount_plants -= 1





animal1 = Animal(name="Reksio")
animal2 = Animal("Ziutek")
animal1.talk()
animal2.talk()
print("animal1.name - ",animal1.name, Animal.total_amount_animals)
print("animal2.name - ",animal2.name, Animal.total_amount_animals)
print("animal1 - ",animal1)
print("animal2 - ",animal2)
print("Animal.total_amount_animals - ",Animal.total_amount_animals)
womabt1 = Wombat()
print("wombat1 - ",womabt1)
cat1 = Cat("Filemon")
print("cat1 - ",cat1)
cat1.miau()
womabt1.make_wombat_sound()
cat1.talk()
plant1 = Plant(name="oak")
plant2 = Plant(name="flower")
plant3 = Plant(name="grass")
print(plant1, Plant.total_amount_plants)
print("ILOŚĆ ROŚLIN: ", Plant.total_amount_plants, "ilość zwierząt:", Animal.total_amount_animals)

# TODO: rozszerzyć rosiczkę o zjadanie zwierzaków
cat1.eat(plant1)
print("ILOŚĆ ROŚLIN: ", Plant.total_amount_plants, "ilość zwierząt:", Animal.total_amount_animals)

