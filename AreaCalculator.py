#Correct use of a function using if else to determine an area if dim3 is 0 will return dim1*dim3

def calculateArea(dim1,dim2,dim3):
    
    if dim3 != 0:
        return(dim1*dim2*dim3)
    else:
        return(dim1*dim2)

length = int(input("\nInput Length:"))
width = int(input("\nInput Width:"))
height = int(input("\nInput Height:"))

print("The total area is",calculateArea(length,width,height))
