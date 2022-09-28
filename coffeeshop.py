class Coffeeshop:
 
    def __init__(self,c,hc,w,n):
        self.coffee = c
        self.hotcocoa = hc
        self.water = w
        self.name = n
        #this is a float

    
    def getName(self):
        return self.name
 
 
    def calculatePrice(self, order):
        if order == "1":
            return self.coffee
        if order == "2":
            return self.hotcocoa
        if order == "3":
            return self.water
        else:
            print("We don't have that here, sorry.")
 
 
def main():
    myOrder = [1,2,3]
    choice = input("Welcome to the Coffee Shop. Please pick an option to get started.\n1. Order\n2. About the Shop\n")

    if int(choice) == 1:
        customer = input("What is your name, Sir?\n")
        drink = Coffeeshop("4.00","3.50","1.00", customer)
        print("Hi, "+ drink.getName())
        myOrder = input("What would you like to order? Pick an option.\n1. Coffee\n2. Hot Cocoa\n3. Water\n")    
        drink.calculatePrice(myOrder)
        print("This costs $" + str(drink.calculatePrice(myOrder)))
 
    elif int(choice) == 2:
        print("This is the virtual coffee shop! Here you may order one of three drinks. Just select the order option and type in a number!")


 
if __name__ == "__main__":
    main()
