
import sys
import threading
from datetime import datetime
import paho.mqtt.client as mqtt
from guizero import App, Text, TextBox, Picture, Box, Waffle, Combo, ListBox,PushButton, Window
import ast
import time
import os
import io
import subprocess



filebarcode1,filebarcode2,filebarcode3,filebarcode4,filebarcode5,filebarcode6,filebarcode7  =   "/home/pi/GUINHIP/barcode1.text","/home/pi/GUINHIP/barcode2.text","/home/pi/GUINHIP/barcode3.text","/home/pi/GUINHIP/barcode4.text","/home/pi/GUINHIP/barcode5.text","/home/pi/GUINHIP/barcode6.text","/home/pi/GUINHIP/barcode7.text"
filebarcode8,filebarcode9,filebarcode10,filebarcode11,filebarcode12,filebarcode13,filebarcode14  =   "/home/pi/GUINHIP/barcode8.text","/home/pi/GUINHIP/barcode9.text","/home/pi/GUINHIP/barcode10.text","/home/pi/GUINHIP/barcode11.text","/home/pi/GUINHIP/barcode12.text","/home/pi/GUINHIP/barcode13.text","/home/pi/GUINHIP/barcode14.text"
filebarcode15,filebarcode16  =   "/home/pi/GUINHIP/barcode15.text","/home/pi/GUINHIP/barcode16.text"
kh_sxngay,kh_sxthang,listsanpham = "/home/pi/thuong/GUINHIP/kh_sxngay.text","/home/pi/thuong/GUINHIP/kh_sxthang.text","/home/pi/thuong/GUINHIP/sanpham.text"

khngay_1,khngay_2,khngay_3,khngay_4,khngay_5,khngay_6 = "/home/pi/GUINHIP/kehoach_ngay/khngay_1.text","/home/pi/GUINHIP/kehoach_ngay/khngay_2.text","/home/pi/GUINHIP/kehoach_ngay/khngay_3.text","/home/pi/GUINHIP/kehoach_ngay/khngay_4.text","/home/pi/GUINHIP/khngay_5.text","/home/pi/GUINHIP/kehoach_ngay/khngay_6.text"
khngay_7,khngay_8,khngay_9,khngay_10,khngay_11 = "/home/pi/GUINHIP/kehoach_ngay/khngay_7.text","/home/pi/GUINHIP/kehoach_ngay/khngay_8.text","/home/pi/GUINHIP/kehoach_ngay/khngay_9.text","/home/pi/GUINHIP/kehoach_ngay/khngay_10.text","/home/pi/GUINHIP/kehoach_ngay/khngay_11.text"
khngay_12,khngay_13,khngay_14,khngay_15,khngay_16 = "/home/pi/GUINHIP/kehoach_ngay/khngay_12.text","/home/pi/GUINHIP/kehoach_ngay/khngay_13.text","/home/pi/GUINHIP/kehoach_ngay/khngay_14.text","/home/pi/GUINHIP/kehoach_ngay/khngay_15.text","/home/pi/GUINHIP/kehoach_ngay/khngay_16.text"
khngay_17,khngay_18,khngay_19,khngay_20,khngay_21,khngay_22 = "/home/pi/GUINHIP/kehoach_ngay/khngay_17.text","/home/pi/GUINHIP/kehoach_ngay/khngay_18.text","/home/pi/GUINHIP/kehoach_ngay/khngay_19.text","/home/pi/GUINHIP/kehoach_ngay/khngay_20.text","/home/pi/GUINHIP/kehoach_ngay/khngay_21.text","/home/pi/GUINHIP/kehoach_ngay/khngay_22.text"
khngay_23,khngay_24,khngay_25,khngay_26,khngay_27 = "/home/pi/GUINHIP/kehoach_ngay/khngay_23.text","/home/pi/GUINHIP/kehoach_ngay/khngay_24.text","/home/pi/GUINHIP/kehoach_ngay/khngay_25.text","/home/pi/GUINHIP/kehoach_ngay/khngay_26.text","/home/pi/GUINHIP/kehoach_ngay/khngay_27.text"
khngay_28,khngay_29,khngay_30,khngay_31 = "/home/pi/GUINHIP/kehoach_ngay/khngay_28.text","/home/pi/GUINHIP/kehoach_ngay/khngay_29.text","/home/pi/GUINHIP/kehoach_ngay/khngay_30.text","/home/pi/GUINHIP/kehoach_ngay/khngay_31.text"

tongkehoach = "/home/pi/GUINHIP/tongkhoach.text"
tongsanphamthang = "/home/pi/GUINHIP/tongspthang.text"
tongsanpham_ngay_1,tongsanpham_ngay_2,tongsanpham_ngay_3,tongsanpham_ngay_4,tongsanpham_ngay_5,tongsanpham_ngay_6 = "/home/pi/GUINHIP/tongsanpham_1.text","/home/pi/GUINHIP/tongsanpham_2.text","/home/pi/GUINHIP/tongsanpham_3.text","/home/pi/GUINHIP/tongsanpham_4.text","/home/pi/GUINHIP/tongsanpham_5.text","/home/pi/GUINHIP/tongsanpham_6.text"
tongsanpham_ngay_9,tongthuchien_thang_k250RR,tongthuchien_thang_k250FT = "/home/pi/GUINHIP/tongsanpham_9.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_k250RR.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_k250FT.text"
tongthuchien_thang_k200,tongthuchien_thang_oll500BRR,tongthuchien_thang_oll500BFT,tongthuchien_thang_oll500M3RR,tongthuchien_thang_oll500M3FT,tongthuchien_thang_oll700RR,tongthuchien_thang_oll700FT = "/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_k200.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_oll500BRR.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_oll500BFT.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_oll500M3RR.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_oll500M3FT.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_oll700RR.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_oll700FT.text"
tongthuchien_thang_smrm4la,tongthuchien_thang_smrm7la,tongthuchien_thang_oll700CFT,tongthuchien_thang_oll700CRR,tongthuchien_thang_k190,tongthuchien_thang_k165RR,tongthuchien_thang_k165FT = "/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_smrm4la.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_smrm7la.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_oll700CRR.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_oll700CFT.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_k190.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_k165RR.text","/home/pi/GUINHIP/tongthuchien_thang/tongthuchien_thang_k165FT.text"

khngay_18_update = "/home/pi/GUINHIP/kehoach_ngay/khngay_update/khngay_18.text"

hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'  }

hid2 = { 4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'  }

qrnhip = {'T05R0-': 'K250RR', 'T05F0-': 'K250FT','T04R0-':'K200', 'T03R0-':'K190', 'T28R0-':'OLLIN500M3RR', 'T28F0-':'OLLIN500M3FT', 'T26R0L':'OLLIN700RR', 'T26F0L':'OLLIN700FT', 'S36R0-':'SMRM4LA', 'S35R0 ':'SMRM7LA', 'T25ROL':'OLLIN500RR', 'T25FOL':'OLLIN500FT', '0K42B2':'K165RR', '0K42B3':'K165FT', 'T29F0-':'OLLIN700720FT', 'T29R0-':'OLLIN700720RR'}

sp = ['K250FT', 'K250RR',  'K200',  'OLLIN500FT',  'OLLIN500RR',  'OLLIN500M3FT',  'OLLIN500M3RR',  'OLLIN700FT',  'OLLIN700RR',  'SMRM4LA',  'SMRM7LA',  'OLLIN700720FT',  'OLLIN700720RR',  'K190',  'K165FT',  'K165RR']
kh = ['khngay_1','khngay_2','khngay_3','khngay_4','khngay_5','khngay_6','khngay_7','khngay_8','khngay_9','khngay_10','khngay_11','khngay_12','khngay_13','khngay_14','khngay_15','khngay_16','khngay_17','khngay_18','khngay_19','khngay_20','khngay_21','khngay_22','khngay_23','khngay_24','khngay_25','khngay_26','khngay_27','khngay_28','khngay_29','khngay_30','khngay_31']
ngay_dem = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
namss = ''
thangss= ''
ngayss = ''
gioss = ''
timer = ''

screen = 0

tmp= ""	
count1 = count2= count3= count4= count5= count6= count7= count8= count9= count10= count11= count12= count13= count14= count15= count16= count17= count18= count19= count20= count21= count22= count23= count24= count25= count26= count27= count28= count29= count30= count31 = 0
ngay1 = ngay2=ngay3 =ngay4 =ngay5 =ngay6 =ngay7 =ngay8 =ngay9 =ngay10 =ngay11 =ngay12 =ngay13 =ngay14 =ngay15 =ngay16 =ngay17 =ngay18 =ngay19 =ngay20 =ngay21 =ngay22 =ngay23 =ngay24 =ngay25 =ngay26 =ngay27 =ngay28 =ngay29 =ngay30 =ngay31 =0

tieude = App(title="HIỂN THỊ DỮ LIỆU VÀ KẾT QUẢ SẢN XUẤT",layout="grid",bg = "white")

tieude .tk.attributes("-fullscreen",True)

##############################################
logo = Box(tieude,layout="grid",grid=[0,0])
Logo = Picture(logo,image="logothaco.png",grid=[0,0],align="left",width = 350,height = 100) #170,320
space= Text(logo,grid=[1,0],text=" ",width = 20)
#time = Box(tieude,layout="grid",grid=[1,0])
realngay = Text(logo, grid=[2,0],align="right",size = 60)
space= Text(logo,grid=[3,0],text=" ",width = 20)
gio = Text(logo, size=60, grid=[4,0],font="Times New Roman", color="blue4",align="right")


###############################################
dong_1= Box(tieude,layout="grid",grid=[0,1])
#space= Text(dong_1,grid=[0,1],text=" ",height = 1)

dong_2= Box(tieude,layout="grid",grid=[0,2])
line=Picture(dong_2,image="toolbar2.png",grid=[2,2],height = 80)
	

###########################################

dong_3 = Box(tieude,layout="grid",grid=[0,3])

space= Text(dong_3,grid=[0,3],text=" ",width = 5)
san_pham = PushButton(dong_3, grid=[1,3],width = "fill",height ="fill")
space= Text(dong_3,grid=[2,3],text=" ",width = 1)
loaisp = PushButton(dong_3, grid=[4,3],width = "fill",height ="fill")
space= Text(dong_3,grid=[5,3],text=" ",width = 1)
don_vi = PushButton(dong_3, grid=[10,3],width = "fill",height ="fill")
space= Text(dong_3,grid=[7,3],text=" ",width = 1)
kehoach_ngay = PushButton(dong_3, grid=[8,3],width = "fill",height ="fill")
space= Text(dong_3,grid=[9,3],text=" ",width = 1)
thuc_hien = PushButton(dong_3, grid=[6,3],width = "fill",height ="fill")
space= Text(dong_3,grid=[11,3],text=" ",width = 1)
HINH_ANH = PushButton(dong_3, grid=[12,3],width = "fill",height ="fill")

# TEN SAN PHAM
space= Text(dong_3,grid=[1,4],height = 2)
sanpham_1 = Text(dong_3,grid=[1,5])
space= Text(dong_3,grid=[1,6],height = 5,text = '-----')
sanpham_2 = Text(dong_3,grid=[1,7])
space= Text(dong_3,grid=[1,8],height = 5,text = '-----')
sanpham_3 = Text(dong_3,grid=[1,9])
space= Text(dong_3,grid=[1,10],height = 5,text = '-----')
tong = Text(dong_3,grid=[1,11],text="TỔNG",size = 40,color = 'red')

# LOAI SAN PHAM
space= Text(dong_3,grid=[4,4],height = 2)
loaisanpham_1 = Text(dong_3,grid=[4,5])
space= Text(dong_3,grid=[4,6],height = 5,text = '-----')
loaisanpham_2 = Text(dong_3,grid=[4,7])
space= Text(dong_3,grid=[4,8],height = 5,text = '-----')
loaisanpham_3 = Text(dong_3,grid=[4,9])
space= Text(dong_3,grid=[4,10],height = 5,text = '-----')

# THUC HIEN
space= Text(dong_3,grid=[6,4],height = 2)
thuchien_1 = Text(dong_3,grid=[6,5])
space= Text(dong_3,grid=[6,6],height = 5,text = '-----')
thuchien_2 = Text(dong_3,grid=[6,7])
space= Text(dong_3,grid=[6,8],height = 5,text = '-----')
thuchien_3 = Text(dong_3,grid=[6,9])
space= Text(dong_3,grid=[6,10],height = 5,text = '-----')
tongthuchien = Text(dong_3,grid=[6,11])
space= Text(dong_3,grid=[6,12],height = 1,text = '-----')

# KE HOACH
space= Text(dong_3,grid=[8,4],height = 2)
kehoach_1 = Text(dong_3,grid=[8,5])
space= Text(dong_3,grid=[8,6],height = 5,text = '-----')
kehoach_2 = Text(dong_3,grid=[8,7])
space= Text(dong_3,grid=[8,8],height = 5,text = '-----')
kehoach_3 = Text(dong_3,grid=[8,9])
space= Text(dong_3,grid=[8,10],height = 5,text = '-----')
tongkehoach = Text(dong_3,grid=[8,11])
space= Text(dong_3,grid=[8,12],height = 1,text = '-----')

# DON VI
space= Text(dong_3,grid=[10,4],height = 2)
donvi_1 = Text(dong_3,grid=[10,5])
space= Text(dong_3,grid=[10,6],height = 5,text = '-----')
donvi_2 = Text(dong_3,grid=[10,7])
space= Text(dong_3,grid=[10,8],height = 5,text = '-----')
donvi_3 = Text(dong_3,grid=[10,9])
space= Text(dong_3,grid=[10,10],height = 5,text = '-----')


# HINH ANH
space= Text(dong_3,grid=[12,4],height = 2)
hinhanh_1 = Picture(dong_3,grid=[12,5],align="top",width=210,height=120) #170,320  ,width=150,height=100
space= Text(dong_3,grid=[12,6],height = 1,text = '-----')
hinhanh_2 = Picture(dong_3,grid=[12,7],align="top",width=210,height=120) #170,320  ,width=150,height=100
space= Text(dong_3,grid=[12,8],height = 1,text = '-----')
hinhanh_3 = Picture(dong_3,grid=[12,9],align="top",width=210,height=120) #170,320  ,width=150,height=100
space= Text(dong_3,grid=[12,10],height = 1,text = '-----')
hinhanh_connect = Picture(dong_3,grid=[12,11],align="top",width=50,height=50) #170,320  ,width=150,height=100

space= Text(dong_3,grid=[0,13],height = 2,text = '')
bar = Box(tieude,layout="grid",grid=[0,14])
#space= Text(bar,grid=[0,14],height = 3,text = '')
line=PushButton(bar,grid=[0,14],width = 237,height = 17)
barcode = TextBox(bar,grid=[0,15],width = 'fill',height = 'fill')
# dong 4-5

############################################

# SETUP THUỘC TÍNH CHO CÁC NÚT HIỂN THỊ TÊN ##########################

barcode.bg = 'white'
barcode.text_size = 10
#barcode.text_color = 'white'
barcode.focus()					# LAY BARCODE (LAY TU HIDRAW3 BI LOOP KHI KO QUET -> treo)
barcode.value = ''
	
line.bg = 'blue'
line.text_color = 'blue'

san_pham.bg = "blue4"
san_pham.text_color = "white"
san_pham.text_size = 32
san_pham.text = "SẢN PHẨM"	

loaisp.bg = "blue4"
loaisp.text_color = "white"
loaisp.text_size = 32
loaisp.text = "LOẠI SẢN PHẨM"	

don_vi.bg = "blue4"
don_vi.text_color = "white"
don_vi.text_size = 32
don_vi.text = "ĐƠN VỊ"	

thuc_hien.bg = "orange red"
thuc_hien.text_color = "Ghost White"
thuc_hien.text_size = 32
thuc_hien.text = "THỰC HIỆN"	

kehoach_ngay.bg = "orange red"
kehoach_ngay.text_color = "Ghost White"
kehoach_ngay.text_size = 32
kehoach_ngay.text = "KẾ HOẠCH"	

HINH_ANH.bg = "blue4"
HINH_ANH.text_color = "Ghost White"
HINH_ANH.text_size = 32
HINH_ANH.text = "HÌNH ẢNH"	


sanpham_1.text_color = "black"
sanpham_1.text_size = 40
sanpham_2.text_color = "black"
sanpham_2.text_size = 40
sanpham_3.text_color = "black"
sanpham_3.text_size = 40

loaisanpham_1.text_color = "black"
loaisanpham_1.text_size = 40
loaisanpham_2.text_color = "black"
loaisanpham_2.text_size = 40
loaisanpham_3.text_color = "black"
loaisanpham_3.text_size = 40

thuchien_1.text_color = "red2"
thuchien_1.text_size = 40
thuchien_2.text_color = "red2"
thuchien_2.text_size = 40
thuchien_3.text_color = "red2"
thuchien_3.text_size = 40

kehoach_1.text_color = "red2"
kehoach_1.text_size = 40
kehoach_2.text_color = "red2"
kehoach_2.text_size = 40
kehoach_3.text_color = "red2"
kehoach_3.text_size = 40

donvi_1.text_color = "dark goldenrod"
donvi_1.text_size = 40
donvi_2.text_color = "dark goldenrod"
donvi_2.text_size = 40
donvi_3.text_color = "dark goldenrod"
donvi_3.text_size = 40


tongthuchien.text_color = "red2"
tongthuchien.text_size = 40


tongkehoach.text_color = "red2"
tongkehoach.text_size = 40


#********************************************************************

def on_connect(mqttc, obj, flags, rc):
	print('CONECTED**********************')
	global ngayss,namss,thangss,timer
	realngay.value = datetime.now().strftime('%d\%m\%Y')
	ngayss = datetime.now().strftime('%d')
	timer = (datetime.now().strftime('%d %m %Y')).split()
	hinhanh_connect.image = 'connect512.png'
	############## SETUP thuộc tính TÊN.thuộctính = GIÁ TRỊ *****************************************************
	
	#truocsau.visible = False  CÓ THỂ SETUP THUỘC TÍNH CỦA TEXT SAU VẪN ĐƯỢC ************************************
def on_disconnect(mqttc, obj, rc):
    print ('DISCONNECT********************')
    hinhanh_connect.image = 'notconnect.png'
	#pass
def on_message(mqttc, obj, msg):
	global ngay1 ,ngay2 ,ngay3 ,ngay4 ,ngay5 ,ngay6 ,ngay7 ,ngay8 ,ngay9 ,ngay10 ,ngay11 ,ngay12 ,ngay13 ,ngay14 ,ngay15 ,ngay16 ,ngay17 ,ngay18 ,ngay19 ,ngay20 ,ngay21 ,ngay22 ,ngay23 ,ngay24 ,ngay25 ,ngay26 ,ngay27 ,ngay28 ,ngay29 ,ngay30 ,ngay31
	global hold, window,text2
	tmpRCV = str(msg.payload.decode("utf-8"))
	
	#print(tmpRCV)
	time.sleep(0.1)
	try:
			data = tmpRCV.split()
	except:
			data = 'null'
	
				
	if(data[0] == "khngay_1"):	
		ngay1 =0	
		with open (khngay_1,'w') as khngay1:
			khngay1.writelines(tmpRCV)
	if(data[0] == "khngay_2"):	
		ngay2 =0	
		with open (khngay_2,'w') as khngay2:
			khngay2.writelines(tmpRCV)
		
	if(data[0] == "khngay_3"):		
		ngay3 =0		
		with open (khngay_3,'w') as khngay3:
			khngay3.writelines(tmpRCV)
		
	if(data[0] == "khngay_4"):	
		ngay4 =0
		with open (khngay_4,'w') as khngay4:
			khngay4.writelines(tmpRCV)
		
	if(data[0] == "khngay_5"):	
		ngay5 =0			
		with open (khngay_5,'w') as khngay5:
			khngay5.writelines(tmpRCV)
		
	if(data[0] == "khngay_6"):	
		ngay6 =0				
		with open (khngay_6,'w') as khngay6:
			khngay6.writelines(tmpRCV)
		
	#time.sleep(0.1)
	if(data[0] == "khngay_7"):	
		ngay7 =0				
		with open (khngay_7,'w') as khngay7:
			khngay7.writelines(tmpRCV)
		
	if(data[0] == "khngay_8"):	
		ngay8 =0				
		with open (khngay_8,'w') as khngay8:
			khngay8.writelines(tmpRCV)
		
	if(data[0] == "khngay_9"):	
		ngay9 =0				
		with open (khngay_9,'w') as khngay9:
			khngay9.writelines(tmpRCV)
		
	if(data[0] == "khngay_10"):		
		ngay10 =0			
		with open (khngay_10,'w') as khngay10:				# NHẬN KẾ HOẠCH SẢN XUẤT VÀ LƯU VÀO TEXT 
			khngay10.writelines(tmpRCV)
		
	if(data[0] == "khngay_11"):		
		ngay11 =0			
		with open (khngay_11,'w') as khngay11:
			khngay11.writelines(tmpRCV)
		
	if(data[0] == "khngay_12"):		
		ngay12 =0			
		with open (khngay_12,'w') as khngay12:
			khngay12.writelines(tmpRCV)
		
	if(data[0] == "khngay_13"):	
		ngay13 =0				
		with open (khngay_13,'w') as khngay13:
			khngay13.writelines(tmpRCV)
		
	if(data[0] == "khngay_14"):		
		ngay14 =0			
		with open (khngay_14,'w') as khngay14:
			khngay14.writelines(tmpRCV)
		
	if(data[0] == "khngay_15"):		
		ngay15 =0			
		with open (khngay_15,'w') as khngay15:
			khngay15.writelines(tmpRCV)
		
	if(data[0] == "khngay_16"):		
		ngay16 =0			
		with open (khngay_16,'w') as khngay16:
			khngay16.writelines(tmpRCV)
		
	#time.sleep(0.1)
	if(data[0] == "khngay_17"):	
		ngay17 = 0				
		with open (khngay_17,'w') as khngay17:
			khngay17.writelines(tmpRCV)
		
	if(data[0] == "khngay_18"):
		ngay18 = 0					
		with open (khngay_18,'w') as khngay18:
			khngay18.writelines(tmpRCV)
		
	if(data[0] == "khngay_19"):	
		ngay19 =0				
		with open (khngay_19,'w') as khngay19:
			khngay19.writelines(tmpRCV)
		
	if(data[0] == "khngay_20"):	
		ngay20 =0				
		with open (khngay_20,'w') as khngay20:
			khngay20.writelines(tmpRCV)
		
	#time.sleep(0.1)
	if(data[0] == "khngay_21"):	
		ngay21 =0	
		#print(ngay21)			
		with open (khngay_21,'w') as khngay21:
			khngay21.writelines(tmpRCV)
		
	if(data[0] == "khngay_22"):	
		ngay22 =0	
		
		with open (khngay_22,'w') as khngay22:
			khngay22.writelines(tmpRCV)
		
	if(data[0] == "khngay_23"):		
		ngay23 =0			
		with open (khngay_23,'w') as khngay23:
			khngay23.writelines(tmpRCV)
		
	if(data[0] == "khngay_24"):	
		ngay24 =0				
		
		with open (khngay_24,'w') as khngay24:
			khngay24.writelines(tmpRCV)
			
	if(data[0] == "khngay_25"):		
		ngay25 =0			
		with open (khngay_25,'w') as khngay25:
			khngay25.writelines(tmpRCV)
		
	if(data[0] == "khngay_26"):	
		ngay26 =0				
		with open (khngay_26,'w') as khngay26:
			khngay26.writelines(tmpRCV)
		
	if(data[0] == "khngay_27"):	
		ngay27 =0				
		with open (khngay_27,'w') as khngay27:
			khngay27.writelines(tmpRCV)
		
	if(data[0] == "khngay_28"):	
		ngay28 =0				
		with open (khngay_28,'w') as khngay28:
			khngay28.writelines(tmpRCV)
		
	#time.sleep(0.1)
	if(data[0] == "khngay_29"):		
		ngay29 =0			
		with open (khngay_29,'w') as khngay29:
			khngay29.writelines(tmpRCV)
		
	if(data[0] == "khngay_30"):	
		ngay30=0				
		with open (khngay_30,'w') as khngay30:
			khngay30.writelines(tmpRCV)
		
	if(data[0] == "khngay_31"):	
		ngay31 =0				
		with open (khngay_31,'w') as khngay31:
			khngay31.writelines(tmpRCV)
	
	#print (data)	
	if(data[0] == "getdata"):	
		try:
			for i in range(2019,2030):
								
				for j in range(1,13):
															
					if (j == int(data[1]) and i == int(data[2])):
						#print ('ok----------------')
						for tt_ngay in ngay_dem:
							
							thuchien_sp = ''
							readth =''
							for name_sp in sp:
								
								with open ('/home/pi/GUINHIP/ktqua_thuchien/'+data[2]+'/thang-'+data[1]+'/ngay-'+tt_ngay+'/'+name_sp+'.text','r') as thuchien1:
									#print (name_sp)
									readth = thuchien1.readline()
									#print (readth)
									if (readth == ''):
										readth = name_sp + ' ' + 'SL'+' '+'0'
								thuchien_sp +=readth+' '
								#print(thuchien_sp)
								#print (readth)
							#print('ok------')
							#thuchien_sp = thuchien_sp + ' '+'getdata' 
											
							mqttc.publish("pub",'ngay'+tt_ngay+' '+thuchien_sp) 
							
							#print(thuchien_sp)	
									
									#break
								
				else:
					break						
				
		except:
			pass
	try:
			welcome = tmpRCV.split('@')
	except:
			welcome = 'null'
	if(welcome[0] == "welcome"):	
		if (hold == 0 and welcome[1] == 'open'):
			window = Window(tieude,title = 'WELCOME')	
			window.tk.attributes("-fullscreen",True)
			window.bg = 'White' 
			space= Text(window,grid=[1,0],height = 4,text = '')
			text2= Text(window,grid=[1,1],size = 60, color = 'Red', font="Times New Roman",width = 'fill')
			img1 = Picture(window,grid=[1,2],width=1130,height=500)
			img1.image = 'K200.png'	
			bar = Box(window,layout="grid",grid=[0,0])
			#space= Text(window,grid=[0,1],width = 10,text = '')
			img2 = Picture(bar,grid=[0,3],width=480,height=220)
			img2.image = 'Chuyen vi.gif'	
			img3 = Picture(bar,grid=[1,3],width=400,height=200)
			img3.image = 'nhipvang.gif'		
			img4 = Picture(bar,grid=[2,3],width=404,height=220)
			img4.image = 'Disp.gif'
			hold = 1
			
		if (welcome[1] == "open"):
			text2.value = ''
			#text2= Text(window,grid=[0,2],size = 40, color = 'blue4', font="Times New Roman",width = 'fill')	
			text2.value = welcome[2]
			window.show()
			
		if (welcome[1] == "close"):
			text2.value = ''
			window.hide()
			
# TEN SAN PHAM ###############################

	 
def on_publish(mqttc, obj, mid):
 #print("mid: "+str(mid))
 pass
 
def on_subscribe(mqttc, obj, mid, granted_qos):
 pass
 
def on_log(mqttc, obj, level, string):
 pass
 	
def thoigian():
	global gioss
	gioss = datetime.now().strftime('%H')
	gio.value = datetime.now().strftime('%H:%M:%S')
	
def ngay():
	global ngayss,namss,thangss,timer
	realngay.value = datetime.now().strftime('%d\%m\%Y')
	ngayss = datetime.now().strftime('%d')
	namss = datetime.now().strftime('%Y')
	thangss = datetime.now().strftime('%m')
	timer = (datetime.now().strftime('%d %m %Y')).split()
	#pass
def lay_sanpham_1(a,b):
	global ten_sp,loai_sp,kh_sp,ma_sp
	if (b == 1):
		#print('k250 truoc')
		sanpham_1.value = 'K250'
		loaisanpham_1.value = 'NHÍP TRƯỚC'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'K250FT'
		ten_sp = 'K250'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_1.image = 'K250-FT.png'
	if (b == 2):
		#print('k250 sau')
		sanpham_1.value = 'K250'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'K250RR'
		ten_sp = 'K250'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'K250-RR.png'
	if (b == 3):
		#print('k200')
		sanpham_1.value = 'K200'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'K200'
		ten_sp = 'K200'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'K200.png'
	if (b == 4):
		#print('500B truoc')
		sanpham_1.value = 'OLL 500B'
		loaisanpham_1.value = 'NHÍP TRƯỚC'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'OLLIN500FT'
		ten_sp = 'OLLIN 500B'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_1.image = 'Ollin500B-FRT.png'
	if (b == 5):
		#print('500B sau')
		sanpham_1.value = 'OLL 500B'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'OLLIN500RR'
		ten_sp = 'OLLIN 500B'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'Ollin500B-RR.png'
	if (b == 6):
		#print('500M3 truoc')
		sanpham_1.value = 'OLL 500-M3'
		loaisanpham_1.value = 'NHÍP TRƯỚC'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'OLLIN500M3FT'
		ten_sp = 'OLLIN 500B-M3'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_1.image = 'Ollin 500B-M3FT.png'
	if (b == 7):
		#print('500M3 sau')
		sanpham_1.value = 'OLL 500-M3'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'OLLIN500M3RR'
		ten_sp = 'OLLIN 500B-M3'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'Ollin 500B-M3RR.png'
	if (b == 8):
		#print('700-720 truoc')
		sanpham_1.value = 'OLLIN 700'
		loaisanpham_1.value = 'NHÍP TRƯỚC'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'OLLIN700FT'
		ten_sp = 'OLLIN 700'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_1.image = 'Ollin700.png'
	if (b == 9):
		#print('700-720 sau')
		sanpham_1.value = 'OLLIN 700'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'OLLIN700RR'
		ten_sp = 'OLLIN 700'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'Ollin700.png'
	if (b == 10):
		#print('SMRM 4la')
		sanpham_1.value = 'SMRM 4 LA'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'SMRM4LA'
		ten_sp = 'SMRM 4LA'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'SMRM 4LA.png'
	if (b == 11):
		#print('SMRM 7la')
		sanpham_1.value = 'SMRM 7 LA'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'SMRM7LA'
		ten_sp = 'SMRM 7LA'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'SMRM 4LA.png'
	if (b == 12):
		#print('700C truoc')
		sanpham_1.value = 'OLLIN 700-720'
		loaisanpham_1.value = 'NHÍP TRƯỚC'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'OLLIN700720FT'
		ten_sp = 'OLLIN 700-720'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_1.image = 'Ollin700C-FRT.png'
	if (b == 13):
		#print('700C sau')
		sanpham_1.value = 'OLLIN 700-720'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'OLLIN700720RR'
		ten_sp = 'OLLIN 700-720'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'Ollin700C-RR.png'
	if (b == 14):
		#print('k165 truoc')
		sanpham_1.value = 'K190'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'K190'
		ten_sp = 'K190'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'K190.png'
	if (b == 16):
		#print('k165 sau')
		sanpham_1.value = 'K165'
		loaisanpham_1.value = 'NHÍP SAU'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'K165RR'
		ten_sp = 'K165'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_1.image = 'K165-RR.png'
	if (b == 15):
		#print('k190')
		sanpham_1.value = 'K165'
		loaisanpham_1.value = 'NHÍP TRƯỚC'
		kehoach_1.value = a
		donvi_1.value = 'Bộ'
		ma_sp = 'K165FT'
		ten_sp = 'K165'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_1.image = 'K165-FT.png'
		
	
	
	
	time.sleep(0.02)
	return ten_sp
	return loai_sp
	return kh_sp
	return ma_sp
def lay_sanpham_2(a,b):
	global ten_sp,loai_sp,kh_sp,ma_sp
	if (b == 1):
		#print('k250 truoc')
		sanpham_2.value = 'K250'
		loaisanpham_2.value = 'NHÍP TRƯỚC'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'K250FT'
		ten_sp = 'K250'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_2.image = 'K250-FT.png'
	if (b == 2):
		#print('k250 sau')
		sanpham_2.value = 'K250'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'K250RR'
		ten_sp = 'K250'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'K250-RR.png'
	if (b == 3):
		#print('k200')
		sanpham_2.value = 'K200'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'K200'
		ten_sp = 'K200'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'K200.png'
	if (b == 4):
		#print('500B truoc')
		sanpham_2.value = 'OLL 500B'
		loaisanpham_2.value = 'NHÍP TRƯỚC'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'OLLIN500FT'
		ten_sp = 'OLLIN 500B'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_2.image = 'Ollin500B-FRT.png'
	if (b == 5):
		#print('500B sau')
		sanpham_2.value = 'OLL 500B'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'OLLIN500RR'
		ten_sp = 'OLLIN 500B'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'Ollin500B-RR.png'
	if (b == 6):
		#print('500M3 truoc')
		sanpham_2.value = 'OLL 500-M3'
		loaisanpham_2.value = 'NHÍP TRƯỚC'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'OLLIN500M3FT'
		ten_sp = 'OLLIN 500B-M3'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_2.image = 'Ollin 500B-M3FT.png'
	if (b == 7):
		#print('500M3 sau')
		sanpham_2.value = 'OLL 500-M3'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'OLLIN500M3RR'
		ten_sp = 'OLLIN 500B-M3'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'Ollin 500B-M3RR.png'
	if (b == 8):
		#print('700-720 truoc')
		sanpham_2.value = 'OLLIN 700'
		loaisanpham_2.value = 'NHÍP TRƯỚC'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'OLLIN700FT'
		ten_sp = 'OLLIN 700'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_2.image = 'Ollin700.png'
	if (b == 9):
		#print('700-720 sau')
		sanpham_2.value = 'OLLIN 700'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'OLLIN700RR'
		ten_sp = 'OLLIN 700'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'Ollin700.png'
	if (b == 10):
		#print('SMRM 4la')
		sanpham_2.value = 'SMRM 4 LA'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'SMRM4LA'
		ten_sp = 'SMRM 4LA'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'SMRM 4LA.png'
	if (b == 11):
		#print('SMRM 7la')
		sanpham_2.value = 'SMRM 7 LA'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'SMRM7LA'
		ten_sp = 'SMRM 7LA'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'SMRM 4LA.png'
	if (b == 12):
		#print('700C truoc')
		sanpham_2.value = 'OLLIN 700-720'
		loaisanpham_2.value = 'NHÍP TRƯỚC'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'OLLIN700720FT'
		ten_sp = 'OLLIN 700-720'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_2.image = 'Ollin700C-FRT.png'
	if (b == 13):
		#print('700C sau')
		sanpham_2.value = 'OLL 700-720'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'OLLIN700720RR'
		ten_sp = 'OLLIN 700-720'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'Ollin700C-RR.png'
	if (b == 14):
		#print('k190')
		sanpham_2.value = 'K190'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'K190'
		ten_sp = 'K190'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'K190.png'
	if (b == 16):
		#print('k165 sau')
		sanpham_2.value = 'K165'
		loaisanpham_2.value = 'NHÍP SAU'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'K165RR'
		ten_sp = 'K165'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_2.image = 'K165-RR.png'
	
	if (b == 15):
		#print('k190')
		sanpham_2.value = 'K165'
		loaisanpham_2.value = 'NHÍP TRƯỚC'
		kehoach_2.value = a
		donvi_2.value = 'Bộ'
		ma_sp = 'K165FT'
		ten_sp = 'K165'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_2.image = 'K165-FT.png'
	
	time.sleep(0.02)
	return ten_sp
	return loai_sp
	return kh_sp
	return ma_sp
def lay_sanpham_3(a,b):
	global ten_sp,loai_sp,kh_sp,ma_sp
	if (b == 1):
		#print('k250 truoc')
		sanpham_3.value = 'K250'
		loaisanpham_3.value = 'NHÍP TRƯỚC'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'K250FT'
		ten_sp = 'K250'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_3.image = 'K250-FT.png'
	if (b == 2):
		#print('k250 sau')
		sanpham_3.value = 'K250'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'K250RR'
		ten_sp = 'K250'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'K250-RR.png'
	if (b == 3):
		#print('k200')
		sanpham_3.value = 'K200'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'K200'
		ten_sp = 'K200'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'K200.png'
	if (b == 4):
		#print('500B truoc')
		sanpham_3.value = 'OLLIN 500B'
		loaisanpham_3.value = 'NHÍP TRƯỚC'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'OLLIN500FT'
		ten_sp = 'OLLIN 500B'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_3.image = 'Ollin500B-FRT.png'
	if (b == 5):
		#print('500B sau')
		sanpham_3.value = 'OLLIN 500B'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'OLLIN500RR'
		ten_sp = 'OLLIN 500B'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'Ollin500B-RR.png'
	if (b == 6):
		#print('500M3 truoc')
		sanpham_3.value = 'OLLIN 500-M3'
		loaisanpham_3.value = 'NHÍP TRƯỚC'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'OLLIN500M3FT'
		ten_sp = 'OLLIN 500B-M3'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_3.image = 'Ollin 500B-M3FT.png'
	if (b == 7):
		#print('500M3 sau')
		sanpham_3.value = 'OLLIN 500-M3'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'OLLIN500M3RR'
		ten_sp = 'OLLIN 500B-M3'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'Ollin 500B-M3RR.png'
	if (b == 8):
		#print('700-720 truoc')
		sanpham_3.value = 'OLLIN 700'
		loaisanpham_3.value = 'NHÍP TRƯỚC'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'OLLIN700FT'
		ten_sp = 'OLLIN 700'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_3.image = 'Ollin700.png'
	if (b == 9):
		#print('700-720 sau')
		sanpham_3.value = 'OLLIN 700'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'OLLIN700RR'
		ten_sp = 'OLLIN 700'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'Ollin700.png'
	if (b == 10):
		#print('SMRM 4la')
		sanpham_3.value = 'SMRM 4 LA'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'SMRM4LA'
		ten_sp = 'SMRM 4LA'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'SMRM 4LA.png'
	if (b == 11):
		#print('SMRM 7la')
		sanpham_3.value = 'SMRM 7 LA'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'SMRM7LA'
		ten_sp = 'SMRM 7LA'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'SMRM 4LA.png'
	if (b == 12):
		#print('700C truoc')
		sanpham_3.value = 'OLLIN 700-720'
		loaisanpham_3.value = 'NHÍP TRƯỚC'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'OLLIN700720FT'
		ten_sp = 'OLLIN 700-720'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_3.image = 'Ollin700C-FRT.png'
	if (b == 13):
		#print('700C sau')
		sanpham_3.value = 'OLLIN 700-720'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'OLLIN700720RR'
		ten_sp = 'OLLIN 700-720'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'Ollin700C-RR.png'
	if (b == 14):
		#print('k190')
		sanpham_3.value = 'K190'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'K190'
		ten_sp = 'K190'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'K190.png'
	if (b == 16):
		#print('k165 sau')
		sanpham_3.value = 'K165'
		loaisanpham_3.value = 'NHÍP SAU'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'K165RR'
		ten_sp = 'K165'
		loai_sp ='NHÍP SAU'
		kh_sp = a
		hinhanh_3.image = 'K165-RR.png'
	
	
	if (b == 15):
		#print('k190')
		sanpham_3.value = 'K165'
		loaisanpham_3.value = 'NHÍP TRƯỚC'
		kehoach_3.value = a
		donvi_3.value = 'Bộ'
		ma_sp = 'K165FT'
		ten_sp = 'K165'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
		hinhanh_3.image = 'K165-FT.png'
	
	time.sleep(0.02)
	return ten_sp
	return loai_sp
	return kh_sp
	return ma_sp
def lay_sanpham_add(a,b):
	global ten_sp,loai_sp,kh_sp,ma_sp
	
	if (b == 1):
		#print('k250 truoc')
		ma_sp = 'K250FT'
		ten_sp = 'K250'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
	if (b == 2):
		#print('k250 sau')
		ma_sp = 'K250RR'
		ten_sp = 'K250'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	if (b == 3):
		#print('k200')
		ma_sp = 'K200'
		ten_sp = 'K200'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	if (b == 4):
		#print('500B truoc')
		ma_sp = 'OLLIN500FT'
		ten_sp = 'OLLIN 500B'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
	if (b == 5):
		#print('500B sau')
		ma_sp = 'OLLIN500RR'
		ten_sp = 'OLLIN 500B'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	if (b == 6):
		#print('500M3 truoc')
		ma_sp = 'OLLIN500M3FT'
		ten_sp = 'OLLIN 500B-M3'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
	if (b == 7):
		#print('500M3 sau')
		ma_sp = 'OLLIN500M3RR'
		ten_sp = 'OLLIN 500B-M3'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	if (b == 8):
		#print('700-720 truoc')
		ma_sp = 'OLLIN700FT'
		ten_sp = 'OLLIN 700'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
	if (b == 9):
		#print('700-720 sau')
		ma_sp = 'OLLIN700RR'
		ten_sp = 'OLLIN 700'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	if (b == 10):
		#print('SMRM 4la')
		ma_sp = 'SMRM4LA'
		ten_sp = 'SMRM 4LA'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	if (b == 11):
		#print('SMRM 7la')
		ma_sp = 'SMRM7LA'
		ten_sp = 'SMRM 7LA'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	if (b == 12):
		#print('700C truoc')
		ma_sp = 'OLLIN700720FT'
		ten_sp = 'OLLIN 700-720'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
	if (b == 13):
		#print('700C sau')
		ma_sp = 'OLLIN700720RR'
		ten_sp = 'OLLIN 700-720'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	if (b == 14):
		#print('k165 truoc')
		ma_sp = 'K190'
		ten_sp = 'K190'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	if (b == 15):
		#print('k165 sau')
		ma_sp = 'K165FT'
		ten_sp = 'K165'
		loai_sp ='NHÍP TRƯỚC'
		kh_sp = a
	if (b == 16):
		#print('k190')
		ma_sp = 'K165RR'
		ten_sp = 'K165'
		loai_sp ='NHÍP SAU'
		kh_sp = a
	time.sleep(0.1)
	return ma_sp
	return ten_sp
	return loai_sp
	return kh_sp
	
def barcode_reader():
	global count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,count13,count14,count15,count16,ngayss,gioss,timer
	global ngay1 ,ngay2 ,ngay3 ,ngay4 ,ngay5 ,ngay6 ,ngay7 ,ngay8 ,ngay9 ,ngay10 ,ngay11 ,ngay12 ,ngay13 ,ngay14 ,ngay15 ,ngay16 ,ngay17 ,ngay18 ,ngay19 ,ngay20 ,ngay21 ,ngay22 ,ngay23 ,ngay24 ,ngay25 ,ngay26 ,ngay27 ,ngay28 ,ngay29 ,ngay30 ,ngay31
	global ten_sp,loai_sp,kh_sp,ten_sp_1,loai_sp_1,kh_sp_1,ten_sp_2,loai_sp_2,kh_sp_2,ten_sp_3,loai_sp_3,kh_sp_3,ten_sp_4,loai_sp_4,kh_sp_4,ten_sp_5,loai_sp_5,kh_sp_5,ten_sp_6,loai_sp_6,kh_sp_6,ten_sp_7,loai_sp_7,kh_sp_7,ten_sp_8,loai_sp_8,kh_sp_8,ten_sp_9
	global loai_sp_9,kh_sp_9,ten_sp_10,loai_sp_10,kh_sp_10,ten_sp_11,loai_sp_11,kh_sp_11,ten_sp_12,loai_sp_12,kh_sp_12,ten_sp_13,loai_sp_13,kh_sp_13,ten_sp_14,loai_sp_14,kh_sp_14,ten_sp_15,loai_sp_15,kh_sp_15,ten_sp_16,loai_sp_16,kh_sp_16
	global ma_sp, ma_sp_1,ma_sp_2,ma_sp_3,ma_sp_4,ma_sp_5,ma_sp_6,ma_sp_7,ma_sp_8,ma_sp_9,ma_sp_10,ma_sp_11,ma_sp_12,ma_sp_13,ma_sp_14,ma_sp_15,ma_sp_16
	global screen
	while True:
		
		try:
			#print(ast.literal_eval(timer[0]))
			#################################
			if ngayss == '01' and ngay1 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay1 = 1
				sanpham = ''
				dem=0
				with open(khngay_1, 'r') as kh1:
					ngay_1 = kh1.readline()
					
					try:
						data1 = ngay_1.split()
						
					except:
						data1 = 'null'
					
					for i in range(1,17):
						if (data1[i] != '0'):						
							sanpham += data1[i] + ' ' +str(i)+ ' '	
							dem=dem+1				# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '02' and ngay2 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay2 = 1
				sanpham = ''
				dem=0
				with open(khngay_2, 'r') as kh2:
					ngay_2 = kh2.readline()
					
					try:
						data2 = ngay_2.split()
						
					except:
						data2 = 'null'
					
					for i in range(1,17):
						if (data2[i] != '0'):						
							sanpham += data2[i] + ' ' +str(i)+ ' '	
							dem=dem+1				# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                              ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp		
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '03' and ngay3 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay3 = 1
				sanpham = ''
				dem=0
				with open(khngay_3, 'r') as kh3:
					ngay_3 = kh3.readline()
					
					try:
						data3 = ngay_3.split()
						
					except:
						data3 = 'null'
					
					for i in range(1,17):
						if (data3[i] != '0'):						
							sanpham += data3[i] + ' ' +str(i)+ ' '	
							dem=dem+1				# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						#time.sleep(0.1)
						#print (sl_sanpham)       
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                          ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp		
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
				
			if ngayss == '04' and ngay4 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay4 = 1
				sanpham = ''
				dem = 0
				with open(khngay_4, 'r') as kh4:
					ngay_4 = kh4.readline()
					time.sleep(0.02)
					try:
						data4 = ngay_4.split()
						
					except:
						data4 = 'null'
					
					for i in range(1,17):
						if (data4[i] != '0'):						
							sanpham += data4[i] + ' ' +str(i)+ ' '	
							dem=dem	+1			# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
					if (sanpham != ''):
						
						sl_sanpham = sanpham.split()				
						#time.sleep(0.1)
						#print (dem)   
						
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	
							
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
										
							
						
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp		
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						
						print ('trong')	
					
					
			if ngayss == '05' and ngay5 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay5 = 1
				sanpham = ''
				dem=0
				with open(khngay_5, 'r') as kh5:
					ngay_5 = kh5.readline()
					
					try:
						data5 = ngay_5.split()
						
					except:
						data5 = 'null'
					
					for i in range(1,17):
						if (data5[i] != '0'):						
							sanpham += data5[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
				##############################################################	
					
			if ngayss == '06' and ngay6 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay6 = 1
				sanpham = ''
				dem=0
				with open(khngay_6, 'r') as kh6:
					ngay_6 = kh6.readline()
					
					try:
						data6 = ngay_6.split()
						
					except:
						data6 = 'null'
					
					for i in range(1,17):
						if (data6[i] != '0'):						
							sanpham += data6[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                              ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '07' and ngay7 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay7 = 1
				sanpham = ''
				dem=0
				with open(khngay_7, 'r') as kh7:
					ngay_7 = kh7.readline()
					
					try:
						data7 = ngay_7.split()
						
					except:
						data7 = 'null'
					
					for i in range(1,17):
						if (data7[i] != '0'):						
							sanpham += data7[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '08' and ngay8 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay8 = 1
				sanpham = ''
				dem=0
				with open(khngay_8, 'r') as kh8:
					ngay_8 = kh8.readline()
					
					try:
						data8 = ngay_8.split()
						
					except:
						data8 = 'null'
					
					for i in range(1,17):
						if (data8[i] != '0'):						
							sanpham += data8[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '09' and ngay9 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay9 = 1
				sanpham = ''
				dem=0
				with open(khngay_9, 'r') as kh9:
					ngay_9 = kh9.readline()
					
					try:
						data9 = ngay_9.split()
						
					except:
						data9 = 'null'
					
					for i in range(1,17):
						if (data9[i] != '0'):						
							sanpham += data9[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                               ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '10' and ngay10 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay10 = 1
				sanpham = ''
				dem=0
				with open(khngay_10, 'r') as kh10:
					ngay_10 = kh10.readline()
					
					try:
						data10 = ngay_10.split()
						
					except:
						data10 = 'null'
					
					for i in range(1,17):
						if (data10[i] != '0'):						
							sanpham += data10[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                               ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '11' and ngay11 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay11 = 1
				sanpham = ''
				dem=0
				with open(khngay_11, 'r') as kh11:
					ngay_11 = kh11.readline()
					
					try:
						data11 = ngay_11.split()
						
					except:
						data11 = 'null'
					
					for i in range(1,17):
						if (data11[i] != '0'):						
							sanpham += data11[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                               ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '12' and ngay12 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay12 = 1
				sanpham = ''
				dem=0
				with open(khngay_12, 'r') as kh12:
					ngay_12 = kh12.readline()
					
					try:
						data12 = ngay_12.split()
						
					except:
						data12 = 'null'
					
					for i in range(1,17):
						if (data12[i] != '0'):						
							sanpham += data12[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp		
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '13' and ngay13 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay13 = 1
				sanpham = ''
				dem=0
				with open(khngay_13, 'r') as kh13:
					ngay_13 = kh13.readline()
					
					try:
						data13 = ngay_13.split()
						
					except:
						data13 = 'null'
					
					for i in range(1,17):
						if (data13[i] != '0'):						
							sanpham += data13[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                 ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '14' and ngay14 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay14 = 1
				sanpham = ''
				dem=0
				with open(khngay_14, 'r') as kh14:
					ngay_14 = kh14.readline()
					
					try:
						data14 = ngay_14.split()
						
					except:
						data14 = 'null'
					
					for i in range(1,17):
						if (data14[i] != '0'):						
							sanpham += data14[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                              ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '15' and ngay15 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay15 = 1
				sanpham = ''
				dem=0
				with open(khngay_15, 'r') as kh15:
					ngay_15 = kh15.readline()
					
					try:
						data15 = ngay_15.split()
						
					except:
						data15 = 'null'
					
					for i in range(1,17):
						if (data15[i] != '0'):						
							sanpham += data15[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                               ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp		
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '16' and ngay16 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay16 = 1
				sanpham = ''
				dem=0
				with open(khngay_16, 'r') as kh16:
					ngay_16 = kh16.readline()
					
					try:
						data16 = ngay_16.split()
						
					except:
						data16 = 'null'
					
					for i in range(1,17):
						if (data16[i] != '0'):						
							sanpham += data16[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp		
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '17' and ngay17 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay17 = 1
				sanpham = ''
				dem=0
				with open(khngay_17, 'r') as kh17:
					ngay_17 = kh17.readline()
					
					try:
						data17 = ngay_17.split()
						
					except:
						data17 = 'null'
					
					for i in range(1,17):
						if (data17[i] != '0'):						
							sanpham += data17[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                               ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '18' and ngay18 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay18 = 1
				sanpham = ''
				dem=0
				with open(khngay_18, 'r') as kh18:
					ngay_18 = kh18.readline()
					
					try:
						data18 = ngay_18.split()
						
					except:
						data18 = 'null'
					
					for i in range(1,17):
						if (data18[i] != '0'):						
							sanpham += data18[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')						
	
					
			if ngayss == '19' and ngay19 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay19 = 1
				sanpham = ''
				dem=0
				with open(khngay_19, 'r') as kh19:
					ngay_19 = kh19.readline()
					
					try:
						data19 = ngay_19.split()
						
					except:
						data19 = 'null'
					
					for i in range(1,17):
						if (data19[i] != '0'):						
							sanpham += data19[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                 ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
	
				
			if ngayss == '20' and ngay20 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				#print ('ngay 20')
				
				ngay20 = 1
				#print(ngay20)
				sanpham = ''
				dem=0
				with open(khngay_20, 'r') as kh20:
					ngay_20 = kh20.readline()
					
					try:
						data20 = ngay_20.split()
						
					except:
						data20 = 'null'
					
					for i in range(1,17):
						if (data20[i] != '0'):						
							sanpham += data20[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
						#print (i)
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                 ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
	
					
			if ngayss == '21' and ngay21 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay21 = 1
				sanpham = ''
				dem=0
				with open(khngay_21, 'r') as kh21:
					ngay_21 = kh21.readline()
					
					try:
						data21 = ngay_21.split()
						
					except:
						data21 = 'null'
					
					for i in range(1,17):
						if (data21[i] != '0'):						
							sanpham += data21[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                              ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '22' and ngay22 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				#print (ngayss)
				ngay22 = 1
				dem=0
				sanpham = ''
				with open(khngay_22, 'r') as kh22:
					ngay_22 = kh22.readline()
					
					try:
						data22 = ngay_22.split()
						
					except:
						data22 = 'null'
					
					for i in range(1,17):
						if (data22[i] != '0'):						
							sanpham += data22[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                               ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '23' and ngay23 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay23 = 1
				sanpham = ''
				dem=0
				with open(khngay_23, 'r') as kh23:
					ngay_23 = kh23.readline()
					
					try:
						data23 = ngay_23.split()
						
					except:
						data23 = 'null'
					
					for i in range(1,17):
						if (data23[i] != '0'):						
							sanpham += data23[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                 ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '24' and ngay24 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay24 = 1
				sanpham = ''
				dem=0
				with open(khngay_24, 'r') as kh24:
					ngay_24 = kh24.readline()
					
					try:
						data24 = ngay_24.split()
						
					except:
						data24 = 'null'
					
					for i in range(1,17):
						if (data24[i] != '0'):						
							sanpham += data24[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                               ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '25' and ngay25 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay25 = 1
				sanpham = ''
				dem=0
				with open(khngay_25, 'r') as kh25:
					ngay_25 = kh25.readline()
					
					try:
						data25 = ngay_25.split()
						
					except:
						data25 = 'null'
					
					for i in range(1,17):
						if (data25[i] != '0'):						
							sanpham += data25[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '26' and ngay26 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay26 = 1
				sanpham = ''
				dem=0
				with open(khngay_26, 'r') as kh26:
					ngay_26 = kh26.readline()
					
					try:
						data26 = ngay_26.split()
						
					except:
						data26 = 'null'
					
					for i in range(1,17):
						if (data26[i] != '0'):						
							sanpham += data26[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp		
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '27' and ngay27 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay27 = 1
				sanpham = ''
				dem=0
				with open(khngay_27, 'r') as kh27:
					ngay_27 = kh27.readline()
					
					try:
						data27 = ngay_27.split()
						
					except:
						data27 = 'null'
					
					for i in range(1,17):
						if (data27[i] != '0'):						
							sanpham += data27[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                               ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp		
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '28' and ngay28 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay28 = 1
				sanpham = ''
				dem=0
				with open(khngay_28, 'r') as kh28:
					ngay_28 = kh28.readline()
					#print(ngay_28)
					try:
						data28 = ngay_28.split()
						
					except:
						data28 = 'null'
					
					for i in range(1,17):
						if (data28[i] != '0'):						
							sanpham += data28[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
									
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '29' and ngay29 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay29 = 1
				sanpham = ''
				dem=0
				with open(khngay_29, 'r') as kh29:
					ngay_29 = kh29.readline()
					
					try:
						data29 = ngay_29.split()
						
					except:
						data29 = 'null'
					
					for i in range(1,17):
						if (data29[i] != '0'):						
							sanpham += data29[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
									
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '30' and ngay30 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay30 = 1
				sanpham = ''
				dem=0
				with open(khngay_30, 'r') as kh30:
					ngay_30 = kh30.readline()
					
					try:
						data30 = ngay_30.split()
						
					except:
						data30 = 'null'
					
					for i in range(1,17):
						if (data30[i] != '0'):						
							sanpham += data30[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                                 ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
					
			if ngayss == '31' and ngay31 == 0:   # CHI THUC HIEN 1 LAN VA KHI NHAN DUOC TIN HIEU UPDATE KE HOACH TU NGUOI QUAN LY
				ngay31 = 1
				sanpham = ''
				dem=0
				with open(khngay_31, 'r') as kh31:
					ngay_31 = kh31.readline()
					
					try:
						data31 = ngay_31.split()
						
					except:
						data31 = 'null'
					
					for i in range(1,17):
						if (data31[i] != '0'):						
							sanpham += data31[i] + ' ' +str(i)+ ' '					# LAY 3 SAN PHAM DAU TIEN KHAC 0 TRONG FILE EXCEL
							dem=dem+1
					if (sanpham != ''):
						sl_sanpham = sanpham.split()				
						if dem == 1:		
							
							sanpham_2.value = ''
							loaisanpham_2.value = ''
							kehoach_2.value = ''
							donvi_2.value = ''
							hinhanh_2.visible = False
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP2-3----')	               
						if dem == 2:				
							
							sanpham_3.value = ''
							loaisanpham_3.value = ''
							kehoach_3.value = ''
							donvi_3.value = ''
							hinhanh_3.visible = False
							#print ('NOT SP3----')	                               ## SO LUONG KE HOACH VA VI TRI CUA SAN PHAM DO (K200 / K250 ...) VI TRI THEO BANG EXCEL
						if (sl_sanpham[1] != ''):
							#time.sleep(0.02)
							hinhanh_1.visible = True
							lay_sanpham_1(ast.literal_eval(sl_sanpham[0]),ast.literal_eval(sl_sanpham[1]))
							ten_sp_1 = ten_sp
							ma_sp_1 = ma_sp
							loai_sp_1 = loai_sp
							kh_sp_1 = kh_sp
							
						
							
						if (sl_sanpham[3] != ''):
							#time.sleep(0.02)
							hinhanh_2.visible = True
							lay_sanpham_2(ast.literal_eval(sl_sanpham[2]),ast.literal_eval(sl_sanpham[3]))				# 3 sp DAU TIEN KHAC 0	
							ten_sp_2 = ten_sp
							ma_sp_2 = ma_sp
							loai_sp_2 = loai_sp
							kh_sp_2 = kh_sp
										
							
							
							
						if (sl_sanpham[5] != ''):
							#time.sleep(0.02)
							hinhanh_3.visible = True
							lay_sanpham_3(ast.literal_eval(sl_sanpham[4]),ast.literal_eval(sl_sanpham[5]))
							ten_sp_3 = ten_sp
							ma_sp_3 = ma_sp
							loai_sp_3 = loai_sp
							kh_sp_3 = kh_sp
							
						
						if (sl_sanpham[7] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[6]),ast.literal_eval(sl_sanpham[7]))
							ten_sp_4 = ten_sp
							ma_sp_4 = ma_sp
							loai_sp_4 = loai_sp
							kh_sp_4 =kh_sp
							
						if (sl_sanpham[9] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[8]),ast.literal_eval(sl_sanpham[9]))
							ten_sp_5= ten_sp
							ma_sp_5 = ma_sp
							loai_sp_5 = loai_sp
							kh_sp_5 =kh_sp
						if (sl_sanpham[11] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[10]),ast.literal_eval(sl_sanpham[11]))			# NEU > 3 SP THI LUU LAI CAC SP DO
							ten_sp_6 = ten_sp
							ma_sp_6 = ma_sp
							loai_sp_6 = loai_sp
							kh_sp_6 =kh_sp
						if (sl_sanpham[13] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[12]),ast.literal_eval(sl_sanpham[13]))
							ten_sp_7 = ten_sp
							ma_sp_7 = ma_sp
							loai_sp_7 = loai_sp
							kh_sp_7 =kh_sp
						if (sl_sanpham[15] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[14]),ast.literal_eval(sl_sanpham[15]))
							ten_sp_8 = ten_sp
							ma_sp_8 = ma_sp
							loai_sp_8 = loai_sp
							kh_sp_8 =kh_sp
						if (sl_sanpham[17] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[16]),ast.literal_eval(sl_sanpham[17]))
							ten_sp_9 = ten_sp
							ma_sp_9 = ma_sp
							loai_sp_9 = loai_sp
							kh_sp_9 =kh_sp
						if (sl_sanpham[19] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[18]),ast.literal_eval(sl_sanpham[19]))
							ten_sp_10 = ten_sp
							ma_sp_10 = ma_sp
							loai_sp_10 = loai_sp
							kh_sp_10 =kh_sp
						if (sl_sanpham[21] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[20]),ast.literal_eval(sl_sanpham[21]))
							ten_sp_11 = ten_sp
							ma_sp_11 = ma_sp
							loai_sp_11 = loai_sp
							kh_sp_11 =kh_sp
						if (sl_sanpham[23] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[22]),ast.literal_eval(sl_sanpham[23]))
							ten_sp_12 = ten_sp
							ma_sp_12 = ma_sp
							loai_sp_12 = loai_sp
							kh_sp_12 =kh_sp
						if (sl_sanpham[25] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[24]),ast.literal_eval(sl_sanpham[25]))
							ten_sp_13 = ten_sp
							ma_sp_13 = ma_sp
							loai_sp_13 = loai_sp
							kh_sp_13 =kh_sp
						if (sl_sanpham[27] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[26]),ast.literal_eval(sl_sanpham[27]))
							ten_sp_14 = ten_sp
							ma_sp_14 = ma_sp
							loai_sp_14 = loai_sp
							kh_sp_14 =kh_sp
						if (sl_sanpham[29] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[28]),ast.literal_eval(sl_sanpham[29]))
							ten_sp_15 = ten_sp
							ma_sp_15 = ma_sp
							loai_sp_15 = loai_sp
							kh_sp_15 =kh_sp
						if (sl_sanpham[31] != ''):
							lay_sanpham_add(ast.literal_eval(sl_sanpham[30]),ast.literal_eval(sl_sanpham[31]))
							ten_sp_16 = ten_sp
							ma_sp_16 = ma_sp
							loai_sp_16 = loai_sp
							kh_sp_16 =kh_sp	
						
						
					else:
						thuchien_1.value = ''
						thuchien_2.value = ''
						thuchien_3.value = ''
						kehoach_1.value = ''
						kehoach_2.value = ''
						kehoach_3.value = ''
						
						sanpham_1.value = ''
						loaisanpham_1.value = ''
						kehoach_1.value = ''
						donvi_1.value = ''
						hinhanh_1.visible = False
						
						sanpham_2.value = ''
						loaisanpham_2.value = ''
						kehoach_2.value = ''
						donvi_2.value = ''
						hinhanh_2.visible = False
							
						sanpham_3.value = ''
						loaisanpham_3.value = ''
						kehoach_3.value = ''
						donvi_3.value = ''
						hinhanh_3.visible = False
						print ('trong')	
					
			
			time.sleep(0.2)
			################################# LAY BARCODE
			ss = barcode.get()
			barcode.value = ''
			bar_tmp = ss[:6]
			#print (bar_tmp)		
			tmp = qrnhip[bar_tmp]
			
			#print (tmp)		
			##################################################
			if (tmp == ma_sp_1):
				#print ('okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
				count1 = count1 + 1
				mqttc.publish("pub",ma_sp_1+' '+str(count1))
				thuchien_1.value = count1
				kehoach_1.value = kh_sp_1
				sanpham_1.value = ten_sp_1
				loaisanpham_1.value = loai_sp_1
				donvi_1.value = 'Bộ'
				
				if (ast.literal_eval(thuchien_1.value) >= ast.literal_eval(kehoach_1.value)):
					mqttc.publish("pub","Warnning"+ma_sp_1) # CANH BAO KHI DA SX DU KE HOACH ************************************
				try:
					
					for index in sp:
						if index == ma_sp_1:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
																						
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_1+'.text','w') as thuchien:
												thuchien.write(ma_sp_1+' '+'SL'+' '+str(count1))
												#print('ok***************************')		
												break
								else:
					
					
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_2):
				count2 = count2 + 1
				mqttc.publish("pub",ma_sp_2+' '+str(count2))			# 3 SP CO KE HOACH KHAC 0 DAU TIEN SE HIEN THI TRUOC (CAN UU TIEN THUC HIEN TRUOC)
				thuchien_2.value = count2
				kehoach_2.value = kh_sp_2
				sanpham_2.value = ten_sp_2
				loaisanpham_2.value = loai_sp_2
				donvi_2.value = 'Bộ'
				if (ast.literal_eval(thuchien_2.value) >= ast.literal_eval(kehoach_2.value)):
						mqttc.publish("pub","Warnning"+ma_sp_2)
				try:
					
					for index in sp:
						if index == ma_sp_2:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_2+'.text','w') as thuchien:
												thuchien.write(ma_sp_2+' '+'SL'+' '+str(count2))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_3):
				count3 = count3 + 1
				mqttc.publish("pub",ma_sp_3+' '+str(count3))
				thuchien_3.value = count3
				kehoach_3.value = kh_sp_3
				sanpham_3.value = ten_sp_3
				loaisanpham_3.value = loai_sp_3
				donvi_3.value = 'Bộ'
				if (ast.literal_eval(thuchien_3.value) >= ast.literal_eval(kehoach_3.value)):
						mqttc.publish("pub","Warnning"+ma_sp_3)
				try:
					
					for index in sp:
						if index == ma_sp_3:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_3+'.text','w') as thuchien:
												thuchien.write(ma_sp_3+' '+'SL'+' '+str(count3))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
			##################################################			SP THU 4 TRO DI THI SE HIEN THI LEN PHIA TREN 
			if (tmp == ma_sp_4):
				count4 = count4 + 1
				mqttc.publish("pub",ma_sp_4+' '+str(count4))
				thuchien_1.value = count4
				kehoach_1.value = kh_sp_4
				sanpham_1.value = ten_sp_4
				loaisanpham_1.value = loai_sp_4
				donvi_1.value = 'Bộ'
				if (ast.literal_eval(thuchien_1.value) >= ast.literal_eval(kehoach_1.value)):
						mqttc.publish("pub","Warnning"+ma_sp_4)
				hinhanh_1.image = 'Ollin500B-FRT.png'
				try:
					
					for index in sp:
						if index == ma_sp_4:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_4+'.text','w') as thuchien:
												thuchien.write(ma_sp_4+' '+'SL'+' '+str(count4))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_5):
				count5 = count5 + 1
				mqttc.publish("pub",ma_sp_5+' '+str(count5))
				thuchien_2.value = count5
				kehoach_2.value = kh_sp_5
				sanpham_2.value = ten_sp_5
				loaisanpham_2.value = loai_sp_5
				donvi_2.value = 'Bộ'
				hinhanh_2.image = 'Ollin500B-RR.png'
				if (ast.literal_eval(thuchien_2.value) >= ast.literal_eval(kehoach_2.value)):
						mqttc.publish("pub","Warnning"+ma_sp_5)
				try:
					
					for index in sp:
						if index == ma_sp_5:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_5+'.text','w') as thuchien:
												thuchien.write(ma_sp_5+' '+'SL'+' '+str(count5))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_6):
				count6 = count6 + 1
				mqttc.publish("pub",ma_sp_6+' '+str(count6))
				thuchien_3.value = count6
				kehoach_3.value = kh_sp_6
				sanpham_3.value = ten_sp_6
				loaisanpham_3.value = loai_sp_6
				donvi_3.value = 'Bộ'
				hinhanh_3.image = 'Ollin 500B-M3FT.png'
				if (ast.literal_eval(thuchien_3.value) >= ast.literal_eval(kehoach_3.value)):
						mqttc.publish("pub","Warnning"+ma_sp_6)
				try:
					
					for index in sp:
						if index == ma_sp_6:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_6+'.text','w') as thuchien:
												thuchien.write(ma_sp_6+' '+'SL'+' '+str(count6))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
			###########################	
			if (tmp == ma_sp_7):
				count7 = count7 + 1
				mqttc.publish("pub",ma_sp_7+' '+str(count7))
				thuchien_1.value = count7
				kehoach_1.value = kh_sp_7
				sanpham_1.value = ten_sp_7
				loaisanpham_1.value = loai_sp_7
				donvi_1.value = 'Bộ'
				hinhanh_1.image = 'Ollin 500B-M3RR.png'
				if (ast.literal_eval(thuchien_1.value) >= ast.literal_eval(kehoach_1.value)):
						mqttc.publish("pub","Warnning"+ma_sp_7)
				try:
					
					for index in sp:
						if index == ma_sp_7:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_7+'.text','w') as thuchien:
												thuchien.write(ma_sp_7+' '+'SL'+' '+str(count7))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_8):
				count8 = count8 + 1
				mqttc.publish("pub",ma_sp_8+' '+str(count8))
				thuchien_2.value = count8
				kehoach_2.value = kh_sp_8
				sanpham_2.value = ten_sp_8
				loaisanpham_2.value = loai_sp_8
				donvi_2.value = 'Bộ'
				hinhanh_2.image = 'Ollin700C-FRT.png'
				if (ast.literal_eval(thuchien_2.value) >= ast.literal_eval(kehoach_2.value)):
						mqttc.publish("pub","Warnning"+ma_sp_8)
						#print('warn 700ft')
				try:
					
					for index in sp:
						if index == ma_sp_8:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_8+'.text','w') as thuchien:
												thuchien.write(ma_sp_8+' '+'SL'+' '+str(count8))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_9):
				count9 = count9 + 1
				mqttc.publish("pub",ma_sp_9+' '+str(count9))
				thuchien_3.value = count9
				kehoach_3.value = kh_sp_9
				sanpham_3.value = ten_sp_9
				loaisanpham_3.value = loai_sp_9
				donvi_3.value = 'Bộ'
				hinhanh_3.image = 'Ollin700C-RR.png'
				if (ast.literal_eval(thuchien_3.value) >= ast.literal_eval(kehoach_3.value)):
						mqttc.publish("pub","Warnning"+ma_sp_9)
						#print('warn 700rr')
				try:
					
					for index in sp:
						if index == ma_sp_9:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_9+'.text','w') as thuchien:
												thuchien.write(ma_sp_9+' '+'SL'+' '+str(count9))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				############################
			if (tmp == ma_sp_10):
				count10 = count10 + 1
				mqttc.publish("pub",ma_sp_10+' '+str(count10))
				thuchien_1.value = count10
				kehoach_1.value = kh_sp_10
				sanpham_1.value = ten_sp_10
				loaisanpham_1.value = loai_sp_10
				donvi_1.value = 'Bộ'
				#hinhanh_1.image = 'SMRM 4LA.png'
				if (ast.literal_eval(thuchien_1.value) >= ast.literal_eval(kehoach_1.value)):
						mqttc.publish("pub","Warnning"+ma_sp_10)
				try:
					
					for index in sp:
						if index == ma_sp_10:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_10+'.text','w') as thuchien:
												thuchien.write(ma_sp_10+' '+'SL'+' '+str(count10))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_11):
				count11 = count11 + 1
				mqttc.publish("pub",ma_sp_11+' '+str(count11))
				thuchien_2.value = count11
				kehoach_2.value = kh_sp_11
				sanpham_2.value = ten_sp_11
				loaisanpham_2.value = loai_sp_11
				donvi_2.value = 'Bộ'
				#hinhanh_2.image = 'SMRM 4LA.png'
				if (ast.literal_eval(thuchien_2.value) >= ast.literal_eval(kehoach_2.value)):
						mqttc.publish("pub","Warnning"+ma_sp_11)
				try:
					
					for index in sp:
						if index == ma_sp_11:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_11+'.text','w') as thuchien:
												thuchien.write(ma_sp_11+' '+'SL'+' '+str(count11))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_12):
				count12 = count12 + 1
				mqttc.publish("pub",ma_sp_12+' '+str(count12))
				thuchien_3.value = count12
				kehoach_3.value = kh_sp_12
				sanpham_3.value = ten_sp_12
				loaisanpham_3.value = loai_sp_12
				donvi_3.value = 'Bộ'
				#hinhanh_3.image = 'Ollin700.png'
				if (ast.literal_eval(thuchien_3.value) >= ast.literal_eval(kehoach_3.value)):
						mqttc.publish("pub","Warnning"+ma_sp_12)
						#print('warn 700-720ft')
				try:
					
					for index in sp:
						if index == ma_sp_12:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_12+'.text','w') as thuchien:
												thuchien.write(ma_sp_12+' '+'SL'+' '+str(count12))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				#########################
			if (tmp == ma_sp_13):
				count13 = count13 + 1
				mqttc.publish("pub",ma_sp_13+' '+str(count13))
				thuchien_1.value = count13
				kehoach_1.value = kh_sp_13
				sanpham_1.value = ten_sp_13
				loaisanpham_1.value = loai_sp_13
				donvi_1.value = 'Bộ'
				#hinhanh_1.image = 'Ollin700.png'
				if (ast.literal_eval(thuchien_1.value) >= ast.literal_eval(kehoach_1.value)):
						mqttc.publish("pub","Warnning"+ma_sp_13)
						#print('warn 700-720rr')
				try:
					
					for index in sp:
						if index == ma_sp_13:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_13+'.text','w') as thuchien:
												thuchien.write(ma_sp_13+' '+'SL'+' '+str(count13))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_14):
				count14 = count14 + 1
				mqttc.publish("pub",ma_sp_14+' '+str(count14))
				thuchien_2.value = count14
				kehoach_2.value = kh_sp_14
				sanpham_2.value = ten_sp_14
				loaisanpham_2.value = loai_sp_14
				donvi_2.value = 'Bộ'
				#hinhanh_2.image = 'K165-FT.png'
				if (ast.literal_eval(thuchien_2.value) >= ast.literal_eval(kehoach_2.value)):
						mqttc.publish("pub","Warnning"+ma_sp_14)
				try:
					
					for index in sp:
						if index == ma_sp_14:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_14+'.text','w') as thuchien:
												thuchien.write(ma_sp_14+' '+'SL'+' '+str(count14))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
			if (tmp == ma_sp_15):
				count15 = count15 + 1
				mqttc.publish("pub",ma_sp_15+' '+str(count15))
				thuchien_3.value = count15
				kehoach_3.value = kh_sp_15
				sanpham_3.value = ten_sp_15
				loaisanpham_3.value = loai_sp_15
				donvi_3.value = 'Bộ'
				#hinhanh_3.image = 'K165-RR.png'
				if (ast.literal_eval(thuchien_3.value) >= ast.literal_eval(kehoach_3.value)):
						mqttc.publish("pub","Warnning"+ma_sp_15)
				try:
					
					for index in sp:
						if index == ma_sp_15:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_15+'.text','w') as thuchien:
												thuchien.write(ma_sp_15+' '+'SL'+' '+str(count15))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				########################
			if (tmp == ma_sp_16):
				count16 = count16 + 1
				mqttc.publish("pub",ma_sp_16+' '+str(count16))
				thuchien_1.value = count16
				kehoach_1.value = kh_sp_16
				sanpham_1.value = ten_sp_16
				loaisanpham_1.value = loai_sp_16
				donvi_1.value = 'Bộ'
				#hinhanh_1.image = 'K190.png'
				if (ast.literal_eval(thuchien_1.value) >= ast.literal_eval(kehoach_1.value)):
						mqttc.publish("pub","Warnning"+ma_sp_16)
				try:
					
					for index in sp:
						if index == ma_sp_16:
							for i in range(2019,2030):
							
								for j in range(1,13):
														
									for k in range(1,32):
										#print('i'+':'+str(i))#print('j'+':'+str(j))#print('k'+':'+str(k))#print(int(timer[1]))
										if (j == int(timer[1]) and k == int(timer[0]) and i == int(timer[2])):
											#print('ok***************************')															
											with open ('/home/pi/GUINHIP/ktqua_thuchien/'+timer[2]+'/thang-'+timer[1]+'/ngay-'+timer[0]+'/'+ma_sp_16+'.text','w') as thuchien:
												thuchien.write(ma_sp_16+' '+'SL'+' '+str(count16))
												break
								else:
									break						
							else:
								break
					
				except:
					pass
				
		except:
			pass
				
		
		
		if (thuchien_1.get() == '' ):
			th_1 = 0
		else:
			th_1 = ast.literal_eval(thuchien_1.value)
		if (thuchien_2.get() == '' ):
			th_2 = 0
		else:
			th_2 = ast.literal_eval(thuchien_2.value)
		
		if (thuchien_3.get() == '' ):
			th_3 = 0
		else:
			th_3 = ast.literal_eval(thuchien_3.value)
			
		
		if (kehoach_1.get() == '' ):
			kh_1 = 0
		else:
			kh_1 = ast.literal_eval(kehoach_1.value)
		if (kehoach_2.get() == '' ):
			kh_2 = 0
		else:
			kh_2 = ast.literal_eval(kehoach_2.value)
		if (kehoach_3.get() == '' ):
			kh_3 = 0
		else:
			kh_3 = ast.literal_eval(kehoach_3.value)
			
		if th_1 == 0 and th_2 == 0 and th_3 == 0:
			tongthuchien.value = ''
		else:
			tongthuchien.value = th_1+ th_2 + th_3
			
		if kh_1 == 0 and kh_2 == 0 and kh_3 == 0:
			tongkehoach.value = ''
		else:
			tongkehoach.value = kh_1+ kh_2 + kh_3
		
		if (gioss == '23'):
			thuchien_1.value = ''
			thuchien_2.value = ''
			thuchien_3.value = ''
		
		if (((gioss == '17') or (gioss == '18') or (gioss == '19')or (gioss == '20')or (gioss == '21')or (gioss == '22')or (gioss == '23')or (gioss == '00')or (gioss == '01')
		or (gioss == '02')or (gioss == '03')or (gioss == '04')or (gioss == '05') or (gioss == '06')) and screen ==1):
			screen =0
			subprocess.call('export DISPLAY=":0"\n' + 'xset dpms force off', shell=True)
			print ('off')
		elif (((gioss == '07') or (gioss == '08')or (gioss == '09')or (gioss == '10')or (gioss == '11')or (gioss == '12')or (gioss == '13')or (gioss == '14')
		or (gioss == '15')or (gioss == '16') )and (screen == 0)):
			screen =1
			#print ('on')
			subprocess.call('export DISPLAY=":0"\n' +'xset dpms force on\n' + 'xset s off\n' +'xset s noblank\n' +'xset -dpms', shell=True)
		
	
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.connect('10.11.15.201', 1883, 60) #dien IP cua Pi, vd: 192.168.1.77
mqttc.subscribe("sub", 0)
mqttc.loop_start()

gio.repeat(1000, thoigian)
realngay.repeat(20000,ngay)		

#try:
	
barcode_reader = threading.Thread(name='barcode_reader',target=barcode_reader)
#barcode_reader.deamon = True
barcode_reader.start()
    #barcode_reader.join()
tieude.display()
#except IndexError:
#           print("ERROR")

