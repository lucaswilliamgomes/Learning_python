# <img src="http://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/python-icon.png" width="30" height="30" />  Learning python

 > This repository is for save python files and assist me in __Python__ <img src="http://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/python-icon.png" width="12" height="12" /> , __English__ <img src="https://image.flaticon.com/icons/svg/1377/1377975.svg" width="12" height="12" />  and __Markdown__ <img src="https://cdn0.iconfinder.com/data/icons/octicons/1024/markdown-512.png" width="12" height="12" /> studies

## functionalities built-in python 

### *args and **kwargs
> *args is used when it is not known how many unnamed arguments the function will receive.  
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
> **kwargs is used when it is not known how many named arguments the function will receive.  
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
> Lambda expressions are concise functions that don't have name

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







 
