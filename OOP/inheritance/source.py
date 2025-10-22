class Hero :
    def __init__(self,name):
        self.health_pool = [0,100,200,300,400,500]
        self.atkPower_pool = [0,10,20,30,40,50]
        self.armor_pool = [0,1,2,3,4,5]
        self.__name = name
        self.__exp = 0
        self.__level =0
    
    def show_info(self):
        print("{} level: {} \n\t health : {}\n\t atkPower : {} \n\t armor : {}".format(
            self.__name,
            self.__level,
            self.__health,
            self.__atkPower,
            self.__armor
            ))

    @property
    def health_pool(self):
        pass

    @property
    def atkPower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @health_pool.setter
    def health_pool(self,input):
        self.__health_pool = input
    
    @atkPower_pool.setter
    def atkPower_pool(self,input):
        self.__atkPower_pool = input
    
    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input

    @gainExp.setter
    def gainExp(self,input):
        self.__exp += input
        if (self.__exp >= 100):
            self.levelUp = self.__exp //100
            self.__exp %= 100

    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__atkPower = self.__atkPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

class Hero_Marksman(Hero):

    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,50,100,150,200,250]
        self.atkPower_pool = [0,20,40,80,160,200]
        self.armor_pool = [0,2,4,1.5,2,2.5]
        self.levelUp = 1

class Hero_Fighter(Hero):
    
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,700,100,150,200,250]
        self.atkPower_pool = [0,25,50,100,120,150]
        self.armor_pool = [0,2,3,4,5,6]
        self.levelUp = 1
