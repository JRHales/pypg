from tkinter import *
import genclasses

def main():
  WINDOWSIZE = '600x400'
  window = TK()
  window.title("pypg")
  window.geometry(WINDOWSIZE)
  print("Begun") #Does it even start
  lbl = Label(window, text="hello", font=("Arial Bold", 50))
  lbl.grid(column=0, row=0)
  player1 = genclasses.Player("Test Player") #Player name is set to test Player. Make actual name input.
  print(player1.getName()) 
  
  window.mainloop()
  

main()
