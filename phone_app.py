# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:17:36 2019

@author: todd
"""

from tkinter import*

pre = {}
phone = {}
bonus = {}


phone['iphone8']=610
phone['iphone8+']=710
phone['iphonex']=910
phone['iphonexs']=1010
phone['iphonemax']=1110
phone['iphonexr']=760
phone['asusAR']=576
phone['asusV']=260
phone['pixel2']=680
phone['pixel2xl']=880
phone['kyoceraDF']=446
phone['motog6']=260
phone['motoz2P']=408
phone['motoz2F']=760
phone['samj7']=260
phone['samj3']=201
phone['samgs8']=700
phone['samgs+']=768
phone['samn9']=1000
phone['samgs9']=800
phone['samgs9+']=930
pre['samj3']=124.99
pre['samj7']=189.99
pre['iphone6']=199.99
bonus['mifi7730']=99.99
bonus['mifi6620']=1.00
bonus['ipadmini4']=379.99
bonus['ipadpro11']=799.99
bonus['ipadpro12.9']=999.99
bonus['ipadpro10.5']=629.99
bonus['samtabe']=1.00
bonus['asuszenpad']=179.99
bonus['ellipsis10']=149.99
bonus['ellipsis8']=19.99
bonus['asuszenpadz8']=50.00
phone['kyoceracadence']=160
phone['kyoceradura']=300
phone['lgv30']=840
phone['samnote8']=900
phone['lgg7']=760
phone['lgstylo2']=274
phone['lgv40']=980
phone['pixel3xl']=950
phone['pixel3']=830
phone['motoz3']=510
bonus['honephone']=29.99
bonus['gizmo']=179.99
bonus['hum']=1.00
bonus['humx']=99.99
bonus['ipad9.7']=309
bonus['samtaba']=29.99
pre['motoe5']=94.99
pre['lgzone']=114.99
pre['motog6']=129.99
pre['iphonese']=159.99






def totalRevenue(x):
    total = 0
    for i in x:
        total += x[i]
    return round(total,2)

#def phone(usr):
#    item = phone[usr]
#    tax = item * .0925
#    charge = 35 + (35*.0925)
#    print("Price is " + str(item))
#    print("Tax is " + str(item * .0925))
#    print("Today is " + str(round(tax + charge,2)))
#    print("Monthly payment: " + str(round(item / 24,2)))
    
def pr():
    usr = input("Phone ")
    print("\n")
    item = pre[usr]
    tax = item * .0925
    charge = 35 + (35 * .0925)
    print("Cost: " + str(round(item + tax + charge, 2)))
    
def bn():
    usr = input("Item: ")
    print("\n")
    item = bonus[usr]
    tax = item * .0925
    total = item + tax
    print("Total: " + str(round(total,2)))
    

root = Tk()


def details():
    if e.get() in phone:
        item = phone[e.get()]
        tax = item * .0925
        charge = 35 + (35*.0925)
        total1 = "Price:",item
        total2 = "Tax:",item*.0925
        total3 = "Today:",round(tax + charge,2)
        total4 = "Monthly:",round(item/24)
        L1.configure(text = total1)
        L2.configure(text = total2)
        L3.configure(text = total3)
        L4.configure(text = total4)
        
        print("Price is " + str(item))
        print("Tax is " + str(item * .0925))
        print("Today is " + str(round(tax + charge,2)))
        print("Monthly payment: " + str(round(item / 24,2)))
        print("\n")
   # elif (e.get() not in phone):
    #    total5 = "Not a valid Model"
     #   L5.configure(text = total5)
      #  print("Not valid model")
        
        




b = Button(root,text="Execute",fg="white",bg="blue",command=details)
b.pack()


L=Label(root,text="Enter Model")
L.pack()

e = Entry(root)
e.pack()

L1 = Label(root, text = " ")
L1.pack()
L2 = Label(root, text = " ")
L2.pack()
L3 = Label(root, text = " ")
L3.pack()
L4 = Label(root, text = " ")
L4.pack()
L5 = Label(root, text = " ")
L5.pack()



#+++++++++++++++++++++++++++++++++++++++++++++++++






#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

root.geometry("200x200")
root.title("POS system")
root.mainloop()



    
    
    
        


    
    
    
    
    
    
    
    
    
    
    
    
    