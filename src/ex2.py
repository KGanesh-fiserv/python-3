import csv
def find_total_visits():
    def readtotalvisits(file, visits):
        with open(file) as csv_file:
            rows = csv.reader(csv_file, delimiter=",")
            for row in rows:
                for val in row:
                    if val == ' 1':
                        visits += 1
        return visits
    total_visits = 0
    total_visits = readtotalvisits("files\week-1.csv", total_visits)
    total_visits = readtotalvisits("files\week-2.csv", total_visits)
    total_visits = readtotalvisits("files\week-3.csv", total_visits)
    return total_visits



def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()