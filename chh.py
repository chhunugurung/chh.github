def num_divide3(num):
    count=0
    for i in range(1, num+1):
        if i%3 == 0:
            count=count+1
    return count        

while True:
    user_input=input("please enter a positive integer or 'done' to terminate program: ")
    if user_input=='done':
        break

    try:
        num=int(user_input)
        if num<=0:
            print("please enter a positive number. ")
        else:
            result=num_divide3(num)
            print(f"The numbers divisible by 3 among numbers from 1 to {num}:{result} ")
    except:
          print("invalid input.")          