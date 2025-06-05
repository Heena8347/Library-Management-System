#%%
def addbook(new_book):
    with open("J:/aimicrodeegree/HEENA/Module 2 python/project1/totalbooks.txt","a+") as l:
        l.write(new_book+"\n")
        
def viewbook():
    with open("J:/aimicrodeegree/HEENA/Module 2 python/project1/totalbooks.txt","r") as l:
        print(l.read())

def borrowbook(rent_book):
    rent_book1=rent_book+"\n"
    with open("J:/aimicrodeegree/HEENA/Module 2 python/project1/totalbooks.txt","r") as l:
        list1=l.readlines()
        if rent_book1 in list1:
            list1.remove(rent_book1)
            with open("J:/aimicrodeegree/HEENA/Module 2 python/project1/rent.txt","a") as l:
              l.write(rent_book1)
        else:
            print("book is not available")

    with open("J:/aimicrodeegree/HEENA/Module 2 python/project1/totalbooks.txt","w") as l:
            l.writelines(list1)

def returnbook(return_b):
    return_book1=return_b+"\n"
    with open("J:/aimicrodeegree/HEENA/Module 2 python/project1/rent.txt","r") as l:
        list1=l.readlines()
        if return_book1 in list1:
            list1.remove(return_book1)
            with open("J:/aimicrodeegree/HEENA/Module 2 python/project1/totalbooks.txt","a") as l:
              l.write(return_book1)
        else:
            print("book is not available")

    with open("J:/aimicrodeegree/HEENA/Module 2 python/project1/rent.txt","w") as l:
            l.writelines(list1)

    
       
    
   

