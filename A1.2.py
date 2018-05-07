# 
# Name: Julian Lankstead
# Student Number: 101043448
#
# References: Gaddis, T (2015). "Starting Out With Python"


Ounces = 0.02835
Stones = 6.350293
Ounces_Input = float(input('How Many Stones Do You Want To Convert?'))
Stones_Input = float(input('How Many Ounces Do You Want To Convert?'))
Ounces_Calc = (Stones_Input/Stones) * Ounces
Stones_Calc = (Ounces_Input/Ounces) * Stones
print ('This is the conversion from Stones to Ounces' , Stones_Calc)
print ('This is the conversion from Ounces to Stones' , Ounces_Calc )
