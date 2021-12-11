
import pandas as pd

df = pd.read_fwf('AoC_3_input.txt', header=None, dtype=str) #Create dataframe from input.txt
for i in range(1, 13):
    df[i] = df[0].str[i-1]
for i in range(1, 13):
    df[i].astype(int)


# print(df) #View dataframe

def binary_diagnostic(data_report):
    """
    Count the 1s and 0s for each column for the higher/lower amounts.
    Calculate gamma_rate bit string and epsilon_rate bit string.
    Converts to decimal and returns gamma_rate multiplied by epsilon_rate.
    """
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(1, 13):
        print(df[i].value_counts().index.tolist())
        print(type(df[i].value_counts()))
        gamma_rate = gamma_rate + df[i].value_counts().index.tolist()[0]
        print(gamma_rate)

    for i in range (1, 13):
        epsilon_rate = epsilon_rate + df[i].value_counts().index.tolist()[1]

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

print(binary_diagnostic(df))