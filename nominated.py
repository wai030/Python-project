nominated={
2013: ["Tony Leung Ka-fai", "Nick Cheung", "Chapman To", "Sean Lau", "Tony Leung Chiu-Wai"], 
2014: ["Nick Cheung", "Tony Leung Chiu-Wai", "Louis Koo", "Sean Lau", "Anthony Wong"],
2015: ["Sean Lau", "Eddie Peng", "Sean Lau", "Huang Bo", "Daniel Wu"],
2016: ["Aaron Kwok", "Andy Lau", "Nick Cheung", "Tony Leung Ka-fai", "Jacky Cheung"],
2017: ["Gordon Lam", "Shawn Yue", "Francis Ng", "Richie Jen", "Tony Leung Ka-fai"],
2018: ["Ronald Cheng", "Andy Lau", "Tian Zhuangzhuang", "Ling Man-lung"],
2019: ["Anthony Wong", "Francis Ng", "Chow Yun-fat", "Aaron Kwok", "Philip Keung"],
2020: ["Tai Bo", "Louis Koo", "Chu Pak Hong", "Aaron Kwok", "Jackson Yee"],
}
freq={}
a =[]
j = 0
for i in range(2013,2021):
    for word in nominated.get(i):
        freq[word]=freq.get(word,0)+1    
        if word not in a:
            a.append(word)
for z in range(0, len(a)):
    print (a[z], end=' ')
    print (':', end=' ') 
    print(freq.get(a[z]))
    if (j < int(freq.get(a[z]))):
        j = freq.get(a[z])
        k= a[z]
      
print("most_nom_actor = {'" + k +"'}")
