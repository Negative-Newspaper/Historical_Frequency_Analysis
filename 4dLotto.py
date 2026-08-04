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
        
#### counting repeating numbers by positions ###

def count_position(list_of_winning_numbers, position):
    position_winning_number = {}
    
    positions = (position - 1) * 2
    
    for row in list_of_winning_numbers:
        winning_number = row["COMBINATIONS"][positions]
        if winning_number in position_winning_number:
            position_winning_number[winning_number] += 1
        else:
            position_winning_number[winning_number] = 1
    print()
    print(f"position {position} number of repeated from number 1 - 9")
    print()
    for number in position_winning_number:
        winning_number = position_winning_number[number]
        
        
        print(f"The number {number} repeated {winning_number}")  


count_position(winning_numbers, 1)
count_position(winning_numbers, 2)
count_position(winning_numbers, 3)
count_position(winning_numbers, 4)

# sample di pa ako marunong mag cowork d2

