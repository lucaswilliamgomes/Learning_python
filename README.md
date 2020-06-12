# <img src="http://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/python-icon.png" width="30" height="30" />  Learning python

 > This repository is for save python exercices, help me remember some python features <img src="http://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/python-icon.png" width="12" height="12" />  and assist me in __English__ <img src="https://image.flaticon.com/icons/svg/1377/1377975.svg" width="12" height="12" />  and __Markdown__ <img src="https://cdn0.iconfinder.com/data/icons/octicons/1024/markdown-512.png" width="12" height="12" /> studies

## functionalities built-in python 

### *args and **kwargs
> __*args__ is used when it is not known how many unnamed arguments the function will receive.  
When is used args inside the function is created a tuple with the arguments used.
````python 
def add (*args):
    sum_ = 0
    print (args)
    for num in args:
        sum_ += num
    return sum_
total = add(10, 20, 2, 5)
print(total)

[Terminal]
> (10, 20, 2, 5)
> 37
````
> __**kwargs__ is used when it is not known how many named arguments the function will receive.  
When is used kwargs inside the function is created a dict with the keys and values used.
````python 
def menu (**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f'{k} = {v}')

menu(name = 'Lucas', age = 18)

[Terminal]
> {'name': 'Lucas', 'age': 18}
> name = Lucas
> age = 18
````

### Lambda expressions (Functions anonymous) 
> __Lambda expressions__ are concise functions that don't have name

````Python
add = lambda *args: sum(args)
print(add(10, 20, 2, 5))

[Terminal]
> 37
````

### List comprehensions
> Is a form concise of manipulated a list
````Python 
list_1 = [10, 20, 2, 5, 9]
pairs = [num for num in list_1 if num % 2 == 0]
print(pairs)

[Terminal]
> [10, 20, 2]
````
### Decorators 
> __Decorators__ are quick ways to add behaviors before and after the decorated function is executed

````python 
#This code calculate the time execution of the count function using a decorator 
from time import time

def calculator_time (func):
    def wrapper ():
        init_time = time()
        func()
        end_time = time()
        time_ = end_time - init_time
        print(f'The time execution the function {func.__name__} was {time_:.2f} seconds')  
    return wrapper

@calculator_time
def count ():
    for x in range (100000000):
        pass

count()

[Terminal]
> The time execution the function count was 5.38 seconds
````
## Object oriented programming

### Getter and Setter
> The __Getter__ is a way of transform the instance attribute in a variable inside class (class attribute) for modify it.
    
__Getter struct__
```` python 
    #Getter
    @property
    def nick_less_numbers (self):
        return self._nick
````
> The __Setter__ is for modify the class attribute created with the __Getter__  

__Setter struct__
````Python
@nick_less_numbers.setter
    def nick_less_numbers (self, valor):
        x = 0 
        while x < len(valor):
            if valor[x].isdigit():
                valor = valor.replace(valor[x], '')
                x -= 1
            x += 1
        self._nick = valor
````
__together__
````python 
 class Nickname:
    def __init__(self, nickname):
        self.nick = nickname
        self.nick_less_numbers = nickname
    
    @property
    def nick_less_numbers (self):
        return self._nick

    @nick_less_numbers.setter
    def nick_less_numbers (self, valor):
        x = 0 
        while x < len(valor):
            if valor[x].isdigit():
                valor = valor.replace(valor[x], '')
                x -= 1
            x += 1
        self._nick = valor

if __name__ == "__main__":
    gamer1 = Nickname('lucas133')
    print(gamer1.nick_less_numbers)

[Terminal]
> lucas
````

## In standard python libraries
### Groupy in intertools
> receives an __ordered list__, separated into groups and returns an iterable
````python 
from itertools import groupby 

studente_notes = [
    {'Name': 'Luiz', 'Note': 9},
    {'Name': 'maria', 'Note': 10},
    {'Name': 'Jose', 'Note': 8},
    {'Name': 'Gadiel', 'Note': 9},
    {'Name': 'Roque', 'Note': 8}]

key_to_sort = lambda item: item ['Note']
studente_notes.sort(key=key_to_sort, reverse=True)
studentes_grouped = groupby(studente_notes, key= key_to_sort)

for group, students in studentes_grouped:
    print(f'Note {group}')
    for student in students:
        print(student)

[Terminal]
> Note 10
> {'Name': 'maria', 'Note': 10}
> Note 9
> {'Name': 'Luiz', 'Note': 9}  
> {'Name': 'Gadiel', 'Note': 9}
> Note 8
> {'Name': 'Jose', 'Note': 8}
> {'Name': 'Roque', 'Note': 8}
````









 
