import csv
import matplotlib.pyplot as plt

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
    sorted_dictionary = {}
    
    the_index = (position - 1) * 2
    
    for row in list_of_winning_numbers:
        winning_number = row["COMBINATIONS"][the_index]
        if winning_number in position_winning_number:
            position_winning_number[winning_number] += 1
        else:
            position_winning_number[winning_number] = 1
            
    #### sort the keys ####        
    keys = (['0','1','2','3','4','5','6','7','8','9'])
    for key in keys:
        if not position_winning_number[key] == "":
            sorted_dictionary[key] = position_winning_number[key]

    return sorted_dictionary

#### Printing chart ####

def show_chart(position):
    data = count_position(winning_numbers, position)

    x_labels = (data.keys())
    y_values = (data.values())

    plt.figure(figsize=(8,6))
    plt.bar(x_labels, y_values, color='skyblue', edgecolor='black')
    plt.xlabel('Digits')
    plt.ylabel('Frequency')

    plt.show()
    
show_chart(1)
show_chart(2)
show_chart(3)
show_chart(4)

# sample di pa ako marunong mag cowork d2

