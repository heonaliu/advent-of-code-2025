f = open('/Users/heona/Documents/Projects/Programming Club - Advent/Day 2/input.txt')

lines = f.read().split(",")
sum = 0
invalid = 0
print(lines)
# strategy ---
# split each ID in half (to find possible combos)
#check if the possible ID combos are under the last ID range
#anything mod 11 is out.
#if yes add it to the sum, else pass

for i in range(len(lines)):
    current_id = lines[i].split("-")
    first = int(current_id[0])
    second = int(current_id[1])
    #if digits are odd than there can be no repeats
    
    # odd numbers for BOTH first and second
    for i in range(first, second + 1):
        if (len(str(first)) % 2 != 0 and len(str(second)) % 2 != 0):
            print("No Invalid ID")
            break
        #for each number from first number to second
        else: 
            digits = int(len(str(i)))
            num = str(i)
            if (digits % 2 == 0):
                mid = int(digits / 2)
                first_half = num[0:mid]
                second_half = num[mid:]
                print(str(first_half) + " " + str(second_half))
                if(int(first_half) == int(second_half)):
                    #invalid number
                    invalid += 1
                    sum += int(num)
                    
print("Invalid IDs: " + str(invalid) + " Sum: " + str(sum))
            
            
        
    
        
    
    
    
    
    
        
        
    
    
    
    
        
    
    
        

