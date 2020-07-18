'''
File name: eqn.py
Homework #3
Problem #2
This file provides the necessary functions to solve a mathematic equation for x.
'''
def sameFormat(equation):
      '''
      This function coverts the equation inputted by the user to one consistent format. This function converts all letters to lowercase and deletes any spaces in the equation.
      This function has one input: equation
      This function has one output: equation
      '''
      equation = equation.lower()
      equation = equation.replace(' ','')
      
      return equation

def subtraction(equation):
      '''
      This function calculates the value of x if the inputted equation is a subtraction equation (includes a - sign in the equation).
      This function has one input: equation
      This function has one output: subtraction
      '''
      for i in range(len(equation)): 
            if equation.index('x') > equation.index('='): #if x comes after the equal sign
                  subSign = equation.index('-')
                  equalSign = equation.index('=')
                  num1 = equation[0:subSign]
                  num2 = equation[subSign+1:equalSign]
                  num1 = int(num1)
                  num2 = int(num2)
                  subtraction = num1 - num2
            elif equation.index('x') == 0: #if x comes before the - sign
                  subSign = equation.index('-')
                  equalSign = equation.index('=')
                  num1 = equation[subSign + 1: equalSign]
                  num2 = equation[equalSign + 1: len(equation) + 1]
                  num1 = int(num1)
                  num2 = int(num2)
                  subtraction = num2 + num1
            else: #if x comes after the - sign but before the = sign
                  subSign = equation.index('-')
                  equalSign = equation.index('=')
                  num1 = equation[0:subSign]
                  num2 = equation[equalSign+1: len(equation) + 1]
                  num1 = int(num1)
                  num2 = int(num2)
                  subtraction = num1 - num2
                  
      return subtraction
                  
      


def addition(equation):
      '''
      This function calculates the value of x if the inputted equation is an addition equation (includes a + sign in the equation).
      This function has one input: equation
      This function has one output: addition
      '''
      for i in range(len(equation)):
            if equation.index('x') > equation.index('='): #if x comes after the = sign
                  addSign = equation.index('+')
                  equalSign = equation.index('=')
                  num1 = equation[0:addSign]
                  num2 = equation[addSign+1:equalSign]
                  num1 = int(num1)
                  num2 = int(num2)
                  addition = num1 + num2
            elif equation.index('x') == 0: #if x comes before the + sign
                  addSign = equation.index('+')
                  equalSign = equation.index('=')
                  num1 = equation[addSign + 1: equalSign]
                  num2 = equation[equalSign + 1: len(equation) + 1]
                  num1 = int(num1)
                  num2 = int(num2)
                  addition = num2 - num1
            else: #if x comes after the + sign but before the = sign
                  addSign = equation.index('+')
                  equalSign = equation.index('=')
                  num1 = equation[0: addSign]
                  num2 = equation[equalSign + 1: len(equation) + 1]
                  num1 = int(num1)
                  num2 = int(num2)
                  addition = num2 - num1

      return addition
                  


def main():
      
      origEquation = input('Please enter your mathematical equation:') #asks user to input an equation
      origEquation =sameFormat(origEquation) #calls origEquation function

      if origEquation.find('=') < 0: #informs the user they did not enter a valid equation if = sign is not present
            print('You did not enter a valid equation.')
            return
      if origEquation.find('x') < 0: #informs the user they did not enter a valid equation if x is not present
            print('You did not enter a valid equation.')
            return
      if origEquation.find('+') > 0 and origEquation.find('-') > 0: #iforms the user they did not enter a valid equation if + sign and - sign are both present
            print('You did not enter a valid equation.')
            return
            
      if origEquation.find('+') > 0: #calls the addition function if a + sign is found in the equation
            print('x =', addition(origEquation))
      elif origEquation.find('-') > 0: #calls the subtraction function if a - sign is found in the equation
            print('x =',subtraction(origEquation))
      else:
            print('You did not enter a valid equation.')
            return


main()
    
