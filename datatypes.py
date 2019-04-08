students_data = [
    {"id":'1', "name": "Bob Micheal", "age":13 , "sex":"Male" , "height":"173cm"},
    {"id":'2', "name": "Anthony Joshua", "age":16 , "sex":"Male" , "height":"164cm"},
    {"id":'3', "name": "Folarin Falana", "age":13 , "sex":"Male" , "height":"189cm"},
    {"id":'4', "name": "Adebimpe Adepoju", "age":12 , "sex":"Female" , "height":"163cm"},
    {"id":'5', "name": "Josephine Sandra", "age":15 , "sex":"female" , "height":"160cm"},
    {"id":'6', "name": "Chisoba Moghalu", "age":13 , "sex":"Male" , "height":"178cm"}
    ]
 
 
def student_id(identity,students_data):
    for student_data in students_data:
	    if(student_data["id"] == identity):
		    return student_data
		


		
student_details = student_id('3',students_data)

print(student_details)



count = 0

while(count < 100):
    count = count + 1
    c = count/3
    a = count/5
    d = count % 3
    b = count % 5
    if(d == 0):
	    print(c,'fuzz')
    if(b == 0):
	    print(a,'buzz')

    if(b == 0) and (d == 0):
        print(c, 'fuzzbuzz')
        print(a, 'fuzzbuzz')




fruits = {'banana','apple','mango','papaya'}
 
for fruit in fruits:
    print('I enjoy  eating' +fruit)

	
Ages = [42, 46, 45, 35]
max(Ages)
 



converter = 0
grammes = 1
 
def converter(g):
    kg = g/1000
    return("The value of ",g," grammes to kilogrammes is ",kg," kg")

converter(5000, grammes)


num = [26,74,54,33,44]

x = num[+0] * num[0]

print(x)
