class GroceryStore():
        
        def __init__(self):
                self.Apple = 1
                self.Pizza = 3
                self.Tea = 0.5
                self.Oragne = 1
                self.Boba = 3
                self.Soup = 2
                self.Water = 0.5
                self.Chocolatemilk = 1.5
                self.Cafe = 3
                self.Milk = 5.00
        
                self.items = {"Apple":1, "Orange":1, 
                              "Tea":0.5, "Boba":4,
                              "Pizza":3, "Pasta":3,
                              "Soup":2, "Water":0.5,
                              "Chocolate milk":1.5,
                              "Cafe":3.0, "Milk":1,}

        

                self.totalPrice = 0
                self.intro = "Hi, Welcome to AWS store. What can i help you today?"
                self.order = []
        
                     


        def getinfo(self):
            return self.intro

        def getPrice(self,x):
                self.Price = x

        def setProduct(self):
                return self.order






def main():

    print("Hi, Welcome to AWS store")


    grocery = {"Pork" : 3,
             "Beef" : 5,
             "Sanwiches" : 3.75,
             "Hamberger" : 4.50,
             "Icecreame" : 0.75,
             "Bread" : 1,
             "Cereal" : 2,
             "Egg" : 1,
             "Noodles" : 2,
             "Fish" : 4  }



    print(list(grocery.keys()))
    request = input("What food would you like to buy?\n")
    price = grocery.get(request)
    many = int(input("How many would you want?\n"))
    print("Here you go!\nYou got " + str(many) + " " + request)
    print("That would be $" + str(round(price*many, 2)) + " dollars")




    toBuy = []
    while True:
        res = input("What would you like to buy? Enter 'stop' if done\n")
        if res == "stop":
            break
        else:
                other = input("What else you need?\n")
                otherPrice= (list(grocery.keys()))
                number = int(input("How many would you want?\n"))
                otherPrice = grocery.get(other)
                print("Here you go!\nYou got " + str(number) + " " + other)
                print("That would be $" + str(round(otherPrice*number, 2)) + " dollars")
    
    





    


if __name__ == "__main__":
    main()
