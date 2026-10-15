## Q1
def freq_word(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
## Q2
def freq_char(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
## Q3
def non_repeat_char(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for key,value in d.items():
        if value==1:
            return key
## Q4
def anagram_check(s1,s2):
    valid=True
    if sorted(s1)==sorted(s2):
        return valid
    else:
        valid=False
        return valid
## Q5
def repeating_char(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for key,value in d.items():
        if value>1:
            return key
## Q6
def zeros_to_end(l):
    non_zeros=[]
    zeros=[]
    result=[]
    for i in l:
        if i==0:
            zeros.append(i)
        else:
            non_zeros.append(i)
    result=non_zeros+zeros
    return result
## Q7
def second_highest(l):
    first=second=float('-inf')
    for i in l:
        if i>first:
            second=first
            first=i
        elif i>second and i!=first:
            second=i
    return second
## Q8 
def remove_duplicates(l):
    d=[]
    for i in l:
        if i not in d:
            d.append(i)
    return d
## Q9
def missing_number(nums):
    n=len(nums)+1
    expected_sum=n*(n+1)//2
    actual_sum=sum(nums)
    missing_value=expected_sum - actual_sum
    return missing_value
## Q10
def target_sum(l,target):
    s=set()
    pair=[]
    for i in l:
        complement=target-i
        if complement in s:
            pair.extend((complement,i))
        s.add(i)
    return pair
## Q11
def closets_to_zero(l):
    close_value=l[0]
    for i in l:
        if abs(i)<abs(close_value):
            close_value=i
        elif abs(i)==abs(close_value) and i>close_value:
            close_value=i
    return close_value
## Q12
def common_values(l1,l2):
    common=[]
    for i in l1:
        for j in l2:
            if i==j:
                if i not in common:
                    common.append(i)
    return common
## Q13
def rotate(l,k):
    n=len(l)
    result=[]
    k=k%n
    result=l[-k:]+l[:-k]
    return result
## Q14
def consecutive_sum(lis):
    max_sum=lis[0]+lis[1]
    current_sum=0
    for i in range(1,len(lis)-1):
        current_sum=lis[i]+lis[i+1]
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum
## Q15
def pairs_of_target(n,target):
    s=set()
    pairs=[]
    for i in n:
        complement=target-i
        if complement in s:
            pairs.append([complement,i])
        s.add(i)
    return pairs








