a=int(input("Enter a "))
b=int(input("Enter b"))
operator=input("Enter operator")

match operator:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '%':
        print(a%b)
    case '//':
        print(a//b)
    case '**':
        print(a**b)