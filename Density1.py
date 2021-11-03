HK_P= 7392000 
D_P= 57036000
D_A=42933 
HK_A=728 

HK_D = HK_P / HK_A
D_D = D_P / D_A
if HK_D <= D_D:
    print("Hong Kong has population density", HK_D)
    print("Denmark has population density", D_D)
else:
    print("Denmark has population density", D_D)
    print("Hong Kong has population density", HK_D)

input()
   
