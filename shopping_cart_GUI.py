#Sudais Arowosaye
#spring 24-25
#an online shoppin platform


from tkinter import *
from tkinter import messagebox

class shopping_GUI:
    def __init__(self):
        self.window = Tk()  
        
        self.items = []  
        self.quantities = []  

        self.count_label = Label(self.window, text="Items in cart: 0", font=("Arial", 12, "bold"))
        self.count_label.grid(row=0, column=3, columnspan=2, pady=10)

        
        label1 = Label(self.window, text= "cereal  \n(milk not included)")
        label1.grid(row=1, column=1)

        self.button1 = Button(self.window, text= "add to cart", command=lambda: self.addItem(cereal))
        self.button1.grid(row=1, column=2, sticky=N)
        self.button1s = Button(self.window, text= "remove from cart", command=lambda: self.removeItem(cereal))
        self.button1s.grid(row=1, column=2, sticky=E)

        img1 = PhotoImage(file="cereal.png")
        pic1 = Label(self.window, image=img1)
        pic1.image = img1
        pic1.grid(row=1,column=0)

 
        
        label2 = Label(self.window, text= "oliveOil\n(doesn't taste like olives)")
        label2.grid(row=2, column=1)

        self.button2 = Button(self.window, text= "add to cart", command=lambda: self.addItem(oliveOil))
        self.button2.grid(row=2, column=2, sticky=N)
        self.button2s = Button(self.window, text= "remove from cart", command=lambda: self.removeItem(oliveOil))
        self.button2s.grid(row=2, column=2, sticky=E)

        img2 = PhotoImage(file="oliveOil.png")
        pic2 = Label(self.window, image=img2)
        pic2.image = img2
        pic2.grid(row=2,column=0)



        label3 = Label(self.window, text= "greenTea\n(made from the leaves of the Camellia)")
        label3.grid(row=3, column=1)

        self.button3 = Button(self.window, text= "add to cart", command=lambda: self.addItem(greenTea))
        self.button3.grid(row=3, column=2, sticky=N)
        self.button3s = Button(self.window, text= "remove from cart", command=lambda: self.removeItem(greenTea))
        self.button3s.grid(row=3, column=2, sticky=E)

        img3 = PhotoImage(file="greenTea.png")
        pic3 = Label(self.window, image=img3)
        pic3.image = img3
        pic3.grid(row=3,column=0)



        label4 = Label(self.window, text= "almondMilk\n(doesn't taste as good as milk)")
        label4.grid(row=1, column=4)

        self.button4 = Button(self.window, text= "add to cart", command=lambda: self.addItem(almondMilk))
        self.button4.grid(row=1, column=5, sticky=N)
        self.button4s = Button(self.window, text= "remove from cart", command=lambda: self.removeItem(almondMilk))
        self.button4s.grid(row=1, column=5, sticky=E)

        img4 = PhotoImage(file="almondMilk.png")
        pic4 = Label(self.window, image=img4)
        pic4.image = img4
        pic4.grid(row=1,column=3)



        label5 = Label(self.window, text= "mozarella\n(cheese)")
        label5.grid(row=2, column=4)

        self.button5 = Button(self.window, text= "add to cart", command=lambda: self.addItem(mozarella))
        self.button5.grid(row=2, column=5, sticky=N)
        self.button5s = Button(self.window, text= "remove from cart", command=lambda: self.removeItem(mozarella))
        self.button5s.grid(row=2, column=5, sticky=E)

        img5 = PhotoImage(file="mozarella.png")
        pic5 = Label(self.window, image=img5)
        pic5.image = img5
        pic5.grid(row=2,column=3)



        label6 = Label(self.window, text= "spaghetti\n(tomatoe sauce not included)")
        label6.grid(row=3, column=4)

        self.button6 = Button(self.window, text= "add to cart", command=lambda: self.addItem(spaghetti))
        self.button6.grid(row=3, column=5, sticky=N)
        self.button6s = Button(self.window, text= "remove from cart", command=lambda: self.removeItem(spaghetti))
        self.button6s.grid(row=3, column=5, sticky=E)

        img6 = PhotoImage(file="spaghetti.png")
        pic6 = Label(self.window, image=img6)
        pic6.image = img6
        pic6.grid(row=3,column=3)


        self.cart = Button(self.window, text= "open cart", command=self.show_cart)
        self.cart.grid(row = 5, column=3)

        self.clear = Button(self.window, text= "clear cart", command=self.reset)
        self.clear.grid(row = 5, column=4)

        self.chk_out = Button(self.window, text= "checkout", command=self.newWindow)
        self.chk_out.grid(row = 5, column=5)







    
        self.window.mainloop()

        

    def count_items(self):
        total_items = sum(self.quantities)
        self.count_label.config(text=f"Items in cart: {total_items}")


    def addItem(self, item, quantity=1):
        """Adds an item to the cart."""
        if quantity > 0:
            index = self.findItem(item)
            if index != -1:
                self.quantities[index] += quantity
            else:
                self.items.append(item)
                self.quantities.append(quantity)
            self.count_items()
        else:
            messagebox.showerror("Error", "Quantity must be positive!")

    def removeItem(self, item):
        """Removes an item from the cart."""
        index = self.findItem(item)
        if index != -1:
            self.quantities[index] -= 1
            if self.quantities[index] <= 0:
                del self.items[index]
                del self.quantities[index]
            self.count_items()
        else:
                messagebox.showerror("Error", "No more in cart!")    

    def findItem(self, item):
        """Finds an item in the cart."""
        try:
            return self.items.index(item)
        except ValueError:
            return -1

    def show_cart(self):
        """Displays the cart contents."""
        cart_items = "\n".join(f"{self.items[i].name}: {self.quantities[i]}" for i in range(len(self.items)))
        messagebox.showinfo("Cart", cart_items if cart_items else "Cart is empty!")    

    def reset(self):
        self.items = []
        self.quantities = []
        self.count_items()

    def view(self):
        totalCost = 0
        receipt = ""
        for i in range(0, len(self.items)):
            item = self.items[i]
            #print(item.name)
            quantity = self.quantities[i]
            # Add logic here to calculate cost considering any discounts
            cost = quantity *item.price
            totalCost += cost * 1.075 + 5
            receipt += f"{item.name:20s} - {quantity:4d} x ${item.price:5.2f} = ${cost:6.2f}\n"
            
        return receipt

    def getTotalCost(self):
        totalCost = 0
        for i in range(0, len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            cost = (quantity * item.price )
            totalCost += cost 
            if totalCost > 0 : totalCost +=5
        return f" the Total cost = {(totalCost *  1.075) :5.2f}"
        
    def newWindow(self):
        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(self.window)

        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        # A Label widget to show in toplevel
        l1 = Label(newWindow, text=f"{self.view()}")
        l1.pack()
        l2 = Label(newWindow, text=f"{self.getTotalCost()}")
        l2.pack()

        self.view()


class Item: 
    # Modified constructor to include category and discount
    def __init__(self, name, description, price, category='general'):
        self.name = name
        self.description = description
        self.price = price
        self.discount = 0
        self.category = category

    # Method to set discount
    def set_discount(self, discount):
        self.discount = discount

    # Method to calculate price after discount
    def get_discounted_price(self):
        return self.price * (1 - self.discount)




# use the function provided in the assignment pdf file

# List of items available for shopping
tomatoSoup = Item("Tomato Soup", "200mL can", 0.70, "Food")
spaghetti = Item("Spaghetti", "500g pack", 1.10, "Food")
blackOlives = Item("Black Olives Jar", "200g Jar", 2.10, "Food")
mozarella = Item("Mozarella", "100g", 1.50, "Dairy")
gratedCheese = Item("Grated Cheese", "100g", 2.20, "Dairy")
greenTea = Item("Green Tea", "100g pack", 3.50, "Beverage")
chocolateBar = Item("Chocolate Bar", "50g bar", 0.99, "Snack")
oliveOil = Item("Olive Oil", "500ml bottle", 5.49, "Food")
cereal = Item("Cereal", "500g box", 2.99, "Food")
almondMilk = Item("Almond Milk", "1L carton", 1.89, "Dairy")

shopping_GUI()