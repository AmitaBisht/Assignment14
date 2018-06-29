with open("passage.txt") as file:
    with open ("test.txt" ,"w") as f1:
        for line in file:
            f1.write(line)
