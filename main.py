print('Bem vindo a Loja de Gelados do Ailton de Jesus RU:4651421')
print('----------------------Cardápio--------------------')
print('------| Tamanho | Capuaçu (CP) | Açaí (AC) |------')
print('------|    P    |   R$ 10,00   |  R$ 12,00 |------')
print('------|    M    |   R$ 15,00   |  R$ 17,00 |------')
print('------|    G    |   R$ 19,00   |  R$ 21,00 |------')
print('--------------------------------------------------')
sair = True
total = 0
while sair:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    sair = True
    if (sabor == 'ac') or (sabor == 'cp'):  # verifica se o sabor foi digitado corretamente
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if (tamanho == 'p') or (tamanho == 'm') or (tamanho == 'g'):  # verifica se o tamanho foi digitado
            # corretamente
            if (tamanho == 'p') and (sabor == 'cp'):
                preco = 10
                total += preco
                print('Você pediu CAPUAÇU no tamanho P: R$10,00')
                sair = input('Deseja mais alguma coisa? (S/N)')
                if sair == 's':
                    continue
                else:
                    sair = False
            elif (tamanho == 'm') and (sabor == 'cp'):
                preco = 15
                total += preco
                print('Você pediu CAPUAÇU no tamanho M: R$15,00')
                sair = input('Deseja mais alguma coisa? (S/N)')
                if sair == 's':
                    continue
                else:
                    sair = False
            elif (tamanho == 'g') and (sabor == 'cp'):
                preco = 19
                total += preco
                print('Você pediu CAPUAÇU no tamanho G: R$19,00')
                sair = input('Deseja mais alguma coisa? (S/N)')
                if sair == 's':
                    continue
                else:
                    sair = False
            elif (tamanho == 'p') and (sabor == 'ac'):
                preco = 12
                total += preco
                print('Você pediu AÇAI no tamanho P: R$12,00')
                sair = input('Deseja mais alguma coisa? (S/N)')
                if sair == 's':
                    continue
                else:
                    sair = False
            elif (tamanho == 'm') and (sabor == 'ac'):
                preco = 17
                total += preco
                print('Você pediu Açai no tamanho G: R$17,00')
                sair = input('Deseja mais alguma coisa? (S/N)')
                if sair == 's':
                    continue
                else:
                    sair = False
            elif (tamanho == 'g') and (sabor == 'ac'):
                preco = 21
                total += preco
                print('Você pediu Açai no tamanho G: R$21,00')
                sair = input('Deseja mais alguma coisa? (S/N)')
                if sair == 's':
                    continue
                else:
                    sair = False
        else:  # printa uma mensagem na tela caso o tamanho tenha sido digitado errado
            print('Tamanho inválido. Tente novamente!')
            continue
    else:  # printa uma mensagem na tela caso o sabor tenha sido digitado errado
        print('Sabor inválido. Tente novamente!')
        continue
    print('valor total a ser pago é de: R${:.2f}'.format(total))
