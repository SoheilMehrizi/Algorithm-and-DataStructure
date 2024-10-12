import hashlib
i = 0
while True:
    i += 1
    data = f"My name is Soheil and 9812101100 is my student number. {i}"

    #setup the sha256 from hashlib 
    m = hashlib.sha256()

    #input the data to the object
    m.update(data.encode('utf-8'))

    #Hash the data in the hexadecimal format
    hash = m.hexdigest()

    """
    now I should Proof that I worked Hard
    to hashing the data not Just using some libraries :)
    So Should Change the Program to return last 4 character of
    Hexa Decimal Hashed Value to '1111'
    """

    if hash[-4:] == '1111':
        print(f"Found it: {data} and it hashed to : {hash}")
        break
