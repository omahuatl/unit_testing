"""
Created on May 9th 2022
@author: OAMA

simple program to understand UNIT TEST

"""
def cuboid_volume(l):
    if type(l) not in [int,float]:
        raise TypeError("The length of cuboid can only be a valid integer or a float")
    return (l*l*l)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(cuboid_volume(10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
