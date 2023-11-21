import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Dine data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
orders_so_far = 1279  # Antall ordrer fra Jan til Nov i 2023
orders_full_year_estimate = orders_so_far / (11/12)  # Ekstrapolerer til fullt år
orders = np.array([736, 959, 813, 816, 968, 864, 1149, 1371, orders_full_year_estimate])

# Konverterer til en pandas Series for tidsanalyse (med år som index)
orders_series = pd.Series(orders, index=pd.to_datetime(years, format='%Y'))

# Oppretter og trener ARIMA-modellen
model = ARIMA(orders_series, order=(1, 1, 1))
model_fit = model.fit()

# Plotter de faktiske og forutsagte ordrene
plt.scatter(years, orders, color='blue', label='Faktiske Ordre')

# Plotter prediksjon for 2023 basert på delvis data
plt.scatter(2023, orders_full_year_estimate, color='green', label='Estimerte Ordre for 2023')

plt.xlabel('År')
plt.ylabel('Antall Ordrer')
plt.title('Ordreprognose med ARIMA')
plt.legend()
plt.show()
