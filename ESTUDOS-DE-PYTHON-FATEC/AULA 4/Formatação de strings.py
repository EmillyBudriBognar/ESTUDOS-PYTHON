# Formatação de strings

# 1ª forma (interpolação)
r = 'Oi %s! Você tem %d anos e recebe R$ %.2f' % (n, i, s)
print(r)

# 2ª forma (método format)
r = 'Oi {}! Você tem {} anos e recebe R$ {:.2f}'.format(n, i, s)
print(r)

# 3ª forma (f-strings)
r = f'Oi {n}! Você tem {i} anos e recebe R$ {s:.2f}'
