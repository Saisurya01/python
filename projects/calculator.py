print('mini calculator')
try:
    while True:
        choice=input("enter Your choice (+,-,*,/): ").lower()
        if (choice!='+' and choice!='-'and choice!='*'and choice!='/'):
            print('invalid input..!')
            continue
        else:
            num1=float(input('Enetr 1st number: '))
            num2=float(input('Enter 2nd number: '))

            if choice=='+':
                print(round(num1+num2,2))
            if choice=='-':
                print(round(num1-num2,2))
            if choice=='*':
                print(round(num1*num2,2))
            if choice=='/':
                print(round(num1/num2,2))

        should_con=input('you want to again use it.. now (y/n): ').lower()
        if should_con=="n":
            print('exiting...')
            break
except ZeroDivisionError:
    print("zero's are not allowed for division....")
except:
    print('invalid input... it allows only numbers')



