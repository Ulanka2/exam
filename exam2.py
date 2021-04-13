def depos(user, user_want):
    month = 1 
    while user < user_want:
        cash = 0.12 * user + user
        user = int(cash)
        print(user)
        month += 1
    else:
        return("your money: " + str(month) + 'month')
print(depos(int(input('wich many input yuor money:? ')), int(input(' How many get money?  '))))
