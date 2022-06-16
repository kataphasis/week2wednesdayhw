from subprocess import BELOW_NORMAL_PRIORITY_CLASS


class shopping_cart:
    def __init__(self):
        self.shoppingcart = []
        self.totalprice = []
        
   
    def add(self):
        done = False
        
        while not done:
            print("""What would you like?
            Apple: $0.45: select a
            Banana: $0.50: select b
            Cabbage: $0.60: select c
            Dates: $2.50: select d
            Eggplant: $1.45: select e
            Go back to main menu: m""")
            item = input("Select a letter(choose multiple times for multiple of the same items): ")
            if item == "a":
                self.shoppingcart.append('Apple')
                self.totalprice.append(0.45)
            elif item == "b":
                self.shoppingcart.append("Banana")
                self.totalprice.append(0.50)
            elif item == "c":
                self.shoppingcart.append("Cabbage")
                self.totalprice.append(0.60)
            elif item == "d":
                self.shoppingcart.append("Dates")
                self.totalprice.append(2.5)
            elif item == "e":
                self.shoppingcart.append("Eggplant")
                self.totalprice.append(1.45)
            elif item == "m":
                done = True
                self.mainmenu()
    def delete(self):
        print("Apple(s):", + self.shoppingcart.count("Apple"))
        print("Banana(s):", + self.shoppingcart.count("Banana"))
        print("Cabbage(s):", + self.shoppingcart.count("Cabbage"))
        print("Dates:", + self.shoppingcart.count("Dates"))
        print("Eggplant(s):", + self.shoppingcart.count("Eggplant"))
        delete_item = input("Which item would you like to delete? Please type out the item, no plural, type anything else to go back:")
        if delete_item is "Apple" or "Banana" or "Cabbage" or "Dates" or "Eggplant":
            print(self.shoppingcart)
            self.shoppingcart.remove(delete_item)
        else:
            self.mainmenu()

    def view(self):
        bananacount = str(self.shoppingcart.count("Banana"))
        datestotal = str(float(self.shoppingcart.count("Dates")) * 2.5)
        datescount = str(self.shoppingcart.count("Dates"))
        applecount = str(self.shoppingcart.count("Apple"))
        appletotal = str(float(self.shoppingcart.count("Apple")) * 0.45)
        bananatotal = str(float(self.shoppingcart.count("Banana")) * 0.5)
        cabbagecount = str(self.shoppingcart.count("Cabbage"))
        cabbagetotal = str(float(self.shoppingcart.count("Cabbage")) * 0.6)
        eggplantcount = str(self.shoppingcart.count("Eggplant"))
        eggplanttotal = str(float(self.shoppingcart.count("Eggplant")) * 1.45)
        totalprice = str(sum(self.totalprice))
        print("Apple(s): ",  applecount, appletotal)
        print("Banana(s): ", bananacount, bananatotal)
        
        print("Cabbage(s): ", cabbagecount, cabbagetotal)
        print("Dates: ", datescount, datestotal)
        print("Eggplant(s): ", eggplantcount, eggplanttotal)
        print("Total price: " , totalprice)
    def quit(self):
        print("Thank you for shopping today! Your final shopping list is below. You will now exit the program.")
        print(self.shoppingcart())
    def mainmenu(self):
        done=False
        print("""Welcome to Patrick's shopping cart!
        Please select an option below
        Shop: s
        Edit Cart: t
        View Cart: u
        Quit: q""")
        while not done:
            decision = input("Please select an option: ").lower()
            if decision == "s":
                self.add()
            elif decision == "t":
                self.delete()
            elif decision == "u":
                self.view()
            elif decision == "q":
                self.quit()
                done=True
_cart_ = shopping_cart()
_cart_.mainmenu()
