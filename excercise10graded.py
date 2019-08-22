def get_country_codes(prices):
    # your code here

    print(prices)

    codes = ""

    for i in prices:
        codes = ", ".join(i.split("$")[0])
        print(codes)


coutry_codes = ("NZ$300, KR$1200, DK$5")

get_country_codes(coutry_codes)
