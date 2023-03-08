# Your task is to write a function maskify, which changes all but the last four characters into '#'.

cc = input("Enter pin :")

def maskify(cc):
    new_string = ''
    if len(cc) > 4:
        new_string += '#' * (len(cc) - 4) + cc[-4:]
    else:
        return cc
    return new_string

print(maskify(cc))
