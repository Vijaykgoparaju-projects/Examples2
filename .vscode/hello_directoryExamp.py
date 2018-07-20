def takes_list(a_list):
#dictcount=len(a_list)
    for item in a_list:
        print(item,'corresponding to',a_list[item])
    #takeinput=input("enter your name\n")
    print(a_list)

mylist={"firstname": "apple","lastname": "goparaju","fruit":"banana"}
takes_list(mylist)