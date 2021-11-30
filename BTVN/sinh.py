import string
ABC = list(string.ascii_uppercase)

def creat(n):
    table_data = []
    for i in range(n):
        row = [ABC[i]]
        for j in range(n):
            row.append(0)
        table_data.append(row)
    return(table_data)

table = creat(10)

def show(table):
    class caro:
        def __init__(self,name,value):
            self.name = name
            self.value = value

        def show_game(self):
            print(f"{self.name} | {self.value}")
        
    for i in range(len(table)):
        a = caro(table[i][0],table[i][1:])
        a.show_game()
    print("\n")

'''
tạm check 4 nc thắng hàng là thắng, ko tính chặn
'''

def check_ngang(table):
    for i in range(len(table)):
        for j in range(i,len(table[i])-3):
            if table[i][j] == 1:
                if table[i][j+1] == 1 and table[i][j+2] == 1 and table[i][j+3] == 1: 
                    print("1 Thắng")
                    break
            elif table[i][j] == 2:
                 if table[i][j+1] == 2 and table[i][j+2] == 12 and table[i][j+3] == 2:
                    print("2 Thắng")
                    break
def check_doc(table):
     for i in range(len(table)-3):
        for j in range(i,len(table[i])):
            if table[i][j] == 1:
                if table[i+1][j] == 1 and table[i+2][j] == 1 and table[i+3][j] == 1: 
                    print("1 Thắng")
                    break
            elif table[i][j] == 2:
                 if table[i+1][j] == 2 and table[i+2][j] == 12 and table[i+3][j] == 2:
                    print("2 Thắng")
                    break
def check_cheo(table):
    for i in range(len(table)-3):
        print (len(table[i]))
        for j in range(i,len(table[i])-3):
        
            if table[i][j] == 1:
                if table[i+1][j+1] == 1 and table[i+2][j+2] == 1 and table[i+3][j+3] == 1: 
                    print("1 Thắng")
                    break
            elif table[i][j] == 2:
                 if table[i+1][j+1] == 2 and table[i+2][j+2] == 12 and table[i+3][j+3] == 2:
                    print("2 Thắng")
                    break
def play(player,row,column):
    for i in range(len(table)):
        if table[i][0] == row:
            if table[i][column] == 0:
                table[i][column] = player
    show(table)
    check_ngang(table)
    check_doc(table)
    check_cheo(table)

play(1,'A',1)
play(2,'B',3)
play(1,'A',2)
play(2,'B',4)
play(1,'A',3)
play(2,'B',5)
play(1,'A',4)


