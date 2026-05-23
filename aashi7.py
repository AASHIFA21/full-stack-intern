'''name=input("name:")
age=int(input("age:"))
place=input("place:")
if age>=18:
    tamil=int(input("tamil:"))
    eng=int(input("eng:"))
    math=int(input ("math:"))
    chemis=int(input("chemis:"))
    phy=int(input("phy:"))
    cs=int(input("cs:"))
    total=tamil+eng+math+chemis+phy+cs
    avrg=total/6
    print("total mark=",total)
    print("average=",avrg)
    if(tamil<35 or eng<35 or math<35 or chemis<35 or phy<35 or cs<35):
    
        print("fail")
    else:
        print("pass")
a=29
if a>20:
    print("a is greater than 20")
elif a<20:
    print("a is lesser than 20")
elif a==20:
    print("a is equal to 20")'''
    
name=input("name:")
age=int(input("age:"))
place=input("place:")
if age>=18:
    tamil=int(input("tamil:"))
    eng=int(input("eng:"))
    math=int(input ("math:"))
    chemis=int(input("chemis:"))
    phy=int(input("phy:"))
    cs=int(input("cs:"))
    total=tamil+eng+math+chemis+phy+cs
    avrg=total/6
    print("total mark=",total)
    print("average=",avrg)
    if(tamil<35 or eng<35 or math<35 or chemis<35 or phy<35 or cs<35):
    
        print("fail")
    else:
        print("pass")
        if avrg>=90:
         print("eligible for MBBS")
        elif avrg>=80:
         print("eligiblr for engin")
        elif avrg>=70:
         print("eligible for science")
        elif avrg>=60:
         print("eligible for arts")
        else:
         print("again study 12th")
             
                      
                        
