## Q1
from solutions import freq_word
s='python is easy and python is powerful'.split()
print(freq_word(s))
## Q2
from solutions import freq_char
s='banana'
print(freq_char(s))
## Q3
from solutions import non_repeat_char 
s='swiss'
print(non_repeat_char(s))
## Q4 
from solutions import anagram_check
s1='silent'
s2='listen'
print(anagram_check(s1,s2))
## Q5
from solutions import repeating_char
s='programming'
print(repeating_char(s))
## Q6
from solutions import zeros_to_end
l=[0,3,0,1,2,0,4]
print(zeros_to_end(l))
## Q7
from solutions import second_highest
l=[10,20,40,30,40,20]
print(second_highest(l))
## Q8
from solutions import remove_duplicates
l=[4,2,4,5,2,7,5]
print(remove_duplicates(l))
## Q9
from solutions import missing_number
nums=[1,2,4,5,6]
print(missing_number(nums))
## Q10
from solutions import target_sum
l=[2,7,11,15]
target=9
print(target_sum(l,target))
## Q11
from solutions import closets_to_zero
l=[-8,-3,5,-2,2]
print(closets_to_zero(l))
## Q12
from solutions import common_values
l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
print(common_values(l1,l2))
## Q13
from solutions import rotate
l=[1,2,3,4,5]
k=2
print(rotate(l,k))
## Q14
from solutions import consecutive_sum
l=[4,7,2,9,5]
print(consecutive_sum(l))
## Q15 
from solutions import pairs_of_target
l=[2,4,3,5,7,8,1]
inp=9
print(pairs_of_target(l,inp))