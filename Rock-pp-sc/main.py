import random

def pl():
    cm=random.choice(['r','p','s'])
    print("choice one from below")
    us=input("'r' for rock \n'p' for paper\n's' for scissor\n")
    print("><><><><><><><><><<..THE RESULT..>><><><><><><><><><\n")
    if us==cm:
        return ' Its TIE..!!\n'
    if is_wi(us,cm):
        cm=org(cm)
        return (f'CONGRATULATIONS..<><> \nYOU WON..!!!, The computers choice was {cm}\n')
    else:
        cm=org(cm)
        return (f'YOU LOST..!!, The computers choice was {cm} \n GIVE IT ANOTHER TRY..><><><')

def org(cm):
    if cm=='r':
        return 'ROCK'
    elif cm=='p':
        return 'PAPER'
    return 'SCISSOR'

def is_wi(p,opp):
    if (p=='r' and opp=='s') or (p=='s' and opp=='p') or (p=='p' and opp=='r'):
        return True
    else:
        return False

print(pl())