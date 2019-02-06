import sys
class Product:
    def __init__(self, name,price,category):
        self.product_name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True :
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change

    def print_info(self):
        print("This product is  ",self.product_name)
        print ("price is ",self.price)
        print("category is ",self.category)

harrypoter = Product('Harry poter',20,'book')
harrypoter.print_info( )
harrypoter.update_price(0.01,True)
harrypoter.print_info()