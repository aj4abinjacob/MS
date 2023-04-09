from phone import Phone

phone1 = Phone("X11", 18999, 5, "Vivo")

print(phone1.name)
phone1.name = "X12"
print(phone1.name)

print(phone1.calculateTotalPrice())
print(phone1.all)


class MyClass:
    def __init__(self):
        self.__my_private_attribute = 42

    def my_public_method(self):
        print("This is a public method.")
        self.__my_private_method()

    def __my_private_method(self):
        print("This is a private method.")


my_object = MyClass()
my_object.my_public_method()
