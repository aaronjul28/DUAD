counter=0
numbers_list=[]
while (counter != 3):
    counter=counter+1
    number=input(f'#{counter} > Enter a random number: ')
    numbers_list.append(number)

numbers_list.sort()
numbers_list .reverse()
print(f"The highest number is {numbers_list[0]}")
