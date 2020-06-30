# _*_encoding: utf-8_*_

import tkinter
from tkinter import ttk
import random
from icon import img
import base64, os

from matplotlib import pyplot as plt 
import matplotlib

import numpy as np



top = tkinter.Tk()
style = ttk.Style()
style.map("C.TButton",
	foreground=[('pressed', 'red'), ('active', 'blue')],
	background=[('pressed', '!disabled', 'white'), ('active', 'white')]
	)
top.title("榮耀卷模擬器v1.2          作者:八雲")
top.resizable(0,0)
top.configure(background='PaleTurquoise1')
style = ttk.Style()
style.configure("BW.TLabel", padding=2,width=10, relief="flat", foreground="black", background="PaleTurquoise1")
style.configure("BW.TLabe2", padding=0,width=10, relief="flat", foreground="black", background="PaleTurquoise1")

tmp = open("tmp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
top.iconbitmap('tmp.ico')
os.remove("tmp.ico")



l1 = ttk.Label(text="力量: ", style="BW.TLabel")
l1.grid(row=0, column=0)
id_str = tkinter.Entry(bg='white')
id_str.grid(row=0, column=1)
id_str.insert(1,"0")
l2 = ttk.Label(text="敏捷: ", style="BW.TLabel")
l2.grid(row=1, column=0)
id_dex = tkinter.Entry(bg='white')
id_dex.grid(row=1, column=1)
id_dex.insert(1,"0")
l3 = ttk.Label(text="智力: ", style="BW.TLabel")
l3.grid(row=2, column=0)
id_int = tkinter.Entry(bg='white')
id_int.grid(row=2, column=1)
id_int.insert(1,"0")
l4 = ttk.Label(text="幸運: ", style="BW.TLabel")
l4.grid(row=3, column=0)
id_luk = tkinter.Entry(bg='white')
id_luk.grid(row=3, column=1)
id_luk.insert(1,"0")
l5 = ttk.Label(text="攻擊: ", style="BW.TLabel")
l5.grid(row=4, column=0)
id_atk = tkinter.Entry(bg='white')
id_atk.grid(row=4, column=1)
id_atk.insert(1,"0")
l6 = ttk.Label(text="衝卷次數: ", style="BW.TLabel")
l6.grid(row=5, column=0)
id_h = tkinter.Entry(bg='white')
id_h.grid(row=5, column=1)
id_h.insert(1,"8")

l7 = ttk.Label(text="榮耀卷價格: ", style="BW.TLabel")
l7.grid(row=0, column=2)
id_reel1 = tkinter.Entry(bg='white')
id_reel1.grid(row=0, column=3)
id_reel1.insert(1,"0")
l8 = ttk.Label(text="恢復卡價格: ", style="BW.TLabel")
l8.grid(row=1, column=2)
id_reel2 = tkinter.Entry(bg='white')
id_reel2.grid(row=1, column=3)
id_reel2.insert(1,"199")


def get_v():
	#if var1.get() == 1:
	plt.show()
	#v1 = var1.get()
	#print(v1)

def check():
	h = id_h.get()		#衝卷次數
	set_str = id_str.get() 	#屬性需求大於
	set_dex = id_dex.get()	#屬性需求大於
	set_int = id_int.get()	#屬性需求大於
	set_luk = id_luk.get() 	#屬性需求大於
	set_atk = id_atk.get() 	#屬性需求大於
	set_reel1 = id_reel1.get() #卷軸1費用
	set_reel2 = id_reel2.get() #卷軸2費用
	print(h,set_str,set_dex,set_int,set_luk,set_atk,set_reel1,set_reel2)

z= 1
zl1=[]
zl2=[]
def mk():
	global z
	plt.cla()
	n= 0
	t= 0
	l= 0
	str= []
	dex= []
	int1= []
	luk= []
	atk= []
	s_str= []
	s_dex= []
	s_int= []
	s_luk= []
	s_atk= []
	if int(id_str.get()) < 14:
		h = 13
	else:
		h = int(id_h.get())-1		#衝卷次數
	if int(id_str.get()) >20:
		set_str = 19
	else:
		set_str = int(id_str.get())-1	#屬性需求大於
	if int(id_dex.get()) >20:
		set_dex = 19
	else:
		set_dex = int(id_dex.get())-1	#屬性需求大於
	if int(id_int.get()) >20:
		set_int = 19
	else:
		set_int = int(id_int.get())-1	#屬性需求大於
	if int(id_luk.get()) >20:
		set_luk = 19
	else:
		set_luk = int(id_luk.get())-1	#屬性需求大於
	if int(id_atk.get()) >20:
		set_atk = 19
	else:
		set_atk = int(id_atk.get())-1	#屬性需求大於
	set_reel1 = int(id_reel1.get()) #卷軸1費用
	set_reel2 = int(id_reel2.get()) #卷軸2費用
	while(t <= h):
		sr = random.randrange(10,21)
		str.append(sr)
		dx = random.randrange(10,21)
		dex.append(dx)
		it = random.randrange(10,21)
		int1.append(it)
		lk = random.randrange(10,21)
		luk.append(lk)
		ak = random.randrange(10,21)
		atk.append(ak)
		if ak>set_atk and sr>set_str and dx>set_dex and it>set_int and lk>set_luk:
			t+=1
		n+=1
	print(f"榮耀卷:{n}張,{n*set_reel1}元")
	print(f"恢復卡:{n-h-1}張,{(n-h-1)*set_reel2}元\n")
	zl1.append(n)
	for s in atk:
		if atk[l]>set_atk and str[l]>set_str and dex[l]>set_dex and int1[l]>set_int and luk[l]>set_luk:
			print(f'第{l+1}次',str[l],dex[l],int1[l],luk[l],atk[l])
			s_str.append(str[l])
			s_dex.append(dex[l])
			s_int.append(int1[l])
			s_luk.append(luk[l])
			s_atk.append(atk[l])
		l+=1
	print(f'\n力量:{sum(s_str)}\n敏捷:{sum(s_dex)}\n智力:{sum(s_int)}\n幸運:{sum(s_luk)}\n攻擊:{sum(s_atk)}')
	zl2.append(z)
	plt.plot(zl2,zl1,'-o')
	for bo1,bo2 in zip(zl2,zl1):
		plt.text(bo1,bo2,bo2, va= 'bottom',fontsize=9)
	z+=1
	if var1.get() == 1:
		plt.ylabel("次數",fontsize=15)
		plt.axhline(y=np.mean(zl1),color="Red")
		plt.text(1, np.mean(zl1), np.around(np.mean(zl1),1), fontsize=10, va='center', ha='center', backgroundcolor='w',alpha=0.5)
		plt.show()
	else:
		plt.close('all') 



ttk.Button(text="開始模擬", style="C.TButton", command=mk).grid(row=4, column=3)
#ttk.Button(text="曲線圖", style="C.TButton", command=get_v).grid(row=3, column=3)
var1 = tkinter.IntVar()
c1 = tkinter.Checkbutton(top, text='曲線圖', variable=var1, onvalue=1, offvalue=0,
					background="PaleTurquoise1",activebackground="PaleTurquoise1")
c1.grid(row=3, column=3)

top.mainloop()
