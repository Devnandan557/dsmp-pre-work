# --------------
# Code starts here
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1 + class_2
print("After concatenating both classes new class is:",new_class)
print("*" *80)
new_class.append('Peter Warden')
print("After adding new student in that class,new class will be:",new_class)
print("*" *80)
new_class.remove('Carla Gentry')
print("Overall updated list is:",new_class)
# Code ends here


# --------------
# Code starts here
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses)
print(courses.values())
total=65+70+80+70+60
print(total)
percentage=total/500 *100
print("percentage obtained by Geoffrey Hinton is:",percentage)
# Code ends here


# --------------
# Code starts here
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,
'yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter warden':75}
topper=max(mathematics,key=mathematics.get)
print(topper)



# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
first_name=topper.split()[0]
print(first_name)
last_name=topper.split()[1]
print(last_name)
full_name=last_name+" " + first_name
print(full_name)
certificate_name=full_name.upper()
print(certificate_name)
# Code starts here



# Code ends here


