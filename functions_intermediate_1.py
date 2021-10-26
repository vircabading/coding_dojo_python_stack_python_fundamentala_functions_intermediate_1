# /////////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python Stack > Python > Fundamentals: Functions Intermediate 1
# By:   Virgilio D. Cabading Jr.    Created: Oct 25, 2021
# /////////////////////////////////////////////////////////////

def print_desc(description) :
    print()
    print("////////////////////////////////////////////////////////////////////////////")
    print(description)
    print()

# /////////////////////////////////////////////////////////////
print_desc("1. Update Values in Dictionaries and Lists")

x = [ [5,2,3], [10,8,9] ] 
print( f"x is {x}")
print( "1. Change the value 10 in x to 15")
x[1][0] = 15
print( f"The new value of x is {x}")
print()

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print (f"the students are: {students}")
print ("2. change the last_name of the first student from 'Jordan' to 'Bryant'")
students[0]['last_name'] = "Bryant"
print (f"the updated  students are: {students}")
print()

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(f"The sports directory is {sports_directory}")
print("3. In the sports_directory, change 'Messi' to 'Andres'")
sports_directory['soccer'][0] = 'Andres'
print(f"The updated sports_directory is {sports_directory}")
print()

z = [ {'x': 10, 'y': 20} ]
print(f"z is: {z}")
print("4. Change the value of 20 in z to 30")
z[0]['y'] = 30
print(f"the new value of z is: {z}")


# /////////////////////////////////////////////////////////////
print_desc("2. Iterate Through a List of Directories")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(students):
    for idx in range(len(students)):
        print("first_name - " + students[idx]['first_name'] + ", last_name - " + students[idx]['last_name'])

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

iterate_dictionary(students)

# /////////////////////////////////////////////////////////////
print_desc("3. Get Values from a List of Dictionaries")

def iterate_dictionary_2 (key_name, some_list):
    for idx in range(len(some_list)):
        print(some_list[idx][key_name])

print("The first_name of students are:")
iterate_dictionary_2('first_name', students)
print()
print("The last_name of students are:")
iterate_dictionary_2("last_name", students)

# /////////////////////////////////////////////////////////////
print_desc("4. Iterate Through a Dictionary with List Values")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo (some_dict):
    print (f"{len(some_dict['locations'])} LOCATIONS ************")
    output = ""
    for idx in range (len(some_dict['locations'])):
        output += f"{idx+1}. {some_dict['locations'][idx]} "
    print(output + "\n")

    output = ""
    print(f"{len(some_dict['instructors'])} INSTRUCTORS *************")
    for idx in range (len(some_dict['instructors'])):
        output += f"{idx+1}. {some_dict['instructors'][idx]} "
    print(output)

printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
