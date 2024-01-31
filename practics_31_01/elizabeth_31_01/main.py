class Cafe:
    def __init__(self, name: str, menu: str) -> None:
        self.__name = name
        self.__menu = menu


    def get_name(self) -> str:
        return self.__name


    def get_menu(self) -> str:
        return self.__menu


    def order_products(self, supplier: object, product_list: list) -> str:
        pass


    def display_menu(self) -> str:
        pass


class Supplier:
    def __init__(self, name: str, product_list: list) -> None:
        self.__name = name
        self.__product_list = product_list


    def get_name(self) -> str:
        return self.__name


    def get_product_list(self) -> list:
        return self.__product_list


    def add_product(self, product: str) -> None:
        for i in self.__product_list:
            if i != product:
                self.__product_list.append(product)


    def delete_product(self, product: str) -> None:
        for i in self.__product_list:
            if i == product:
                pass



    def display_products(self) -> str:
        pass