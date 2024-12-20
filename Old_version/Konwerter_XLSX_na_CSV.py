import pandas as pd

# Wczytanie pliku Excel
plik_xlsx = 'AMD_Stock_Data_DoPrzekonwertowania.xlsx'  # Zmienna ścieżka do pliku Excel
dane = pd.read_excel(plik_xlsx)

# Zapisanie danych do pliku CSV
plik_csv = 'AMD_Stock_Data.csv'  # Zmienna ścieżka do pliku CSV
dane.to_csv(plik_csv, index=False)

print("Plik został zapisany jako CSV.")
