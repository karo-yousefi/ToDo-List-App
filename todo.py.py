#Importing Stuff
from tkinter import *
from tkinter import ttk, filedialog
import time #For naming the save file 

#Craeting a window
win = Tk()
win.geometry('450x450')
win.title('ToDo App')
win.config(bg = '#616163')

#Constans
var_tasks = []
var_savepath = StringVar()

#Functions:

def fun_addtask():  #Add a new task 
    temp_newtask = in_task.get()

    if temp_newtask != '':
        lst_tasks.insert('end', temp_newtask)
        in_task.delete('0', 'end')



def fun_removetask():  #Removing selected task
    temp_select = lst_tasks.curselection()
    lst_tasks.delete(temp_select, temp_select)


def fun_done(): #Done a task
    n = lst_tasks.curselection()
    lst_tasks.itemconfig(n, foreground = 'red', background = 'black')
    lst_tasks.select_clear('0', 'end')


def fun_undone():  #Not done a task
    n = lst_tasks.curselection()
    lst_tasks.itemconfig(n, foreground = 'black', background = 'white')
    lst_tasks.select_clear('0', 'end')



def fun_azsort():  #Sort function (A-Z)
    var_tasks = lst_tasks.get('0', 'end')
    var_tasks = list(var_tasks)
    var_tasks.sort()
    lst_tasks.delete('0', 'end')

    for task in var_tasks:
        lst_tasks.insert('end', task)


def fun_zasort():  #Sort function (Z-A)
    var_tasks = lst_tasks.get('0', 'end')
    var_tasks = list(var_tasks)
    var_tasks.sort(reverse = True)
    lst_tasks.delete('0', 'end')
    
    for task in var_tasks:
        lst_tasks.insert('end', task)

    

def fun_clear():  #Claer all function
    lst_tasks.delete('0', 'end')


def fun_save():  #Save function
    save_name = time.strftime('%Y-%m-%d-%H%M%S')

    with open(var_savepath.get()+'/'+save_name+'.txt', 'w') as f:
        print(var_savepath.get()+'/'+save_name+'.txt')
        var_tasks = lst_tasks.get('0', 'end')
        var_tasks = list(var_tasks)

        for task in var_tasks:
            f.write(task+ '\n')



def fun_load():  #Load function

    lst_tasks.delete('0', 'end')

    path = filedialog.askopenfile()
    task = path.read().splitlines()
    for i in task:
        lst_tasks.insert('end', i)
        
        


def fun_save_loc():  #Change the save file locaion function
    path = filedialog.askdirectory()
    var_savepath.set(path)




#Lables:

lb_todoapp = Label(text = 'ToDo App', fg = '#ddd5d0', bg = '#204151', font = ('', 20, 'underline')) 
lb_todoapp.place(x = 170, y = 0)

lb_newtask = Label(text = 'New Task:', fg = '#ddd5d0', bg = '#586f6b', font = ('', 10, 'bold'))
lb_newtask.place(x = 60, y = 65)



#Buttons:

bt_addtask = ttk.Button(text = 'Add Task', command = fun_addtask)
bt_addtask.place(x = 30, y = 100)


bt_removetask = ttk.Button(text = 'Remove Task', command = fun_removetask)
bt_removetask.place(x = 30, y = 130)


bt_azsort = ttk.Button(text = 'Sort (A-Z)', command = fun_azsort)
bt_azsort.place(x = 30, y = 160)


bt_zasort = ttk.Button(text = 'Sort (Z-A)', command = fun_zasort)
bt_zasort.place(x = 30, y = 190)


bt_done = ttk.Button(text = 'Done', command = fun_done)
bt_done.place(x = 30, y = 220)


bt_done = ttk.Button(text = 'Not Done', command = fun_done)
bt_done.place(x = 30, y = 250)


bt_clear = ttk.Button(text = 'Clear All', command = fun_clear)
bt_clear.place(x = 30, y = 280)


bt_save = ttk.Button(text = 'Save List', command = fun_save)
bt_save.place(x = 372, y = 395)


bt_load = ttk.Button(text = 'Load List', command = fun_load)
bt_load.place(x = 372, y = 425)


bt_save_loc = ttk.Button(text = 'Select Save Location', command = fun_save_loc)
bt_save_loc.place(x = 250, y = 425)



#Other widgets:

in_task = ttk.Entry(width = 40)
in_task.place(x = 140, y = 65)


lst_tasks = Listbox(width = 40, height = 18)
lst_tasks.place(x = 140, y = 100)



win.mainloop()