print('select korean(1) or english(2)')
language=int(input(':'))


if language==1:
    print('+ - * / 에서 하나를 고르세요')
    calcul_math_enter = input(':')
    try:
        if calcul_math_enter == '+':
            print("n+n같이 입력하세요 ('n은 숫자입니다.')")
            a, b = map(int, input('').split('+'))
            calcul_math_answer = a + b
            print(calcul_math_answer)
        elif calcul_math_enter == '-':
            print("n-n같이 입력하세요 ('n은 숫자입니다.')")
            a, b = map(int, input('').split('-'))
            calcul_math_answer = a - b
            print(calcul_math_answer)
        elif calcul_math_enter == '*':
            print("n*n같이 입력하세요 ('n은 숫자입니다.')")
            a, b = map(int, input('').split('*'))
            calcul_math_answer = a * b
            print(calcul_math_answer)
        elif calcul_math_enter == '/':
            print("n/n같이 입력하세요 ('n은 숫자입니다.')")
            a, b = map(int, input('').split('/'))
            calcul_math_answer = a / b  # 나누기 연산 수정
            print(calcul_math_answer)
        else:
            print('err.calculator')
    except ValueError:
        print('에러:숫자를 입력하세요.')
    except ZeroDivisionError:
        print('에러:0으로 나눌수 없습니다.')
    except Exception as e:
        print(f'에러: {e}')
elif language==2:
    print('select in + - * / ')
    calcul_math_enter = input(':')
    try:
        if calcul_math_enter == '+':
            print("enter like n+n ('n is number')")
            a, b = map(int, input('').split('+'))
            calcul_math_answer = a + b
            print(calcul_math_answer)
        elif calcul_math_enter == '-':
            print("enter like n-n ('n is number")
            a, b = map(int, input('').split('-'))
            calcul_math_answer = a - b
            print(calcul_math_answer)
        elif calcul_math_enter == '*':
            print("enter like n*n ('n is number")
            a, b = map(int, input('').split('*'))
            calcul_math_answer = a * b
            print(calcul_math_answer)
        elif calcul_math_enter == '/':
            print("enter like n/n ('n is number)")
            a, b = map(int, input('').split('/'))
            calcul_math_answer = a / b  # 나누기 연산 수정
            print(calcul_math_answer)
        else:
            print('err.calculator')
    except ValueError:
        print('error: enter number')
    except ZeroDivisionError:
        print('error: ZeroDivisionError')
    except Exception as e:
        print(f'error: {e}')