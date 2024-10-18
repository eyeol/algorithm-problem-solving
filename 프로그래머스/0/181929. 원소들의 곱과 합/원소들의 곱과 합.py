def solution(num_list):
    
    num_mul = 1
    for num in num_list:
        num_mul *= num
    
    return int(num_mul < sum(num_list)**2)
    
    
