#Base converrsion function with no conditionals
def base_conversion_math(b,t,v):
    
    #Math import for logarthim function
    import math
    
    #Preparing the inputs for the program
    v = str(v)
    b = int(b)
    t = int(t)
    
    #Intializing the changing variables
    b10 = 0
    conversion = ''
    
    #Convert inputted value to base 10
    for e in range(len(v)):
        digit = int(value[(len(value) - 1) - e])
        b10 = b10 + (digit * (b**e))
    
    #Convert the base 10 number to the desired base (t)
    l = int((math.log(b10)) / (math.log(t)))
    for d in range(l,-1,-1):
        c = b10 // (t**d)
        b10 -= (c*(t**d))
        conversion += str(c)
    
    #The output of the function should be the converted number
    return conversion

#User input into the program
value = input('What is the number you are converting? ')
start_base = input('What is the base of that number? ')
end_base = input('What is the base that you want to convert to? ')

#Run the function
run = base_conversion_math(start_base,end_base,value)
print(run)