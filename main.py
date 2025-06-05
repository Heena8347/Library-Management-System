def main():
    import Lms as l
    a=int(input('''Enter your choice:
    1. add book
    2.view book
    3.borrow book
    4.return book  :--> '''))
    if a==1:
        b=input("Enter name of book for add-->")
        l.addbook(b)
        print('Successfully added.')
    elif a==2:
        l.viewbook()
    elif a==3:
        c=input("which book you want to borrow -->")
        l.borrowbook(c)
    elif a==4:
        d=input("which book you are returning? -->")
        l.returnbook(d)

__name__="__main__"
main()
