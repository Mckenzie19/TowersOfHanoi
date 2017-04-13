#Towers of Hanoi

'''
This program has two main features:
    -A computer run class that will have the computer play the
     Towers of Hanoi game and return how many moves it made
    -A user run class that uses tkinter to interact with the user, allowing
     them to play the game for themselves through text
'''

from htDisk import Disk
from htPeg import Peg
import tkinter as tk
from tkinter import *


class computerGame(object):

    def __init__(self):

        keepgoing=True
        while keepgoing==True:
            #Initializes the pegs and disks to be used
            self.pegs, self.num_disks, self.disks=self.hTowers()
            
            #Displays starting layout in text form
            print('Starting disk layout: ')
            for a in range(3):
                print('Peg'+str(a+1), self.pegs[a].getDiskList())
                
            #Computer goes through all moves
            self.pegs, self.moves=self.autoMoves(self.num_disks, self.pegs, 1, 3, 2, 0)

            #Displays the final layout in text form
            print('Final disk layout: ')
            for a in range(3):
                print('Peg'+str(a+1), self.pegs[a].getDiskList())

            #Displays the total number of moves the computer made
            print("Total number of moves made: ", self.moves)

            #Allows the user to play the game again if they so choose
            choice=input('Play again? ')

            if choice in ('y', 'Y'):
                keepgoing=True
            else:
                keepgoing=False  

    
    def hTowers(self):

        #Sets how many disks the user wants to work with 
        num_disks=int(input("Please input the number of disks: "))
        #Creates Disk objects in a list
        disks=[Disk(1,i+1) for i in range(num_disks)]
        #Assigns disks to peg objects
        pegs=[Peg(i,diskList=[disks[a] for a in range(num_disks) if disks[a].getCurrentPeg()==i]) for i in range(1,4)]

        return pegs, num_disks, disks


    def autoMoves(self, pegsLen, pegs, cPeg, goal, alt, moves):    

        if pegsLen>0:

            #Move all disks to the alternate peg except for the largest disk
            pegs, moves=self.autoMoves(pegsLen-1, pegs, cPeg, alt, goal, moves)
            
            moves+=1

            #Displays to the user what the computer is currently doing
            x=pegs[cPeg-1].getDiskList()
            print("Moving", x[0], "from", pegs[cPeg-1], "to", pegs[goal-1])
            
            #Move the largest disk to the the goal peg
            pegs[goal-1].addDisk(pegs[cPeg-1].moveDisk())
            
            #Move all other disks to the goal peg
            pegs, moves=self.autoMoves(pegsLen-1, pegs, alt, goal, cPeg, moves)
        
        return pegs, moves
       

class userGame(object):

    def __init__(self):

        #Initializes the pegs and disks to be used
        pegs, num_disks, disks=self.hTowers()
        self.pegs=pegs
        self.num_disks=num_disks
        self.disks=disks
        self.move=0

        #Makes sure no pegs or disks are currently choosen
        self.choosenDisk=0
        self.choosenPeg=0

        #Sets the main window with which the user will interact with the most
        self.root=tk.Tk()
        self.root.title("Towers of Hanoi")

        #Sets the frames for the main window and places them in the grid
        self.content=tk.Frame(self.root)
        self.content.grid(column=0, row=0)
        self.frame=tk.Frame(self.content, borderwidth=5, relief="sunken", width=200, height=100)
        self.frame.grid(column=0, row=0)

        #Creates disk button column header
        self.l1=tk.Label(self.frame, text="Choose which disk to move: ")
        self.l1.grid(column=1, row=1, sticky=W)

        #This loop creates the disk buttons, implementing specific commands for each one
        self.diskList=[]
        for a in range(self.num_disks):
            self.diskList.append(Button(self.frame, text="Disk "+str(a+1), command=lambda a=a: self.chooseDisk(a)))
            self.diskList[a].grid(column=1, row=a+2, sticky=W)

        #Creates the peg column header
        self.l2=tk.Label(self.frame, text="Choose which peg to move the disk to: ")
        self.l2.grid(column=2, row=1, sticky=W)

        #This loop creates the three peg buttons, giving each a corresponding command
        self.pegEndList=[]
        for j in range(3):
            self.pegEndList.append(Button(self.frame, text="Peg "+str(j+1), command= lambda j=j: self.choosePeg(j)))
            self.pegEndList[j].grid(column=2, row=j+2, sticky=W)

        #This next chunck of code sets up the text box that the user will be getting their data for the game from
        self.output=tk.Listbox(self.frame, width=30)
        self.output_scrollbar=tk.Scrollbar(self.frame) #This scrollbar will make sure that the user always sees the most recent data
        self.output.grid(column=3, row=1, rowspan=6, sticky=E)
        self.layout()
        self.output.configure(yscrollcommand=self.output_scrollbar.set) #Sets up the scrollbar commands
        self.output_scrollbar.configure(command=self.output.yview)

        #This sets up the main window dimensions
        self.sw=self.root.winfo_screenwidth()
        self.sh=self.root.winfo_screenheight()
        self.rootsize=tuple(int(_) for _ in self.root.geometry().split('+')[0].split('x'))
        self.x=(self.sw/2)-(self.rootsize[0]/2)
        self.y=(self.sh/2)-(self.rootsize[1]/2)

        self.root.geometry('+%d+%d' % (self.rootsize[0]+self.x, self.rootsize[1]+self.y))
                
        self.root.mainloop()


    #Sets up the peg and disk objects for the game
    def hTowers(self):

        #Sets how many disks the user wants to work with 
        num_disks=int(input("Please input the number of disks: "))
        #Creates Disk objects in a list
        disks=[Disk(1,i+1) for i in range(num_disks)]
        #Assigns disks to peg objects
        pegs=[Peg(i,diskList=[disks[a] for a in range(num_disks) if disks[a].getCurrentPeg()==i]) for i in range(1,4)]

        return pegs, num_disks, disks


    #This is the command that the disk buttons will call
    def chooseDisk(self, a):
        self.choosenDisk=(a+1) #Saves the choosen disk number

        #Checks if the user has already selected a peg button
        if self.choosenPeg!=0: #If yes, then game moves disk from current peg to selected peg
            self.output.insert(END, "Moving Disk "+str(self.choosenDisk)+" to Peg "+str(self.choosenPeg))
            pegNum=self.disks[self.choosenDisk-1].getCurrentPeg() #Gets the peg number that the disk is currently on
            pegList=self.pegs[pegNum-1].getDiskList()
            if(pegList[0]==self.disks[self.choosenDisk-1]): #Makes sure that the user is not trying to move a disk that has another disk on top of it
                
                self.pegs[self.choosenPeg-1].addDisk(self.pegs[pegNum-1].moveDisk()) #Moves the disk and updates both disk and peg objects
                self.layout() #Creates user output
                self.move+=1 
                self.output.insert(END, "Number of moves made: "+str(self.move)) #Reports to the user how many moves they have made so far

                #This moves the scrollbar down for the user
                self.output.select_clear(self.output.size()-2)
                self.output.select_set(END)
                self.output.yview(END)

                #Checks if the user has won the game now
                win=self.checkWin()
                if win==True:
                    self.winProcedure(self.root) 
                else:
                    self.choosenDisk=0
                    self.choosenPeg=0

            #Reports to the user that they were unable to move the selected disk
            else:
                self.output.insert(END, "Disk "+str(self.choosenDisk)+" is currently blocked.")
                self.output.insert(END, "Please choose a different disk.")
                self.output.select_clear(self.output.size()-2)
                self.output.select_set(END)
                self.output.yview(END)
                
                self.choosenDisk=0
                self.choosenPeg=0

    #This is the command run when a peg button is clicked
    def choosePeg(self, i):
        self.choosenPeg=(i+1) #Saves the peg number
        
        if self.choosenDisk!=0: #Checks if the user has already selected a disk button
            self.output.insert(END, "Moving Disk "+str(self.choosenDisk)+" to Peg "+str(self.choosenPeg))
            pegNum=self.disks[self.choosenDisk-1].getCurrentPeg() #Gets the peg that the choosen disk is currently on
            pegList=self.pegs[pegNum-1].getDiskList()
            if(pegList[0]==self.disks[self.choosenDisk-1]): #Checks that the disk object being moved is not blocked by another disk

                #Moves the choosen disk to the selected peg and updates both objects
                self.pegs[self.choosenPeg-1].addDisk(self.pegs[pegNum-1].moveDisk())
                self.layout() #Gets output for the user
                self.move+=1
                self.output.insert(END, "Number of moves made: "+str(self.move)) #Informs user how many moves they have made

                #Moves the scrollbar to the end of the listbox for the user
                self.output.select_clear(self.output.size()-2)
                self.output.select_set(END)
                self.output.yview(END)

                #Checks if the user has won the game yet
                win=self.checkWin()
                if win==True:
                    self.winProcedure(self.root) 
                else:
                    self.choosenDisk=0
                    self.choosenPeg=0

            #Reports to the user that they were unable to move the selected disk
            else:
                self.output.insert(END, "Disk "+str(self.choosenDisk)+" is currently blocked.")
                self.output.insert(END, "Please choose a different disk.")
                self.output.select_clear(self.output.size()-2)
                self.output.select_set(END)
                self.output.yview(END)
                
                self.choosenDisk=0
                self.choosenPeg=0


    #This function will show the user what the layout of disks is currently
    def layout(self):
        
        self.output.insert(END, "The current layout of disks is: ")
        for a in range(3):
                self.output.insert(END, 'Peg'+str(a+1)+' '+str(self.pegs[a].getDiskList()))


    #This function checks if the user has all of the disks in the correct layout
    def checkWin(self):

        #Checks if the first two pegs are empty of disks
        if (self.pegs[0].getNumDisks()!=0) or (self.pegs[1].getNumDisks()!=0):
            return False

        #Checks if the disks are arranged with the largest at the bottom and the smallest at the top
        diskList=self.pegs[2].getDiskList()
        for a in range(0, self.num_disks-1):
            if diskList[a].getSize()>diskList[a+1].getSize():
                return False

        return True

    #Once the user has won the game, a new window is created informing them of this, and giving them two options
    #Either play again or end game
    def winProcedure(self, master):

        self.winRoot=tk.Toplevel(master) #Creates a new Top level window which with the user will interact
        self.winRoot.title("You Win!")

        #Creates the frame for the window
        self.winFrame=tk.Frame(self.winRoot, borderwidth=5, relief="sunken", width=200, height=100)
        self.winFrame.grid(row=0, column=0)

        #Sets up a message for the user, and questions what they want to do next
        self.winLb=tk.Label(self.winFrame, text="You win! You made "+str(self.move)+" moves. \n Play again?")
        self.winLb.grid(column=0, columnspan=2, row=1)

        #Creates buttons that the user can use to either play another game, or end the game completely
        self.yes=tk.Button(self.winFrame, text="Play Again", command=self.playAgain)
        self.yes.grid(column=0, row=2, rowspan=2)
        self.no=tk.Button(self.winFrame, text="Exit Game", command=self.exitGame)
        self.no.grid(column=1, row=2, rowspan=2)

        #Sets up some of the windows sizing
        self.Wsw=self.winRoot.winfo_screenwidth()
        self.Wsh=self.winRoot.winfo_screenheight()
        self.Wrootsize=tuple(int(_) for _ in self.winRoot.geometry().split('+')[0].split('x'))
        self.Wx=(self.Wsw/2)-(self.Wrootsize[0]/2)
        self.Wy=(self.Wsh/2)-(self.Wrootsize[1]/2)
        self.winRoot.geometry('+%d+%d' % (self.Wrootsize[0]+self.Wx, self.Wrootsize[1]+self.Wy))

    #Creates a new userGame() object, causing the game to be played again
    def playAgain(self):

        self.winRoot.destroy()
        self.root.destroy()

        b=userGame()

    #Destroys the main windows, effectively ending the game
    def exitGame(self):

        self.winRoot.destroy()
        self.root.destroy()
        
        
