from pandas import read_csv

discounts = read_csv('./discounts.csv')

t_shirt = read_csv('./t_shirt.csv')

if __name__ == '__main__':
    print(t_shirt)
    print(discounts)