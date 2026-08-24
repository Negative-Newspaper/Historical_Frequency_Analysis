import csv
import matplotlib.pyplot as plt



def load_and_validate_data(csv_data):

    winning_numbers = []
    
    try:
        with open(csv_data, mode= "r")as file:
            reader = csv.DictReader(file)
            print(" ")    
            print("Data loaded successfully")
            
            for row in reader:
                
                validation = True

                if not row["COMBINATIONS"]:
                    validation = False
                else: 
                    if "" in row["COMBINATIONS"].split("-"):
                        validation = False
                        continue
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
    except:
        print(f" Error: The file '{csv_data}' does not exist or it is not a CSV file.")
    
       
    print(f"Valid records: {len(winning_numbers)}")
    return winning_numbers


#### counting repeating numbers ####

def counting_repeating_numbers(load_and_validate_data):
    number_of_winning_numbers = {}
    
    print("Most Common Winning Numbers: ")

    for row in load_and_validate_data:
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
    print(f"Possition {position}")
    print(" ")      
    keys = (['0','1','2','3','4','5','6','7','8','9'])
    for key in keys:
        if key in position_winning_number:
            sorted_dictionary[key] = position_winning_number[key]
        
        repeated = sorted_dictionary[key]
        
        print(f"{key}: repeated {repeated}")
        
    return sorted_dictionary

#### Printing chart ####

def show_chart(load_and_validate_data, position):
    data = count_position(load_and_validate_data, position)

    x_labels = (data.keys())
    y_values = (data.values())

    plt.figure(figsize=(8,6))
    plt.bar(x_labels, y_values, color='skyblue', edgecolor='black')
    plt.title(f"Digit Frequency - Position {position}")
    plt.xlabel('Digits')
    plt.ylabel('Frequency')

    plt.show()
    

validated_csv = load_and_validate_data("4D_lotto.csv")

print(" ")
print(" ")
show_chart(validated_csv, 1)
print(" ")
show_chart(validated_csv, 2)
print(" ")
show_chart(validated_csv, 3)
print(" ")
show_chart(validated_csv, 4)
print(" ")
counting_repeating_numbers(validated_csv)

# sample di pa ako marunong mag cowork d2

