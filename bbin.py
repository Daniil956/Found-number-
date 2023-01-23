from random import randint

x= randint(0,100)

count_perebor=0
for i in range (0, 101):
    count_perebor+=1
    if i==x:
        print("Число найдено")
        break

# print ("Найдено число", x , "после стольких попыток" ,count_perebor,)




counut_random =1 
mid = randint(0, 100)
while x!=mid:
    mid=randint(0,100)
    counut_random+=1

# print ("Найдено число", x , "после стольких попыток" ,counut_random,)

count_bin = 0
print("Давай начём игру - угадай число от 0 до 100")

left = 0
right = 100

mid = (left + right) // 2

mid = int (input ("Введите число: "))
while x!=mid:
    print (mid)
    if x<mid: 
        print ("меньше")
        right = mid +1

    else: 
        print ("больше")
        left = mid - 1
    mid = (left + right) // 2
    # mid= int(input("Введите число: "))
    count_bin+=1
    
print ("Найдено число", x , "после стольких попыток" ,count_bin,)
