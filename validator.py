import json
import requests
import os
import time

print(' ------------------------------WELCOME TO DARKWEBDEITY VALIDTOR TOOL---------------------------             ')
print('')

print('Select services')
print('Type 1 for Loqate')
print('Type 2 for numverify')
input_value=input("Enter option  ")

if input_value == "1":
    key=input('Enter your loqate Key:')
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        #code for api
        response = requests.get("https://services.postcodeanywhere.co.uk/PhoneNumberValidation/Interactive/Validate/v2.20/json3.ws?=&Key="+key+"&Phone="+number)
        Firstjson= response.json()
        Convjson = json.dumps(Firstjson)
        stripjson = Convjson[11:]
        stripjson=stripjson[:-2]
        newjson=json.loads(stripjson)

        if newjson['IsValid'] =="Yes":
           status="VALID"
           f = open("Results/"+newjson['NetworkName']+".txt", "a")
           f.write(newjson['PhoneNumber']+"\n")
           f.close()
           print(newjson['PhoneNumber']+" => "+status)

        elif newjson['IsValid'] == "No":
            status="INVALID"
            f = open("invalid.txt", "a")
            f.write(number+"\n")
            f.close()
            print(number+" => "+status)
    
    file.close()
    x=input("thanks")
     
elif input_value == "2":
    key=input('Enter your numverify Key:')
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        #code for api
        response = requests.get("http://apilayer.net/api/validate?access_key="+key+"&number="+number)
        results= response.json()

        if results['success']== False:
            print('Please check your api key and try again')
            thanks=input()
            exit()
        if results['valid'] ==True:
               status="VALID"
               f = open("Results/"+results['carrier']+".txt", "a")
               f.write(results['international_format']+"\n")
               f.close()
               print(results['international_format']+" => "+status)

        elif results['valid'] ==False:
               status="INVALID"
               f = open("invalid.txt", "a")
               f.write(number+"\n")
               f.close()
               print(number+" => "+status)
        time.sleep(2)
            
    file.close()
    x=input("thanks")







