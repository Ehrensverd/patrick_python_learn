### Forklaring av Koden

Koden nedenfor utfører en tidsserieanalyse for å forutsi fremtidige ordrer basert på historiske data ved hjelp av en polynomisk tilpasning. Her er en steg-for-steg forklaring:

#### 1. Importere Biblioteker
```python
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
```
- `numpy`: Et bibliotek brukt for numeriske beregninger.
- `scipy.optimize.curve_fit`: En funksjon for å tilpasse en kurve til data.
- `matplotlib.pyplot`: Et bibliotek for å lage grafikk og plotte data.

#### 2. Definere Data
```python
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
orders_so_far = 1279  # Antall ordrer fra Jan til Nov i 2023
orders_full_year_estimate = orders_so_far / (11/12)  # Ekstrapolerer til fullt år
orders = np.array([736, 959, 813, 816, 968, 864, 1149, 1371, orders_full_year_estimate])
```
- Definerer en tidsserie (`years`) og tilhørende ordreantall (`orders`).
- Inkluderer et estimat for 2023 basert på data tilgjengelig så langt i året.

#### 3. Normalisering og Polynomisk Funksjon
```python
years_normalized = years - years.min()

def polynomial(x, *coeffs):
    return sum([coeff * (x ** i) for i, coeff in enumerate(coeffs)])
```
- Normaliserer årstallene for numerisk stabilitet.
- Definerer en polynomisk funksjon for kurvetilpasning.

#### 4. Kurvetilpasning og Prediksjon
```python
initial_guess = [1] * 4
params, covariance = curve_fit(polynomial, years_normalized, orders, p0=initial_guess)

future_year = 2023
future_year_normalized = future_year - years.min()
predicted_orders = polynomial(future_year_normalized, *params)
```
- Tilpasser en polynomisk kurve til de normaliserte årstallene og ordrene.
- Predikerer ordreantall for et fremtidig år (2023).

#### 5. Plott og Annotasjoner
```python
plt.scatter(years, orders, label='Faktiske Ordre')
plt.plot(years, polynomial(years_normalized, *params), label='Tilpasset Kurve', color='red')
plt.scatter(future_year, predicted_orders, color='green', label='Forventet Ordrer for 2023')
for i, txt in enumerate(orders):
    plt.annotate(f"{int(txt)}", (years[i], orders[i]), textcoords="offset points", xytext=(15,-15), ha='center')
plt.annotate(f"{predicted_orders:.0f}", (future_year, predicted_orders), textcoords="offset points", xytext=(15,-15), ha='center', color='green')
plt.xlabel('År')
plt.ylabel('Antall Ordrer')
plt.title('Ordreprognose')
plt.legend()
plt.show()
```
- Plotter både de faktiske ordrene og den tilpassede kurven.
- Annoterer hver datapunkt med ordreantall.
- Annoterer den forventede verdien for 2023.

