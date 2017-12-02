"""This is the main program file used to analyze the information witin open_tickets.csv the file shows 
a bargraph displaying the total 'assigned' tickets for each employee in the list. Once the data is collected
the program then creates a file named 'final_results.csv' and moves the bar graph data to this file
*NOTE- to run successfully make sure to install matplot lib and numpy"""
import csv 
import matplotlib.pyplot as plt
import numpy as name_position

ticket_file = open("open_tickets.csv").read()#reads in data
ticket_file_list = ticket_file.split("\n")#splits data by row using \n character
ticketList_noHeader = ticket_file_list[1:len(ticket_file_list) - 1]#remove header from data
#print (ticket_file_list)
column_list=[]
for column in ticket_file_list[0:1]:
    datapoint= column.split(",")
    column_list= datapoint
print(column_list)   

name_position= column_list.index('Ticket Owner')#records position of ticket owner column

row_list= []
name_list=[]
#The below loop runs through the ticketList_noHeader list and splits the column by "," escape character
#And appends the column to row_list variable
for column in ticketList_noHeader:
    fieldtest= column.split(",")
    row_list.append(fieldtest)

#The below loops through row_list and appaneds the names from the index of name_position var and appends it to name_list
for column in row_list:
    name_list.append(column[name_position])     

first_name=[]
for name in name_list:
    first_name.append(name.split(" ")[0])

name_dictionary = {}
#This for loop creates a new key for each element and totals all elements within the array
#Placing all information in the above dictionary
for name in first_name:
    if name in name_dictionary:
        name_dictionary[name] = name_dictionary[name] + 1
    else:
        name_dictionary[name] = 1
print(name_dictionary)
"""The below creates a file named final_results.csv and writes a new line according to the values
in the name_dictionary"""
csv_file_creator = csv.DictWriter(
   open('final_results.csv', 'w', newline=""),
   fieldnames= ['name', 'ticket_total']
)

for a in name_dictionary:
    csv_file_creator.writerow({'name':a, 'ticket_total':name_dictionary[a]})

#Displays information as bar chart using matplot lib
plt.bar(range(len(name_dictionary)), name_dictionary.values(), align='center')
plt.xticks(range(len(name_dictionary)), name_dictionary.keys())
plt.show() 

"""To do list: 
1. Create function to loop through data and clean up extraneous data
2. Add function to analyze closed_tickets.csv
3. Provide descriptive analytics to categorize according to 'My request is related to' column within closed_tickets.csv
"""
