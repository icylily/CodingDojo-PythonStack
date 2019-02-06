import product
class Store:
    def __init__(self,name,procudt):
        self.store_name = name
        self.product = []

    def add_product(self, new_product):
        self.product.append(new_product)
        return self

    def sell_product(self, id):
        self.product[id].print_info(self.product[id])
        self.product.pop(id)
        return self

    def inflation(self, percent_increase):
        for x in self.product:
            x.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for x in self.product:
            if x.category == category:
                x.update_price(percent_discount,False)
        return self
