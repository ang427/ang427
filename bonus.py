import tkinter as tk

from tkinter import *

from tkinter import messagebox

dis=.10

str1=''

def reset():

    cat1item1var.set(0)
    cat1item2var.set(0)
    cat1item3var.set(0)

    

    cat2item1var.set(0)
    cat2item2var.set(0)
    cat2item3var.set(0)
    cat2item4var.set(0)

    

    cat3item1var.set(0)
    cat3item2var.set(0)

   

    cat4item1var.set(0)
    cat4item2var.set(0)
    cat4item3var.set(0)
    cat4item4var.set(0)
    cat4item5var.set(0)

   

    cat5item1var.set(0)
    cat5item2var.set(0)
    cat5item3var.set(0)
    cat5item4var.set(0)
    
    t1.delete('1.0',END)

def rbutton():
    global dis
    if var.get()==1:
        dis=.10
    elif var.get()==2:
        dis=.15

def calc():
    s=0
    t1.delete('1.0',END)
    
    if cat1item1var.get()==1:
        s=s+12.95
    if cat1item2var.get()==1:
        s=s+10.99
    if cat1item3var.get()==1:
        s=s+25.59

    if cat2item1var.get()==1:
        s=s+11.95
    if cat2item2var.get()==1:
        s=s+12.95
    if cat2item3var.get()==1:
        s=s+45.15
    if cat2item4var.get()==1:
        s=s+25.99

    if cat3item1var.get()==1:
        s=s+35.95
    if cat3item2var.get()==1:
        s=s+30.85
        
    if cat4item1var.get()==1:
        s=s+89.99
    if cat4item2var.get()==1:
        s=s+15.99
    if cat4item3var.get()==1:
        s=s+23.89
    if cat4item4var.get()==1:
        s=s+70.15
    if cat4item5var.get()==1:
        s=s+30.85

    if cat5item1var.get()==1:
        s=s+17.96
    if cat5item2var.get()==1:
        s=s+27.15
    if cat5item3var.get()==1:
        s=s+10.89
    if cat5item4var.get()==1:
        s=s+8.95

    discount=s*dis
    afterdiscount=s-discount
    tax=afterdiscount*7.25/100
    aftertax=afterdiscount+tax

    global str1

    str1='Total merchandise : $'+'{:.2f}'.format(s)+'\r\n'+'Discount : $' + '{:.2f}'.format(discount)+'\r\n'+'7.25% Tax : $'+'{:.2f}'.format(tax)+'\r\n'+ 'Total : $'+'{:.2f}'.format(aftertax)


def checkOut():

    calc()
    t1.delete('1.0',END)
    t1.insert(tk.END, str1)
root=tk.Tk()
root.geometry('500x570+400+20')
root.title('Retail Store Management')
var = IntVar()

l1=tk.Label(root,text="Retail Store Management",font=("Times New Roman", 20))
l1.place(x=50,y=7)


fc=tk.Radiobutton(root,value=1,variable=var,text="First Time Customer",font=("Times New Roman", 10),command=rbutton)
fc.place(x=20,y=30)
sc=tk.Radiobutton(root,value=2,variable=var,text="First Time +Local Customer",font=("Times New Roman", 10),command=rbutton)
sc.place(x=20,y=50)

cat1item1var=IntVar()
cat1item2var=IntVar()
cat1item3var=IntVar()

l1=tk.Label(root,text="Category-1")

l1.place(x=20,y=80)

cat1item1=tk.Checkbutton(root,variable=cat1item1var, text="Item 1",command=calc)
cat1item1.place(x=20,y=100)

cat1item2=tk.Checkbutton(root,variable=cat1item2var,text="Item 2",command=calc)
cat1item2.place(x=80,y=100)

cat1item3=tk.Checkbutton(root,variable=cat1item3var,text="Item 3",command=calc)
cat1item3.place(x=140,y=100)


cat2item1var=IntVar()
cat2item2var=IntVar()
cat2item3var=IntVar()
cat2item4var=IntVar()



l2=tk.Label(root,text="Category-2")
l2.place(x=20,y=140)

cat2item1=tk.Checkbutton(root,variable=cat2item1var,text="Item 1",command=calc)
cat2item1.place(x=20,y=160)
cat2item2=tk.Checkbutton(root,variable=cat2item2var,text="Item 2",command=calc)
cat2item2.place(x=80,y=160)
cat2item3=tk.Checkbutton(root,variable=cat2item3var,text="Item 3",command=calc)
cat2item3.place(x=140,y=160)
cat2item4=tk.Checkbutton(root,variable=cat2item4var,text="Item 4",command=calc)
cat2item4.place(x=200,y=160)


cat3item1var=IntVar()

cat3item2var=IntVar()


l3=tk.Label(root,text="Category-3")

l3.place(x=20,y=200)

cat3item1=tk.Checkbutton(root,variable=cat3item1var,text="Item 1",command=calc)
cat3item1.place(x=20,y=220)
cat3item2=tk.Checkbutton(root,variable=cat3item2var,text="Item 2",command=calc)
cat3item2.place(x=80,y=220)


cat4item1var=IntVar()
cat4item2var=IntVar()
cat4item3var=IntVar()
cat4item4var=IntVar()
cat4item5var=IntVar()


l4=tk.Label(root,text="Category-4")
l4.place(x=20,y=250)

cat4item1=tk.Checkbutton(root,variable=cat4item1var,text="Item 1",command=calc)
cat4item1.place(x=20,y=270)
cat4item2=tk.Checkbutton(root,variable=cat4item2var,text="Item 2",command=calc)
cat4item2.place(x=80,y=270)
cat4item2=tk.Checkbutton(root,variable=cat4item3var,text="Item 3",command=calc)
cat4item2.place(x=140,y=270)
cat4item2=tk.Checkbutton(root,variable=cat4item4var,text="Item 4",command=calc)
cat4item2.place(x=200,y=270)
cat4item2=tk.Checkbutton(root,variable=cat4item5var,text="Item 5",command=calc)
cat4item2.place(x=260,y=270)


cat5item1var=IntVar()
cat5item2var=IntVar()
cat5item3var=IntVar()
cat5item4var=IntVar()

l5=tk.Label(root,text="Category-5")
l5.place(x=20,y=300)

cat5item1=tk.Checkbutton(root,variable=cat5item1var,text="Item 1",command=calc)
cat5item1.place(x=20,y=320)
cat5item2=tk.Checkbutton(root,variable=cat5item2var,text="Item 2",command=calc)
cat5item2.place(x=80,y=320)
cat5item2=tk.Checkbutton(root,variable=cat5item3var,text="Item 3",command=calc)
cat5item2.place(x=140,y=320)
cat5item2=tk.Checkbutton(root,variable=cat5item4var,text="Item 4",command=calc)
cat5item2.place(x=200,y=320)


chkout = tk.Button(root,text="Check out",command=checkOut,font=("Arial",10))

chkout.place(x=20,y=350)

reset = tk.Button(root,text="Reset",command=reset,font=("Arial",10))

reset.place(x=220,y=350)

qquit = tk.Button(root,text="Quit",command=root.destroy,font=("Arial",10))

qquit.place(x=320,y=20)



l5=tk.Label(root,text="List Of Purchases")

l5.place(x=20,y=410)

t1=tk.Text(root,font=("Arial", 10),width=40,height=20)

t1.place(x=20,y=440)

root.mainloop()
