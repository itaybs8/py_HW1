length= int(input("how long the length?"))
width= int(input("what the width of the volume?"))
height= int(input("how heigh do u want it to be from 1 to 10?"))


def calculate_volume(l1,w1,h1):
    v=l1*w1*h1
    print ("result is " + str(v))
    return v


print("The volume of the rectangular prism is " + str(calculate_volume(length, width,height)) + " cubic feet.")
#x=calculate_volume(length, width,height)
#print("i have :" + str(x))
#x1=calculate_volume(1,1,1)
#print("i have 1 :" + str(x1))



