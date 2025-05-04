size = 10
width = (4*size) - 3 #determining the fixed width of each line based on the side
wing = ''

for i in range(1,size+1): #iterate until the middle line
    mystring = wing + chr(size+96-i+1) + wing[::-1] #string is composed of 2 wings + current letter
    print(mystring.center(width,'-')) #string is printed in the center
    wing = mystring[:1+((i-1)*2)]+'-' #wing is the string's first half + '-'

wing = wing[:-2] #remove '-a' from the wing

for j in range(size,1,-1): #iterate back to the bottom
    wing = wing[:-2] #remove the last 2 characters of the wing
    mystring = wing + chr(size+96-j+2) + wing[::-1] #same logic as above
    print(mystring.center(width,'-'))



