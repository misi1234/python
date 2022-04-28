import pyautogui
from tkinter import *
from python.setup import *

app = Tk()
app.geometry("800x450")
app.title("IP számoló")
app.config(bg=GREEN)


def szamolas():
    _ip = ip.get()
    _mask = mask.get()
    if _ip == "":
        pyautogui.alert("Üres mező! IP cím!")
    else:
        if _mask == "":
            pyautogui.alert("Üres mező! Maszk!")
        
        elif _mask != "" and _ip != "":
            try:
                _ip = _ip.split(".")
            except:
                pyautogui.alert("Hiba az IP címmel!")

            try:
                _mask = _mask.split(".")
            except:
                pyautogui.alert("Hiba a Maszkkal!")   

            for i in range(len(_mask)):
                _mask[i] = int(_mask[i])
                if _mask[i] > 255:
                    pyautogui.alert("Túl nagy érték! Max. 255") 
                    break
                else:
                    continue

            for i in range(len(_ip)):
                _ip[i] = int(_ip[i])
                if _ip[i] > 255:
                    pyautogui.alert('Túl nagy érték! Max. 255')
                    break
                else:
                    continue

            ip_bin = []
            mask_bin = []
            for i in range(len(_ip)):
                x = bin(_ip[i]).strip("0b")
                if len(x) < 8:
                    nullak = 8-len(x)
                    x = "0"*nullak + x
                elif x == "":
                    x = "0"*8

                ip_bin.append(x)
            for i in range(len(_mask)):
                x = bin(_mask[i]).strip("0b")
                if len(x) < 8:
                    nullak = 8-len(x)
                    x = x + "0"*nullak
                elif x == "":
                    x = "0"*8
                mask_bin.append(x)

            ip_list = ""
            mask_list = ""
            for i in range(len(ip_bin)):
                ip_list += ip_bin[i]
                mask_list += mask_bin[i]

            ip_list = list(ip_list)
            mask_list = list(mask_list)

            print(ip_list)
            print(mask_list)

            halozat_cim_bin = ""

            for i in range(32):
                print(ip_list[i],mask_list[i])
                if ip_list[i] == "1" and mask_list[i] == "1":
                    halozat_cim_bin += "1"
                else:
                    halozat_cim_bin += "0"   

            print("halozat cim "+halozat_cim_bin)
            uj = ""
            for i in range(32):
                if i % 8 == 0 and i >= 9:
                    if i == 32:
                        break
                    else:
                        uj += halozat_cim_bin[i]+'.'
                        print(i)
                else:
                    uj += halozat_cim_bin[i]
                    print('uj: ',i)
            print("uj: ",uj)
            print(len(uj)-4)

        print(_mask)
        print(_ip)


#title 
title = Label(app,font=("sans-serif",20),text="IP számoló",bg=BLUE,fg=WHITE)
title.pack(side=TOP,fill=X)


#ipcim
ip_title = Label(app,font=("Sans-serif",15),text="IP cím",bg=GREEN,fg=WHITE,highlightbackground=WHITE,highlightthickness=1,borderwidth=2)
ip_title.place(x=10,y=70)

ip = Entry(app,font=("sans-serif",15),bg=GREEN,fg=WHITE,highlightbackground=WHITE,highlightthickness=1,borderwidth=2)
ip.place(x=110,y=70)

#maszk
mask_title = Label(app,font=("sans-serif",15),text="Maszk",bg=GREEN,fg=WHITE,highlightbackground=WHITE,highlightthickness=1,borderwidth=2)
mask_title.place(x=10,y=120)

mask = Entry(app,font=("sans-serif",15),bg=GREEN,fg=WHITE,highlightbackground=WHITE,highlightthickness=1,borderwidth=2)
mask.place(x=110,y=120)



#szamolas gomb
btn = Button(app,font=("sans-serif",17),bg=WHITE,fg=DARKBLUE,text="SZÁMOL",command=szamolas,highlightbackground=WHITE,highlightthickness=1,activebackground=GREEN,activeforeground=WHITE,borderwidth=1)
btn.place(width=300,height=40,x=400,y=90)



#halozat cime
halozat_cim = Label(app,font=("sans-serif",15),bg=GREEN,fg=WHITE,text="Hálózat címe: ")
halozat_cim.place(x=50,y=200)

#halozat cime bin
halozat_cim_bin = Label(app,font=("sans-serif",15),bg=GREEN,fg=WHITE,text="Hálózat címe bináris: ")
halozat_cim_bin.place(x=50,y=240)

#elso cim
elso_cim = Label(app,font=("sans-serif",15),bg=GREEN,fg=WHITE,text="Első cím: ")
elso_cim.place(x=50,y=280)

#utolso cima
utolso_cim = Label(app,font=("sans-serif",15),bg=GREEN,fg=WHITE,text="Utolsó cím: ")
utolso_cim.place(x=50,y=320)

#szoras
szoras_cim = Label(app,font=("sans-serif",15),bg=GREEN,fg=WHITE,text="Szórási cím: ")
szoras_cim.place(x=50,y=360)




#run
if __name__ == "__main__":
    app.mainloop()
