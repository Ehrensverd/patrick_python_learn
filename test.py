import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Dine data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
orders_so_far = 1279  # Antall ordrer fra Jan til Nov i 2023
orders_full_year_estimate = orders_so_far / (11/12)  # Ekstrapolerer til fullt år
orders = np.array([736, 959, 813, 816, 968, 864, 1149, 1371, orders_full_year_estimate])

# Normaliserer årstallene for bedre numerisk stabilitet ved tilpasning
years_normalized = years - years.min()

# Polynomfunksjon av grad n
def polynomial(x, *coeffs):
    return sum([coeff * (x ** i) for i, coeff in enumerate(coeffs)])

# Tilpasser kurven
initial_guess = [1] * 4  # Polynom av grad 3
params, covariance = curve_fit(polynomial, years_normalized, orders, p0=initial_guess)

# Predikerer fremtidige ordre
future_year = 2023
future_year_normalized = future_year - years.min()
predicted_orders = polynomial(future_year_normalized, *params)
print(f"Forventede ordrer for {future_year}: {predicted_orders:.0f}")

# Plotter data og tilpasset kurve
plt.scatter(years, orders, label='Faktiske Ordre')
plt.plot(years, polynomial(years_normalized, *params), label='Tilpasset Kurve', color='red')

# Inkluderer fremtidig prediksjon i plottet
plt.scatter(future_year, predicted_orders, color='green', label='Forventet Ordrer for 2023')

# Legger til etiketter for hvert punkt
for i, txt in enumerate(orders):
    plt.annotate(f"{int(txt)}", (years[i], orders[i]), textcoords="offset points", xytext=(15,-15), ha='center')

# Legger til etikett for den forventede verdien i 2023
plt.annotate(f"{predicted_orders:.0f}", (future_year, predicted_orders), textcoords="offset points", xytext=(15,-15), ha='center', color='green')

plt.xlabel('År')
plt.ylabel('Antall Ordrer')
plt.title('Ordreprognose')
plt.legend()
plt.show()
