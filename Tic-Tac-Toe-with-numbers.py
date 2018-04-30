while True:
    print("for play against computer select 1")
    print("for play as 2 players select 2")
    q=input()
    if q in ["1","2"]:
        break
    else:
        print("wrong selection")
if q=="2":
    p1=str(input("player one name:"))
    p2=str(input("player two name:"))
    p11=["1","3","5","7","9"]
    p12=["0","2","4","6","8"]
    b=[["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"]]
    print("----------------")
    print("|",b[0][0],"|",b[0][1],"|",b[0][2],"|")
    print("|",b[1][0],"|",b[1][1],"|",b[1][2],"|")
    print("|",b[2][0],"|",b[2][1],"|",b[2][2],"|")
    print("----------------")
    print(p1,"choose number from",p11,"with no Repetition")
    print(p2,"choose number from",p12,"with no Repetition")
    a=[[0,0,0],[0,0,0],[0,0,0]]
    rp=[""]
    w=0
    o=222
    while (True):
        print(p1 +" turn")
        y=True
        while y :
                n1=input("enter number :")
                if n1 in p11 :
                    p11.remove(n1)
                    n1=int(n1)
                    y=False
                else:
                    print ("choose number from ",p11)
        p=str(input("enter the position :"))
        s=True
        while s:
                if p in rp or p not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"] :
                    p=str(input("wrong position or that position is taken enter another position :"))
                else:
                    s=False
        rp.append(p)
        if p=="a1":
            a[0][0]=n1
            b[0][0]=n1
        elif p=="a2":
            a[0][1]=n1
            b[0][1]=n1               
        elif p=="a3":
            a[0][2]=n1
            b[0][2]=n1          
        elif p=="b1":
            a[1][0]=n1
            b[1][0]=n1           
        elif p=="b2":
            a[1][1]=n1
            b[1][1]=n1   
        elif p=="b3":
            a[1][2]=n1
            b[1][2]=n1       
        elif p=="c1":
            a[2][0]=n1
            b[2][0]=n1      
        elif p=="c2":
            a[2][1]=n1 
            b[2][1]=n1      
        elif p=="c3":
            a[2][2]=n1
            b[2][2]=n1
        print("----------------")
        print("|",b[0][0],"|",b[0][1],"|",b[0][2],"|")
        print("|",b[1][0],"|",b[1][1],"|",b[1][2],"|")
        print("|",b[2][0],"|",b[2][1],"|",b[2][2],"|")
        print("----------------")
        if (("a1" in rp and "a2" in rp and "a3" in rp)):
                    sum=a[0][0]+a[0][1]+a[0][2]
                    if sum ==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if(("b1" in rp and "b2" in rp and "b3" in rp)):
                    sum=a[1][0]+a[1][1]+a[1][2]
                    if sum ==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if (("c1" in rp and "c2" in rp and "c3" in rp)):
                sum=a[2][0]+a[2][1]+a[2][2]
                if sum ==15:
                    print (p1+" is the winner" )
                    o=111
                    break    
        if (("a1" in rp and "b1" in rp and "c1" in rp)):
                    sum=a[0][0]+a[1][0]+a[2][0]
                    if sum==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if (("a2" in rp and "b2" in rp and "c2" in rp)):
                    sum=a[0][1]+a[1][1]+a[2][1]
                    if sum==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if (("a3" in rp and "b3" in rp and "c3" in rp)) :
                    sum=a[0][2]+a[1][2]+a[2][2]
                    if sum ==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if "a1" in rp and "b2" in rp and "c3" in rp :
            sum=0
            if a[0][0]+a[1][1]+a[2][2]==15 :
                print (p1+" is the winner" )
                o=111
        if "a3" in rp and "b2" in rp and "c1" in rp :
            sum=0
            if a[0][2]+a[1][1]+a[2][0]==15 :
                print (p1+" is the winner" )
                o=111
        w+=1
        if o==111:
            break
        if w>=9:
            print("draw")
            break
        print(p2 +" turn")
        y=True
        while y :
                n2=input("enter number :")
                if n2 in p12 :
                    p12.remove(n2)
                    n2=int(n2)
                    y=False
                else:
                    print ("choose number from ",p12)
        p=str(input("position :"))
        s=True
        while s:
                if p in rp or p not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
                    p=str(input("wrong position or that position is taken enter another position :"))
                else :
                    s=False
        rp.append(p)
        if p=="a1":
            a[0][0]=n2
            b[0][0]=n2
        elif p=="a2":
            a[0][1]=n2
            b[0][1]=n2               
        elif p=="a3":
            a[0][2]=n2
            b[0][2]=n2          
        elif p=="b1":
            a[1][0]=n2
            b[1][0]=n2           
        elif p=="b2":
            a[1][1]=n2
            b[1][1]=n2   
        elif p=="b3":
            a[1][2]=n2
            b[1][2]=n2       
        elif p=="c1":
            a[2][0]=n2
            b[2][0]=n2      
        elif p=="c2":
            a[2][1]=n2 
            b[2][1]=n2      
        elif p=="c3":
            a[2][2]=n2
            b[2][2]=n2
        print("----------------")
        print("|",b[0][0],"|",b[0][1],"|",b[0][2],"|")
        print("|",b[1][0],"|",b[1][1],"|",b[1][2],"|")
        print("|",b[2][0],"|",b[2][1],"|",b[2][2],"|")
        print("----------------")
        if (("a1" in rp and "a2" in rp and "a3" in rp)):
                    sum=a[0][0]+a[0][1]+a[0][2]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if  (("b1" in rp and "b2" in rp and "b3" in rp)):
                    sum=a[1][0]+a[1][1]+a[1][2]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if  (("c1" in rp and "c2" in rp and "c3" in rp)):
                    sum=a[2][0]+a[2][1]+a[2][2]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break    
        if (("a1" in rp and "b1" in rp and "c1" in rp)):
                    sum=a[0][0]+a[1][0]+a[2][0]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if (("a2" in rp and "b2" in rp and "c2" in rp)):
                    sum=a[0][1]+a[1][1]+a[2][1]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if (("a3" in rp and "b3" in rp and "c3" in rp)) :
                    sum=a[0][2]+a[1][2]+a[2][2]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if "a1" in rp and "b2" in rp and "c3" in rp :
            sum=0
            if a[0][0]+a[1][1]+a[2][2]==15 :
                print (p2+" is the winner" )
                o=111
        if "a3" in rp and "b2" in rp and "c1" in rp :
            sum=0
            if a[0][2]+a[1][1]+a[2][0]==15 :
                print (p2+" is the winner" )
                o=111
        w+=1
        if o==111:
            break
        if w>=9:
            print("draw")
else:
    import random
    p1=str(input("player name:"))
    p2="computer"
    p11=["1","3","5","7","9"]
    p12=["0","2","4","6","8"]
    b=[["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"]]
    for i in range (3):
        print (b[i])
    print(p1,"choose number from",p11,"with no Repetition")

    a=[[0,0,0],[0,0,0],[0,0,0]]
    rp=[""]
    cp=["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
    w=0
    o=222
    while (True):
        print(p1 +" turn")
        y=True
        while y :
                n1=input("enter number :")
                if n1 in p11 :
                    p11.remove(n1)
                    n1=int(n1)
                    y=False
                else:
                    print ("choose number from ",p11)
        p=str(input("enter the position :"))
        s=True
        while s:
                if p in rp or p not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"] :
                    p=str(input("wrong position or that position is taken enter another position :"))
                else:
                    s=False
        rp.append(p)
        cp.remove(p)
        if p=="a1":
            a[0][0]=n1
            b[0][0]=n1
        elif p=="a2":
            a[0][1]=n1
            b[0][1]=n1               
        elif p=="a3":
            a[0][2]=n1
            b[0][2]=n1          
        elif p=="b1":
            a[1][0]=n1
            b[1][0]=n1           
        elif p=="b2":
            a[1][1]=n1
            b[1][1]=n1   
        elif p=="b3":
            a[1][2]=n1
            b[1][2]=n1       
        elif p=="c1":
            a[2][0]=n1
            b[2][0]=n1      
        elif p=="c2":
            a[2][1]=n1 
            b[2][1]=n1      
        elif p=="c3":
            a[2][2]=n1
            b[2][2]=n1
        print("----------------")
        print("|",b[0][0],"|",b[0][1],"|",b[0][2],"|")
        print("|",b[1][0],"|",b[1][1],"|",b[1][2],"|")
        print("|",b[2][0],"|",b[2][1],"|",b[2][2],"|")
        print("----------------")
        if (("a1" in rp and "a2" in rp and "a3" in rp)):
                    sum=a[0][0]+a[0][1]+a[0][2]
                    if sum ==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if(("b1" in rp and "b2" in rp and "b3" in rp)):
                    sum=a[1][0]+a[1][1]+a[1][2]
                    if sum ==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if (("c1" in rp and "c2" in rp and "c3" in rp)):
                sum=a[2][0]+a[2][1]+a[2][2]
                if sum ==15:
                    print (p1+" is the winner" )
                    o=111
                    break    
        if (("a1" in rp and "b1" in rp and "c1" in rp)):
                    sum=a[0][0]+a[1][0]+a[2][0]
                    if sum==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if (("a2" in rp and "b2" in rp and "c2" in rp)):
                    sum=a[0][1]+a[1][1]+a[2][1]
                    if sum==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if (("a3" in rp and "b3" in rp and "c3" in rp)) :
                    sum=a[0][2]+a[1][2]+a[2][2]
                    if sum ==15:
                        print (p1+" is the winner" )
                        o=111
                        break
        if "a1" in rp and "b2" in rp and "c3" in rp :
            sum=0
            if a[0][0]+a[1][1]+a[2][2]==15 :
                print (p1+" is the winner" )
                o=111
        if "a3" in rp and "b2" in rp and "c1" in rp :
            sum=0
            if a[0][2]+a[1][1]+a[2][0]==15 :
                print (p1+" is the winner" )
                o=111
        w+=1
        if o==111:
            break
        if w>=9:
            print("draw")
            break
        print(p2,"turn")
        for i in range(27):
            if i==1:
                if ("a1" in rp and"a2"in rp) and ("a3" not in rp):
                    p="a3"
                    if(str(15-a[0][0]-a[0][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][0]-a[0][1])in p12:
                        n2=15-a[0][0]-a[0][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==2:
                if ("a1" in rp and"a3"in rp) and ("a2" not in rp):
                    p="a2"
                    if(str(15-a[0][0]-a[0][2])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][0]-a[0][2])in p12:
                        n2=15-a[0][0]-a[0][2]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==3:
                if ("a3" in rp and"a2"in rp) and ("a1" not in rp):
                    p="a1"
                    if(str(15-a[0][2]-a[0][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][2]-a[0][1])in p12:
                        n2=15-a[0][2]-a[0][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==4:
                if ("b1" in rp and"b2"in rp) and ("b3" not in rp):
                    p="b3"
                    if(str(15-a[1][0]-a[1][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[1][0]-a[1][1])in p12:
                        n2=15-a[1][0]-a[1][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==5:
                if ("b1" in rp and"b3"in rp) and ("b2" not in rp):
                    p="b2"
                    if(str(15-a[1][0]-a[1][2])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[1][0]-a[1][2])in p12:
                        n2=15-a[1][0]-a[1][2]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==6:
                if ("b3" in rp and"b2"in rp) and ("b1" not in rp):
                    p="b1"
                    if(str(15-a[1][2]-a[1][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[1][2]-a[1][1])in p12:
                        n2=15-a[1][2]-a[1][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==7:
                if ("c1" in rp and"c2"in rp) and ("c3" not in rp):
                    p="c3"
                    if(str(15-a[2][0]-a[2][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[2][0]-a[2][1])in p12:
                        n2=15-a[2][0]-a[2][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==8:
                if ("c1" in rp and"c3"in rp) and ("c2" not in rp):
                    p="c2"
                    if(str(15-a[2][0]-a[2][2])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[2][0]-a[2][2])in p12:
                        n2=15-a[2][0]-a[2][2]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==9:
                if ("c3" in rp and"c2"in rp) and ("c1" not in rp):
                    p="c1"
                    if(str(15-a[2][2]-a[2][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[2][2]-a[2][1])in p12:
                        n2=15-a[2][2]-a[2][1]
                    else:
                        n2=int(random.choice(p12))    
                    break
            if i==10:
                if ("a1" in rp and"b1"in rp) and ("c1" not in rp):
                    p="c1"
                    if(str(15-a[0][0]-a[1][0])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][0]-a[1][0])in p12:
                        n2=15-a[0][0]-a[1][0]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==11:
                if ("a1" in rp and"c1"in rp) and ("b1" not in rp):
                    p="b1"
                    if(str(15-a[0][0]-a[2][0])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][0]-a[2][0])in p12:
                        n2=15-a[0][0]-a[2][0]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==12:
                if ("c1" in rp and"b1"in rp) and ("a1" not in rp):
                    p="a1"
                    if(str(15-a[2][0]-a[1][0])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[2][0]-a[1][0])in p12:
                        n2=15-a[2][0]-a[1][0]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==13:
                if ("a2" in rp and"b2"in rp) and ("c2" not in rp):
                    p="c2"
                    if(str(15-a[0][1]-a[1][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][1]-a[1][1])in p12:
                        n2=15-a[0][1]-a[1][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==14:
                if ("a2" in rp and"c2"in rp) and ("b2" not in rp):
                    p="b2"
                    if(str(15-a[0][1]-a[2][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][1]-a[2][1])in p12:
                        n2=15-a[0][1]-a[2][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==15:
                if ("c2" in rp and"b2"in rp) and ("a2" not in rp):
                    p="a2"
                    if(str(15-a[2][1]-a[1][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[2][1]-a[1][1])in p12:
                        n2=15-a[2][1]-a[1][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==16:
                if ("a3" in rp and"b3"in rp) and ("c3" not in rp):
                    p="c3"
                    if(str(15-a[0][2]-a[1][2])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][2]-a[1][2])in p12:
                        n2=15-a[0][2]-a[1][2]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==17:
                if ("a3"  in rp and"c3"in rp) and ("b3" not in rp):
                    p="b3"
                    if(str(15-a[0][2]-a[2][2])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][2]-a[2][2])in p12:
                        n2=15-a[0][2]-a[2][2]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==18:
                if ("c3" in rp and"b3"in rp) and ("a3" not in rp):
                    p="a3"
                    if(str(15-a[2][2]-a[1][2])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[2][2]-a[1][2])in p12:
                        n2=15-a[2][2]-a[1][2]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==19:
                if ("a1" in rp and"b2"in rp) and ("c3" not in rp):
                    p="c3"
                    if(str(15-a[0][0]-a[1][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][0]-a[1][1])in p12:
                        n2=15-a[0][0]-a[1][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==20:
                if ("a1"  in rp and"c3"in rp) and ("b2" not in rp):
                    p="b2"
                    if(str(15-a[0][0]-a[2][2])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][0]-a[2][2])in p12:
                        n2=15-a[0][0]-a[2][2]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==21:
                if ("c3" in rp and"b2"in rp) and ("a1" not in rp):
                    p="a1"
                    if(str(15-a[2][2]-a[1][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[2][2]-a[1][1])in p12:
                        n2=15-a[2][2]-a[1][1]
                    else:
                        n2=int(random.choice(p12))                    
                    break
            if i==22:
                if ("a3" in rp and"b2"in rp) and ("c1" not in rp):
                    p="c1"
                    if(str(15-a[0][2]-a[1][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[0][2]-a[1][1])in p12:
                        n2=15-a[0][2]-a[1][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==23:
                if ("a3" in rp and"c1"in rp) and ("b2" not in rp):
                    p="b2"
                    if(str(15-a[0][2]-a[2][0])in p11):

                        n2=int(random.choice(p12))
                    elif str(15-a[0][2]-a[2][0])in p12:
                        n2=15-a[0][2]-a[2][0]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==24:
                if ("c1" in rp and"b2"in rp) and ("a3" not in rp):
                    p="a3"
                    if(str(15-a[2][0]-a[1][1])in p11):
                        n2=int(random.choice(p12))
                    elif str(15-a[2][0]-a[1][1])in p12:
                        n2=15-a[2][0]-a[1][1]
                    else:
                        n2=int(random.choice(p12))
                    break
            if i==25:
                if len(rp)<=2:
                    p=random.choice(cp)
                    n2=int(random.choice(p12))
                    break
            if i==26:
                if not((("a1" in rp and"a2"in rp) and ("a3" not in rp))and (("a1" in rp and"a3"in rp) and ("a2" not in rp))and (("a3" in rp and"a2"in rp) and ("a1" not in rp))and (("b1" in rp and"b2"in rp) and ("b3" not in rp))and (("b1" in rp and"b3"in rp) and ("b2" not in rp))and (("b3" in rp and"b2"in rp) and ("b1" not in rp))and (("c1" in rp and"c2"in rp) and ("c3" not in rp))and (("c1" in rp and"c3"in rp) and ("c2" not in rp))and (("c3" in rp and"c2"in rp) and ("c1" not in rp))and (("a1" in rp and"b1"in rp) and ("c1" not in rp))and (("a1" in rp and"c1"in rp) and ("b1" not in rp))and (("c1" in rp and"b1"in rp) and ("a1" not in rp))and (("a2" in rp and"b2"in rp) and ("c2" not in rp))and (("a2" in rp and"c2"in rp) and ("b2" not in rp))and (("c2" in rp and"b2"in rp) and ("a2" not in rp))and (("a3" in rp and"b3"in rp) and ("c3" not in rp))and (("a3" in rp and"c3"in rp) and ("b3" not in rp))and (("c3" in rp and"b3"in rp) and ("a3" not in rp))and(("a1" in rp and"b2"in rp) and ("c3" not in rp)) and(("a1" in rp and"c3"in rp) and ("b2" not in rp)) and (("c3" in rp and"b2"in rp) and ("a1" not in rp))and (("a3" in rp and"b2"in rp) and ("c1" not in rp))and (("a3" in rp and"c1"in rp) and ("b2" not in rp))and (("c1" in rp and"b2"in rp) and ("a3" not in rp))and (len(rp)<=2)):
                    p=random.choice(cp)
                    n2=int(random.choice(p12))
                    break
        p12.remove(str(n2))
        rp.append(p)
        cp.remove(p)
        if p=="a1":
            a[0][0]=n2
            b[0][0]=n2
        elif p=="a2":
            a[0][1]=n2
            b[0][1]=n2               
        elif p=="a3":
            a[0][2]=n2
            b[0][2]=n2          
        elif p=="b1":
            a[1][0]=n2
            b[1][0]=n2           
        elif p=="b2":
            a[1][1]=n2
            b[1][1]=n2   
        elif p=="b3":
            a[1][2]=n2
            b[1][2]=n2       
        elif p=="c1":
            a[2][0]=n2
            b[2][0]=n2      
        elif p=="c2":
            a[2][1]=n2 
            b[2][1]=n2      
        elif p=="c3":
            a[2][2]=n2
            b[2][2]=n2
        print("----------------")
        print("|",b[0][0],"|",b[0][1],"|",b[0][2],"|")
        print("|",b[1][0],"|",b[1][1],"|",b[1][2],"|")
        print("|",b[2][0],"|",b[2][1],"|",b[2][2],"|")
        print("----------------")
        if (("a1" in rp and "a2" in rp and "a3" in rp)):
                    sum=a[0][0]+a[0][1]+a[0][2]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if  (("b1" in rp and "b2" in rp and "b3" in rp)):
                    sum=a[1][0]+a[1][1]+a[1][2]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if  (("c1" in rp and "c2" in rp and "c3" in rp)):
                    sum=a[2][0]+a[2][1]+a[2][2]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break    
        if (("a1" in rp and "b1" in rp and "c1" in rp)):
                    sum=a[0][0]+a[1][0]+a[2][0]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if (("a2" in rp and "b2" in rp and "c2" in rp)):
                    sum=a[0][1]+a[1][1]+a[2][1]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if (("a3" in rp and "b3" in rp and "c3" in rp)) :
                    sum=a[0][2]+a[1][2]+a[2][2]
                    if sum ==15:
                        print (p2+" is the winner" )
                        o=111
                        break
        if "a1" in rp and "b2" in rp and "c3" in rp :
            sum=0
            if a[0][0]+a[1][1]+a[2][2]==15 :
                print (p2+" is the winner" )
                o=111
        if "a3" in rp and "b2" in rp and "c1" in rp :
            sum=0
            if a[0][2]+a[1][1]+a[2][0]==15 :
                print (p2+" is the winner" )
                o=111
        w+=1
        if o==111:
            break
        if w>=9:
            print("draw")
