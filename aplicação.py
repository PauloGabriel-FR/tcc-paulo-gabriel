from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from classifi import processingy,saveconfig
from tkinter import messagebox
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

window = Tk()
filenamelabel = StringVar () 
filename = StringVar () 
selected = StringVar ()
waite = StringVar ()
window.title("Classificação")
filenamelabel.set("File name")
window.geometry('1100x200')
def clicked():
    

    out =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files","*.mp4"),("all files","*.*")))
    filename.set(out)
    listaf = out.split('/')
    filenamelabel.set(out.split('/')[len(listaf)-1])
    

btn = Button(window,text='File MP4', command=clicked)
 
btn.grid(column=0,row=1)

l1 = Label(window, textvariable=filenamelabel, font=("Helvetica", 12), background="white") 
l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

COR = Entry(window)
l3 = Label(window, text= "Coloração", font=("Helvetica", 12)) 
l3.grid(row = 0, column = 1, sticky = W, pady = 2)   

 
 #set the selected item
 
COR.grid(row=1, column=1, padx = 4,pady = 4)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

defeito = Entry(window)
l5 = Label(window, text= "Defeito Grave", font=("Helvetica", 12)) 
l5.grid(row = 0, column = 2, sticky = W, pady = 2)   

 
defeito.grid(row=1, column=2, padx = 4,pady = 4)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

defeitol = Entry(window)
l6 = Label(window, text= "Defeito Leve", font=("Helvetica", 12)) 
l6.grid(row = 0, column = 3, sticky = W, pady = 2)   

 
defeitol.grid(row=1, column=3, padx = 4,pady = 4)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

manchas = Entry(window)
l7 = Label(window, text= "Manchas", font=("Helvetica", 12)) 
l7.grid(row = 0, column = 4, sticky = W, pady = 2)   

 
manchas.grid(row=1, column=4, padx = 4,pady = 4)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

style = Style(window) 
style.configure("TRadiobutton",  
                 font = ("Helvetica", 12, "bold")) 
rad1 = Radiobutton(window,text='Extra', value=1, variable=selected)
 
rad2 = Radiobutton(window,text='I', value=2, variable=selected)
 
rad3 = Radiobutton(window,text='II', value=3, variable=selected)

rad4 = Radiobutton(window,text='III', value=4, variable=selected)

rad5 = Radiobutton(window,text='Descarte', value=5, variable=selected)
l8 = Label(window, text= "Classe", font=("Helvetica", 12)) 
l8.grid(row = 0, column = 7, sticky = W, pady = 2)  
rad1.grid(column=5, row=1)
 
rad2.grid(column=6, row=1)
 
rad3.grid(column=7, row=1)

rad4.grid(column=8, row=1)

rad5.grid(column=9, row=1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def onclick():
    try:
        Y = processingy(selected.get())
    except Exception as e:
        messagebox.showerror("Error", "Selecione uma opção de Qualidade!!")
    try:    
        cor = float(COR.get())
        defeitog = float(defeito.get())
        defeitoleve = float(defeitol.get())
        manchas1 = float(manchas.get())
    except Exception as e:
        messagebox.showerror("Error", "Selecione apenas caracteristicas validas!!!")  
    saveconfig(filename.get(),cor,defeitog,defeitoleve,manchas1,Y)    
    messagebox.showinfo("Sucesso", "Dados Salvos")
  
         
    
        
             
btn1 = Button(window,text='OK', command=onclick)
 
btn1.grid(column=3,row=4, pady = 40)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
window.mainloop()