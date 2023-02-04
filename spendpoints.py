import csv
import sys

def spend_points(spend_amount):
    n= spend_amount
    payer_points = {}
    transactions = []
    
    with open('transactions.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            payer = row['payer']
            points = int(row['points'])
            timestamp = row['timestamp']
            transactions.append((timestamp, payer, points))
            

    transactions.sort(key=lambda x: x[0])
    # print(transactions)
    temp=0
    for transaction in transactions:
        timestamp, payer, points = transaction
        if payer not in payer_points:
            payer_points[payer] = points
        else:
            payer_points[payer] += points
            if(payer_points[payer]<0):
                payer_points[payer] -= points
                temp = 0-points
                continue
        
        if spend_amount > 0:
            x=payer_points[payer] + temp
            if x > 0:
                spend = min(spend_amount, x)
                payer_points[payer] -= (spend+temp)
                spend_amount -= (spend+temp)
                temp=0
        
        for k,v in payer_points.items():
            if(v<0):
                payer_points[k] = 0
                print('not enough points from payers to spend {} points'.format(n))

    return payer_points

if __name__ == '__main__':
    spend_amount = int(sys.argv[1])
    result = spend_points(spend_amount)
    print(result)
