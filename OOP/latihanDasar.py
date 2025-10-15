#latihan OOP dasar
class Hero :

    def __init__ (self,Name:str,Health:int,attackPower:int,armorNumber:int):
        self.name = Name
        self.health = Health
        self.attackpower = attackPower
        self.armor = armorNumber

    def serang(self, Lawan): 
        print(self.name +' menyerang ' +Lawan.name)
        Lawan.diserang(self,self.attackpower)

    def diserang(self,Lawan,attackpower_lawan):
        print(self.name + ' diserang ' +Lawan.name)
        attack_diterima = attackpower_lawan/self.armor
        print(f"serangan terasa adalah : {str(attack_diterima)}")
        self.health -= attack_diterima
        print("darah "+self.name +" tersisa "+ str(self.health)+"\n")


Sett = Hero("Sett",150,15,8)
Yasuo = Hero("Yasuo",200,12,10)

Sett.serang(Yasuo)
Yasuo.serang(Sett)
