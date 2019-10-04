#Areas of Rectangles program
#P3T1
#CTI-110
#Andrew Jones

#Get length and width of rectangle 1
length1 = int(input('Enter length of rectangle 1: '))
width1 = int(input('Enter width of rectangle 1: '))

#input length and width of rectangle 2
length2 = int(input('Enter length of rectangle 2: '))
width2 = int(input('Enter width of rectangle 2: '))

#Calculate area of rectangles
area1 = length1 * width1
area2 = length2 * width2

#Determine which has bigger area
if area1 > area2:
    print ("Rectangle 1 has the greatest area.")
else:
    if area2 > area1:
    print ("Rectangle 2 has the greatest area.")
else:
    print ("Rectangles are the same size.")
