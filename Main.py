#Amaliya Razyan Nurhayati (V3922005)
#Bimo Adji Kusnadi (V3922010)
#Catur Yudha Prasetya(V3922011)
#Fabianus Jan Krisna Wijaya(V3922017)
#Fauzi Ihsan Anshori(V3922021)
#KELOMPOK WELL

from cProfile import label
import string
from tkinter import *
import random
import time
from tkinter import messagebox
from tkinter import filedialog
from turtle import clear

root = Tk()

root.geometry("1275x720+0+0")
root.resizable(0,0)
root.title("Aplikasi Dekstop Kasir") 

topFrame=Frame(root,bd=10,relief=RIDGE,bg='grey')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='SUMBER SHOP',font=('Castellar',39,'bold'),fg='#FFFAF4',bg='#808080', bd=15,width=30) #judul aplikasi
labelTitle.grid(row=0,column=10) #terganti


root.config(bg='#000000') #warna cepitan terganti

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar() 
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()

# variabel menu atasan
menu1 = StringVar()
menu2 = StringVar()
menu3 = StringVar()
menu4 = StringVar()
menu5 = StringVar()
menu6 = StringVar()
menu7 = StringVar()
menu8 = StringVar()
menu9 = StringVar()

# variabel menu bawahan
menu10 = StringVar()
menu11 = StringVar()
menu12 = StringVar()
menu13 = StringVar()
menu14 = StringVar()
menu15 = StringVar()
menu16 = StringVar()
menu17 = StringVar()
menu18 = StringVar()

# variabel Harga dalam struk
hargaAtasanvar=StringVar()
hargaBawahanvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
taxvaluevar=StringVar()

menu1.set('0')
menu2.set('0')
menu3.set('0')
menu4.set('0')
menu5.set('0')
menu6.set('0')
menu7.set('0')
menu8.set('0')
menu9.set('0')

menu10.set('0')
menu11.set('0')
menu12.set('0')
menu13.set('0')
menu14.set('0')
menu15.set('0')
menu16.set('0')
menu17.set('0')
menu18.set('0')

tax=(5/100)
def totalcost():
    global hargaAtasan,hargaBawahan,subtotalItems,totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get():

        item1=int(menu1.get())
        item2=int(menu2.get())
        item3=int(menu3.get())
        item4=int(menu4.get())
        item5=int(menu5.get())
        item6=int(menu6.get())
        item7=int(menu7.get())
        item8=int(menu8.get())
        item9=int(menu9.get())

        item10=int(menu10.get())
        item11=int(menu11.get())
        item12=int(menu12.get())
        item13=int(menu13.get())
        item14=int(menu14.get())
        item15=int(menu15.get())
        item16=int(menu16.get())
        item17=int(menu17.get())
        item18=int(menu18.get())


        hargaAtasan=(item1*250000) + (item2*150000) + (item3*170000) + (item4*55000) + (item5*300000) + (item6*500000) + (item7*200000) \
        + (item8*100000) + (item9*170000)
        hargaBawahan=(item10*120000) + (item11*335000) + (item12*40000) + (item13*90000) + (item14*50000) + (item15*55000) \
        + (item16*400000) + (item17*69000) + (item18*130000)

        hargaAtasanvar.set(str(hargaAtasan))
        hargaBawahanvar.set(str(hargaBawahan))
        
        subtotalItems=hargaAtasan+hargaBawahan
        subtotalvar.set(str(subtotalItems))
        taxvaluevar.set(str(tax))
        totaltax= subtotalItems*tax
        
        
        servicetaxvar.set(totaltax)
        
        totalcost=subtotalItems+totaltax
        totalcostvar.set(str(totalcost))
        
    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')

def struk():
    global billnumber,date
    if hargaAtasanvar.get() != '' or hargaBawahanvar.get() != '':
        textStruk.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='SS-'+str(x)
        date=time.strftime('%d/%m/%Y')
        
        textStruk.insert(END,'\n\t\tSUMBER SHOP\n')
        textStruk.insert(END,'\tJl. Sumbersuko 69, Kab. Madiun\n')
        textStruk.insert(END,'\t\tTlp.0510111721\n\n')
        textStruk.insert(END,'======================================\n\n')
        textStruk.insert(END,'Resep Ref : ' +billnumber)
        textStruk.insert(END,'\nTanggal : '+date)
        textStruk.insert(END,'\n\n======================================\n\n')

        if menu1.get()!='0':
            textStruk.insert(END,f'Hoodie\t\t\tRp. {int(menu1.get())*250000}\n\n')

        if menu2.get()!='0':
            textStruk.insert(END,f'Sweater\t\t\tRp. {int(menu2.get())*150000}\n\n')

        if menu3.get()!='0':
            textStruk.insert(END,f'Kemeja\t\t\tRp. {int(menu3.get())*170000}\n\n')

        if menu4.get() != '0':
            textStruk.insert(END, f'Kaos:\t\t\tRp. {int(menu4.get()) * 55000}\n\n')

        if menu5.get() != '0':
            textStruk.insert(END, f'Batik:\t\t\tRp. {int(menu5.get()) * 300000}\n\n')

        if menu6.get() != '0':
            textStruk.insert(END, f'Rompi:\t\t\tRp. {int(menu6.get()) * 500000}\n\n')

        if menu7.get() != '0':
            textStruk.insert(END, f'Gaun:\t\t\tRp. {int(menu7.get()) * 200000}\n\n')

        if menu8.get() != '0':
            textStruk.insert(END, f'Denim:\t\t\tRp. {int(menu8.get()) * 100000}\n\n')

        if menu9.get() != '0':
            textStruk.insert(END, f'Jas:\t\t\tRp. {int(menu9.get()) * 170000}\n\n')

        if menu10.get() != '0':
            textStruk.insert(END, f'Jeans:\t\t\tRp. {int(menu10.get()) * 120000}\n\n')

        if menu11.get() != '0':
            textStruk.insert(END, f'Training:\t\t\tRp. {int(menu11.get()) * 335000}\n\n')

        if menu12.get() != '0':
            textStruk.insert(END, f'Chinos:\t\t\tRp. {int(menu12.get()) * 40000}\n\n')

        if menu13.get() != '0':
            textStruk.insert(END, f'Rok:\t\t\tRp. {int(menu13.get()) * 90000}\n\n')

        if menu14.get() != '0':
            textStruk.insert(END, f'Legging :\t\t\tRp. {int(menu14.get()) * 50000}\n\n')

        if menu15.get() != '0':
            textStruk.insert(END, f'Blouse:\t\t\tRp. {int(menu15.get()) * 55000}\n\n')

        if menu16.get() != '0':
            textStruk.insert(END, f'Jogger:\t\t\tRp. {int(menu16.get()) * 400000}\n\n')

        if menu17.get() != '0':
            textStruk.insert(END, f'Trousers:\t\t\tRp. {int(menu17.get()) * 69000}\n\n')

        if menu18.get() != '0':
            textStruk.insert(END, f'Culottes:\t\t\tRp. {int(menu18.get()) * 130000}\n\n')

        textStruk.insert(END,'======================================\n')
        if hargaAtasanvar.get()!='Rp 0':
            textStruk.insert(END,f'Harga dari Pakaian Atas\t\t\tRp. {hargaAtasan}\n\n')
        if hargaBawahanvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari Pakaian Bawah\t\tRp. {hargaBawahan}\n\n')

        textStruk.insert(END, f'Sub Total\t\t\tRp. {subtotalItems}\n\n')
        textStruk.insert(END, f'Pajak Pelayanan\t\t\tRp. {totaltax}\n\n')
        textStruk.insert(END, f'Harga total\t\t\tRP. {subtotalItems+totaltax}\n\n')
        textStruk.insert(END,'======================================\n\n')
        textStruk.insert(END,'Terima Kasih sudah berbelanja di tempa kami, semoga harimu senin terus\n')

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')

def save():
    if textStruk.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt') 
        if url==None:
            pass
        else:

            bill_data=textStruk.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Informasi','Struk Anda berhasil disimpan')

def reset():
    textStruk.delete(1.0,END)
    menu1.set('0')
    menu2.set('0')
    menu3.set('0')
    menu4.set('0')
    menu5.set('0')
    menu6.set('0')
    menu7.set('0')
    menu8.set('0')
    menu9.set('0')

    menu10.set('0')
    menu11.set('0')
    menu12.set('0')
    menu13.set('0')
    menu14.set('0')
    menu15.set('0')
    menu16.set('0')
    menu17.set('0')
    menu18.set('0')

    # batas untuk variables

    textHoodie.config(state=DISABLED)
    textSweater.config(state=DISABLED)
    textKemeja.config(state=DISABLED)
    textKaos.config(state=DISABLED)
    textBatik.config(state=DISABLED)
    textRompi.config(state=DISABLED)
    textGaun.config(state=DISABLED)
    textDenim.config(state=DISABLED)
    textJas.config(state=DISABLED)

    textJeans.config(state=DISABLED)
    textTraining.config(state=DISABLED)
    textChinos.config(state=DISABLED)
    textRok.config(state=DISABLED)
    textLegging.config(state=DISABLED)
    textBlouse.config(state=DISABLED)
    textJogger.config(state=DISABLED)
    textTrousers.config(state=DISABLED)
    textCulottes.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    hargaBawahanvar.set('')
    hargaAtasanvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    taxvaluevar.set('')

def Hoodie():
    if var1.get()==1:
        textHoodie.config(state=NORMAL)
        textHoodie.delete(0,END)
        textHoodie.focus()
    else:
        textHoodie.config(state=DISABLED)
        menu1.set('0')

def Sweater():
    if var2.get()==1:
        textSweater.config(state=NORMAL)
        textSweater.delete(0,END)
        textSweater.focus()
    else:
        textSweater.config(state=DISABLED)
        menu2.set('0')

def Kemeja():
    if var3.get()==1:
        textKemeja.config(state=NORMAL)
        textKemeja.delete(0,END)
        textKemeja.focus()
    else:
        textKemeja.config(state=DISABLED)
        menu3.set('0')

def Kaos():
    if var4.get()==1:
        textKaos.config(state=NORMAL)
        textKaos.delete(0,END)
        textKaos.focus()

    else:
        textKaos.config(state=DISABLED)
        menu4.set('0')

def Batik ():
    if var5.get()==1:
        textBatik.config(state=NORMAL)
        textBatik.delete(0,END)
        textBatik.focus()
    else:
        textBatik.config(state=DISABLED)
        menu5.set('0')

def Rompi():
    if var6.get()==1:
        textRompi.config(state=NORMAL)
        textRompi.delete(0,END)
        textRompi.focus()
    else:
        textRompi.config(state=DISABLED)
        menu6.set('0')

def Gaun():
    if var7.get()==1:
        textGaun.config(state=NORMAL)
        textGaun.delete(0,END)
        textGaun.focus()
    else:
        textGaun.config(state=DISABLED)
        menu7.set('0')

def Denim():
    if var8.get()==1:
        textDenim.config(state=NORMAL)
        textDenim.delete(0,END)
        textDenim.focus()
    else:
        textDenim.config(state=DISABLED)
        menu8.set('0')

def Jas():
    if var9.get()==1:
        textJas.config(state=NORMAL)
        textJas.delete(0,END)
        textJas.focus()
    else:
        textJas.config(state=DISABLED)
        menu9.set('0')

def Jeans():
    if var10.get()==1:
        textJeans.config(state=NORMAL)
        textJeans.delete(0,END)
        textJeans.focus()
    else:
        textJeans.config(state=DISABLED)
        menu10.set('0')

def Training():
    if var11.get()==1:
        textTraining.config(state=NORMAL)
        textTraining.focus()
        textTraining.delete(0, END)
    else:
        textTraining.config(state=DISABLED)
        menu11.set('0')

def Chinos():
    if var12.get()==1:
        textChinos.config(state=NORMAL)
        textChinos.delete(0,END)
        textChinos.focus()
    else:
        textChinos.config(state=DISABLED)
        menu12.set('0')

def Rok():
    if var13.get()==1:
        textRok.config(state=NORMAL)
        textRok.delete(0,END)
        textRok.focus()
    else:
        textRok.config(state=DISABLED)
        menu13.set('0')

def Legging():
    if var14.get()==1:
        textLegging.config(state=NORMAL)
        textLegging.delete(0,END)
        textLegging.focus()
    else:
        textLegging.config(state=DISABLED)
        menu14.set('0')

def Blouse():
    if var15.get()==1:
        textBlouse.config(state=NORMAL)
        textBlouse.delete(0,END)
        textBlouse.focus()
    else:
        textBlouse.config(state=DISABLED)
        menu15.set('0')

def Jogger():
    if var16.get()==1:
        textJogger.config(state=NORMAL)
        textJogger.delete(0,END)
        textJogger.focus()
    else:
        textJogger.config(state=DISABLED)
        menu16.set('0')

def Trousers():
    if var17.get()==1:
        textTrousers.config(state=NORMAL)
        textTrousers.delete(0,END)
        textTrousers.focus()
    else:
        textTrousers.config(state=DISABLED)
        menu17.set('0')

def Culottes(): 
    if var18.get()==1:
        textCulottes.config(state=NORMAL)
        textCulottes.delete(0,END)
        textCulottes.focus()
    else:
        textCulottes.config(state=DISABLED)
        menu18.set('0')

def tambahAngka(angka):
	angkaPer = layar.get()
	layar.delete(0, END)
	layar.insert(0, str(angkaPer) + str(angka))

def hapus():
	layar.delete(0, END)

def samaDengan():
	angka_kedua = layar.get()
	layar.delete(0, END)

	if math == "tambah":
		layar.insert(0, angkaFirst + int(angka_kedua))

	if math == "kurang":
		layar.insert(0, angkaFirst - int(angka_kedua))

	if math == "kali":
		layar.insert(0, angkaFirst * int(angka_kedua))

	if math == "bagi":
		layar.insert(0, angkaFirst / int(angka_kedua))


def tambah():
	angka_pertama = layar.get()
	layar.delete(0, END)
	global angkaFirst
	global math
	angkaFirst = int(angka_pertama)
	math = "tambah"


def kurang():
	angka_pertama = layar.get()
	layar.delete(0, END)
	global angkaFirst
	global math
	angkaFirst = int(angka_pertama)
	math = "kurang"

def kali():
	angka_pertama = layar.get()
	layar.delete(0, END)
	global angkaFirst
	global math
	angkaFirst = int(angka_pertama)
	math = "kali"

def bagi():
	angka_pertama = layar.get()
	layar.delete(0, END)
	global angkaFirst
	global math
	angkaFirst = int(angka_pertama)
	math = "bagi"

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='#DCDCDC')
menuFrame.pack(side=LEFT)

hargaFrame=Frame(menuFrame,bd=9,relief=RIDGE,bg='#808080',pady=12)#terganti
hargaFrame.pack(side=BOTTOM)

atasanFrame=LabelFrame(menuFrame,text=' Atasan ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
atasanFrame.pack(side=LEFT)

bawahanFrame=LabelFrame(menuFrame,text=' Bawahan ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
bawahanFrame.pack(side=RIGHT)

kalkulatorFrame=LabelFrame(menuFrame,text=' Kalkulator ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
kalkulatorFrame.pack(fill='x')#terubah

layar = Entry(kalkulatorFrame, font=('Calibri',14,'bold'), width=25, borderwidth=6)
layar.grid(column=0, row=0, columnspan=4, pady=10.50)

Hoodie=Checkbutton(atasanFrame,text=' Hoodie ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var1,
                        command=Hoodie, bg='#f6f6f6')
Hoodie.grid(row=0,column=0,sticky=W)

Sweater=Checkbutton(atasanFrame,text=' Sweater ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var2,
                        command=Sweater, bg='#f6f6f6')
Sweater.grid(row=1,column=0,sticky=W)

Kemeja=Checkbutton(atasanFrame,text=' Kemeja ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var3,
                        command=Kemeja, bg='#f6f6f6')
Kemeja.grid(row=2,column=0,sticky=W)

Kaos=Checkbutton(atasanFrame,text=' Kaos ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var4,
                        command=Kaos, bg='#f6f6f6')
Kaos.grid(row=3,column=0,sticky=W)

Batik=Checkbutton(atasanFrame,text=' Batik ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var5,
                        command=Batik, bg='#f6f6f6')
Batik.grid(row=4,column=0,sticky=W)

Rompi=Checkbutton(atasanFrame,text= ' Rompi ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var6,
                        command=Rompi, bg='#f6f6f6')
Rompi.grid(row=5,column=0,sticky=W)

Gaun=Checkbutton(atasanFrame,text=' Gaun ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var7,
                        command=Gaun, bg='#f6f6f6')
Gaun.grid(row=6,column=0,sticky=W)

Denim=Checkbutton(atasanFrame,text=' Denim ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var8,
                        command=Denim, bg='#f6f6f6')
Denim.grid(row=7,column=0,sticky=W)

Jas=Checkbutton(atasanFrame,text='Jas',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var9,
                        command=Jas, bg='#f6f6f6')
Jas.grid(row=8,column=0,sticky=W)


textHoodie=Entry(atasanFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=menu1)
textHoodie.grid(row=0,column=1)

textSweater=Entry(atasanFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=menu2)
textSweater.grid(row=1,column=1)

textKemeja=Entry(atasanFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=menu3)
textKemeja.grid(row=2,column=1)

textKaos=Entry(atasanFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=menu4)
textKaos.grid(row=3,column=1)

textBatik=Entry(atasanFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=menu5)
textBatik.grid(row=4,column=1)

textRompi=Entry(atasanFrame,font=('Calibri','16','bold'),bd=7, width=8,state=DISABLED,textvar=menu6)
textRompi.grid(row=5,column=1)

textGaun=Entry(atasanFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=menu7)
textGaun.grid(row=6,column=1)

textDenim=Entry(atasanFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=menu8)
textDenim.grid(row=7,column=1)

textJas=Entry(atasanFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=menu9)
textJas.grid(row=8,column=1)

Jeans=Checkbutton(bawahanFrame,text='Jeans',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var10,
                        command=Jeans, bg='#f6f6f6')
Jeans.grid(row=0,column=0,sticky=W)

Training=Checkbutton(bawahanFrame,text='Training',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var11,
                        command=Training, bg='#f6f6f6')
Training.grid(row=1,column=0,sticky=W)

Chinos=Checkbutton(bawahanFrame,text='Chinos',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var12,
                        command=Chinos, bg='#f6f6f6')
Chinos.grid(row=2,column=0,sticky=W)

Rok=Checkbutton(bawahanFrame,text='Rok',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var13,
                        command=Rok, bg='#f6f6f6')
Rok.grid(row=3,column=0,sticky=W)

Legging=Checkbutton(bawahanFrame,text='Legging',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var14,
                        command=Legging, bg='#f6f6f6')
Legging.grid(row=4,column=0,sticky=W)

Blouse=Checkbutton(bawahanFrame,text='Blouse',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var15,
                        command=Blouse, bg='#f6f6f6')
Blouse.grid(row=5,column=0,sticky=W)

Jogger=Checkbutton(bawahanFrame,text='Jogger',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var16,
                        command=Jogger, bg='#f6f6f6')
Jogger.grid(row=6,column=0,sticky=W)

Trousers=Checkbutton(bawahanFrame,text='Trousers',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var17,
                        command=Trousers, bg='#f6f6f6')
Trousers.grid(row=7,column=0,sticky=W)

Culottes=Checkbutton(bawahanFrame,text='Culottes',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var18,
                        command=Culottes, bg='#f6f6f6')
Culottes.grid(row=8,column=0,sticky=W)

textJeans=Entry(bawahanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=menu10)
textJeans.grid(row=0,column=1)

textTraining=Entry(bawahanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=menu11)
textTraining.grid(row=1,column=1)

textChinos=Entry(bawahanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=menu12)
textChinos.grid(row=2,column=1)

textRok=Entry(bawahanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=menu13)
textRok.grid(row=3,column=1)

textLegging=Entry(bawahanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=menu14)
textLegging.grid(row=4,column=1)

textBlouse=Entry(bawahanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=menu15)
textBlouse.grid(row=5,column=1)

textJogger=Entry(bawahanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=menu16)
textJogger.grid(row=6,column=1)

textTrousers=Entry(bawahanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=menu17)
textTrousers.grid(row=7,column=1)

textCulottes=Entry(bawahanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=menu18)
textCulottes.grid(row=8,column=1)

angka1 = Button(kalkulatorFrame, text=1, padx=40, pady=20, command=lambda: tambahAngka(1))
angka2 = Button(kalkulatorFrame, text=2, padx=40, pady=20, command=lambda: tambahAngka(2))
angka3 = Button(kalkulatorFrame, text=3, padx=40, pady=20, command=lambda: tambahAngka(3))
angka4 = Button(kalkulatorFrame, text=4, padx=40, pady=20, command=lambda: tambahAngka(4))
angka5 = Button(kalkulatorFrame, text=5, padx=40, pady=20, command=lambda: tambahAngka(5))
angka6 = Button(kalkulatorFrame, text=6, padx=40, pady=20, command=lambda: tambahAngka(6))
angka7 = Button(kalkulatorFrame, text=7, padx=40, pady=20, command=lambda: tambahAngka(7))
angka8 = Button(kalkulatorFrame, text=8, padx=40, pady=20, command=lambda: tambahAngka(8))
angka9 = Button(kalkulatorFrame, text=9, padx=40, pady=20, command=lambda: tambahAngka(9))
angka0 = Button(kalkulatorFrame, text=0, padx=40, pady=20, command=lambda: tambahAngka(0))

hapus = Button(kalkulatorFrame, text="hapus", padx=76, pady=20, bg='red', fg='white', command=hapus)
samaDengan = Button(kalkulatorFrame, text="=", padx=90, pady=50, command=samaDengan)

tambah = Button(kalkulatorFrame, text="+", padx=40, pady=20, command=tambah)
kurang = Button(kalkulatorFrame, text="-", padx=40, pady=20, command=kurang)
bagi = Button(kalkulatorFrame, text="/", padx=40, pady=20, command=bagi)

kali = Button(kalkulatorFrame, text="*", padx=40, pady=20, command=kali)

angka1.grid(column=0, row=1)
angka2.grid(column=1, row=1)
angka3.grid(column=2, row=1)
angka4.grid(column=3, row=1)

angka5.grid(column=0, row=2)
angka6.grid(column=1, row=2)
angka7.grid(column=2, row=2)
angka8.grid(column=3, row=2)

angka9.grid(column=0, row=3)
angka0.grid(column=1, row=3)
hapus.grid(column=2, row=3, columnspan=2)
samaDengan.grid(column=2, row=4, columnspan=2, rowspan=2)

tambah.grid(column=0, row=5)
kurang.grid(column=1, row=5)
kali.grid(column=0, row=4)
bagi.grid(column=1, row=4)



rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=LEFT)

strukFrame=Frame(rightFrame,bd=1,relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()

LabelhargaAtasan=Label(hargaFrame,text='    HARGA DARI ATASAN', font=('Constantia',12,'bold'),bg='#808080',fg='#000000')
LabelhargaAtasan.grid(row=0,column=0, rowspan=2)

texthargaAtasan=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargaAtasanvar)
texthargaAtasan.grid(row=0,column=1,padx=41, rowspan=2)

LabelhargaBawahan=Label(hargaFrame,text='   HARGA DARI BAWAHAN', font=('Constantia',12,'bold'),bg='#808080',fg='#000000')
LabelhargaBawahan.grid(row=1,column=0, rowspan=2)

texthargaBawahan=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargaBawahanvar)
texthargaBawahan.grid(row=1,column=1,padx=41, rowspan=2)

LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Constantia',12,'bold'),bg='#808080',fg='#000000')
LabelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

LabelTax=Label(hargaFrame,text='Pajak'+' '+str(tax*100)+'%', font=('Constantia',12,'bold'),bg='#808080',fg='#000000')
LabelTax.grid(row=1,column=2)

textTax=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=servicetaxvar)
textTax.grid(row=1,column=3,padx=41)

LabelHargaTotal=Label(hargaFrame,text='HARGA TOTAL', font=('Constantia',12,'bold'),bg='#808080',fg='#000000') #terganti
LabelHargaTotal.grid(row=2,column=2)

textHargaTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=totalcostvar)
textHargaTotal.grid(row=2,column=3,padx=41)

buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='#808080',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Struk',font=('arial',12,'bold'),fg='#fefefe',bg='#808080',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan= Button(buttonFrame,text='Simpan',font=('arial',12,'bold'),fg='#fefefe',bg='#808080',bd=3,padx=12,
                    command=save)
buttonSimpan.grid(row=0,column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=4)

textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=39,height=27)
textStruk.grid(row=0,column=0)

root.mainloop()