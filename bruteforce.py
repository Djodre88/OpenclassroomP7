import itertools

"""Open text file datas"""
with open("stocks_list.txt", "r",) as datas:
    datas = datas.read()
    datas = datas.splitlines()
    ser_datas = []
    for data in datas:
        data = data.split()
        stock_dict = {
            "name" : data[0],
            "price" : int(data[1]),
            "profit" : float(data[2][:-1])/100
            }
        stock_dict["abs"] = round(stock_dict["price"]*stock_dict["profit"], 2)
        ser_datas.append(stock_dict)
    # print(ser_datas)

def get_stocks_data_lists(ser_datas):
    stocks_name = []
    stocks_price =[]
    stocks_abs_profit = []
    for stock in ser_datas:
        stocks_name.append(stock["name"])
        stocks_price.append(stock["price"])
        stocks_abs_profit.append(stock["abs"])
    return stocks_name, stocks_price, stocks_abs_profit 

def sort_stocks_rate(ser_datas):
    """Sort sotcks based on rentability rate"""
    sorted_stocks = sorted(ser_datas, key=lambda k: k["profit"], reverse=True)
    # print(sorted_stocks)
    return sorted_stocks

def sort_stocks_abs(ser_datas):
    """Sort sotcks based on rentability rate"""
    sorted_stocks = sorted(ser_datas, key=lambda k: k["abs"], reverse=True)
    # print(sorted_stocks)
    return sorted_stocks

def buy_stocks_by_rate(capital_initial, ser_datas):
    capital_restant = capital_initial
    bought_stocks = []
    for stock in ser_datas:
        if capital_restant - stock["price"] > 0:
            capital_restant -= stock["price"]
            bought_stocks.append(stock)
            # print("\nname achetée : {}".format(stock))
            # print("Le capital restant est de {} euros".format(capital_restant))
    print("\nLe capital restant est de {} euros\n".format(capital_restant))
    return bought_stocks, capital_restant

def buy_stocks_by_abs(capital_initial, ser_datas):
    capital_restant = capital_initial
    bought_stocks = []
    # while capital_restant > 0:
    for stock in ser_datas:
        if capital_restant - stock["price"] > 0:
            capital_restant -= stock["price"]
            bought_stocks.append(stock)
                # print("\nname achetée : {}".format(stock))
                # print("Le capital restant est de {} euros".format(capital_restant))
    print("\nLe capital restant est de {} euros\n".format(capital_restant))
    return bought_stocks, capital_restant

def profitability_calculation(bought_stocks):
    stock_gain = []
    for stock in bought_stocks:
        gain = stock["price"]*stock["profit"]
        stock_gain.append(gain)
    total_gain = round(sum(stock_gain),2)
    return total_gain

def display_results(capital_initial, total_cost, capital_restant, gain, profit):
    conclusion = "\nInitial Capital : {} €\
        \nTotal cost : {} €\
        \nRemainder : {} €\
        \nProfit value: {} €\
        \nProfit rate : {} %".format(capital_initial, total_cost, capital_restant, gain, profit)
    separation = "\n========================="
    print(separation, conclusion, separation,"\n")

def main():
    capital_initial = 500
    # sorted_stocks = sort_stocks_abs(ser_datas)
    # for stock in sorted_stocks:
    #     print(stock)
    # bought_stocks = buy_stocks_by_abs(capital_initial, sorted_stocks)[0]
    # capital_restant = buy_stocks_by_abs(capital_initial, sorted_stocks)[1]
    # for stock in bought_stocks:
    #     print(stock)
    # gain = profitability_calculation(bought_stocks)
    # total_cost = capital_initial - capital_restant
    # profit = gain*100/(capital_initial)
    # display_results(capital_initial, total_cost, capital_restant, gain, profit)

    all_valable_combinaisons = []
    stocks_name = get_stocks_data_lists(ser_datas)[0]
    stocks_prices = get_stocks_data_lists(ser_datas)[1]
    stocks_abs_profit = get_stocks_data_lists(ser_datas)[2]
    for L in range(0, len(stocks_name)+1):
        for subset1, subset2, subset3 in zip(itertools.combinations(stocks_name, L), itertools.combinations(stocks_prices, L), itertools.combinations(stocks_abs_profit, L)):
            s={
                "combinaison" : subset1,
                "cost" : sum(subset2),
                "profit" : round(sum(subset3),2)
            }
            if s["cost"]>capital_initial:
                pass
            else:
                all_valable_combinaisons.append(s)
    all_sorted_combinaisons = sorted(all_valable_combinaisons, key=lambda k: k["profit"], reverse=True)
    for i in range(3):
        # print("Portefeuille {} :".format(i+1))
        print(f"Portefeuille {i+1} :")
        for action in all_sorted_combinaisons[i]["combinaison"]:
            # print("combinaison: {}".format(all_sorted_combinaisons[i]["combinaison"]))
            print(action)
        print("---------------")
        print("coût: {}".format(all_sorted_combinaisons[i]["cost"]))
        print("Profit {}\n".format(all_sorted_combinaisons[i]["profit"]))

main()
