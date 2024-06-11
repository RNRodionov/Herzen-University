def salesByMonth():
  import matplotlib.pyplot as plt
  import numpy as np
  import pandas as pd

  data = pd.read_csv('MarketingSpend.csv', skiprows=1, names=['Date', 'Offline Spend', 'Online Spend'])
  data['Offline Spend'] = data['Offline Spend'].astype(float)
  data['Online Spend'] = data['Online Spend'].astype(float)
  data['Date'] = pd.to_datetime(data['Date'])
  data['Month'] = data['Date'].dt.to_period('M')
  data = data.drop(columns=['Date'])
  monthlySales = data.groupby('Month').sum()

  salesTypes = ['Online Spend', 'Offline Spend']
  salesData = {type: monthlySales[type].values for type in salesTypes}

  months = monthlySales.index.strftime('%B')

  width = 0.6
  fig, ax = plt.subplots()
  left = np.zeros(len(months))
  for salesType, dataValues in salesData.items():
      p = ax.barh(months, dataValues, width, label=salesType, left=left)
      left += dataValues
      ax.bar_label(p, label_type='center')
  for month, salesSum in zip(months, monthlySales.sum(axis=1)):
      ax.text(salesSum, month,  round(salesSum, 2) , ha='left', va='center')
  ax.set_title('Monthly Sales')
  ax.legend()
  ax.tick_params(axis='y', labelsize=8)
  plt.tight_layout() 

  plt.savefig(f'plots/salesByMonth.png')
  