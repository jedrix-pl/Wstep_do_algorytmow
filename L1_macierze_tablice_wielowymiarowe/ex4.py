import numpy as np
import pandas as pd
from termcolor import colored


def check_data(pandasDataFrame1, pandasDataFrame2):
    correctList1 = []
    for row in range(len(pandasDataFrame1.values)):
        if str(pandasDataFrame1['Item no.'][row]) in pandasDataFrame2['Item no.'].values:
            correctList1.append(1)

    if sum(correctList1) == len(receipt_data):
        msg = "\n\tData is CORRECT\n"
        print(colored(msg, 'green'))
        return True
    else:
        msg = "\n\tData is INCORRECT\n"
        print(colored(msg, 'red'))
        return False


def total_price(pandasReceipt, pandasItemsInfo):
    total_price = 0
    for row in range(len(pandasReceipt['Item no.'].values)):
        item_no = pandasReceipt['Item no.'][row]
        quant = float(pandasReceipt['pieces/weight'][row])
        single_price = float(pandasItemsInfo[pandasItemsInfo['Item no.'] == str(item_no)]['Price'].values)
        price = single_price * quant
        total_price += price

    print("\n\tTOTAL PRICE:", total_price)


if __name__ == '__main__':
    receipt_data = np.array([[101, 1001, 3],
                            [101, 22, 2],
                            [101, 2292, 5],
                            [101, 1921, 2]])

    receipt_col_names = ['Client no.', 'Item no.', 'pieces/weight']

    RECEIPT = pd.DataFrame(receipt_data, columns=receipt_col_names)


    items_info_data = np.array([['potatoe', 1921, 1.50, 'kg'],
                                ['nutella', 2292, 9.50, 'pieces'],
                                ['book', 1001, 15.00, 'pieces'],
                                ['apple', 22, 3.00, 'kg']])

    items_info_data_col_names = ['Item', 'Item no.', 'Price', 'Measure']

    ITEMS_INFO = pd.DataFrame(items_info_data, columns=items_info_data_col_names)


    if check_data(RECEIPT, ITEMS_INFO):
        total_price(RECEIPT, ITEMS_INFO)