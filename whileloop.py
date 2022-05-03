# getting sum, count and average.
# i added try and except so user in enter wrong input
user = -1
total = 0
count = 0
while count != user:
    try:
        user = input("Enter a number: ")
        if user == "done":
            break
        total += int(user)
        count += 1
        average = total / count
    except:
        print("Invalid Input")
print("Total is: {}, Count is: {}, Average is: {}".format(total, count, average))
