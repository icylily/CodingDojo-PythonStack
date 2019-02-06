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
