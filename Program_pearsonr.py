import os
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import numpy as np

# Ustaw katalog roboczy na lokalizację skryptu
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Debug: Wyświetl katalog roboczy i zawartość folderu
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())

# Wczytaj dane z pełnymi ścieżkami do plików (opcjonalne dla testowania)
amd_file = os.path.join(os.getcwd(), "AMD.csv")
nvidia_file = os.path.join(os.getcwd(), "NVIDIA.csv")

# Sprawdź, czy pliki istnieją
if not os.path.exists(amd_file) or not os.path.exists(nvidia_file):
    raise FileNotFoundError("Pliki AMD.csv lub NVIDIA.csv nie zostały znalezione w katalogu.")

# Wczytaj dane
amd_data = pd.read_csv(amd_file)
nvidia_data = pd.read_csv(nvidia_file)

# Zamień 'date' na format datetime
amd_data['date'] = pd.to_datetime(amd_data['date'])
nvidia_data['date'] = pd.to_datetime(nvidia_data['date'])

# Połącz dane na wspólne daty
merged_data = pd.merge(
    amd_data[['date', 'close']],
    nvidia_data[['date', 'close']],
    on='date',
    suffixes=('_amd', '_nvidia')
)

# Oblicz współczynnik korelacji Pearsona
correlation, p_value = pearsonr(merged_data['close_amd'], merged_data['close_nvidia'])

# Wyniki
print(f'Współczynnik korelacji Pearsona: {correlation:.2f}')
print(f'P-wartość: {p_value:.4f}')

# Wykres - scatter plot i line plot dla cen zamknięcia
plt.figure(figsize=(10, 6))

# Scatter plot dla cen zamknięcia AMD i NVIDIA
plt.scatter(merged_data['close_amd'], merged_data['close_nvidia'], color='blue', label='Dane')

# Dopasowanie prostej regresji liniowej
slope, intercept = np.polyfit(merged_data['close_amd'], merged_data['close_nvidia'], 1)  # 1 oznacza dopasowanie prostej

# Rysowanie linii regresji
plt.plot(merged_data['close_amd'], slope * merged_data['close_amd'] + intercept, color='red', linestyle='--', label='Linia trendu')

# Etykiety osi
plt.xlabel('Cena zamknięcia AMD')
plt.ylabel('Cena zamknięcia NVIDIA')
plt.title('Korelacja cen akcji AMD i NVIDIA')

# Dodaj legendę
plt.legend()

# Wyświetl wykres
plt.show()
