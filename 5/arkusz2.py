import pandas as pd  # importujemy bibliotekę pandas jako alias

excel_data = pd.read_excel('sales.xlsx')
print(excel_data)
#   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000

data = pd.DataFrame(excel_data)
print(data.values)
# [[Timestamp('2018-05-12 00:00:00') 'Sila Ahmed' 60000]
#  [Timestamp('2019-12-06 00:00:00') 'Mir Hossain' 50000]
#  [Timestamp('2020-08-09 00:00:00') 'Sarmin Jahan' 45000]
#  [Timestamp('2021-04-07 00:00:00') 'Mahmudul Hasan' 30000]]
print(data.columns)
# Index(['Sales Date', 'Sales Person', 'Amount'], dtype='object')

print(data.items)
# <bound method DataFrame.items of   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000>

print(data.index[-1])  # 3
print(data.columns[0])  # Sales Date

print(data[data['Amount'] > 47000])
#   Sales Date Sales Person  Amount
# 0 2018-05-12   Sila Ahmed   60000
# 1 2019-12-06  Mir Hossain   50000
