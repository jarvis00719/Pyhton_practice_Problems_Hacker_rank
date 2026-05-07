#Input Statements:-

##---Engilsh Newspaper---##
eng_subs = int(input())

eng_sub_roll_no = [int(i) for i in range(eng_subs)]
eng_sub_roll_no = input().split()

##----French Newspaper----##
french_subs = int(input())

french_sub_roll_no = [int(i) for i in range(french_subs)]
french_sub_roll_no = input().split()

eng_set = set(eng_sub_roll_no)
french_set = set(french_sub_roll_no)

symm_diff = eng_set.symmetric_difference(french_set)

print(len(symm_diff))
