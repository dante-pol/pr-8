class Supplier:
    def __init__(self, name: str):
        self.__name = name
        self.__product_list = []

    def __str__(self):
        pass

    def add_product(self, product: str):
        self.product_list.append(product)

    def del_product(self, product: str):
        self.product_list.remove(product)

    def display_products(self) -> str:
        return f'{self.product_list}'

    def get_product(self):
        pass


class Cafe:
    def __init__(self, name: str):
        self.__name = name
        self.__menu = []

    def __str__(self):
        pass

    def order_products(self, supplier, product_list):
        pass

    def display_menu(self):
        return f'{self.__menu}'

    def get_menu(self):
        return self.__menu

    def set_menu(self, menu):
        self.__menu.append(menu)


c1 = Cafe('Шаурма 24')
c1.get_menu('лаваш')

s1 = Supplier('Хлебзавод')




