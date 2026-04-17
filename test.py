import matplotlib.pyplot as plt

def breaking_records(score):

    max_score,min_score = score[0] ,score[0]
    
    max_record_break = 0
    lowest_record_break = 0

    res = []
    for s in (score):
        if s>max_score:
            max_record_break +=1


        elif s<min_score:
            lowest_record_break +=1
            

        
        
    return max_record_break, lowest_record_break




#Input Statements!!
no_of_games = int(input())
scores = list(map(int, input().split()))

print(breaking_records(scores))





    





        



