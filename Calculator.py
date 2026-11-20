# Creating a place to store answers
answer_store = []

#define calculator function

def calculator():
    #Titling and info
    print('Python Calculator')
    print('Use only +(add), -(sub), *(mult), /(divide(dont divide by 0)), **(exponent(use a decimal if you want to root it))')

    while True:
        # Calculator setup
        num1 = input('first number here---> ')


        #Store logic
        if num1 == 'store':
            if len(answer_store) == 0:
                print('no values stored')
                continue
            print(answer_store)
            index = int(input('which store index would you like to use? (indexes start from 0) '))
            num1 = answer_store[index]

        operator = input('put operator here ---> ')

        num2 = input('second number here---> ')

        #Store logic
        if num2 == 'store':
            if len(answer_store) == 0:
                     print('no values stored')
                     continue
            print(answer_store)
            index = int(input('which store index would you like to use? (indexes start from 0) '))
            num2 = answer_store[index]

        # If all info is ready then:
        if num1 and num2 and operator:

            """
             Convert the inputs into numbers that can handle decimals 
             (inputs are usually strings so it is vital for this step)
             """


            new_num1 = float(num1)
            new_num2 = float(num2)

            if operator == '+':
                result = new_num1 + new_num2
            elif operator == '-':
                result = new_num1 - new_num2
            elif operator == '*':
                result = new_num1 * new_num2
            elif operator == '/':
                if new_num2 == 0:
                    print("No way to divide by zero")
                    continue
                result = new_num1 / new_num2
            elif operator == '**':
                result = new_num1 ** new_num2
            else:
                print("Not listed operator")
                continue

            # Get result and store in answer_store
            answer_store.append(result)
            print(f"result: {result}")

# Execute
calculator()
