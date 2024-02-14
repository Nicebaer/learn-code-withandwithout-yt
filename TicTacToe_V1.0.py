#Das ist mein erster Code, der mithilfe von YT Tutorial durchgeführt wurde, kleines TicTacToe Spiel.
#Mithilfe von ChatGPT habe ich die Abfrage für "Unentschieden" eingebaut.
#YT- Tutorial:

'''
String -> Hallo / 123 / user123
Integer int -> 123, 5, 0, -1, -10
floats -> 1.0, 1.1, 1.2, 1.3, 1.4, 1.5
Boolean bool -> True / False
'''

'''
print("Positionen")
print("0", "|", "1", "|", "2")  
print("--|---|--")
print("3", "|", "4", "|", "5") 
print("--|---|--")
print("6", "|", "7", "|", "8")
print("Aktuelles Feld")
print_3x3(values)
'''

#check if the position is ok
def check_ok(values,wich_pos):
  if wich_pos < 0 or wich_pos > 8 :
    print("Benutze bitte 0-8")
    return False
  elif values[wich_pos] != " ":
    print("Das Gewählte  Feld ist besetzt!")
    return False

  else:
    return True
#ende

#Standart Beginn 3x3 Gitter
def print_3x3(values):
  
  print(values[0], "|", values[1], "|", values[2])  
  print("--|---|--")
  print(values[3], "|", values[4], "|", values[5]) 
  print("--|---|--")
  print(values[6], "|", values[7], "|", values[8])
#ende

#check if the game is over
def check_winner(values):
  if(values[0] == values[1] == values[2] != " "):
    return True
  elif(values[3] == values[4] == values[5] != " "):
    return True
  elif(values[6] == values[7] == values[8] != " "):
    return True
  elif(values[0] == values[3] == values[6] != " "):
    return True
  elif(values[1] == values[4] == values[7] != " "):
    return True
  elif(values[2] == values[5] == values[8] != " "):
    return True
  elif(values[0] == values[4] == values[8] != " "):
    return True
  elif(values[2] == values[4] == values[6] != " "):
    return True
  else:
    return False
#ende

def unentschieden_check(values):
  if values[0] != " " and values[1] != " " and values[2] != " " and values[3] != " " and values[4] != " " and values[5] != " " and values[6] != " " and values[7] != " " and values[8] != " ":
    return True

#Ein Spiel
def new_game():
  
  values = [" "] * 9

  #Game bis Sieg oder Unentschieden
  while True:
    print_3x3(values)
    
    #Spieler 1
    wich_pos = int(input("Spieler 1: Wo möchtest du dein X setzen[0-8]?"))
    
    while check_ok(values,wich_pos) == False :
      
      wich_pos = int(input("Spieler 1: Wo möchtest du dein X setzen[0-8]?"))
    values[wich_pos] = "X"
    print_3x3(values)
    
    #Check ob Win
    if check_winner(values) == True:
      print("Spieler 1 hat gewonnen!")
      break
    #Check auf Unentschieden
    if unentschieden_check(values):
      print("Unentschieden!")
      break
    
    #Spieler 2
    wich_pos = int(input("Spieler 2: Wo möchtest du dein O setzen[0-8]?"))
  
    while check_ok(values,wich_pos) == False :
  
      wich_pos = int(input("Spieler 2: Wo möchtest du dein O setzen[0-8]?"))
    values[wich_pos] = "O"
    
    #Check ob Win
    if check_winner(values) == True:
      print("Spieler 2 hat gewonnen!")
      break
    #Check auf Unentschieden
    if unentschieden_check(values):
      print("Unentschieden!")
      break
#ende
new_game()
#ende



