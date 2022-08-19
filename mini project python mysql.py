#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import psycopg2
import platform
import os

connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="localhost",
                                  port="5432",
                                  database="databse")
cursor = connection.cursor()
#custname varchar(20),addr varchar (30),jrdate varchar(10),source varchar(10),destination varchar(10));
def registercust():
    l = []
    name = input('enter name: ')
    l.append(name)
    addr = input("enter in address: ")
    l.append(addr)
    jr_date = input('journey date: ')
    l.append(jr_date)
    source = input('enter source: ')
    l.append(source)
    destination = input('enter destination: ')
    l.append(destination)
    cust = (l)

    sql = "insert into pdata(custname, addr, jrdate,source,destination) values(%s,%s,%s,%s,%s);"
    cursor.execute(sql,cust)
    connection.commit()
    
    
def classtypeview():
    print('do you want to see class type available')
    print('enter 1 for yes')
    choice = int(input("enter your choice: "))
    if choice == 1:
        sql = 'select * from classtype;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
            
def ticketprice():
    print('price chart')
    print('1.first class -> $100')
    print('2.business class -> $75')
    print('3.economic class -> $50')
    
    choice = int(input('enter your choice: '))
    n = int(input('how many passengers: '))
    
    if choice == 1:
        print('you choose first class')
        print('the price is', 100*n)
    elif choice == 2:
        print('you choose buisness class')
        print('the price is', 75*n)
    elif choice == 3:
        print('you choose econmic class')
        print('the price is', 50*n)
    else:
        print('choose a valid class')
        
def menuview():
    print('press 1 to see menu')
    choice = int(input('enter choice: '))
    if choice == 1:
        sql = 'select * from food;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            print(i)

def orderItem():
    global s 
    print('do you want to see menu available? Enter 1 for yes')
    choice = int(input('enter choice: '))
    if choice == 1:
        sql = 'select * from food;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    print('do you want to purchase from above list? Enter your choice')
    d = int(input('enter your choice: '))
    if d == 1:
        print('tea')
        a = int(input('enter a quantity: '))
        s = 10*a
        print('Total ammount is', s)
    elif d == 2:
        print('coffee')
        a = int(input('enter a quantity: '))
        s = 10*a
        print('Total ammount is', s)
    elif d == 3:
        print('cold drink')
        a = int(input('enter a quantity: '))
        s = 20*a
        print('Total ammount is', s)
    elif d == 4:
        print('nugget')
        a = int(input('enter a quantity: '))
        s = 10*a
        print('Total ammount is', s)
    elif d == 5:
        print('sandwhich')
        a = int(input('enter a quantity: '))
        s = 50*a
        print('Total ammount is', s)
    elif d == 6:
        print('packcake')
        a = int(input('enter a quantity: '))
        s = 30*a
        print('Total ammount is', s)
    elif d == 7:
        print('fries')
        a = int(input('enter a quantity: '))
        s = 10*a
        print('Total ammount is', s)
    elif d == 8:
        print('milk')
        a = int(input('enter a quantity: '))
        s = 20*a
        print('Total ammount is', s)
    elif d == 9:
        print('noddles')
        a = int(input('enter a quantity: '))
        s = 50*a
        print('Total ammount is', s)
    elif d == 10:
        print('pasta')
        a = int(input('enter a quantity: '))
        s = 50*a
        print('Total ammount is', s)
    else:
        print('please enter a valid option')

def lugageBill():
    global z
    print('do you want to see rate for luggage? enter 1 for yes')
    ch = int(input('enter your choice: '))
    if ch == 1:
        sql = 'select * from lugage;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    y = int(input('please enter your weight of extra luggage: '))
    if y == 20:
        z = y*1000
    elif y==25:
        z = y*1500
    elif y==30:
        z= y*2000
    elif y==50:
        z = y*3000
    return z

def lb():
    print('your lugage bill is', z)
def result():
    print('your food bill is', s)
def ticketAmmount():
    name = input('enter your name: ')
    print('customer name: ', name)
    lb()
    result()
    
def menu():
    print('press 1 to enter customer data')
    print('press 2 to view class')
    print('press 3 to view ticket ammount')
    print('press 4 for the price')
    print('press 5 for the food bill')
    print('press 6 for the lugage bill')
    print('press 7 for the complete ammount')
    print('press 8 for exit')
    userinput = int(input('enter your choice: '))
    if userinput == 1:
        registercust()
    elif userinput == 2:
        classtypeview()
    elif userinput == 3:
        ticketprice()
    elif userinput == 4:
        menuview()
    elif userinput == 5:
        orderItem()
    elif userinput == 6:
        lugageBill()
    elif userinput == 7:
        ticketAmmount()
    elif userinput == 8:
        quit()
    else:
        print('enter a correct choice')
        
menu()

def runAgain():
    runagain = input('do you want to continue again? y/n')
    while (runagain.lower() == 'y'):
        menu()

runAgain()
        




            


# In[ ]:


1	"tea"	10


# In[2]:


import platform
platform.system()


# In[ ]:



sunday: 6pm
tuesday: 6pm
wendsay: 6pm
saturday: 5:30pm

