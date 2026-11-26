import tkinter as tk
from random import *
import time
#######################################################################################################################test

def board(line,column,nr_mine):
    lst = []
    for k in range(column):
        ss_lst = []
        for i in range(line):
            ss_lst.append(0)
        lst.append(ss_lst)
    
    def place_mine(lst,nr_mine):
        lst = lst

        for j in range (nr_mine):
            print(f"place_mine_nr_mine = {nr_mine}")
            a = randint(0,column-1)
            b = randint(0,line-1)

            if lst[a][b] == 'MINE':
                while lst[a][b] == 'MINE':
                    a = randint(0,column-1)
                    b = randint(0,line-1)
            else:
                lst[a][b] = 'MINE'
        print(f"lst = {lst}")
        return lst

    lst = place_mine(lst,nr_mine)

    return lst

#board(2,3,2)

def final_board(line2,column2,nr_mine2):
    print(f'nr_mine2 = {nr_mine2}')
    
    lst = board(line2,column2,nr_mine2)
#    print(lst)

    for k in range (column2):
        for i in range(line2):
            if lst[k][i] != 'MINE':
                pass

            #coin
            if lst[k][i] == 'MINE':
                if k == 0 and i == 0 :#en haut a gauche
                    if lst[k][i+1] != 'MINE':
                        lst[k][i+1] += 1 

                    if lst[k+1][i] != 'MINE':
                        lst[k+1][i] += 1 

                    if lst[k+1][i+1] != 'MINE':
                        lst[k+1][i+1] += 1
                    pass
                    
                elif k == column2-1 and i == 0:#en bas a gauche
                    if lst[k-1][i] != 'MINE':
                        lst[k-1][i] += 1 

                    if lst[k-1][i+1] != 'MINE':
                        lst[k-1][i+1] += 1

                    if lst[k][i+1] != 'MINE':
                        lst[k][i+1] += 1 
                    pass
    
                elif k == 0 and i == line2-1:#en haut a droite
                    if lst[k][i-1] != 'MINE':
                        lst[k][i-1] += 1 

                    if lst[k+1][i-1] != 'MINE':
                        lst[k+1][i-1] += 1

                    if lst[k+1][i] != 'MINE':
                        lst[k+1][i] += 1  
                        pass
    
                elif k == column2-1 and i == line2-1:#en bas a droite
                    if lst[k-1][i-1] != 'MINE':
                        lst[k-1][i-1] += 1

                    if lst[k-1][i] != 'MINE':
                        lst[k-1][i] += 1 

                    if lst[k][i-1] != 'MINE':
                        lst[k][i-1] += 1 
                        pass
    
                #bordure
    
                elif (k == 0 and i != 0) and (k == 0 and i != line2-1 ):#ligne haut
                    if lst[k][i-1] != 'MINE':
                        lst[k][i-1] += 1

                    if lst[k][i+1] != 'MINE':
                        lst[k][i+1] += 1  

                    if lst[k+1][i-1] != 'MINE':
                        lst[k+1][i-1] += 1

                    if lst[k+1][i] != 'MINE':
                        lst[k+1][i] += 1  

                    if lst[k+1][i+1] != 'MINE':
                        lst[k+1][i+1] += 1
    
                elif (k != 0 and i == 0) and (k != column2-1 and i == 0 ):#colonne gauche
                    if lst[k-1][i] != 'MINE':
                        lst[k-1][i] += 1

                    if lst[k+1][i] != 'MINE':
                        lst[k+1][i] += 1  

                    if lst[k-1][i+1] != 'MINE':
                        lst[k-1][i+1] += 1

                    if lst[k][i+1] != 'MINE':
                        lst[k][i+1] += 1 

                    if lst[k+1][i+1] != 'MINE':
                        lst[k+1][i+1] += 1
    
                elif (k != 0 and i == line2-1) and (k != column2-1 and i == line2-1 ):#colonne droite
                    if lst[k-1][i] != 'MINE':
                        lst[k-1][i] += 1

                    if lst[k+1][i] != 'MINE':
                        lst[k+1][i] += 1 

                    if lst[k-1][i-1] != 'MINE':
                        lst[k-1][i-1] += 1

                    if lst[k][i-1] != 'MINE':
                        lst[k][i-1] += 1 

                    if lst[k+1][i-1] != 'MINE':
                        lst[k+1][i-1] += 1
    
                elif (k == column2-1 and i != 0) and (k == column2-1 and i != line2-1 ):#ligne bas
                    if lst[k][i-1] != 'MINE':
                        lst[k][i-1] += 1

                    if lst[k][i+1] != 'MINE':
                        lst[k][i+1] += 1 

                    if lst[k-1][i-1] != 'MINE':
                        lst[k-1][i-1] += 1

                    if lst[k-1][i] != 'MINE':
                        lst[k-1][i] += 1 

                    if lst[k-1][i+1] != 'MINE':
                        lst[k-1][i+1] += 1
    
                else :#autre
                    if lst[k-1][i-1] != 'MINE':
                        lst[k-1][i-1] += 1

                    if lst[k-1][i] != 'MINE':
                        lst[k-1][i] += 1 

                    if lst[k-1][i+1] != 'MINE':
                        lst[k-1][i+1] += 1

                    if lst[k][i-1] != 'MINE':
                        lst[k][i-1] += 1 

                    if lst[k][i+1] != 'MINE':
                        lst[k][i+1] += 1 

                    if lst[k+1][i-1] != 'MINE':
                        lst[k+1][i-1] += 1

                    if lst[k+1][i] != 'MINE':
                        lst[k+1][i] += 1  

                    if lst[k+1][i+1] != 'MINE':
                        lst[k+1][i+1] += 1

#    print(" ")
#    for elem in lst:
#        print(elem)
#
    return lst

#final_board(5,4,3)



def demineur():
    window = tk.Tk()
    window.geometry("2000x1000")
    window.title('DEMINEUR')

    title = tk.Label(text = "Demineur", font = ("bold", 30), bg = 'grey')
    title.place(x = 1000, y = 25)

#______________________________________________________________________________________________________________________________________________________
# Setting up of the chronometer:

    seconde = 0
    minute = 0
    heure = 0
    state = 1
    
    def chrono(seconde, minute, heure):
        nonlocal state

        chrono_frame = tk.Frame(window, width = 100, height = 100)
#        chrono_frame.propagate(False)
        chrono_frame.place(x = 1565,y = 200)
            
        time_label = tk.Label(chrono_frame, text = f"0{heure} : 0{minute} : 0{seconde}", font = ("BOLD", 33))
        time_label.pack()
    
        def stop_action():
            nonlocal state
            nonlocal seconde
    
            if state == 1:
                state = 0
                print(f"state = {state}")
                return
            
            elif state == 0:
                state = 1
                print(f"state = {state}")
                return

        chrono_button  = tk.Button(chrono_frame, text = "STOP/START", command = stop_action, width = 20, height = 2)
        chrono_button.pack()
    
        if state == 1:
    
            if seconde == 60:
                minute += 1
                seconde = 0
    
            if minute == 60:
                heure += 1
                minute = 0
    
            seconde += 1
#           print(state)
            seconde_letter = seconde
            minute_letter = minute
            heure_letter = heure
    
            if seconde < 10:
                seconde_letter = f"0{seconde}"
    
            if minute < 10:
                minute_letter = f"0{minute}"
    
            if heure < 10:
                heure_letter = f"0{heure}"
    
            time_label.config(text = f"{heure_letter} : {minute_letter} : {seconde_letter}")
            window.after(1000, chrono, seconde, minute, heure)
    
        if state == 0:

            window.after(1000, chrono, seconde, minute, heure)
#           print(0)
#______________________________________________________________________________________________________________________________________________________

    nb_mine = 0
    nb_line = 0
    nb_column = 0

    def action_nb_mine():
        nonlocal nb_mine
        nb_mine = int(entry_mine.get())
        print(f'nb_mine : int(entry_mine.get()) = {nb_mine}')
        button_nb_mine.destroy()
        print(f"nb_mine = {nb_mine}")
        print(f"nb_mine = {type(nb_mine)}")
    
    def action_nb_line():
        nonlocal nb_line
        nb_line = int(entry_nb_line.get())
        print(f"entry_nb_line = {nb_line}")
        button_nb_line.destroy()
        print(f"nb_line = {nb_line}")
        print(f"nb_line = {type(nb_line)}")
#       print(f"sizex = {float((int((1241/nb_line)/10))*10)}")

    def action_nb_column():
        nonlocal nb_column
        nb_column = int(entry_nb_column.get())
        print(f"entry_nb_column = {nb_column}")
        button_nb_column.destroy()
        print(f"nb_column = {nb_column}")
        print(f"nb_column = {type(nb_column)}")
#       print(f"sizey = {float((int((791/nb_column)/10))*10)}")

#_______________________________________________________________________________________________________________________________________________________________
    def action_start():
        nonlocal nb_line, nb_column, nb_mine
        entry_mine.destroy()
        entry_nb_line.destroy()
        entry_nb_column.destroy()
        button_nb_mine.destroy()
        button_nb_line.destroy()
        button_nb_column.destroy()
        button_start.destroy()
#_______________________________________________________________________________________________________________________________________________________________
        button_board(nb_line, nb_column, nb_mine)
        chrono(seconde, minute, heure)
#_______________________________________________________________________________________________________________________________________________________________
        


    entry_mine = tk.Entry(window, width = 27, font = ("bold", 33) )
    entry_mine.place(x = 700 , y = 350)

    button_nb_mine = tk.Button(window, text = 'nb_mine', command = action_nb_mine, width = 10 , height = 3)
    button_nb_mine.place(x = 1350 , y = 350)

    entry_nb_line = tk.Entry(window, width = 27, font = ("bold", 33) )
    entry_nb_line.place(x = 700 , y = 450)

    button_nb_line = tk.Button(window, text = 'nb_line', command = action_nb_line, width = 10 , height = 3)
    button_nb_line.place(x = 1350 , y = 450)

    entry_nb_column = tk.Entry(window, width = 27, font = ("bold", 33) )
    entry_nb_column.place(x = 700 , y = 550)

    button_nb_column = tk.Button(window, text = 'nb_column', command =  action_nb_column, width = 10 , height = 3)
    button_nb_column.place(x = 1350 , y = 550)

    button_start = tk.Button(window, text = 'START', font = ('BOLD',50), command = action_start)
    button_start.place(x = 900, y = 700)



    def button_board(line,column,mine):
        line = line
        column = column

        game_back = tk.Frame(bg = 'grey',width = 1250,height = 800)
        game_back.propagate(True)
        game_back.place(x= 72 ,y =123)


        lst = []

        print(f" line_type = {type(line)}")
        print(f" column_type = {type(column)} ")

        sizex = int(1241/float(column))
        print(f"sizex = {sizex}")
        sizey = int(791/float(line))
        print(f"sizey = {sizey}")

        back_board = final_board(line,column,mine)

        def action(nnn,value):
            if value == 'MINE' :        
                nnn.config(text = value, bg = "red")

            if value == 0 :        
                nnn.config(text = " ", bg = "white")

            if value == 1 :        
                nnn.config(text = value, bg = "grey")

            if value == 2 :        
                nnn.config(text = value, bg = "yellow")

            if value == 3 :        
                nnn.config(text = value, bg = "orange")

            if value == 4 :        
                nnn.config(text = value, bg = "orange")

            if value == 5 :        
                nnn.config(text = value, bg = "green")

            if value == 6 :        
                nnn.config(text = value, bg = "green")

            if value == 7 :        
                nnn.config(text = value, bg = "pink")

            if value == 8 :        
                nnn.config(text = value, bg = "pink") 

            if value == 9 :        
                nnn.config(text = value, bg = "purple")
        
        for i in range(column):
            ss_lst = []
            for k in range(line):
            
                bb = back_board[i][k]

                case = tk.Button(window, text = " ")

                case.config( command = lambda case = case, bb = bb : action(case,bb) )

                case.place(x = 77+i*(1+sizex) , y = 127+k*(1+sizey), width = sizex, height = sizey)
            
                ss_lst.append(case)
            lst.append(ss_lst)
        return lst
        

    window.mainloop()
    

demineur()