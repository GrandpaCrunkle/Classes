# Example


def calcArea(dim1, dim2, dim3):
    if dim3 != 0:
        return(dim1*dim2*dim3)
    else:
        return(dim1*dim2)
        
length = int(input("\nInput Length:"))
width = int(input("\nInput Width:"))
height = int(input("\nInput Height (or 0 to continue):"))

print("Blah blah blah area is",calcArea(length,width,height))

