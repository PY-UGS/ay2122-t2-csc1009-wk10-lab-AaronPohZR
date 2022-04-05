#Question1
#Print output of Hellow Glasgow!
print("Hello Glasgow!")
    
#Question2
#Enter 2 number and storing it as int in variable x and y
x = int(input("Enter the number for x: "))
y = int(input("Enter the number for y: "))
#Find the average of the 2 numbers and storing it as float in variable averageTwoNumber
averageTwoNumber = float((x+y)/2)
#Print output of the average of the 2 numbers
print("The average of these 2 numbers:" ,averageTwoNumber)

#Question3
def modCodeToModFullName(modCode):
    """Create a switch functiion and accept string input, perform dictiionary lookup"""
    switch ={
        "CSC1006":'Mathematics 2',
        "CSC1007":'Operating Systems',
        "CSC1008":'Data Structures and Algorithms',
        "CSC1009":'Object-Oriented Programming',
        "CSC1010":'Computer Networks',
    }
    return switch.get(modCode,"Invalid module code")

#Enter module code and storing it as string in variable z
z = input("Enter the module code: ")
#Print out module full name from switch function
print(modCodeToModFullName(z))

#Question4
start = 102
end = 66
#Using a for loop to find the number ranging for 102 to 66 and deducting it by 1
for num in range(start, end, -1):
    #If number mod by 2 is not equal to zero means its a odd number hence print out number
    if num%2 != 0:
        print(num)