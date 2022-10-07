


MAX_LINE= 8
MAX_BET = 500
MIN_BET = 1



def deposit():
    while True: 
        amount = input ("what do like to deposit ? $ ")
        if amount.isdigit():
            amount= int(amount)
            if amount > 0:
                break
            else :
                print("amount must be greater than zero. please try again :-( ")
        else :
                print("please entre a number")
    return amount

def get_number_of_lines():
    while True: 
        lines = input ("Entre how many line you want to bet on (1 - "+str(MAX_LINE)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINE:
                break
            else :
                print("entre the valid number of lines")
        else :
                print("please entre a number")
    return lines
def bet ():
    while True: 
        amount = input ("what do like to bet on each line  ? $ ")
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else :
                print(f"amount must be between  ${MIN_BET} - ${MAX_BET} .")
        else :
                print("please entre a number")
    return amount













def main():
    balance= deposit()
    lines= get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines 
        if total_bet >balance:
            print(f"YOU do not have enough to bet that amount,your current balance is : {balance}")
        else:
            break
    
    print(f"you are betting &{bet} on {lines} lines . Total bet is equal to :{total_bet} ")

main()



