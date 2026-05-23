'''name=input("enter thr name")
age=int(input("enter the age"))
place=input("enter the place")
if age>=18:
    tamil=int(input("tamil:"))
    eng=int(input("eng:"))
    math=int(input("math:"))
    chemis=int(input("chmis:"))
    phy=int(input("phy:"))
    cs=int(input("cs:"))
    total=tamil+eng+math+chemis+phy+cs
    avrg=total/6
    print("total mark=",total)
    print("average=",avrg)
    if (tamil<35 or eng<35 or math<35 or chemis<35 or phy<35 or cs<35):
        print("fail")
    else:
        print("pass")
        if avrg>=90:
             print("eligible for MBBS")
        elif avrg>=80:
            print("eligible for engni")
        elif avrg>=70:
            print("eligible for science")
        elif avrg>=60:\
            print("eligible for arts")
        else:
            print("not eligible for anything")'''
name=input("enter the name")
age=int(input("enter the age:"))
experience=int(input("enter the experience:"))
designation=input("enter the job(developer/tester):")
if age>=18:
    print("eligible to work")

    if designation=="developer":
       if experience==1:
          print("salary will be 30000")
       elif experience>=2:
          print("salary will be 40000")
       elif experience>=3:
          print("salary will be 50000")
    elif designation=="tester":
       if experience==1:
          print("salary will be 20000")
       elif experience>=2:
            print("salary will be 30000")
       elif experience>=3:
            print("salary will be 40000")
    else:
            print("invalid designation")
else:
            print("not eligible to work")

                         
            
        
                                                                                
