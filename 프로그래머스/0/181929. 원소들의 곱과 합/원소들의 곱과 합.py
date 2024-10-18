def solution(num_list):
    answer = 0
    
    sum_add = 0
    sum_mul = 1
    
    for num in num_list:
        sum_add += num
        sum_mul *= num
    
    if sum_mul < sum_add**2:
        answer = 1
    
    return answer

