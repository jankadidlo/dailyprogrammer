def check_sameness(nck1, nck2):
    counter = 0

    def rearrange_necklace(nck2, y=0):
        # move all letters in string one index lower
        out = ""
        for i in range(len(nck2)):
            out = out + nck2[y - 1]
            y = y + 1
        return out

    # compare the length of the two strings
    try:
        len(nck1) == len(nck2)
    except:
        return 0

    # compare necklace, rearrange and compare again until back in default
    for i in range(len(nck1)):
        if nck1 == nck2:
            counter = counter + 1
        nck2 = rearrange_necklace(nck2)

    return counter

print("Enter first necklace:")
x = input()
print("Enter second necklace:")
y = input()

print(check_sameness(x,y))