m1 = int(input('Enter marks for 1st subject:'))
m2 = int(input('Enter marks for 2nd subject:'))
m3 = int(input('Enter marks for 3rd subject:'))
m4 = int(input('Enter marks for 4th subject:'))
m5 = int(input('Enter marks for 5th subject:'))

avg=(m1 + m2 + m3 + m4 + m5)/5

if avg>=81 and avg<=100:
    print("Your Grade is A+.")
elif avg>=61 and avg<81:
    print("Your Grade is A.")
elif avg>=41 and avg<61:
    print("Your Grade is B.")
elif avg>=21 and avg<41:
    print("Your Grade is C.")
else:
    print("Your Grade is D.")