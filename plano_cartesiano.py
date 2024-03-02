# Proposta A:
print('Proposta A: Imagine um plano cartesiano, agora vamos deslocar ele em um certo número para as abscissas e outro número às ordenadas.')
# Importação de Bibliotecas:
import math as m
# Dados de Entrada:
abscissas_x = int(input('\nDigite um valor de deslocamento no eixo das abscissas (X): '))
ordenadas_y = int(input('Digite um valor de deslocamento no eixo das ordenadas (Y): '))
quantidade_pontos = int(input('\nQuantos pontos você quer analisar?: '))
# Outras variáveis
contador = 1
distancia_maxima = 0
distancia_minima = m.sqrt(m.inf**2 + m.inf**2)
ponto_dist_min = ''
quadrantes = ''
pontos_1 = 0
pontos_2 = 0
pontos_3 = 0
pontos_4 = 0
# Início do Algoritmo:
while contador != quantidade_pontos+1:
    ponto = input(f'\nDigite a coordenada do {contador}º ponto. Siga o exemplo: 3 7: ')
    if ponto.strip().find(' ') == -1 and ponto.split()[0] != int and ponto.split()[len(ponto.split()) - 1] != int: # Corrigindo os dados inseridos
        print('Valor inválido! Deve conter espaço entre dois números inteiros, sem parênteses.')
        continue
    ponto = ponto.split()
    x_ponto = int(ponto[0])
    y_ponto = int(ponto[1])
    distancia = m.sqrt((x_ponto - abscissas_x)**2 + (y_ponto - ordenadas_y)**2) # Aplicando a fórmula de distância:
    if distancia > distancia_maxima: # Alterando as distâncias máxima e mínima:
        distancia_maxima = distancia
        ponto_dist_max = f'({x_ponto}, {y_ponto})'
    if distancia < distancia_minima:
        distancia_minima = distancia
        ponto_dist_min = f'({x_ponto}, {y_ponto})'
# Configurando os quadrantes:
    if x_ponto - abscissas_x > 0  and y_ponto - ordenadas_y > 0:
        quadrantes += f'O ponto ({x_ponto}, {y_ponto}) está no 1º quadrante em sua forma transladada.\n'
        pontos_1 += 1
    elif x_ponto - abscissas_x < 0 and y_ponto - ordenadas_y > 0:
        quadrantes += f'O ponto ({x_ponto}, {y_ponto}) está no 2º quadrante em sua forma transladada.\n'
        pontos_2 += 1
    elif x_ponto - abscissas_x < 0 and y_ponto - ordenadas_y < 0:
        quadrantes += f'O ponto ({x_ponto}, {y_ponto}) está no 3º quadrante em sua forma transladada.\n'
        pontos_3 += 1
    elif x_ponto - abscissas_x > 0 and y_ponto - ordenadas_y < 0:
        quadrantes += f'O ponto ({x_ponto}, {y_ponto}) está no 4º quadrante em sua forma transladada.\n'
        pontos_4 += 1
    elif x_ponto - abscissas_x == 0 and y_ponto - ordenadas_y == 0:
        quadrantes += f'O ponto ({x_ponto}, {y_ponto}) está na origem do plano em sua forma transladada.\n'
    elif x_ponto - abscissas_x == 0 and y_ponto - ordenadas_y != 0:
        quadrantes += f'O ponto ({x_ponto}, {y_ponto}) está sob o eixo das ordenadas em sua forma transladada.\n'
    elif x_ponto - abscissas_x != 0 and y_ponto - ordenadas_y == 0:
        quadrantes += f'O ponto ({x_ponto}, {y_ponto}) está sob o eixo das abscissas em sua forma transladada.\n'
    contador += 1
# Saídas:
print('\n', quadrantes)
print(f'O ponto com maior distância é {ponto_dist_max}, com distância de {distancia_maxima: .2f}'.replace('.', ','))
print(f'O ponto com menor distância é {ponto_dist_min}, com distância de {distancia_minima: .2f}'.replace('.', ','))
print(f'Existem {pontos_1} pontos no primeiro quadrante.')
print(f'Existem {pontos_2} pontos no segundo quadrante')
print(f'Existem {pontos_3} pontos no terceiro quadrante')
print(f'Existem {pontos_4} pontos no quarto quadrante')

# Proposta B:
print('\nProposta B: Agora, vamos imaginar um robô que a todo o deslocamento anda uma unidade em Y, e duas em X.')
# Dados de Entrada:
inicio_robo = input('\nDigite o ponto em que o robô irá iniciar sua trajetória. Siga o exemplo: -3 15: ')
deslocamento = int(input('Digite o valor do deslocamento do robô: '))
# Formatando Variável
x_inicio = int(inicio_robo.split()[0])
y_inicio = int(inicio_robo.split()[1])
#Condições:
if deslocamento % 3 == 0: # Se for divisível por 3
    x_inicio += (deslocamento // 3) * 2
    y_inicio += deslocamento // 3
elif deslocamento % 3 == 1: # Se não, se o resto for 1
    x_inicio += (deslocamento // 3) * 2
    y_inicio += deslocamento // 3 + 1
else: # Se não, se o resto for 2
    x_inicio +=  2 * (deslocamento // 3) + 1
    y_inicio += deslocamento//3 + 1
print(f'\nCom o deslocamento de {deslocamento} unidades, o robô parará no ponto ({x_inicio}, {y_inicio}) ')




















