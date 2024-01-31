class Cafe:
    def __init__(self, name: str, menu: list):
        self.__name = name
        self.__menu = []
        
    def order_products(self):
        pass


class Supplier:
    def __init__(self, name: str, product_list: list):
        self.__name = name
        self.__product_list = []
        
        
    def get_product_list(self) -> list:
        return self.__product_list
    
    
    def add_products(self, name_product):
        for product in self.__product_list:
            if name_product == product:
                return
        self.__product_list.append(name_product)
    
    
    def del_products(self, name_product):
        for product in self.__product_list:
            if name_product != product:
                return
        self.__product_list.remove(name_product)
            
            
    def display_products(self) -> list:
        return f'{self.__product_list}'
    
    
