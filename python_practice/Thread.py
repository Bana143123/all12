# import threading
# import time

# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#         time.sleep(1)

# def print_letters():
#     for letter in "abcde":
#         print(f"Letter: {letter}")
#         time.sleep(1)

# # Creating threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Starting threads
# thread1.start()
# thread2.start()

# # Waiting for both threads to finish
# thread1.join()
# thread2.join()

# print("Both threads have finished.")
import requests
import csv
s=requests.get("https://reqres.in/api/users?page=3&per_page=2")
print(s)
if s.status_code==200:
    d=s.json()
    print(d)
    dat=d.get("data",[])
    print(dat)
    file="C:\\Users\\Span63\\Downloads\\users_data.csv"
    with open(file,mode="w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["id","email","first_name","last_name","avatar"])
        for des in dat:
            writer.writerow([des["id"],des["email"],des["first_name"],des["last_name"],des["avatar"]])
    print("data has saved successfully")
else:
    print("getting error code")

