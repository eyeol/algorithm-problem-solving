def solution(num_list):
    
    sum_mul = 1
    
    for num in num_list:
        sum_mul *= num
    
    if sum_mul < sum(num_list)**2:
        return 1
    
    return 0

