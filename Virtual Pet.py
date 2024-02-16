###imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time
import winsound
###Root setup()
root = tk.Tk()
root.title('Virtual Cat')
root.geometry('5000x5000')
###Photo
photo_Start = tk.PhotoImage(file='D:\Code in py\Cat.py.gif')
photo_Sleep =tk.PhotoImage(file='D:\Code in py\Cat.py.sleep.gif')
photo_Walkleft=tk.PhotoImage(file='D:\Code in py\Cat.py.walk.gif')
photo_wash=tk.PhotoImage(file='D:\Code in py\Cat.py .wash.gif')
photo_Walkright=tk.PhotoImage(file='D:\Code in py\Cat.py.walk.right.gif')
photo_play=tk.PhotoImage(file='D:\Code in py\Cat.py.play.gif' )
photo_feed=tk.PhotoImage(file='D:\Code in py\Cat.py.feed.gif')
photo_opps=tk.PhotoImage(file='D:\Code in py\Cat.py.opps.gif')
photo_pat_me=tk.PhotoImage(file='D:\Code in py\Pat_me.png')


def meow():
    winsound.PlaySound("D:\Code in py\Meow.wav", winsound.SND_ASYNC)
def patted():
   meow()
   Label_photo_n.config(image=photo_pat_me)
   
###Random Lists
Walk_side=[photo_Walkleft,photo_Walkright]
After_sleep=[photo_Start,photo_Walkleft,photo_Walkright,photo_Sleep,photo_play,photo_opps]

###Random movement
Walk_random = random.choice(Walk_side)
Sleepa_random=random.choice(After_sleep)
Label_photo_n= tk.Button(root, image=Sleepa_random, bg='black', command = patted,padx=50, pady=50)
Label_photo_n.place(x=610, y=100)
Opps_store='D:\Code in py\Cat.py.opps.gif'




###Variables and lists
hunger=5
dirty= False
age= 2
a_t='Cat'
bored= True
sleeping=True
happy=True
oh="CALLING VET"
Danger='death'
Warning_ = True
Breeds=['Pesian','Buremese']
mood=' '

###Top settings
LAH=tk.Label(root, text='Hunger = 5')
LAH.pack(pady=0, padx=0)


LA=tk.Label(root, text='Bored = True')
LA.pack(pady=0, padx=1)



###Statements
if sleeping == True:
    BS= tk.Button(root, bg='red', padx=10, state= 'disabled')
    BS.place(x=150 ,y=50)
    LS= tk.Label(root, text='Your pet is sleepy.')
    LS.place(x=200 ,y=50)
   
else:
    BS= tk.Button(root, bg='white', padx=10, state= 'disabled')
    BS.place(x=150 ,y=50)
    LS= tk.Label(root, text='Your pet is sleepy')
    LS.place(x=200 ,y=50)


if hunger == 5:
    BH= tk.Button(root, bg='red', padx=10, state= 'disabled')
    BH.place(x=150 ,y=150)
    LH= tk.Label(root, text='Your pet is hungry')
    LH.place(x=200 ,y=150)


if bored == True:
    BB= tk.Button(root, bg='red', padx=10, state= 'disabled')
    BB.place(x=150 ,y=250)
    LB= tk.Label(root, text='Your pet is bored')
    LB.place(x=200 ,y=250)
  


if dirty == True:
    BD= tk.Button(root, bg='red', padx=10, state= 'disabled')
    BD.place(x=150 ,y=350)
    LD= tk.Label(root, text='Your pet is bored')
    LD.place(x=200 ,y=350)

else:
    BD= tk.Button(root, bg='white', padx=10, state= 'disabled')
    BD.place(x=150 ,y=350)
    LD= tk.Label(root, text='Your pet is dirty')
    LD.place(x=200 ,y=350)
    

###Main core

def CB(e):
    L11.config(text=(C.get()))

def eat():
    hunger=4
    BH= tk.Button(root, bg='white', padx=10, state= 'disabled')
    BH.place(x=150 ,y=150)
    BD= tk.Button(root, bg='red', padx=10, state= 'disabled')
    BD.place(x=150 ,y=350)
    LAH.config(text='Hunger = 4(Lowest num)')
    Label_photo_n.config(image=photo_feed)
  
    
def play():
    BB= tk.Button(root, bg='white', padx=10, state= 'disabled')
    BB.place(x=150 ,y=250)
    bored= False
    BH= tk.Button(root, bg='red', padx=10, state= 'disabled')
    BH.place(x=150 ,y=150)
    BD= tk.Button(root, bg='red', padx=10, state= 'disabled')
    BD.place(x=150 ,y=350)
    LA.config(text='Bored = False')
    LAH.config(text='Hunger = 5')
    Label_photo_n.config(image=photo_play)

   
    
   
      
def walk():
    Walk_side=[photo_Walkleft,photo_Walkright]
    Walk_random = random.choice(Walk_side)
    Label_photo_n.config(image=Walk_random)
    
   
def wash():
     BS= tk.Button(root, bg='red', padx=10, state= 'disabled')
     BS.place(x=150 ,y=50)
     BD=tk.Button(root, bg='white', padx=10, state= 'disabled')
     BD.place(x=150 ,y=350)
     dirty=False
     BH= tk.Button(root, bg='white', padx=10, state= 'disabled')
     BH.place(x=150 ,y=150)
     BB= tk.Button(root, bg='white', padx=10, state= 'disabled')
     BB.place(x=150 ,y=250)
     LS= tk.Label(root, text='Your pet is sleepy.')
     LS.place(x=200 ,y=50)
     Label_photo_n.config(image=photo_wash)
    
     
def sleep():
    BS= tk.Button(root, bg='white', padx=10, state= 'disabled')
    BS.place(x=150 ,y=50)
    LS= tk.Label(root, text='Your pet is sleepy.')
    LS.place(x=200 ,y=50)
    Warning_ = False
    Label_photo_n.config(image=photo_Sleep)
 

def UNLOCK():
    user1='V_C_Sara'
    user2='Lily@gmail.com'
    Login6=Login.get()
    if Login.get()== user1 or Login.get()== user2 :
       L11.config(text='Tec_Cat')
       messagebox.showinfo(title='Logged in',message='Hi '+Login6)
    else:
        messagebox.showinfo(title='Error',message=Login6+' is not found in membership lists')

def randomize():
    for c in range(1):
         Sleepa_random=random.choice(After_sleep)
         Label_photo_n.config(image=Sleepa_random)
def clean_poo():
   Label_photo_n.config(image= photo_Start)


###Unlock custom cat

Unlock=tk.Label(root,text='Login:')
Unlock.place(x=1090, y=180)

Login= tk.Entry(root, bg='white',font='corier')
Login.place(x=1090, y=200)

B_Unlock=tk.Button(root, text='ENTER', command=UNLOCK)
B_Unlock.place(x=1090,y=230)
    
            
###Buttons
Button_F= tk.Button(root, text='Feed', command= eat, padx=50, bg='pink')
Button_F.place(x=150, y=500)

Button_P= tk.Button(root, text='Play', command= play, padx=50, bg='yellow')
Button_P.place(x=500, y=500)

Button_W= tk.Button(root, text='Wash', command= wash, padx=50, bg='white')
Button_W.place(x=850, y=500)

Button_S= tk.Button(root, text='Sleep', command= sleep, padx=50, bg='lightblue')
Button_S.place(x=1150, y=500)

Button_WK=tk.Button(root, text='Walk', command=walk, padx=50, bg='lightgreen')
Button_WK.place(x=150,y=600)

Button_Randomize=tk.Button(root, text='Randomize pet actions',command=randomize, padx=50, bg='purple')
Button_Randomize.place(x=450,y=600)

Clean_droppings=tk.Button(root, text='Clean droppings', command= clean_poo)
Clean_droppings.place(x=850, y=600)

#Other widgets(Textboxes, labels ,mini buttons + drop-down menu)  
L1= tk.Label(root, text='Name:')
L1.place(x=150, y=400)


C = ttk.Combobox(root, values=['NO NAME','Cutie','Max','Mill', 'Sassy'])
C.place(x=190,y=450)

C.bind('<<ComboboxSelected>>',CB)

L11=tk.Label(root ,text="Name:")
L11.pack(pady=1)




root.mainloop()
