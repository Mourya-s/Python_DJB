# numpy --> fast operation on arrays

# >floor: convert decimal to smallest int, 2.3-->2  , 5.9-->5, -1,2-->-2
# >ciel: convert decimal to largest, 3.1-->4,   1.5-->2
# >rint: covert decimal to nearest int , 3.4-->3,  3.5-->4(odd) , 2.5-->2(even)

# my code 
import numpy

A = list(map(float, input().split()))

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

# chatgpt code
import numpy

numpy.set_printoptions(sign=' ')

A = numpy.array(list(map(float, input().split())))

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
