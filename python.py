#NumPy Basics
import numpy as np
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]],dtype='int32')
print(a)
b=np.array([[9.0,8.0,7.0],[9.87,9.76,7.54]])
print(b)
#Get dimensions
print(a.ndim," ",b.ndim)
#Get shape
print(a.shape," ",b.shape)
#Get the type
print(a.dtype," ",b.dtype)
#Get size = size of each element(bytes)
print(a.itemsize)
#Get the number of elements
print(a.size)
#Get the bytes size
print(a.nbytes)
#Access elements
print(a[1][0])
#Get a specific row
print(a[1])
#Get a specific column
print(a[:,3])
#Slicing of elements
print(a[0][1:6:2])
#Changing values
a[1][5]=20
print(a)
a[:,2]=54
print(a)


#3-d example

c=np.array([[[1,2],[3,4],[5,6],[7,8]],[[9,10],[11,12],[13,14],[15,16]],[[17,18],[19,20],[21,22],[23,24]]])
print(c)
print(c.ndim)
print(c.shape)
print(c.itemsize)
print(c.size)
print(c[:,1,1])

print("Built-in functions")
#All 0's matrix
print(np.zeros((3,4,3)))
#All 1's matrix
print(np.ones((3,4,3),dtype='int32'))
#Any other number
print(np.full((3,2,4),99,dtype='float64'))
# Any other number
print(np.full_like(a,99))

#Random decimal numbers
print(np.random.rand(4,2))
print(np.random.random_sample(c.shape))
#print between 0 and 7
print(np.random.randint(7,size=(3,3)))
#between 4 and 7
print(np.random.randint(4,7,size=(3,3)))
#The identity matrix
print(np.identity(5))
#repeat an array
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)

output=np.ones((5,5,))
print(output)
z=np.zeros((3,3))
z[1,1]=9
print(z)

output[1:4,1:4]=z
print(output)

#copy functio
a=[1,2,4]
b=a.copy()
print("b",b)

#mathematical operations
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
print(a+2)
print(b-1)
print(a*7)
print(a/-1)
c=np.array([2,3,4])
d=np.array([3,4,5])
print(c+d)
print(c*d)
print(np.sin(a))

#linear algebra
x=np.array([[1,2],[3,4],[5,6]])
y=np.array([[1,2,3],[4,5,6]])
print(np.matmul(x,y))
print(x@y)
v=np.identity(5)
print(np.linalg.det(v))

#statistics
stats=np.array([[1,2,9],[4,5,6]])
print(np.min(stats))
print(np.max(stats))
print(np.min(stats, axis=0))

print(np.sum(stats))

#Reorganizing arrays
before=np.array([[1,2,9],[4,5,6]])
print(before.shape)
after=before.reshape((6,1))
print(after)

#vertically stacking vectors
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2]))
print(np.hstack([v1,v2]))

#Loading data from file
o=np.genfromtxt('data.txt',delimiter=',')
print(o)
o=o.astype('int64')
print(o)

#Boolean masking and advanced indexing


idx=~((o>50) & (o<100))
print(o[idx])
