import re
import itertools

def solution(expression):
    operators = ['+', '-', '*']
    operator_permutations = list(itertools.permutations(operators))
    
    numbers = list(map(int, re.split(r'[\+\-\*]', expression)))
    operators_in_expression = re.findall(r'[\+\-\*]', expression)
    
    max_value = 0
    
    for operator_priority in operator_permutations:
        temp_numbers = numbers[:]
        temp_operators = operators_in_expression[:]
        
        for op in operator_priority:
            idx = 0
            while idx < len(temp_operators):
                if temp_operators[idx] == op:
                    if op == '+':
                        result = temp_numbers[idx] + temp_numbers[idx + 1]
                    elif op == '-':
                        result = temp_numbers[idx] - temp_numbers[idx + 1]
                    elif op == '*':
                        result = temp_numbers[idx] * temp_numbers[idx + 1]
                    
                    temp_numbers[idx] = result
                    del temp_numbers[idx + 1]  
                    del temp_operators[idx]    
                else:
                    idx += 1
        
        max_value = max(max_value, abs(temp_numbers[0]))
    return max_value