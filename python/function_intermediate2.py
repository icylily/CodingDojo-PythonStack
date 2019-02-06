# Change the value 10 in x to 15. Once you're done, x should now be[[5, 2, 3], [15, 8, 9]].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30
def update_values():
    x = [ [5,2,3], [10,8,9] ] 
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]
    sports_directory = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
    }
    z = [ {'x': 10, 'y': 20} ]
    x[1][0]=15
    print(x)
    students[0]['last_name'] = ''
    students[0]['last_name'] = 'Bryant'
    print(students)
    sports_directory['soccer'][0] = 'Andres'
    print(sports_directory)
    z[0]['y']=30
    print(z)
    return


update_values()


should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary(students):
    for x in range(len(students)):
        
        for key in students[x]:
            print(key + '-'+students[x][key],end = ',')
        print('')
    return 
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])
    return 


iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        print(str(len(some_dict[key])) +' '+ key + ":")
        for x in range(len(some_dict[key])):
            print(some_dict[key][x])
    return
printInfo(dojo)
