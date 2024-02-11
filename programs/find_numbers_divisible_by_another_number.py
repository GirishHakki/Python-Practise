#solution 1 using for loop

# print("The numbers divisible by 13 are: ")
# for i in range(1,100):
#     if i % 13 ==0:
#         print(i)

#solution 2 using Lambda Function and Filter()

l = [39,48,26,98,33,67,87]
result = list(filter(lambda x : x % 13 == 0,l))
print("The numbers divisible by 13 are", result)