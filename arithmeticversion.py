from tkinter import *
from tkinter import messagebox
def evaluate(text): 
  text=text.replace("^","**")
  text=text.replace("x","*")
  result=eval(text)
  return result


def Toplam():
    sonuc=evaluate(sayi1.get()) 
    lbl_sonuc.config(text=str(sonuc))

def Cikar():
    sonuc=int(sayi1.get()) - int(sayi2.get())
    lbl_sonuc.config(text=str(sonuc))
    
def Topla():
    sonuc=int(sayi1.get()) + int(sayi2.get())
    lbl_sonuc.config(text=str(sonuc))
    
def Carp():
    sonuc=int(sayi1.get()) * int(sayi2.get())
    lbl_sonuc.config(text=str(sonuc))
    
def Bol():
    sonuc=int(sayi1.get()) / int(sayi2.get())
    lbl_sonuc.config(text=str(sonuc))
    
pencere=Tk()
pencere.title("Calculator")
pencere.geometry("250x100")
Label(pencere,text="Input :").grid(row=0, column=0)

Label(pencere,text="Result:").grid(row=2, column=0)
lbl_sonuc=Label(pencere,text="...")
lbl_sonuc.grid(row=2, column=1)
sayi1=Entry(pencere,width=5)
sayi1.grid(row=0, column=1)


Button(pencere, text="Close", command=pencere.destroy).grid(row=3, column=0)
Button(pencere, text="Calculate", command=Toplam).grid(row=3, column=1)


pencere.mainloop()
