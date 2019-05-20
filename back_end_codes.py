def Jules (string1, string2):
    string1_split=string1.split()
    string2_split=string2.split()

    print (string1_split, string2_split)
    new_list = []
    for i in range (len(string2)):
        for string1_split[i] in string2:
            new_list.append(string1_split[i])
    return new_list

String1 = input ("Enter your first String: ")
String2 = input ("Enter your second string: ")

print (Jules(String1, String2))