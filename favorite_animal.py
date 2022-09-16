class Cat:
    def __init__ (self, play, color, sound, sleep, name):
        self.play = play
        self.sound = sound
        self.color = color
        self.sleep = sleep
        self.name = name
#define actions below
    def isSleep(self):
        if(self.sleep):
            print(self.name + " is sleep")
        else:
            print(self.name + " is bored")
        return self.sleep

    def eat(self):
        self.sleep = True
        print("full")
    

    def getName(self):
        return self.name

    def getSound(self):
        return self.sound 

def main():

    cat1 = Cat("Chinese Li-Hua", "Black",  "meowwwww", False, "Katty")
    cat2 = Cat("Maine Coon", "Brown", "meow", True, "Milk")

#Katty's action
    print(cat1.getName())
    print(cat1.getSound())
    cat1.isSleep()

    
#Milk's actions 
    print(cat2.getName())
    cat1.eat()
    cat2.isSleep()
    

if __name__ == "__main__":
    main()
