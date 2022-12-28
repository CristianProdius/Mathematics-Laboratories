def truthTable(expression,inputs=10):
  print("Boolean Expression:")
  print("  E = " + expression.upper())
  expression = expression.lower()
  
  expression = expression.replace("+","|")
  expression = expression.replace("*","&")
  expression = expression.replace("!","~")
  
  print("\nTruth Table:")
  if inputs==2:
    print("  -------------")
    print("  | K | X | E |")
    print("  -------------")
    
    for k in range(0,2):
      for x in range(0,2):
        e = eval(expression)
        print("  | " + str(k) + " | " + str(x) + " | " + str(e) + " |" )
        print("  -------------")
        
  elif inputs==3:
    print("  -----------------")
    print("  | K | X | Y | E |")
    print("  -----------------")
    
    for k in range(0,2):
      for x in range(0,2):
        for y in range(0,2):
          e = eval(expression)
          print("  | " + str(k) + " | " + str(x) + " | " + str(y) + " | " + str(e) + " |")
          print("  -----------------")
    
  elif inputs==4:
    print("  ---------------------")
    print("  | K | X | Y | Z | E |")
    print("  ---------------------")
    
    for k in range(0,2):
      for x in range(0,2):
        for y in range(0,2):
          for z in range(0,2):
            e = eval(expression)
            print("  | " + str(k) + " | " + str(x) + " | " + str(y) + " | " + str(z) + " | " + str(e) + " |" )
            print("  ---------------------")
  
  elif inputs==5:
    print("  -------------------------")
    print("  | K | X | Y | Z | W | E |")
    print("  -------------------------")
    
    for k in range(0,2):
      for x in range(0,2):
        for y in range(0,2):
          for z in range(0,2):
            for w in range(0,2):
              e = eval(expression)
              print("  | " + str(k) + " | " + str(x) + " | " + str(y) + " | " + str(z) + " | " + str(w) + " |" +str(e) + "|")
              print("  ---------------------")
            

expression = "(!X+Y)*Z+(!Z*Y*K)"
truthTable(expression,4)