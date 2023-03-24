import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="12345",database="food")
if conn.is_connected():
    print("sucessfully connected")
print("ORDER YOUR FOOD HERE")
c1=conn.cursor()
print("1.CREATE YOUR ACCOUNT")
print("2.ORDER FOOD")
print("3.LOG IN")
print("4.EXIT")
choice=int(input("enter your choice:"))
if choice ==1:
    v_cust_name=input("enter your name:")
    v_account_no=int(input("enter your own account number:"))
    v_SQL_insert="insert into myc values('"+ v_cust_name+"','"+str(v_account_no)+"')"
    c1.execute(v_SQL_insert)
    conn.commit()
    print("account created")
if choice==2:
    v_f_name=input("enter the name of food:")
    v_price=int(input("enter the cost of your food:"))
    v_address=input("enter your address:")
    v_SQL_insert="insert into sales values('"+ v_f_name+"',"+str(v_price)+",'"+v_address+"')"
    c1.execute(v_SQL_insert)
    conn.commit()
    print("sucessfully phased")
    
if choice==4:
    print("THANK YOU FOR VISITING")
if choice==3:
    print('')
    print('TO LOGIN FILL THESE DETAILS')
    print('')
    cust_name=input('enter your name:')
    print('')
    v_account_no=int(input('enter your account no.:'))
    c1=conn.cursor()
    c1.execute('select * from myc')
    data=c1.fetchall()
    count=c1.rowcount
    for row in data:
        if (cust_name in row) and (v_account_no in row):
            print(' ')
            print(' ')
            print('WELCOME TO YOUR FOOD SERVICE')
            print(' ')
            print(' ')
            print('TO SEE CUSTOMER DETAILS PRESS :1 ')
            print(' ')
            print('TO UPDATE DETAILS PRESS :2')
            print(' ')
            print('TO EXIT PRESS :3')
            print(' ')
            print('TO SEE ORDERED FOOD PRESS :4 ')
            print(' ')
            c2=int(input('enter your choice:'))
            if (c2==1):
                c1=conn.cursor()
                c1.execute('select * from myc')
                data=c1.fetchall()
                count=c1.rowcount
                print('total customers are',count)
                for row in data:
                    print(row)
                print("VISIT AGAIN")
            elif (c2==2):
                print('')
                print('TO UPDATE FILL THIS')
                print('')
                v_cust_name=input("enter your name:")
                print('')
                v_account_no=int(input("enter your own account number:"))
                v_SQL_insert="insert into myc values('"+ v_cust_name+"','"+str(v_account_no)+"')"
                c1.execute(v_SQL_insert)
                conn.commit()
                print('customer details succesully updated')
            elif (c2==3):
                print('THANK YOU FOR VISITING')
            elif(c2==4):
                  c1=conn.cursor()
                  c1.execute('select * from sales')
                  data=c1.fetchall()
                  count=c1.rowcount
                  print('total order food  is',count)
                  for row in data:
                     print(row)
                  print("VISIT AGAIN")
                 
            else:
                 print('SORRY SOMETHING WENT WRONG')
?
