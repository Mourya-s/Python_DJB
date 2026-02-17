# import numpy

# my_array = numpy.array([[2, 5], 
#                         [3, 7],
#                         [1, 3],
#                         [4, 0]])

# print numpy.min(my_array, axis = 0)         #Output : [1 0]
# print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
# print numpy.min(my_array, axis = None)      #Output : 0
# print numpy.min(my_array)                   #Output : 0

# same way for max



#my code
import numpy 
li=[]

n=int(input("enter the number "))
for i in range(n):
    x=list(map(int,input().split()))
    li.append(x)

    
li1= numpy.min(li, axis = 1)      
print(max(li1))


