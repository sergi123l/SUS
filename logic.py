from random import randint

import requests

# Функция для получения рандомной картинки покемона через API
def get_img():
    url = f'https://pokeapi.co/api/v2/pokemon/{randint(1,1000)}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return (data['sprites']['other']['home']['front_default'])
    else:
        get_img()

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, name):
        self.paw = randint(50,110)
        self.hopi = randint(250,500)
        sus = randint(5,10)
        self.name = name    # Поле или атрибут класса
        if sus == 5 :
            self.sus = "https://i.pinimg.com/originals/c1/16/b7/c116b7e8a3f87176d1492936181bbf1e.jpg"
        else:
            self.sus = "https://i.ytimg.com/vi/rgrojk0qRnw/maxresdefault.jpg"
        
        if self.paw > 19:
            self.sot = 'https://i.yapx.cc/GvBae.gif'
        else:
            self.sot = 'https://avatars.mds.yandex.net/i?id=670a5c569f6fd02740ceea44a800424ca4bed18d-9863472-images-thumbs&n=13'
        self.img = get_img()

        Pokemon.pokemons[name] = self

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}, ед. здоровья - {self.hopi} силушки - {self.paw}"
    def __lt__(self,other):
        return self.hopi < other.hopi
    def __gt__(self,other):
        return self.hopi > other.hopi
    def __eq__(self,other):
        return self.hopi == other.hopi
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def sas(self):
        return self.sus
    def sad(self):
        return self.sot
    def attack(self, enemy):
            if enemy.hopi > self.paw:
                enemy.hopi -= self.paw
                return f"Сражение @{self.name} с @{enemy.name},врагу снесли {enemy.hopi}"
            else:
                enemy.hp = 0
                return f"Победа @{self.name} над @{enemy.name}! "
            
    def hill(self):
        self.hopi += 200
        return f'здоровье - {self.hopi}'
class Figher(Pokemon):
    def attack(self, enemy):
        udar = randint(1,3)
        if udar == 2 :
            self.paw += 15
        blok = randint(1,59)
        if blok != 56:
            return super().attack(enemy)
class Wizzard(Pokemon):
    def attack(self, enemy):
        nope = randint(1,3)
        aga = randint (1,5)
        if nope == 2:
            enemy.hopi += 9
        if aga == 3:
            self.hopi += 25
            enemy.paw -= 12
        return super().attack(enemy)
    
Ba =Pokemon("user1")
se =Pokemon("user2")

print(Ba.info())
print(se.info())
print(Ba < se)
print(se < Ba)
print(Ba > se)
print(se > Ba)
print(se == Ba)

















