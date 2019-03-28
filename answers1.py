Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
students_data = [
    {"id":'1', "name": "Bob Micheal", "age":13 , "sex":"Male" , "height":"173cm"},
    {"id":'2', "name": "Anthony Joshua", "age":16 , "sex":"Male" , "height":"164cm"},
    {"id":'3', "name": "Folarin Falana", "age":13 , "sex":"Male" , "height":"189cm"},
    {"id":'4', "name": "Adebimpe Adepoju", "age":12 , "sex":"Female" , "height":"163cm"},
    {"id":'5', "name": "Josephine Sandra", "age":15 , "sex":"female" , "height":"160cm"},
    {"id":'6', "name": "Chisoba Moghalu", "age":13 , "sex":"Male" , "height":"178cm"}
    ]
>>> 
>>> 
>>>  def student_id(identity):
	for student_data in students_data:
		if(student_data["id"] == identity):
			return student_data
		
SyntaxError: unexpected indent
>>> 
>>> def student_id(identity):
	for student_data in students_data:
		if(student_data["id"]== identity):
			return student_data

		
>>> student_details = student_id(3)
>>> student_details
{'id': 3, 'name': 'Folarin Falana', 'age': 13, 'sex': 'Male', 'height': '189cm'}


>>> count = 0
>>> 
>>> while(count < 100):
	count = count + 1
	c = count/3
	a = count/5
	d = count % 3
	b = count % 5
	if (d == 0):
		print(c,'fuzz')
	if (b == 0):
		print(a,'buzz')

	if (b == 0)and (d == 0):
		print(c, 'fuzzbuzz')
		print(a, 'fuzzbuzz')

>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> 
>>> for d in [3,1,4,5]:
	print(d, end=" ")

	
3 1 4 5 
>>> 
>>> for i in range(5):
	print(i, 2**i)

	
0 1
1 2
2 4
3 8
4 16
>>>

>>> fruits = {'banana','apple','mango','papaya'}
>>> 
>>> for fruit in fruits:
	print('I enjoy eating '+fruit)

	
I enjoy eating banana
I enjoy eating apple
I enjoy eating mango
I enjoy eating papaya

>>> max_number = 22
>>> 
>>> while max_number > 25:
	print(max_number)

>>> converter = 0
>>> 
>>> def converter(g):
	kg = g/1000
	return("The value of ",g," grammes to kilogrammes is ",kg," kg")



