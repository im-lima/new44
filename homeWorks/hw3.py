class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def moneyX(self):
        amount = float(input("Сколько денег вы хотите добавить на счет? "))
        self.__balance += amount

    def _kill(self):
        self.__balance = 0

    def __jackpot(self):
        self.__balance *= 10

    def merge_balance(self, other):
        if isinstance(other, Bank):
            self.__balance += other.__balance

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Клиент: {self.__name}, Баланс: {self.__balance}"

client1 = Bank("Alice", 100)
client2 = Bank("Bob", 150)

client1.moneyX()

client1.merge_balance(client2)

print(client1)
print(client2)

client1._kill()
print(client1)
