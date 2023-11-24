from ValidationException import ValidationException


def validate_file(filepath):
    with open(filepath, "r") as file:
        line = file.readline()
        while line:
            line  = file.readline()
            x = line.split(",")
            try: 
                type(int(x[1]))
            except:
                raise ValidationException("Invalid mileage: " + x[1])
        print("No ints contained in file")

def ex1():
    try:
        validate_file("files\input.txt")
    except ValidationException as ve:
        print(ve)

ex1()