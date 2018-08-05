# Question1

dic1={
    1:10,
    2:20
    }
dic2={
    3:30,
    4:40
    }
dic3={
    5:50,
    6:60
    }
dic4 ={ **dic1, **dic2, **dic3}
print(dic4)

# Question2
my_dictionary = {
    "a":1,
    "b":True,
    "c":[1,2,3],
    "d":{"Hello":5,"World" : 5}
    }
my_dictionary["XYZ"] =["Nepal"]
print(my_dictionary.get('pqe'))
print(my_dictionary.values())
del (my_dictionary["XYZ"])

#Question3

my_list = list(range(0, 10))
print(sum(my_list))

#Question4

another_list = [4, 5, 9, 1, 0, 2, 3]
print(min(another_list))
print(max(another_list))

#Question5
listing_list = [4, 5, 9, 1, 0, 2, 3,3,4,5,2,3,7,8,9]
def duplicate(x):
   return list(set(x))
p = duplicate(listing_list)
print(p)

#Question6
next_list = [4, 5, 9, 1, 0, 2, 3]
print(len(next_list))

#Question7
Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Sample_List.pop()
Sample_List.pop()
Sample_List.pop(0)
print(Sample_List)

#Question8
a = [1, 2, 3, 4]
number = int(input("enter a number"))
a.append(number)
print(a)

#Question9
a = [1, 2, 3, 4, 5, 5, 6]
b = [4, 3, 2, 8,5 , 6, 7]
c =(set(a))
d =(set(b))
similar = list(c.intersection(d))
unique1= list(c.difference(d))
unique2= list(d.difference(c))
final_list = similar + unique1+ unique2
print(final_list)

#Question10
specified_list = [4, 5, 9, 1, 0, 2, 3,3,4,5,2,3,7,8,9]
number = int(input("enter a number"))
print(specified_list.index(number))

#Question11
sample_list =[11, 33, 50]
a = str(sample_list[0])
b = str(sample_list[1])
c = str(sample_list[2])
final = a +b +c
print(final)

#Question12
dictionary = {
    "a":1,
    "b":True,
    "c":[1,2,3],
    "d":"Hello",
    "e":(100, 200),
    "f": set([1,2,3,3])
  }
print(len(dictionary))

#Question13
x =  (1, "hello",True,2,False,3.22)

#Question14
x =  [1, "hello",True,2,False,3.22]
y = tuple(x)
print(type(y))

#Question15

a = [1, 2, 3, 4, 5, 5, 6]
b = set(a)
print(b)













































































