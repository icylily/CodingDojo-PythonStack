class Animal:
    def __init__(self,name,age=1):
        self.name = name
        self.age = age
        self.health_level = 5
        self.happiness_level = 5
    
    def display_info(self):
        print("This animal's name is: ",self.name," age is: ",self.age, "health lever is: ",self.health_level,"happiness level is:",self.happiness_level)
        return self
    def feed(self):
        if self.health_level<10:
            self.health_level += 1
            print(self.name," health level +1  now health level is :",self.health_level)
            
        if self.happiness_level <10:
            self.happiness_level+=1
            print(self.name,"happiness level +1 now happiness level is:",self.happiness_level)

        if(self.happiness_level == 10 and self.happiness_level ==10):
            print("both health lever and happiness level are reached the maxim , no more feed")
        return self
    
class Lion(Animal):
    def __init__(self, name,age=1):
        super().__init__(name,age)
        self.isLionking = False

    def display_info(self):
        print("The Lion's name is: ", self.name, " age is: ", self.age,"health lever is: ", self.health_level, "happiness level is:", self.happiness_level)
        return self

    def feed(self):
        print("I am a Lion, I like beef.")
        super().feed()

class Tiger(Animal):

    def __init__(self, name, age=1):
        super().__init__(name, age)
        self.canSwim = False

    def display_info(self):
        print("The Tiger's name is: ", self.name, " age is: ", self.age, "health lever is: ",self.health_level, "happiness level is:", self.happiness_level)
        return self

    def feed(self):
        print("I am a Tiger, I like beef.")
        super().feed()
        return self


class Bear(Animal):

    def __init__(self, name, age=1):
        super().__init__(name, age)
        self.isPolarBear = False

    def display_info(self):
        print("The Bear's name is: ", self.name, " age is: ", self.age, "health lever is: ",self.health_level, "happiness level is:", self.happiness_level)
        return self

    def feed(self):
        print("I am a Bear, I like fish.")
        super().feed()
        return sel

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def add_bear(self, name):
        self.animals.append(Bear(name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_bear("Snow")
zoo1.add_bear("April")
zoo1.print_all_info()
