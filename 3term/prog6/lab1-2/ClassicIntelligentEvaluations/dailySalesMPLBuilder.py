def salesByDay():
  import matplotlib.pyplot as plt
  import pandas as pd

  data = pd.read_csv('Retail.csv')
  data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
  dailySales = data.groupby(
      data['InvoiceDate'].dt.dayofyear)['Quantity'].sum()

  plt.figure(figsize=(10, 6))
  plt.scatter(dailySales.index, dailySales.values, color='green', alpha=0.7)
  plt.xlabel('Day of Year')
  plt.ylabel('Quantity Sold')
  plt.title('Daily Sales')
  plt.xticks(range(1, 365, 15))
  plt.grid(True)
  plt.tight_layout()

  plt.savefig(f'plots/salesByDay.png')
