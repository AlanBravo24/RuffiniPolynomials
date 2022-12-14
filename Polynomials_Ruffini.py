import logging 
import math
'''
This program uses Ruffini's rule to find the roots of polynomials up to degree 4. 
This rule is a special case of synthetic division in which the divisor is a lineal factor.
Made by Alan Bravo on 10/02/22 using Python 3.9.0
'''
#Setting up the basicConfig for the logging module
logging.basicConfig(filename="log.log", filemode="w", level=logging.INFO)
#Function that finds all the divisors of a number and adds them to a list which will be used to find the roots of the polynomials..
divisors = list()
def Divisor(n):
    for i in range(1, abs(n)):
        if n%i == 0:
            divisors.append(i)
            divisors.append(-i)
    divisors.append(n)
    divisors.append(-n)
#The user will input the degree of the polynomial. The accepted range is 2-4.
while True:
    degree = int(input("Enter the degree of the polynomial (2 - 4):  "))
    if 2 <= degree <= 4:
        break
    else:
        print("Invalid value.")
#Solving if the degree of the polynomial is 4
if degree == 4:
    try:
        print("Enter the terms using the format: ax^4 + bx^3 + cx^2 + dx + e = 0")
        term1_4_4 = int(input("Enter a: "))
        term2_4_4 = int(input("Enter b: "))
        term3_4_4 = int(input("Enter c: "))
        term4_4_4 = int(input("Enter d: "))
        iterm_4_4 = int(input("Enter e: "))
        Divisor(iterm_4_4)
        #Applying Ruffini's algorithm to find the first root.
        for i in divisors:
            op1_4_4 = term1_4_4 * i 
            op2_4_4 = term2_4_4 + op1_4_4 ## 
            op3_4_4 = op2_4_4 * i
            op4_4_4 = term3_4_4 + op3_4_4 ##
            op5_4_4 = op4_4_4 * i
            op6_4_4 = term4_4_4 + op5_4_4 ##
            op7_4_4 = op6_4_4 * i
            op8_4_4 = iterm_4_4 + op7_4_4 ##
            logging.debug(f" 4th degree with {i} = {op8_4_4}")
            if op8_4_4 == 0:
                break
        logging.info(f" 4th degree =  {term1_4_4} {op2_4_4} {op4_4_4} {op6_4_4} and the remainder is: {op8_4_4}")
        x1_4 = i
        ##3rd degree##
        #Applying Ruffini's algorithm to find the second root.
        term1_3_4 = term1_4_4
        term2_3_4 = op2_4_4
        term3_3_4 = op4_4_4
        iterm_3_4 = op6_4_4
        Divisor(op6_4_4)
        for i in divisors:
            op1_3_4 = term1_3_4 * i
            op2_3_4 = term2_3_4 + op1_3_4 ##
            op3_3_4 = op2_3_4 * i
            op4_3_4 = term3_3_4 + op3_3_4 ##
            op5_3_4 = op4_3_4 * i
            op6_3_4 = iterm_3_4 + op5_3_4 ##
            logging.debug(f" 3rd degree with {i} = {op6_3_4}")
            if op6_3_4 == 0:
                break
        logging.info(f" 3rd degree =  {term1_3_4} {op2_3_4} {op4_3_4} and the remainder is: {op6_3_4}")
        x2_4 = i
        ##2 degree##
        #Applying the quadratic formula to find the two remaining roots.
        a_4 = term1_3_4
        b_4 = op2_3_4
        c_4 = op4_3_4

        op1_2_4 = b_4 * -1
        op2_2_4 = b_4 ** 2
        op3_2_4 = -4 * a_4 * c_4
        op4_2_4 = 2 * a_4

        op5_2_4 = op2_2_4 + op3_2_4
        op6_2_4 = math.sqrt(op5_2_4)

        x3_4=(op1_2_4+op6_2_4)/op4_2_4
        x4_4=(op1_2_4-op6_2_4)/op4_2_4
        
        logging.info(f" 2nd degree =  x2 = {x3_4} / x3 = {x4_4}")
        #The 4 roots are shown.
        print(f" Results =  x1 = {x1_4} / x2 = {x2_4} / x3 = {x3_4} / x4 = {x4_4}")
    except ZeroDivisionError:
        print("The equation could not be solved.")
#Solving if the degree of the polynomial is 3
elif degree == 3:
    try:
        print("Enter the terms using the format: ax^3 + bx^2 + cx + d = 0")
        term1_3_3 = int(input("Enter a: "))
        term2_3_3 = int(input("Enter b: "))
        term3_3_3 = int(input("Enter c: "))
        iterm_3_3 = int(input("Enter d: "))
        Divisor(iterm_3_3)
        #Applying Ruffini's algorithm to find the first root.
        for i in divisors:
            op1_3_3 = term1_3_3 * i
            op2_3_3 = term2_3_3 + op1_3_3 ##
            op3_3_3 = op2_3_3 * i
            op4_3_3 = term3_3_3 + op3_3_3 ##
            op5_3_3 = op4_3_3 * i
            op6_3_3 = iterm_3_3 + op5_3_3 ##
            logging.debug(f" 3rd degree with {i} = {op6_3_3}")
            if op6_3_3 == 0:
                break
        #The 3 roots are shown
        logging.info(f" 3rd degree =  {term1_3_3} {op2_3_3} {op4_3_3} and the remainder is:  {op6_3_3}")
        x1_3 = i
        #### Degree 2 ####
        #Applying the quadratic formula to find the two remaining roots.
        a_3 = term1_3_3
        b_3 = op2_3_3
        c_3 = op4_3_3

        op1_2_3 = b_3 * -1
        op2_2_3 = b_3 ** 2
        op3_2_3 = -4 * a_3 * c_3
        op4_2_3 = 2 * a_3

        op5_2_3 = op2_2_3 + op3_2_3
        op6_2_3 = math.sqrt(op5_2_3)

        x2_3=(op1_2_3+op6_2_3)/op4_2_3
        x3_3=(op1_2_3-op6_2_3)/op4_2_3
        
        logging.info(f" 2nd degree =  x2 = {x2_3} / x3 = {x3_3}")
        print(f" Results =  x1 = {x1_3} / x2 = {x2_3} / x3 = {x3_3}")
    except ZeroDivisionError:
        print("The equation could not be solved.")
    except ValueError:
        print("The equation could not be solved.")  
#Solving if the degree of the polynomial is 2
elif degree == 2:
    #Applying the quadratic formula to find the two roots.
    try:
        print("Enter the terms using the format: ax^2 + bx + c = 0")
        a_2 = int(input("Enter a: "))
        b_2 = int(input("Enter b: "))
        c_2 = int(input("Enter c: "))

        op1_2_2 = b_2 * -1
        op2_2_2 = b_2 ** 2
        op3_2_2 = -4 * a_2 * c_2
        op4_2_2 = 2 * a_2

        op5_2_2 = op2_2_2 + op3_2_2
        op6_2_2 = math.sqrt(op5_2_2)

        x1_2=(op1_2_2+op6_2_2)/op4_2_2
        x2_2=(op1_2_2-op6_2_2)/op4_2_2
        #The 2 roots are shown
        print(f" Results =  x1 = {x1_2} / x2 = {x2_2}")
    except ZeroDivisionError :
        print("The equation could not be solved.")
    except ValueError:
        print("The equation could not be solved.")