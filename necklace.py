import urllib
import urllib.request


# https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/ modified to make it an "app" to be usable for other data sources
def rearrange_necklace(nck1, y=0):
    # move all indices in string one step lower
    out = ""
    for i in range(len(nck1)):
        out = out + nck1[y - 1]
        y = y + 1
    return out


def count_repeatings(nck1):
    out = 0
    check = nck1
    for i in range(len(nck1)):
        if check == nck1:
            out += 1
        nck1 = rearrange_necklace(nck1)
    return out


# compare the length of the two strings
def check_length(nck1, nck2):
    try:
        len(nck1) == len(nck2)
    except:
        return 0
    return 1

# compare necklace, rearrange and compare again until back in default
def check_sameness(nck1, nck2):
    if not check_length(nck1, nck2):
        return 0
    out = 0
    for i in range(len(nck1)):
        if nck1 == nck2:
            out = 1
            return out
        nck2 = rearrange_necklace(nck2)
    return out


# find the same necklaces from link
def find_repeatings(link, smnum=1):
    # open the link and get the data into a list
    try:
        f = urllib.request.urlopen(link)
        bulk = f.read()
        decoded = bulk.decode('utf-8').splitlines()
    except:
        raise Exception("Connection failed, please check your link.")

    # this part finds repeating necklaces, skips any already found repeating and prints out necklaces that repeat smnum or more amount of times
    i_cursor = 0
    found = []
    for i in decoded:
        repeats = 0
        current_check = []
        try:
            i != decoded[-1]
        except:
            return 1
        if not i in found:
            cursor = i_cursor + 1
            current_check.append(i)
            while decoded[cursor] != decoded[-1]:
                if check_sameness(i, decoded[cursor]) == 1:
                    found.append(decoded[cursor])
                    current_check.append(decoded[cursor])
                    repeats += 1
                cursor += 1
        # after each check print out the repeating necklaces if there are more than or equal to the number we are looking for
        if repeats >= smnum:
            print(current_check)
        i_cursor += 1

    return 1


# "app interface" to choose/test the requirements
print("Choose a number:\n1 - compare two necklaces\n2 - check how many times a necklace repeats in itself\n3 - find repeating necklaces in data from a link")
option = input()

if option == "1":
    print("Please enter first necklace:")
    nck1 = input()
    print("Please enter second necklace:")
    nck2 = input()
    print(check_sameness(nck1, nck2))

elif option == "2":
    print("Please enter your necklace:")
    nck1 = input()
    print(count_repeatings(nck1))

# for testing use link: "https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt"
elif option == "3":
    print("Please link to the data:")
    link = input()
    print("Enter repeating necklace threshold:")
    smnum = int(input())
    find_repeatings(link, smnum)

else:
    print("Wrong imput. Shutting down.")