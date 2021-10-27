i= input('Please enter a string ')
#input of a string is taken 
def max_frequent(string):
    d = dict()
# flagging or a counter is set for every alphabet 
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print (max_frequent(i))
