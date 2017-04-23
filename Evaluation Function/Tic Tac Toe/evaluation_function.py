def evaluate(ttt):
    for i in range(3):
        if ttt[i][0] == ttt[i][1] and ttt[i][1] == ttt[i][2]:
            if ttt[i][0] == 'x':
                return 10
            elif ttt[i][0] == '0':
                return -10
    for i in range(3):
        if ttt[0][i] == ttt[1][i] and ttt[1][i] == ttt[2][i]:
            if ttt[0][i] == 'x':
                return 10
            elif ttt[0][i] == '0':
                return -10
    if ttt[0][0] == ttt[1][1] and ttt[1][1] == ttt[2][2]:
        if ttt[0][i] == 'x':
            return 10
        elif ttt[0][i] == '0':
            return -10
    if ttt[0][2] == ttt[1][1] and ttt[1][1] == ttt[2][0]:
        if ttt[0][i] == 'x':
            return 10
        elif ttt[0][i] == '0':
            return -10

def main():
    ttt = [['x','x','-'],['0','0','0'],['-','-','-']]
    value = evaluate(ttt)
    print(value)

if __name__ == '__main__':
    main()
