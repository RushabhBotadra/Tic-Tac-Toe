Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> board=[" "," "," "," "," "," "," "," "," "]
>>> 
>>> def create_board():
	print(board[0] + "|" +board[1] + "|" +board[2])
	print("-----------")
	print(board[3] + "|" +board[4] + "|" +board[5])
	print("-----------")
	print(board[6] + "|" +board[7] + "|" +board[8])
	print("-----------")

	
>>> def info():
	a=input("enter the name")
	a1=input("choose your symbol")
	b=input("enter the name")
	b1=input("choose your symbol")

>>> def chance_a():
    print("A's turn")
    choice=int(input("enter the location where u want to add"))
    if(board[choice]!== " "):
        print("game over!!")
    elif(board[choice]==" "):
        board[choice]='a1'
        return chance_b()
    else:
        print("sorry")
        return chance_a()
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> def chance_a():
    print("A's turn")
    choice=int(input("enter the location where u want to add"))
    if(board[choice]!=" "):
        print("game over!!")
    elif(board[choice]==" "):
        board[choice]='a1'
        return chance_b()
    else:
        print("sorry")
        return chance_a()

>>> def chance_a():
    print("A's turn")
    choice=int(input("enter the location where u want to add"))
    if(board[choice]!=):
        print("game over!!")
    elif(board[choice]==" "):
        board[choice]='a1'
        return chance_b()
    else:
        print("sorry")
        return chance_a()
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> def chance_b():
    print("B's turn")
    choice=int(input("enter the location where u want to add"))
    if(board[choice]!=" "):
        print("game over!!")
    elif(board[choice]==" "):
        board[choice]='b1'
        return chance_a()
    else:
        print("sorry")
        return chance_b()

>>> def play_game():
	chance_a()

	
>>> create_board()
 | | 
-----------
 | | 
-----------
 | | 
-----------
>>> info()
enter the namerushabh
choose your symbolX
enter the nameishita
choose your symbolY
>>> play_game()
A's turn
enter the location where u want to add0
B's turn
enter the location where u want to add4
A's turn
enter the location where u want to add2
B's turn
enter the location where u want to add1
A's turn
enter the location where u want to add7
B's turn
enter the location where u want to add5
A's turn
enter the location where u want to add3
B's turn
enter the location where u want to add6
A's turn
enter the location where u want to add8
B's turn
enter the location where u want to add2
game over!!
>>> def result():
	if(board[0]==board[4]==board[8]=='a1'):
		print("A WON")
	elif(board[0]==board[1]==board[2]=='a1'):
		print("A WON")
	elif(board[0]==board[3]==board[6]=='a1'):
		print("A WON")
	elif(board[1]==board[4]==board[7]=='a1'):
		print("A WON")
	elif(board[2]==board[5]==board[8]=='a1'):
		print("A WON")
	elif(board[3]==board[4]==board[5]=='a1'):
		print("A WON")
	elif(board[6]==board[7]==board[8]=='a1'):
		print("A WON")
	elif(board[0]==board[4]==board[8]=='b1'):
		print("B WON")
	elif(board[0]==board[1]==board[2]=='b1'):
		print("B WON")
	elif(board[0]==board[3]==board[6]=='b1'):
		print("B WON")
	elif(board[1]==board[4]==board[7]=='b1'):
		print("B WON")
	elif(board[2]==board[5]==board[8]=='b1'):
		print("B WON")
	elif(board[3]==board[4]==board[5]=='b1'):
		print("B WON")
	elif(board[6]==board[7]==board[8]=='b1'):
		print("B WON")
	else:
		print("MATCH TIE")

		
>>> result()
MATCH TIE
>>> 
