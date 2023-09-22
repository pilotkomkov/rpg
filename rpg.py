import random
import time
class Player :
    def __init__(self, name, hp, dmg):
        self.name=name
        self.hp=hp
        self.dmg=dmg
        self.lvl=1
        self.exp=0
    def player_create(name,choose_race,job_choose):
        hp = 0
        dmg = 0
        if choose_race== races_list[0]:
            hp += 75
            dmg += 90
        elif choose_race == races_list[1]:
            hp += 91
            dmg += 100
        elif choose_race == races_list[2]:
            hp += 100
            dmg += 70
        elif choose_race ==races_list[3]:
            hp+=65
            dmg+=90
        else:
            print("In our world do not live this race")
            hp+=0
            dmg+=0
        if job_choose==job_list[0]:
            hp+=35
            dmg+=34
        elif job_choose==job_list[1]:
            hp+=20
            dmg+=19
        elif job_choose==job_list[2]:
            hp+=26
            dmg+=29
        elif job_choose==job_list[3]:
            hp+=50
            dmg+=50    
        else:
            print("You can not have this job")
            hp+=0
            dmg +=0
        return Player(name,hp,dmg)
    def attack(self,victim):
        maximum.xp = self.lvl*10
        victim.hp-=self.dmg
        if victim.hp<=0:
            print(f"Congrats {victim.name} is dead")
            return False
        else:
            print(f"{victim.name} is alive{victim.hp}")
            return True
    def lvl_up(maximum_xp):
        self.exp -= maximum_xp
        self.lvl += 1
        self.dmg += self.lvl*2
        self.hp += self.lvl*2
        print(f"Поздравляем! Вы прокачали {self.lvl}")
class Enemy:
    def __init__(self,name,hp,dmg):
        self.name=name
        self.hp=hp
        self.dmg=dmg
    def  create_enemy () :
        enemy_name=random.choice(enemy_list)
        enemy_hp=random.randint(300,550)
        enemy_dmg=random.randint(150,300)
        return Enemy(enemy_name,enemy_hp,enemy_dmg)
    def attack (self,victim):
        victim.hp-=self.dmg
        if victim.hp<=0:
            print("You lose")
            time.sleep(2)
            quit()
        else:
            print(f"{victim.name},{victim.hp}")
            time.sleep(2)
def choose():
    ask=input(f"Do you want to fight with{enemy.name}?")
    if ask=="Yes" or ask == "yes":
        result=hero.attack(enemy)
        if result==True:
            enemy.attack(hero)
            choose()
    elif ask =="No" or ask == "no":
        print("You escape")
    else:
        print("Uncorrect command")
        choose()
races_list = ["Elfs", "Gnoms", "Humans", "Magicians"]
job_list = ["Sworder", "Healer", "Airer","witcher"]
enemy_list = ["Org", "Goblin", "мотемотичка"]

name=input("What is your name?")
choose_race = input(f"What is your race?{races_list}")
print(choose_race)
job_choose = input(f"What is your job?{job_list}")
hero = Player.player_create(name, choose_race, job_choose)
print(hero.name, hero.hp, hero.dmg, hero.lvl,hero.exp)
while True:
    events = random.randint(1, 2)
    if events == 1:
        print("никто не встретился")
    elif events == 2:
        enemy = Enemy.create_enemy()    
        print(f"вы встретили {enemy.name}")
        print(f"у вас {hero.hp} здоровья, и {hero.dmg} урона") 
        print(f"у врага {enemy.hp} здоровья, и {enemy.dmg} урона")
        time.sleep(2)
        choose()
