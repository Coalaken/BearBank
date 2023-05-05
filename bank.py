from tabulate import tabulate
from colorama import Fore


class User:
    
    """Пользователь""" 

    MAX_AGE = 100
    MIN_AGE = 16

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def show_details(self):
        pass


class Bank(User):
    
    """Банк"""
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.balance = 0 
        
    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        
    def show_details(self):
        table = [['name', 'age', 'balance'],
                 [self.name, self.age, f'${self.balance}']]
        print(Fore.LIGHTGREEN_EX + tabulate(table, headers='firstrow', tablefmt='grid'))
        
    def show_balance(self):
        print('Balance: ' + Fore.LIGHTYELLOW_EX + f'${self.balance}')
        
    def withdrow(self, amount):
        if amount > self.balance:
            print("Incorrect value")
        self.balance -= amount

  
"""Табличка с возможными коммандами"""
commands_table = [["commands:", '-> About:'],
                    ['cm', '-> show commands'],
                    ['profile', '->show profile'],
                    ['deposid', '-> put it on the balance'],
                    ['balance', '-> check balance'],
                    ['withdraw', '-> withdraw money xD']]


def user_creation():
    name = input('name: ')
    if name.isdigit():
        raise ValueError("str?")

    age = input('age: ')
    if not age.isdigit():
        raise ValueError("int?")

    the_user = Bank(name.title(), age)
    print('User created!!! ', Fore.RED + 'ʕ♡˙ᴥ˙♡ʔ' + Fore.WHITE)
    the_user.show_details()
    return the_user
    

def show_commands():
    print(Fore.LIGHTGREEN_EX + tabulate(commands_table, headers='firstrow', tablefmt='grid'))


if __name__ == '__main__':

    print(Fore.RED + "| *** Service started *** |")
    print("")    
    print(Fore.WHITE + "Hi, let's create new user?!", Fore.RED + " ʕ◉ᴥ◉ʔ" + Fore.WHITE)
    print()
    
    '''Создание пользователя'''

    user = None
    while user is None:
        try:
            user = user_creation()
        except ValueError:
            print(Fore.RED + "Invalid value".upper() + Fore.WHITE)
            print()
            continue
        except Exception:
            print(Fore.RED + "Invalid value".upper() + Fore.WHITE)
            print()
            continue

    print()
    print()
    
    """Старт"""
    print("What we will do? ")
    print()
    print("Commands:")    
    print(tabulate(commands_table, headers='firstrow', tablefmt='grid')) 
    print()
    print()

    task = input(Fore.RED + "ʕ'ᴥ'ʔっ:$ " + Fore.WHITE)
    while task != 'exit':
        
        """Показать комманды"""
        if task == 'cm':
            show_commands()
            
        """Внести депозит"""
        if task == 'deposit':
            try:
                amount = int(input(Fore.RED + 'ʕ •ₒ•ʔ amount:' + Fore.WHITE))
                user.deposit(amount)
            except Exception as e:
                print(Fore.RED + "invalid value".upper() + Fore.WHITE)
                continue                
        
        """Показать баланс"""
        if task == 'balance':
            user.show_balance()
        
        """Снять деньги"""
        if task == 'withdraw':
            amount = int(input(Fore.RED + 'ʕ •ₒ•ʔ amount:' + Fore.WHITE))
            if user.balance < amount:
                print('Little balance')
            user.withdrow(amount)
            user.show_balance()

        if task == 'profile':
            user.show_details()
            
        task = input(Fore.RED + "ʕ'ᴥ'ʔっ:$ " + Fore.WHITE)
