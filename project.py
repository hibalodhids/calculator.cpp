import pandas as pd
import seaborn as sb 
import numpy as np 
import matplotlib.pyplot as plt
# json data 
data = {
    'sno': list(range(1, 12)),
    'date': pd.to_datetime([
        '6/28/2025', '6/29/2025', '6/30/2025', '7/1/2025', '7/2/2025',
        '7/3/2025', '7/4/2025', '7/5/2025', '7/6/2025', '7/7/2025',
        '7/8/2025'
    ]),
    'price': [
        107602.8, 108361.1, 107171.1, 105694.3, 108843.7,
        109600.5, 107989.6, 108204.7, 108204.7, 107602.8,
        108950.0
    ]
}

df = pd.DataFrame(data)



X = df['sno'].values
y = df['price'].values
m, b = np.polyfit(X, y, 1)
predicted_price_7pm = m * 12 + b

print(predicted_price_7pm)

plt.scatter(X, y, color='blue', label='Actual Data')

plt.plot(X, m*X + b, color='red', label='Regression Line')

plt.scatter(12, predicted_price_7pm, color='green', s=100, label='Prediction (sno=12)')

plt.xlabel('Serial Number (sno)')
plt.ylabel('Price')
plt.title('Price Prediction with Linear Regression')
plt.legend()
plt.show()