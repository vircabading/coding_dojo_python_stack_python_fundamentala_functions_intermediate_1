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


"""
# /////////////////////////////////////////////////////////////
print_desc("2.")


# /////////////////////////////////////////////////////////////
print_desc("3.")


# /////////////////////////////////////////////////////////////
print_desc("4.")

"""