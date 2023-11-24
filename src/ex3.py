import os
 
def create_files(name:str) -> int:
    # Get word.txt from files directory
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    dir=dir.replace('src', 'files')
    os.chdir(dir)
   
    #Open/Modify files
    with open(name, "r") as input_file, open("large-words.txt", "w") as large, open("small-words.txt", "w") as small:
        unique = set()
        for line in input_file:
            for word in line.strip().split():
                if word not in unique:
                    unique.add(word)
                    if len(word) >= 3: large.write(word+"\n")
                    else: small.write(word+"\n")
        return len(unique)
 
 
 
def ex3():
    total_words = create_files("words.txt")
    print(f"Total words: {total_words}.")
 
ex3()