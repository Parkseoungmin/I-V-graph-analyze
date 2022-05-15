import pandas as pd
import matplotlib.pyplot as plt
import glob
from tqdm import tqdm

file_path = '.\dat\*.csv'
csv = []
for filename in glob.glob(file_path,recursive=True):
    csv.append(filename)

csv_tqdm = tqdm(csv)
for i in csv_tqdm:
    filename = i.split('\\')[-1][:-4]
    csv_tqdm.set_description(f'Processing {filename}')

    Data = pd.read_csv(".\dat\%s"%filename+'.csv',names=['Value','Voltage','Current','four','five','six'])

    Value = "DataValue"

    find_row = Data.loc[(Data['Value'] == Value)]
    # find_row = find_row.iloc[:,1:3]
    # print(find_row)

    find_columns_v = find_row['Voltage']
    find_columns_c = find_row['Current']
    Voltage = list(map(float,find_columns_v.values.tolist()))
    Current_abs = list(map(abs,map(float,find_columns_c.values.tolist())))
    Current_lin = list(map(float,find_columns_c.values.tolist()))
    # print(Voltage)
    # print(Current_lin)
    Voltage_2 = []
    for i in range(0,len(Voltage),10):
        Voltage_2.append(Voltage[i])
    Current_lin_2 = []
    for i in range(0,len(Current_lin),10):
        Current_lin_2.append(Current_lin[i])
    Current_abs_2 = []
    for i in range(0,len(Current_abs),10):
        Current_abs_2.append(Current_abs[i])


    plt.rc('font',size = 15)
    plt.figure(figsize=(15,7))

    plt.subplot(121)
    plt.plot(Voltage,Current_lin,Voltage_2,Current_lin_2, "b>")
    plt.title('I-V graph_linear')
    plt.xlabel('Voltage [V]',labelpad=10)
    plt.ylabel('Current [A]',labelpad=10)
    plt.grid(True)

    plt.subplot(122)
    plt.plot(Voltage,Current_abs,"g-",Voltage_2,Current_abs_2,'c>')
    plt.yscale('log')
    plt.title('I-V graph_abs')
    plt.xlabel('Voltage [V]',labelpad=10)
    plt.ylabel('Current [A]',labelpad=10)
    plt.grid(True)

    plt.savefig('.\\res\\%s.png'%filename)
    plt.show(block=False)
    plt.pause(1)
    plt.close()


