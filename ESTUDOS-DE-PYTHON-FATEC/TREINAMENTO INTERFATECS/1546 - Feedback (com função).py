def responsavel(feedback):
    if feedback == 1:
        return 'Rolien'
    elif feedback == 2:
        return 'Naej'
    elif feedback == 3:
        return 'Elehcim'
    else:
        return 'Odranoel'

def direciona_feedbacks():
    qtd_feedbacks = int(input())
    while qtd_feedbacks > 0:
        feedback = int(input())
        print(responsavel(feedback))
        qtd_feedbacks -= 1

def main():
    qtd_dias = int(input())
    while qtd_dias > 0:
        direciona_feedbacks()
        qtd_dias -= 1

main()
