import boto3
from botocore.exceptions import ClientError

def calculate():
    with open("calculator-log.txt", "w") as file:
        u_input = ""
        while True:
            x= input("Enter first number: ")
            if x == "q":
                break
            y=input("Enter second number: ")
            if y == "q":
                break
            file.write(x + " + " + y + " = " + str((int(x)+ int(y)))+"\n")


def ex4():
    calculate()
    print('*** Uploading file to S3 ***')
    s3_client = boto3.client('s3')
    file = 'calculator-log.txt'
    bucket_name = 'sia-test-bucket'
    key_path = '2023/March/Meeting Minutes/notes.txt'
    try:
        response = s3_client.upload_file(file, bucket_name, key_path)
        print(response)  # No news is good news!
    except ClientError as e:
        print(e)
    
    ex4()
