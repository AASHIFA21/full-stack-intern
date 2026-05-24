#hotel menu
name=input("enter the hotel name")
sapadu=input("enter the sapadu for(mrg/after/ni8)")
if sapadu=="mrg":
    item=input("item: ")
    qty=int(input("qty: "))
    if item=="idly":
        print("idly =$20")
        print("total=",qty*20)
    elif item=="dosa":
        print("idly=$40")
        print("total=",qty*40)
elif sapadu=="after":
    item=input("item: ")
    qty=int(input("qty: "))
    if item=="meals":
        print("meals=$100")
        print("total=",qty*100)
    elif item=="biryani":
        print("biryani=$200")
        print("total=",qty*200)
elif sapadu=="ni8":
    item=input("item: ")
    qty=int(input("qty: "))
    if item=="shawarma":
        print("shawarma=$150")
        print("total=",qty*150)
    elif item=="porotta":
        print("parotta=$50")
        print("total=",qty*50)
        
    



































