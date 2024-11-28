def arithmetic_arranger(problems, show_answers=False):
    # Too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Lists to hold each line of the final output
    first_line, second_line, dashes, answers = [], [], [], []
    
    for problem in problems:
        # Split into components
        parts = problem.split()
        operand1, operator, operand2 = parts[0], parts[1], parts[2]
        
        # Check operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if numbers only contain digits
        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check if numbers are within four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Calculate width for formatting
        width = max(len(operand1), len(operand2)) + 2
        
        # Build each line
        first_line.append(operand1.rjust(width))
        second_line.append(operator + operand2.rjust(width - 1))
        dashes.append('-' * width)
        
        # Calculate answers if required
        if show_answers:
            answer = str(eval(problem))
            answers.append(answer.rjust(width))
    
    # Combine lines with proper spacing between problems
    arranged_problems = '\n'.join([
        '    '.join(first_line),
        '    '.join(second_line),
        '    '.join(dashes)
    ])
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
