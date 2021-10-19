import pandas as pd


def hexlist_to_dec(x_list):
    x_list.reverse()
    y = "0x"+"".join(x_list)
    return int(y, 16)


def mutliHexString_to_dec(hexString, startingIdx=36,
                          dataStartIdx=2, dataEndIdx=6):
    x_list = hexString[startingIdx:-1].split(" ")
    y_dec = hexlist_to_dec(x_list[dataStartIdx:dataEndIdx])
    return y_dec


def calculate_press(df):
    count = 0
    dec_values_list = []
    for _, row in df.iterrows():
        if count == 0:
            pass
        dec_values_list.append(mutliHexString_to_dec(row.iloc[0]) / 100)
        count += 1

    return dec_values_list


def calculate_temp(df):
    count = 0
    dec_values_list = []
    for _, row in df.iterrows():
        if count == 0:
            pass
        dec_values_list.append(mutliHexString_to_dec(
            row.iloc[0], dataStartIdx=6, dataEndIdx=8) / 10
        )
        count += 1

    return dec_values_list


def main():
    df = pd.read_csv('test.txt')
    df['Physical Pressure'] = calculate_press(df)
    df['Physical Temp'] = calculate_temp(df)

    df.to_csv('out_r1.csv', index=False)


if __name__ == "__main__":
    main()
