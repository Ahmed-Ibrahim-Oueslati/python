def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return ('Error: Too many problems.')
    for i in problems:
        if i.split()[1] not in ['+','-']:  
            print("Error: Operator must be '+' or '-'.")
            return
        for j in i.split():
            if len(j) > 4:
                print('Error: Numbers cannot be more than four digits.')
                return 
            if not (j.isdigit()) and j not in ['+','-'] :
                    print(j)
                    print('Error: Numbers must only contain digits.')
                    return
        h = i.split()
        lenx = max (len(i.split()[0]),len(i.split()[2],))
        print(lenx)
        print(i.split()[0])
        print(i.split()[1],i.split()[2])

        p = lenx  + 2
        dash = ''
        for i in range(p):
             dash = dash +'-'
        print(dash)
        

print(f'\n{arithmetic_arranger(["32 + 6982", "3801 - 2", "45 + 43", "123 + 49"])}')