import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gmean

def wczytaj_dane_z_pliku(plik_csv):
    """Wczytuje dane z podanego pliku CSV."""
    try:
        dane = pd.read_csv(plik_csv)
        print(f"Dane z pliku '{plik_csv}' zostały pomyślnie wczytane.")
        return dane
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {plik_csv}. Upewnij się, że plik istnieje w tym samym folderze co skrypt.")
        return None

def oblicz_statystyki(dane, kolumna):
    """Oblicza podstawowe statystyki dla wybranej kolumny."""
    print(f"\nStatystyki dla kolumny: {kolumna}")
    srednia_arytmetyczna = round(dane[kolumna].mean(), 3)
    print(f"Średnia arytmetyczna: {srednia_arytmetyczna}")

    if all(dane[kolumna] > 0):
        srednia_geometryczna = round(gmean(dane[kolumna]), 3)
        print(f"Średnia geometryczna: {srednia_geometryczna}")
    else:
        srednia_geometryczna = None
        print("Średnia geometryczna nie może być obliczona (kolumna zawiera wartości niedodatnie).")

    moda = round(dane[kolumna].mode().iloc[0], 3)
    print(f"Moda: {moda}")

    mediana = round(dane[kolumna].median(), 3)
    print(f"Mediana: {mediana}")

    Q1 = round(dane[kolumna].quantile(0.25), 3)
    Q3 = round(dane[kolumna].quantile(0.75), 3)
    print(f"Pierwszy kwartyl (Q1): {Q1}")
    print(f"Trzeci kwartyl (Q3): {Q3}")

    odchylenie_przecietne = round(np.mean(np.abs(dane[kolumna] - dane[kolumna].mean())), 3)
    print(f"Odchylenie przeciętne: {odchylenie_przecietne}")

    wariancja = round(dane[kolumna].var(), 3)
    odchylenie_standardowe = round(dane[kolumna].std(), 3)
    print(f"Wariancja: {wariancja}")
    print(f"Odchylenie standardowe: {odchylenie_standardowe}")

    dolna_granica = round(srednia_arytmetyczna - odchylenie_standardowe, 3)
    gorna_granica = round(srednia_arytmetyczna + odchylenie_standardowe, 3)
    print(f"Typowy obszar zmienności: ({dolna_granica}, {gorna_granica})")

    odchylenie_cwiartkowe = round((Q3 - Q1) / 2, 3)
    print(f"Odchylenie ćwiartkowe: {odchylenie_cwiartkowe}")

    klasyczny_wsk_asymetrii = round(3 * (srednia_arytmetyczna - mediana) / odchylenie_standardowe, 3)
    pozycyjny_wsk_asymetrii = round((Q3 + Q1 - 2 * mediana) / (Q3 - Q1), 3)
    print(f"Asymetria klasyczna: {klasyczny_wsk_asymetrii}")
    print(f"Asymetria pozycyjna: {pozycyjny_wsk_asymetrii}")

def oblicz_korelacje_miedzy_plikami(dane1, dane2, kolumna):
    """Oblicza korelację między danymi z dwóch różnych plików CSV."""
    korelacja = round(dane1[kolumna].corr(dane2[kolumna]), 3)
    print(f"\nKorelacja Pearsona między kolumną '{kolumna}' z dwóch plików: {korelacja}")
    return korelacja

def rysuj_histogram(dane, kolumna, szerokosc_przedzialu, tytul):
    """Rysuje histogram dla wybranej kolumny z podaną szerokością przedziału i wyświetla go."""
    plt.figure(figsize=(10, 6))
    licznosti, przedzialy, _ = plt.hist(dane[kolumna], bins=range(int(dane[kolumna].min()), 
                                                      int(dane[kolumna].max()) + szerokosc_przedzialu, 
                                                      szerokosc_przedzialu), 
                                        color='skyblue', edgecolor='black')

    for licz, x_wartosc in zip(licznosti, przedzialy[:-1]):
        plt.text(x_wartosc + szerokosc_przedzialu / 2, licz, str(int(licz)), 
                 ha='center', va='bottom', fontsize=9)

    max_licznosc = int(max(licznosti))
    krok_y = 50  
    plt.yticks(range(0, max_licznosc + krok_y, krok_y))

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.title(tytul)
    plt.xlabel(kolumna)
    plt.ylabel("Liczność")
    plt.show()
    print("Histogram został wyświetlony.")

def main():
    # Wczytanie pierwszego pliku
    plik1 = "NVIDIA.csv" #input("Podaj nazwę pierwszego pliku CSV: ")
    dane1 = wczytaj_dane_z_pliku(plik1)

    if dane1 is None:
        return

    print("Dostępne kolumny w pierwszym pliku:", list(dane1.columns))

    # Wczytanie drugiego pliku
    plik2 = "AMD.csv" #input("Podaj nazwę drugiego pliku CSV: ")
    dane2 = wczytaj_dane_z_pliku(plik2)

    if dane2 is None:
        return

    print("Dostępne kolumny w drugim pliku:", list(dane2.columns))

    # Wybór kolumny
    kolumna = input("Wybierz wspólną kolumnę do analizy (musi istnieć w obu plikach): ")

    # Wyświetlanie statystyk dla obu plików
    print("\nObliczenia dla pierwszego pliku:")
    oblicz_statystyki(dane1, kolumna)

    print("\nObliczenia dla drugiego pliku:")
    oblicz_statystyki(dane2, kolumna)

    # Rysowanie histogramów
    szerokosc_przedzialu = int(input("Podaj szerokość przedziału do histogramu: "))
    print("\nHistogram dla pierwszego pliku:")
    rysuj_histogram(dane1, kolumna, szerokosc_przedzialu, f"Histogram dla kolumny '{kolumna}' {plik1}")

    print("\nHistogram dla drugiego pliku:")
    rysuj_histogram(dane2, kolumna, szerokosc_przedzialu, f"Histogram dla kolumny '{kolumna}' {plik2}")

    # Obliczenie korelacji
    oblicz_korelacje_miedzy_plikami(dane1, dane2, kolumna)

if __name__ == "__main__":
    main()
