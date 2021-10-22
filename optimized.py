
def open_file(filename):    
    """Open txt file datas"""
    with open(filename, "r",) as datas:
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
    return ser_datas

def optimized_solution(ser_datas, cout_max):
    """ Gets serialized stocks 
        and calculates the best return on investment
    """

    benef_list = []
    cout_list = []
    for action in ser_datas:
        benef_list.append(action["abs"])
        cout_list.append(action["price"])

    # print(cout_list)
    # print(benef_list)

    # cout_max = 15
    # benef_list = [1, 2, 3, 7, 10]
    # cout_list = [2, 5, 7, 12, 9]

    B=[]

    for i in range(len(benef_list)+1):
        if i==0:
            sol=[]
            for j in range(cout_max+1):            
                sol.append(0)
            B.append(sol)
        else:
            sol=[]
            for j in range(cout_max+1):
                if j < cout_list[i-1]:
                    sol.append(B[i-1][j])
                else:
                    sol.append(max(B[i-1][j], (B[i-1][j-cout_list[i-1]]) + benef_list[i-1]))
            B.append(sol)

    print(f"La solution optimale rapporte {round(B[i][cout_max],2)} euros")

def main():
    filename = "stocks_list.txt"
    cout_max = 500
    ser_datas = open_file(filename)

    optimized_solution(ser_datas, cout_max)

main()
