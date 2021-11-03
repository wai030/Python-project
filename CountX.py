##Write a for loop to ask the user to enter 5 words or phrases, then count
##the number of words that contains the letter “x” (non-case-sensitive).
i = 0
final = 0
a = [None] *5
for i in range(0,5):
    a [i]= input().count("x")
    final = final +a[i]
print(final)
input()

    

