A="=============Library============="
print(A.center(30))
book=input("enter the name of book : ")
booksection={"section-A":200 ,"section-B":200,"section-C": 200,"section-D":200}
type=input("enter the book condition for eg.hardcover or softcover: ")
price={
     "section A": 100,
     "section B": 200,
     "section C": 300,
     "section D": 400,
}
if book.startswith(("a","b","c","d","e")):
     if type in ("hardcover","softcover"):
            print("the price of ",book,type,"is ,", price["section A"] ,"rupees")
            print("section A","|","books available",booksection["section-A"])
     else:
         print("no book available")
elif book.startswith(("f","g","h","i","j")):     
     if type in ("hardcover","softcover"):
         print(("the price of ",book,type,"is ,", price["section B"],"rupees"))
         print("section B |","books available",booksection["section-B"])
     else:
         print("book not available")
elif book.startswith(("k","l","m","n","o","p")):
     if type in ("hardcover","softcover"):
         print("the price of ",book,type,"is ,", price["section C"] ,"rupees")
         print("section C | ","books available",booksection["section-C"])
     else:
         print("book not available !")
elif book.startswith(("q","r","s","t","u","x","y","z")):
    if type in ("hardcover","softcover"):
         print("the price of ",book,type,"is ,", price["section D"],"rupees")
         print("section D |","books available",booksection["section-D"])
    else:
        print("book not available")
