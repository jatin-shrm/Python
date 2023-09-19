#Print the sum of the current number and the previous number
num=int(input("Enter the number till you want the sum "))
curr_num=0
prev_num=0
for i in range(1,num+1):
    sum=curr_num+prev_num
    prev_num=curr_num
    curr_num=i
    print(f"Current number is {curr_num} and Previous number is {prev_num} and the sum is {sum}")