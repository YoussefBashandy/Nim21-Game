Nim21=21
while Nim21>1:
    P1=int(input("Enter a number from 1 to 3 P1: "))
    if P1>3:
        print("Error")
        P1=int(input("Enter a number from 1 to 3 P1: "))
        Rem1=Nim21 - P1
        print (Rem1)
    else:   
        Rem1=Nim21 - P1
        print (Rem1)
    if Rem1==1:
        print ("Player 1 wins")
    P2=int(input("Enter a number from 1 to 3 P2: "))
    if P2>3:
        print ("Error")
        P2=int(input("Enter a number from 1 to 3 P2: "))
        Nim21=Rem1 - P2
        print (Nim21)
    else:    
        Nim21=Rem1 - P2
        print (Nim21)
    if Nim21==1:
        print ("Player 2 wins")
