import json
d={}
with open("Shilpika.json","w")as fb:
    fb.write(json.dumps(d,indent=4))
while True:
    ch=int(input("Enter choice\n 1.Register\n 2.Login\n 3.Update\n 4.Delete\n"))
    if ch==1:
        username=input("Enter Username\n")
        with open("Shilpika.json","r")as fb:
            y=fb.read()
            m=json.loads(y)
            if username in m.keys():
                print("Usernmae already exsists ! !")
            else:
                pwd=input("Enter Password")
                d[username]=pwd
            print(d)
            with open("Shilpika.json","w")as fb:
                fb.write(json.dumps(d,indent=4))
    elif ch==2:
        username=input("Enter the Username")
        with open("Shilpika.json","r") as fb:
            y=fb.read()
            m=json.loads(y)
            if username in m.keys():
                pwd=input("Enter password")
                if m[username]==pwd:
                    print("Login Successfull ! !")
                else:
                    print("Incorrect password")
            else:
                print("Please Register !!!")
    elif ch==3:
        uername=input("Enter username")
        with open("Shilpika.json","r")as fb:
            y=fb.read()
            m=json.loads(y)
            if username in m.keys():
                pwd=input("Enter password")
                if m[username]==pwd:
                    newpwd=input("Enter a new password")
                    m[username]=newpwd
                    with open("Shilpika.json","w")as fb:
                        fb.write(json.dumps(m,indent=4))
                        print(m)
                else:
                    print("Incorrect password")
            else:
                print("Please Register")
    elif ch==4:
        username=input("Enter username")
        with open("Shilpika.json","r")as fb:
            y=fb.read()
            m=json.loads(y)
            if username in m.keys():
                pwd=input("Enter password")
                if m[username]==pwd:
                    m.pop(username)
                    with open("Shilpika.json","w")as fb:
                        fb.write(json.dumps(m,indent=4))
                        print(m)
                else:
                    print("Incorrect Password")
            else:
                print("Please Register")
                
