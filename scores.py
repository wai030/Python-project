scores = {"Anna":80,  "Ben":30,  "Cindy":72, "Don":20, "Edmond": 100}
list = [score for score in scores if scores.get(score)>=40]
print(list)
