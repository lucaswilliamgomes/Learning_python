from time import sleep


def menu ():
    print(''' 
        KEEP THE TASKS IN DAY 

        1 - View all tasks
        2 - add task 
        3 - Delete task
        4 - undo delete 
        5 - Quit 
''')


def validate_option (op_chosen, final):
    if op_chosen.isnumeric():
        if int(op_chosen) >= 1 and int(op_chosen) <= final:
            return True 
    else:
        return False


def view_tasks ():
    print(f'    ALL TASKS\n')
    cont = 1
    with open ('tasks.txt', 'r+') as tasks:
        for line in tasks:
            print(f'    {cont} | {line}', end='')
            cont += 1
        print()


def add_task():
    print('ADD NEW TASK')
    with open ('tasks.txt','a+') as task:
        task.write(input ('     '))
        task.write(f'\n')


def delete_line(line):
    deleted = ''
    with open('tasks.txt','r') as tasks:
        texto = tasks.readlines()
    with open('tasks.txt','w') as tasks:
        for i in texto:
            if (texto.index(i) + 1) == line:
                deleted = i
                tasks.write('')
                return deleted
            else:
                tasks.write(i)
    


def delete_task ():
    print('    DELETE TASK')
    print()
    cont = 1
    with open ('tasks.txt', 'r+') as tasks:
        for line in tasks:
            print(f'    {cont} | {line}',end='')
            cont += 1
        print()
    selection = input('what task you want delete?: ')
    while True:
        if validate_option(selection, cont-1):
            break
        else:
            selection = input ('Type again your option : ')
    selection = int (selection)
    deleted = delete_line(selection)
    return deleted



        
def undo_delete ( deleted, delete = False):
    if delete:
        print('Restoring task...')
        sleep(1)
        with open ('tasks.txt', 'a+') as tasks:
            tasks.write(deleted)
        print('Restored with successfful')
        delete = False
    else: 
        print('You dont deleted a task')


tasks = list ()
task_deleted = ''
dlt = False
while True:
    menu()
    option = input ('Type your option : ')
    while True:
        if validate_option(option, 5):
            break
        else:
            option = input ('Type again your option : ')
    print()
    option = int(option)

    if option == 1:
        view_tasks()

    elif option == 2:
        add_task()

    elif option == 3:
        task_deleted = delete_task()
        dlt = True    
        
    elif option == 4:
        undo_delete(task_deleted, dlt) 
        dlt = False
        task_deleted = ''

    elif option == 5:
        print('    going out')
        sleep(1)
        break
    