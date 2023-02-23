# WRITTEN BY MICAH CARSON, USING VISUAL STUDIO CODE
# CONVERTS VALUE BETWEEN NUMBER BASES 2 - 36

#Base conversion function given a number, the base of that number, and the new base you want to change it to
def base_conversion(sb,tb,value):
    
    #Import math for logarithm operations
    import math
    
    #User input type setup for the function
    sb = int(sb)
    tb = int(tb)
    value = str(value)
    
    #Check if user inputted bases are applicable to the program
    if 2 <= sb <= 36 and 2 <= tb <= 36:
        
        #Begin converting number to base 10
        b10 = 0
        
        #Check if the first character is negative
        if value[0] == '-':
            negative_value = True
            value = value[1:len(value)]
        else:
            negative_value = False
        
        #Perform algorithms for each place value in the given number
        for e in range(len(value)):
            
            #Sort through each digit of the given value
            digit = value[(len(value) - 1) - e]
            if digit.isdigit() == False:
                
                #Check if it is an accepted alternate number (A-Z)
                if 65 <= ord(digit) <= 90:
                    digit = int(ord(digit) - 55)
                    
                    #Testing if the value is smaller than the start base
                    if digit < sb:
                        b10 = b10 + (digit * (sb**e))
                    else:
                        return 'Error: Number not in number system'
                else:
                    return 'Error: Invaild character'
            else:
                
                #Testing if the value is smaller than the start base
                if int(digit) < sb:
                    b10 = b10 + (int(digit) * (sb**e))
                else:
                    return 'Error: Number not in number system'
    
        #Begin converting from base 10 to target base    
        conversion = ''
        
        #Finding the total number of digits in the new number
        l1 = math.log(b10)
        l2 = math.log(tb)
        l = int(l1/l2)
        
        #Cycle through all of the new place values
        for d in range(l,-1,-1):
            c = b10 // (tb**d)
            b10 -= (c*(tb**d))
            
            #If the coeffecient is greater than 9 change it to its correct symbol
            if c >= 10:
                c = chr(c + 55)
            else:
                pass
            
            #Slowly add to the conversion
            conversion += str(c)

        #Return the conversion accounting for negatives
        if negative_value == True:
            return '-' + conversion
        else:
            return conversion
    
    else:
        return 'Error: Base(s) not in acceptable range (2 - 36)'

#User input into the program
value = input('What is the number you are converting? ')
start_base = input('What is the base of that number? ')
end_base = input('What is the base that you want to convert to? ')

#Run the function
run = base_conversion(start_base,end_base,value)
print(run)