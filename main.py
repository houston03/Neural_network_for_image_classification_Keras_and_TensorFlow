import io
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Customers.csv', sep=";", decimal=",")
print('Формат данных: ', df.shape)
print('Тип данных: ',df.dtypes)

df = df[['Prices', 'Number', 'Customer_id']].astype(float)
# Выбор числовых колонок
df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
print(numeric_cols)
# Выбор нечисловых колонок
df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values
print(non_numeric_cols)
print('Описательная статистика:')
print(df.describe())
cols = df.columns[:4]
colours = ['#000099', '#ffff00'] # желтые – это пропущенные. синие - не пропущенные.
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))
# Замена пропущенных значений медианой
median = df['Customer_id'].median()
print(median)
df['Customer_id'] = df['Customer_id'].fillna(median)

# Проверка пропущенных данных после замены пропущенных значений медианой
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('Пропущенные значения: ')
    print('{} - {}%'.format(col, pct_missing*100))
# Визуализация разброса значений по Prices
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x = df['Customer_id'], y = df['Prices'])
plt.xlabel("Customer_id")
plt.ylabel("Prices")
plt.show()
print('Вывод результата расчета средней цены и первых пяти значений данных: ')
print(df.Prices.mean())
print(df.head())