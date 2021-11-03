i = 0
a = [0,0,0,0,0,0,0,0,0,0]
final = 0
for i in range(0,10):
    a[i]= int(input())
    final = final + a[i] 
    i += 1
final = final / 10
print (final)
