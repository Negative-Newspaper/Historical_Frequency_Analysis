import csv

winning_numbers = []


with open("4d_lotto.csv", mode= "r")as file:
    reader = csv.DictReader(file)
        
    for row in reader:
        
        validation = True

        if not row["COMBINATIONS"]:
            validation = False
        else: 
            if "" in row["COMBINATIONS"].split("-"):
                validation = False
                break
                      
            for part in row["COMBINATIONS"].split("-"):
                if part.isalpha():
                    validation = False
                    break
                elif part.isdigit() and int(part) > 9:
                    validation = False
                    break
                elif len(row["COMBINATIONS"].split("-")) > 4 or len(row["COMBINATIONS"].split("-")) < 4:
                    validation = False
                    break
                    
        if validation == True:
            winning_numbers.append(row)
 


#### counting repeating numbers ####
number_of_winning_numbers = {}

for row in winning_numbers:
    winning_number = row["COMBINATIONS"]
    if winning_number in number_of_winning_numbers:
        number_of_winning_numbers[winning_number] += 1
    else:
        number_of_winning_numbers[winning_number] = 1
            
for number in number_of_winning_numbers:
    repeated = number_of_winning_numbers[number]
    
    if repeated > 2:
        print(f"the number {number} repeated {repeated}")
        
#### counting repeating numbers by possitions ###

first_position_winning_number = {}
second_position_winning_number = {}
third_position_winning_number = {}
forth_position_winning_number = {}

for row in winning_numbers:
    for part in row["COMBINATIONS"][0]:
        first_winning_number = part
        
        if first_winning_number in first_position_winning_number:
            first_position_winning_number[first_winning_number] += 1
        else:
            first_position_winning_number[first_winning_number] = 1
            

for row in winning_numbers:
    for part in row["COMBINATIONS"][2]:
        second_winning_number = part
        if second_winning_number in second_position_winning_number:
            second_position_winning_number[second_winning_number] += 1
        else:
            second_position_winning_number[second_winning_number] = 1

   
for row in winning_numbers:
    for part in row["COMBINATIONS"][4]:
       third_winning_number = part
       if third_winning_number in third_position_winning_number:
           third_position_winning_number[third_winning_number] += 1
       else:
           third_position_winning_number[third_winning_number] = 1

for row in winning_numbers:
    for part in row["COMBINATIONS"][6]:
        forth_winning_number = part
        if forth_winning_number in forth_position_winning_number:
            forth_position_winning_number[forth_winning_number] += 1
        else:
            forth_position_winning_number[forth_winning_number] =1

print()
print()
print("First position number")
print()
for number in first_position_winning_number:
    winning_number = first_position_winning_number[number]
    
    print(f"the number {number} repeated {winning_number}")
    
print()
print()
print("Second position number")
print()

for number in second_position_winning_number:
    winning_number = second_position_winning_number[number]
    print(f"the number {number} repeated {winning_number}")

print()
print()
print("Third position number")
print()

for number in third_position_winning_number:
    winning_number = third_position_winning_number[number]
    print(f"the number {number} repeated {winning_number}")

print()
print()
print("Fourth position number")
print()

for number in forth_position_winning_number:
    winning_number = forth_position_winning_number[number]
    
    print(f"the number {number} repeated {winning_number}")