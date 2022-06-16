import json
d={}
with open("Bank.json","w")as fb:
    fb.write(json.dumps(d))
while True:
    ch=int(input("Enter the choice\n 1.Create account\n 2.Balance Enquiry\n 3.Deposit\n 4.Withdraw\n"))
    if ch==1:
        name=input("Enter Name\n")
        pin=int(input("Enter PIN\n"))
        rupees=input("Rs\n")
        amt=int(input("Enter Amount\n"))
        with open("Bank.json","r")as fb:
            y=fb.read()
            m=json.loads(y)
            d[name]=pin
            d[rupees]=amt
        with open("Bank.json","w")as fb:
            fb.write(json.dumps(d))
            print(d)
    if ch==2:
        print("Security check")
        name=input("Enter Name\n")
        with open("Bank.json","r")as fb:
            y=fb.read()
            m=json.loads(y)
            if name in m.keys():
                pin=int(input("Enter PIN\n"))
                if m[name]== pin:
                    print("Balance=",m[rupees])
                else:
                    print("Incorrect PIN !")
            else:
                print("Please Create an account !!!")
    if ch==3:
        name=input("Enter Name\n")
        with open("Bank.json","r")as fb:
            y=fb.read()
            m=json.loads(y)
            if name in m.keys():
                pin=int(input("Enter PIN\n"))
                if m[name]==pin:
                    amount=int(input("Enter the amount to be deposited\n"))
                    m[rupees]=m[rupees]+amount
                    print("Balance=",m[rupees])
                    with open("Bank.json","w")as fb:
                        fb.write(json.dumps(m))
                        print(m)
                else:
                    print("Incorrect amount entered !")
            else:
                print("Please Create an account !!!")
    if ch==4:
        name=input("Enter Name\n")
        with open("Bank.json","r")as fb:
            y=fb.read()
            m=json.loads(y)
            if name in m.keys():
                pin=int(input("Enter PIN\n"))
                if m[name]==pin:
                    amount=int(input("Enter the amount to be withdraw\n"))
                    m[rupees]=m[rupees]-amount
                    print("Balance=",m[rupees])
                    with open("Bank.json","w")as fb:
                        fb.write(json.dumps(m))
                        print(m)
                else:
                    print("Incorrect amount entered !")
            else:
                print("Please Create an account !!!")
            
            
            
