# --- DATA ---

data1 = (7, False, "Apple", True, 7, 98.6) #Tuple

data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"} #List

data3 = ["A", 7, -1, 3.14, True, 7  ] #Set

data4 = {
    "name": "Joe", 
    "age": 26,
    "active": True,
    "hourly_wage": 14.75
} #Dictionary


# --- TASKS ---

#Data1 Tasks
print(len(data1)) #Count number of items

print(data1[3]) #Find the value of the fourth item

countSeven = 0
for item in data1:
    if item == 7:
        countSeven = countSeven + 1
print(countSeven) #Count the number of times 7 appears

#Data2 Tasks
data2.pop() #Remove a random element

data2.add('Alpha') #Add 'Alpha' to the data set

print(data2) #Print the data set

#Data3 Tasks
data3.reverse() #Put the data set in reverse order

data3[1] = 'B' #Change the second value to 'B'

data3.pop(len(data3)-1)
print(data3) #Remove last item and print the data set

#Data4 Tasks
data4['active'] = False #Change 'active' to false

data4['address'] = '123 West Main Street' #Add 'address' with a value of "123 West Main Street"

print(data4['hourly_wage'] * 40) #Print the weekly salary for Joe if he worked a full 40 hour week.

print(data4) #Print the data set