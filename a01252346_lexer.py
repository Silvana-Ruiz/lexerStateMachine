class Lexer:
  def __init__(self):
    self.state = 'q0'
    self.letString = ''
    self.operators = ['+', '-', '*', '/']

  def checkExpression(self, lines):
    print(lines)
    for line in lines:
      print(line)

      for c in line:
        print(c, '---- state entrante', self.state)

        # Ignore newlines unless they are used to separate let from the variable name (example: let
        #                                                                                       num=3;)
        if c.isspace() and c == '\n' and self.state != 'q1':
          continue

        if self.state == 'q11' and c != ' ': # Only stay in q11 if the char is a space
          self.state = 'q0' # Allows us to check for new expressions

        match self.state:
          case 'q0':
            validTransition =  self.q0CheckTransitions(c)
            if not validTransition:
              return False
            
          case 'q1':
            validTransition =  self.q1CheckTransitions(c)
            if not validTransition:
              return False
          
          case 'q2':
            validTransition =  self.q2CheckTransitions(c)
            if not validTransition:
              return False
          
          case 'q3':
            validTransition =  self.q3CheckTransitions(c)
            if not validTransition:
              return False
                    
          case 'q4':
            validTransition =  self.q4CheckTransitions(c)
            if not validTransition:
              return False
            
          case 'q5':
            validTransition =  self.q5CheckTransitions(c)
            if not validTransition:
              return False  
          
          case 'q6':
            validTransition =  self.q6CheckTransitions(c)
            if not validTransition:
              return False  
            
          case 'q7':
            validTransition =  self.q7CheckTransitions(c)
            if not validTransition:
              return False  

          case 'q8':
            validTransition =  self.q8CheckTransitions(c)
            if not validTransition:
              return False  
            
          case 'q9':
            validTransition =  self.q9CheckTransitions(c)
            if not validTransition:
              return False  
            
          case 'q10':
            validTransition =  self.q10CheckTransitions(c)
            if not validTransition:
              return False  
  
    print('Final state:', self.state)

    # Check if we are at the final state
    return self.state == 'q11'

  def q0CheckTransitions(self, c):
    # Verifying spaces 
    if not self.letString and c == ' ':
      return True
    elif self.letString and c == ' ': # Space between the let word
      self.letString = ''
      return False

    # Check for let keyword
    elif not self.letString and c == 'l':
      self.letString += c
    elif self.letString == 'l' and c == 'e':
      self.letString += c
    elif self.letString == 'le' and c == 't':
      self.letString += c
      self.state = 'q1'
    else:
      self.letString = ''
      return False
    return True
  
  def q1CheckTransitions(self, c):
    if (c.isspace() and c == '\n') or c == ' ':
      self.letString = ''
      self.state = 'q2'
    else:
      return False
    return True
          
  def q2CheckTransitions(self, c):
    if c.isalpha(): # Variable name must start with an alphabetic char
      self.state = 'q3'
    elif c != ' ': # Skipping spaces
      return False
    return True
    
  def q3CheckTransitions(self, c):
    if c == ' ':
      self.state = 'q4'
    elif c == '=':
      self.state = 'q5'
    elif not c.isalnum(): # Variable name can have letters and numbers
      return False
    return True
  
  def q4CheckTransitions(self, c):
    if c == '=':
      self.state = 'q5'
    elif c != ' ': # Spaces before '='
      return False
    return True
    
  def q5CheckTransitions(self, c): 
    if c.isdigit():
      self.state ='q6'
    elif c != ' ': # Spaces after '='
      return False
    return True
    
  def q6CheckTransitions(self, c):
    if c == '.':
      self.state = 'q7'
    elif c == ' ':
      self.state = 'q10'
    elif c in self.operators:
      self.state = 'q9'
    elif c == ';':
      self.state = 'q11'
    elif not c.isdigit():
      return False
    return True
    
  def q7CheckTransitions(self, c):
    if c.isdigit():
      self.state = 'q8' 
    else:
      return False
    return True
    
  def q8CheckTransitions(self, c):
    if c in self.operators:
      self.state = 'q9'
    elif c == ' ':
      self.state = 'q10'
    elif c == ';':
      self.state = 'q11'
    elif not c.isdigit():
      return False
    return True
    
  def q9CheckTransitions(self, c):
    if c == ' ':
      self.state = 'q5'
    elif c.isdigit():
      self.state = 'q6'
    else:
      return False
    return True
    
               
  def q10CheckTransitions(self, c):
    if c in self.operators:
      self.state = 'q9'
    elif c == ';':
      self.state = 'q11'
    elif c != ' ':
      return False
    return True
               
        
              
def main(): 
  file = open("input.txt", "r");
  lines = file.readlines()
  lexer = Lexer()

  print(lexer.checkExpression(lines))
  file.close()

main()
