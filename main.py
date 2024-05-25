"""
Cesar Hideki Imai - 10402758
João Victor Dallapé Madeira - 10400725
Luiz Henrique Bonilha Pasquinelli - 10401415

Alfabeto = {+,-,*,/,(,),0,1,2,3,4,5,6,7,8,9}
Símbolo não-terminal inicial = I
Símbolo não-terminais = {I,S,K,T,Z,F,N,D}
Regras de produção:
{
I -> S
S -> TK
K -> +TK
K -> -TK
K -> (vazio)
T -> FZ
Z -> *FZ
Z -> /FZ
Z -> (vazio)
F -> (S)
F -> N
N -> 1D|2D|3D|4D|5D|6D|7D|8D|9D
D -> 0D|1D|2D|3D|4D|5D|6D|7D|8D|9D
D -> e (vazio)
}
"""


def analisador_sintatico(stack,expression):

    # Mostrar passo-a-passo (melhor escolher só um teste para executar)
    #print("Pilha: ", stack)
    #print("Expressão: ", expression)
    
    
    if len(expression) == 0: # Caso tenha lido toda a expressão
        return not (stack[-1] == "I" or stack[-1] == "T" or stack[-1] == "F")
        # Retorna False para caso I, T ou F esteja no topo da pilha, se não True
    
    elif len(expression) > 0 and len(stack) > 0: # Caso não tenha lido toda a expressão
        
        if stack[-1] == expression[0]: # Caso haja o mesmo caractere na pilha e na expressão
            stack.pop() # Remove o caractere no topo da pilha
            expression = expression[1:] # Remove o primeiro caractere da expressão
            return analisador_sintatico(stack,expression)
            
        elif stack[-1] == 'I': # Caso haja o símbolo inicial I no topo da pilha
            stack.pop()
            stack.append('S') # Adiciona S no topo da pilha
            return analisador_sintatico(stack,expression)

        elif stack[-1] == 'S': # Caso haja o símbolo S no topo da pilha
            stack.pop()
            stack.append('K')
            stack.append('T')
            return analisador_sintatico(stack,expression)

        elif stack[-1] == 'K': # Caso haja o símbolo K no topo da pilha
            if expression[0] == '+':
                stack.append('T')
                stack.append('+')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '-':
                stack.append('T')
                stack.append('-')
                return analisador_sintatico(stack,expression)
            else:
                stack.pop()
                return analisador_sintatico(stack,expression)

        elif stack[-1] == 'T': # Caso haja o símbolo T no topo da pilha
            stack.pop()
            stack.append('Z')
            stack.append('F')
            return analisador_sintatico(stack,expression)

        elif stack[-1] == 'Z': # Caso haja o símbolo Z no topo da pilha
            
            if expression[0] == '*':
                stack.append('F')
                stack.append('*')
                return analisador_sintatico(stack,expression)
            if expression[0] == '/':
                stack.append('F')
                stack.append('/')
                return analisador_sintatico(stack,expression)
            else:
                stack.pop()
                return analisador_sintatico(stack,expression)

        elif stack[-1] == 'F': # Caso haja o símbolo F no topo da pilha
            stack.pop()
            if expression[0] == '(':
                stack.append(')')
                stack.append('S')
                stack.append('(')
                return analisador_sintatico(stack,expression)
            else:
                stack.append('N')
                return analisador_sintatico(stack,expression)

        elif stack[-1] == 'N': # Caso haja o símbolo N no topo da pilha
            stack.pop()
            stack.append('D')
            if expression[0] == '1':
                stack.append('1')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '2':
                stack.append('2')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '3':
                stack.append('3')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '4':
                stack.append('4')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '5':
                stack.append('5')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '6':
                stack.append('6')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '7':
                stack.append('7')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '8':
                stack.append('8')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '9':
                stack.append('9')
                return analisador_sintatico(stack,expression)
            else:
                return False
            
        elif stack[-1] == 'D': # Caso haja o símbolo D no topo da pilha
            if expression[0] == '1':
                stack.append('1')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '2':
                stack.append('2')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '3':
                stack.append('3')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '4':
                stack.append('4')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '5':
                stack.append('5')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '6':
                stack.append('6')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '7':
                stack.append('7')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '8':
                stack.append('8')
                return analisador_sintatico(stack,expression)
            elif expression[0] == '9':
                stack.append('9')
                return analisador_sintatico(stack,expression)
            else:
                stack.pop()
                return analisador_sintatico(stack,expression)

        else:
            return False

    else:
        return False

        
def main():
    #Testes:

    # True
    t1 = "1+2*3" 
    t2 = "(4-5)/6" 
    t3 = "7*8+9" 
    t4 = "3*(8-2)" 
    t5 = "(1+2)*3" 
    t6 = "4/(5-6)" 
    t7 = "7*(8-9)" 
    t8 = "1+2*3/(4-5)" 
    t9 = "(6+7)*8-9" 
    t10 = "2*(3+4)/(5-6)" 
    t11 = "2+3*4" 
    t12 = "5/(6-7)" 
    t13 = "8*(9-1)" 
    t14 = "(6/2)+5" 
    t15 = "4/(5*6+7)"
    t16 = "7*(8-9)/1"
    t17 = "2*(3+4)/(5-6)*7"
    t18 = "2+3*4/(5-6)*7"
    t19 = "2+3*4/(5-6)*7+8"
    t20 = "2+3*4/(5-6)*7+8-9"

    # False
    t21 = "1++2" 
    t22 = "(4-)/6"
    t23 = "0"
    t24 = "()"
    t25 = "0/2"
    t26 = "1+2*3+*4"
    t27 = "231!"
    t28 = "abcd"
    t29 = "(2+3)+*4"
    t30 = "1+(2*)-3"
    t31 = "(2+/3)*4"
    t32 = "(2+3*)/4+"
    t33 = "1+2+3+4+"
    t34 = "(2+3)+4)+"
    t35 = ""
    t36 = "/2+3-4*5"
    t37 = "(2+/3+4)-5" 
    t38 = "1+(2*)3-4"
    t39 = "(2+3*)+4-"
    t40 = "/1-2+3*4"

    print("Teste 1:", analisador_sintatico(['I'],t1))
    print("Teste 2:", analisador_sintatico(['I'],t2))
    print("Teste 3:", analisador_sintatico(['I'],t3))
    print("Teste 4:", analisador_sintatico(['I'],t4))
    print("Teste 5:", analisador_sintatico(['I'],t5))
    print("Teste 6:", analisador_sintatico(['I'],t6))
    print("Teste 7:", analisador_sintatico(['I'],t7))
    print("Teste 8:", analisador_sintatico(['I'],t8))
    print("Teste 9:", analisador_sintatico(['I'],t9))
    print("Teste 10:", analisador_sintatico(['I'],t10))
    print("Teste 11:", analisador_sintatico(['I'],t11))
    print("Teste 12:", analisador_sintatico(['I'],t12))
    print("Teste 13:", analisador_sintatico(['I'],t13))
    print("Teste 14:", analisador_sintatico(['I'],t14))
    print("Teste 15:", analisador_sintatico(['I'],t15))
    print("Teste 16:", analisador_sintatico(['I'],t16))
    print("Teste 17:", analisador_sintatico(['I'],t17))
    print("Teste 18:", analisador_sintatico(['I'],t18))
    print("Teste 19:", analisador_sintatico(['I'],t19))
    print("Teste 20:", analisador_sintatico(['I'],t20))
    print("Teste 21:", analisador_sintatico(['I'],t21))
    print("Teste 22:", analisador_sintatico(['I'],t22))
    print("Teste 23:", analisador_sintatico(['I'],t23))
    print("Teste 24:", analisador_sintatico(['I'],t24))
    print("Teste 25:", analisador_sintatico(['I'],t25))
    print("Teste 26:", analisador_sintatico(['I'],t26))
    print("Teste 27:", analisador_sintatico(['I'],t27))
    print("Teste 28:", analisador_sintatico(['I'],t28))
    print("Teste 29:", analisador_sintatico(['I'],t29))
    print("Teste 30:", analisador_sintatico(['I'],t30))
    print("Teste 31:", analisador_sintatico(['I'],t31))
    print("Teste 32:", analisador_sintatico(['I'],t32))
    print("Teste 33:", analisador_sintatico(['I'],t33))
    print("Teste 34:", analisador_sintatico(['I'],t34))
    print("Teste 35:", analisador_sintatico(['I'],t35))
    print("Teste 36:", analisador_sintatico(['I'],t36))
    print("Teste 37:", analisador_sintatico(['I'],t37))
    print("Teste 38:", analisador_sintatico(['I'],t38))
    print("Teste 39:", analisador_sintatico(['I'],t39))
    print("Teste 40:", analisador_sintatico(['I'],t40))


main()