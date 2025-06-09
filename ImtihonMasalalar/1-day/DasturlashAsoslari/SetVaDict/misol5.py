set1={4,5,6,7,8,9}	
set2={5,6,7,10,11}
#  ^ - .symmetric_difference
print(sum(set1 ^ set2) - sum(set1 & set2))