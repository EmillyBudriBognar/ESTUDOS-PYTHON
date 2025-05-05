qtd_dias = int(input())

while qtd_dias > 0:
    qtd_feedbacks = int(input())
    
    while qtd_feedbacks > 0:
        feedback = int(input())
        if feedback == 1:
            print('Rolien')
        elif feedback == 2:
            print('Naej')
        elif feedback == 3:
            print('Elehcim')
        else:
            print('Odranoel')
        qtd_feedbacks -= 1

    qtd_dias -= 1

