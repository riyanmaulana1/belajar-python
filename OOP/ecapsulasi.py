#latihan encapsulasi
'''sistem lv dan exp '''

class Hero :
    __jumlah = 0

    def __init__(self,name,health,attPower,armor):
        self.__name = name
        self.__healthStandar = health 
        self.__atkPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__atkPower = self.__atkPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        
        self.__health = self.__healthMax

        Hero.__jumlah += 1 
    

    @property
    def info(self):
        return "nama {} level {} : \n\t health : {}/{} \n\t atkPower : {} \n\t armor : {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__atkPower,self.__armor)
    
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        while (self.__exp >= 100) :
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * (1.5 ** (self.__level-1))
            self.__atkPower = self.__atkPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

            self.__health = self.__healthMax

            print(self.__name, "level up! level sekarang adalah ",self.__level)


    def attack(self, Lawan): 
        print(self.__name +' menyerang ' +Lawan.__name)
        Lawan.diserang(self,self.__atkPower)
        self.gainExp = 50

    def diserang(self,Lawan,attackpower_lawan):
        print(self.__name + ' diserang ' +Lawan.__name)
        attack_diterima = attackpower_lawan/self.__armor
        print(f"serangan terasa adalah : {str(attack_diterima)}")
        self.__health -= attack_diterima
        print("darah "+self.__name +" tersisa "+ str(self.__health)+"\n")

miya = Hero("Miya",2225,115,17)
gwen = Hero("Gwen",2300,130,20)
print(miya.info)

print()
miya.attack(gwen)
miya.attack(gwen)
print()

print("Status kedua hero")
print(miya.info)
print(gwen.info)
