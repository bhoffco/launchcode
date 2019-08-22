def test(string):
    return ", ".join([item.split("$")[0] for item in string.split(", ")])


string = "NZ$300, KR$1200, DK$5"
print(test(string))


def get_country_codes(prices):
    # your code here

    prices = prices.split(", ")
    print(prices)
    # print(prices[0][:2])

    code = ""

    for i in prices:

        code = code + " ,".join(i.split("$")[0])
    return code
