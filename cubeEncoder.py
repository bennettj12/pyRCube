import rCube as R
import base64
import random
import string
from tkinter import Tk
from tkinter.filedialog import askopenfilename
# cubeEncoder.py
# Contains methods that take in cubes and spit out encoded strings, or takes in strings and converts them to cubes

# raw encoded string:      TOP      FRONT     LEFT      RIGHT     BACK     BOTTOM
#                       ccccccccc,ccccccccc,ccccccccc,ccccccccc,ccccccccc,ccccccccc
#       w w w
#       w 1 w
#       w w w
# o o o g g g r r r b b b
# o 3 o g 2 g r 4 r b 5 b
# o o o g g g r r r b b b
#       y y y
#       y 6 y
#       y y y


def random_string_generator(size=6, chars=string.ascii_uppercase
                            + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def save_cube_to_file(cube, path="", name=""):
    rand_string = random_string_generator(8)
    if path != "":
        path = path + '/'
    if name == "":
        path = path + 'Cube' + rand_string + '.pycube'
    else:
        path = path + name + '.pycube'
    cube_string = encodeCube(cube)
    output = open(path, 'w')
    result = output.write(cube_string)
    output.close()
    print("Cube saved: " + path)
    return path


def open_cube_from_file(path=""):
    if path == "":
        extension = '.pycube'
        ftypes = [
            ('pyrCube state files', extension),
            ('All files', '*'),
        ]
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        # show an "Open" dialog box and return the path to the selected file
        filename = askopenfilename(title="Select cube", filetypes=ftypes)
    else:
        filename = path
    cube_file = open(filename, 'r')
    cube_string = cube_file.read()
    print(cube_string)
    print(len(cube_string))
    if len(cube_string) == 72:
        return decodeCube(cube_string)
    else:
        return None


def sideString(side):
    matrix = side.side
    arr = matrix[0] + matrix[1] + matrix[2]
    return ''.join(arr)


def sideString_to_Side(s):
    # this function accepts a sidestring and turns it into a side
    if len(s) != 9:
        return None
    side = R.Side('z')
    side.setRow(0, [s[0], s[1], s[2]])
    side.setRow(1, [s[3], s[4], s[5]])
    side.setRow(2, [s[6], s[7], s[8]])
    return side


def encodeCube(cube):
    # This function accepts a cube object and returns a bytestring
    top = sideString(cube.white)
    front = sideString(cube.green)
    left = sideString(cube.orange)
    right = sideString(cube.red)
    back = sideString(cube.blue)
    bottom = sideString(cube.yellow)

    cube_string = (top + front + left + right + back + bottom)
    cube_string = cube_string.encode()
    based = base64.b64encode(cube_string)
    based = based.decode()
    return based


def decodeCube(base64_cube_string):
    # This function accepts bytes and returns a cube object
    cube_string = base64.decodebytes(
        base64_cube_string.encode()
    ).decode()

    # Defining splitting point
    n = 9
    # Using list comprehension
    sideStrings = [(cube_string[i:i+n]) for
                   i in range(0, len(cube_string), n)]
    sides = []
    for sideString in sideStrings:
        sides.append(sideString_to_Side(sideString))
    cube = R.rCube()
    cube.white = sides[0]
    cube.green = sides[1]
    cube.orange = sides[2]
    cube.red = sides[3]
    cube.blue = sides[4]
    cube.yellow = sides[5]

    return cube


def main():
    # create a cube, save it to a file, then open it back up
    cube = R.rCube()
    cube.randomize()
    cube.print()
    path = save_cube_to_file(cube, "", "myRandomCube")
    cube2 = open_cube_from_file(path)
    cube2.print()


if __name__ == '__main__':
    main()
