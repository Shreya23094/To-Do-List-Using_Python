import tkinter
from tkinter import *

root=Tk()
root.title("𝑻𝑶-𝑫𝑶-𝑳𝑰𝑺𝑻")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list=[]

#User defined function to input a task from the user
def addTask():
    task=task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open('list.txt',"a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)

#User defined function to delete a task selected by the user
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('list.txt','w') as taskfile:
            for tasks in task_list:
                taskfile.write(tasks+"\n")
                    
            
    listbox.delete(ANCHOR)

def openTaskfile():
    try:
        global task_list
        with open('list.txt',"r") as taskfile:
            tasks=taskfile.readlines()
            for task in tasks:
                if task!='\n':
                    task_list.append(task)
                    listbox.insert(END ,task)
    except:
        file=open('list.txt',"w") 
        file.close()
#icon
image_icon=PhotoImage(file="task.png")
root.iconphoto(False,image_icon)

#background
root.configure(background='#394867')

#main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=105)

task=StringVar()
task_entry=Entry(frame,font=("Times", "24", "bold italic"),width=18,bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font=("Times", "24", "bold"),width=6,bg="#9BA4B5",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1=Frame(root,bd=3,width=650,height=300,bg="#394867")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=("Times", "24", "bold italic"),width=22,height=11,bg="#394867",fg="white",cursor="hand2",selectbackground="#394867")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskfile()

#delete
delete_icon=PhotoImage(file="delete.png")
Button(root,image=delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM)

root.mainloop()