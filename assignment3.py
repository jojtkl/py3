# Topic :List Exercise
# # Q1. Create a list of 5 random numbers and print the list.

l1=[20,30,40,33,22]
print(l1)
print(type(l1))
# # Q2. Insert 3 new values to the list and print the updated list.

l1.extend([11,12,13])
up_l1=l1
print(up_l1)

# # Q3. Try to use a for loop to print each element in the list.

for element in l1:
    print(element)




# Topic: Dictionary Exercise

# #Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
Dict={'name':'John',
      'Age':25,
      'Address':'Newyork'}
print(Dict)
print(type(Dict))
# #Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
#
Dict.update({'phone':'1212324354'})
print(Dict)



# Topic: Set Exercise

# Q1.Create a set with values 1, 2, 3, 4, and 5.
s={1,2,3,4,5}
print(s)
print(type(s))
#
# # Q2. Add the value 6 to the set created in Q1.
s.add(6)
print(s)
print(type(s))
#
# # Q3. Remove the value 3 from the set created in Q1.
s.remove(3)
print(s)



#Topic:Tuple Exercise

#Q1. Create a tuple with values 1, 2, 3, and 4
Tuple=(1,2,3,4)
print(Tuple,type(Tuple))

# Q2. Print the length of the tuple created in Q1.
print(len(Tuple))