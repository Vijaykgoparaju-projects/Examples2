def takes_list(a_list,lookFor):
    myindex=a_list.index(lookFor)
    while myindex>=0:
        a_list.remove(lookFor)
        #print(a_list)
        try:
            myindex=a_list.index(lookFor)
            print("next instance found at:- ",str(myindex))
        except ValueError:
            print("All matching values in the list are deleted, thanks\n",a_list)
            remove_AllMatchValuesFromList(a_list)


def remove_AllMatchValuesFromList(mylist):
    
    mylist_totalcount=len(mylist)
    if(mylist_totalcount>0):
        lookFor=input("enter you want to look up in list:-\n")
        mylist_count=mylist.count(lookFor)
        print(lookFor,"appeared for:- ",str(mylist_count)," number of times in list")
    else:
        print("There are no items in the list\n",mylist)
        exit()
    mylist.sort()
    print(mylist)
    try:
        myindex=mylist.index(lookFor)
        takes_list(mylist,lookFor)
    except ValueError:
        print("There is no matching value, please try again")
        remove_AllMatchValuesFromList(mylist)



class MyBigList:
    def __init__(self, mylist):
        self.myNewList=mylist
        remove_AllMatchValuesFromList(self.myNewList)

mylist=["vijay","mahesh","banana","vijay","uday","vijay"]
BigList=MyBigList(mylist)
    