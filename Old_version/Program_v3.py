import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gmean

def wczytaj_dane():
    """Funkcja do wczytywania danych z pliku CSV."""
    plik_csv = "NVIDIA.csv"  # Możesz zmienić na dynamiczne wczytywanie
    try:
        dane = pd.read_csv(plik_csv)
        print("Dane zostały pomyślnie wczytane.")
        return dane
    except FileNotFoundError:
        print("Nie znaleziono pliku. Upewnij się, że plik istnieje w tym samym folderze co skrypt.")
        return None
    
def zapisz_do_excela(dane, szereg, nazwa_kolumny):
    """Zapisuje dane i szereg rozdzielczy do pliku Excel."""
    with pd.ExcelWriter("nvidia_data_test1.xlsx", engine='openpyxl') as writer:
        dane.to_excel(writer, sheet_name="Dane oryginalne", index=False)
        szereg_df = pd.DataFrame(szereg).reset_index()
        szereg_df.columns = [nazwa_kolumny, 'Liczność']
        szereg_df.to_excel(writer, sheet_name="Szereg rozdzielczy", index=False)
    print("Dane zapisano do pliku 'nvidia_data_test.xlsx'.")

def generuj_szereg_rozdzielczy(dane, kolumna, szerokosc_przedzialu):
    """Funkcja generująca szereg rozdzielczy dla wybranej kolumny."""
    print(f"Szereg rozdzielczy dla kolumny '{kolumna}' z przedziałem co {szerokosc_przedzialu}:")
    if dane[kolumna].dtype in ['int64', 'float64']:
        min_wartosc = dane[kolumna].min()
        max_wartosc = dane[kolumna].max()
        bins = list(range(int(min_wartosc), int(max_wartosc) + szerokosc_przedzialu, szerokosc_przedzialu))
        szereg = pd.cut(dane[kolumna], bins=bins, right=False).value_counts().sort_index()
    else:
        szereg = dane[kolumna].value_counts()
    print(szereg)
    return szereg


def rysuj_histogram(dane, kolumna, szerokosc_przedzialu):
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
    plt.title(f"Histogram dla kolumny '{kolumna}' (przedziały co {szerokosc_przedzialu})")
    plt.xlabel(kolumna)
    plt.ylabel("Liczność")
    plt.show()
    print("Histogram został wyświetlony.")

def oblicz_statystyki(dane, kolumna):
    """Oblicza podstawowe statystyki dla wybranej kolumny."""
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

    return srednia_arytmetyczna, srednia_geometryczna, moda, mediana

def oblicz_wartosci_cwiartkowe(dane, kolumna):
    """Oblicza wartości ćwiartkowe Q1 i Q3 dla wybranej kolumny."""
    Q1 = round(dane[kolumna].quantile(0.25), 3)
    Q3 = round(dane[kolumna].quantile(0.75), 3)
    print(f"Pierwszy kwartyl (Q1): {Q1}")
    print(f"Trzeci kwartyl (Q3): {Q3}")
    return Q1, Q3

def oblicz_odchylenie_przecietne(dane, kolumna):
    srednia = dane[kolumna].mean()
    odchylenie_przecietne = round(np.mean(np.abs(dane[kolumna] - srednia)), 3)
    print(f"Odchylenie przeciętne: {odchylenie_przecietne}")
    return odchylenie_przecietne

def oblicz_wariancje_odchylenie_std(dane, kolumna):
    wariancja = round(dane[kolumna].var(), 3)
    odchylenie_standardowe = round(dane[kolumna].std(), 3)
    print(f"Wariancja: {wariancja}")
    print(f"Odchylenie standardowe: {odchylenie_standardowe}")
    return wariancja, odchylenie_standardowe

def oblicz_typowy_obszar_zmiennosci(dane, kolumna):
    srednia = dane[kolumna].mean()
    odchylenie_standardowe = dane[kolumna].std()
    dolna_granica = round(srednia - odchylenie_standardowe, 3)
    gorna_granica = round(srednia + odchylenie_standardowe, 3)
    print(f"Typowy obszar zmienności: ({dolna_granica}, {gorna_granica})")
    return dolna_granica, gorna_granica

def oblicz_odchylenie_cwiartkowe(Q1, Q3):
    odchylenie_cwiartkowe = round((Q3 - Q1) / 2, 3)
    print(f"Odchylenie ćwiartkowe: {odchylenie_cwiartkowe}")
    return odchylenie_cwiartkowe

def oblicz_wskazniki_asymetrii(dane, kolumna, Q1, Q3):
    srednia = dane[kolumna].mean()
    mediana = dane[kolumna].median()
    odchylenie_standardowe = dane[kolumna].std()
    klasyczny_wsk_asymetrii = round(3 * (srednia - mediana) / odchylenie_standardowe, 3)
    pozycyjny_wsk_asymetrii = round((Q3 + Q1 - 2 * mediana) / (Q3 - Q1), 3)
    print(f"Asymetria klasyczna: {klasyczny_wsk_asymetrii}")
    print(f"Asymetria pozycyjna: {pozycyjny_wsk_asymetrii}")
    return klasyczny_wsk_asymetrii, pozycyjny_wsk_asymetrii

def oblicz_korelacje(dane, kolumna1, kolumna2):
    korelacja = round(dane[kolumna1].corr(dane[kolumna2]), 3)
    print(f"Korelacja Pearsona między '{kolumna1}' a '{kolumna2}': {korelacja}")
    return korelacja

def main():
    dane = wczytaj_dane()
    if dane is None:
        return
    print("Dostępne kolumny:", list(dane.columns))
    kolumna = input("Wybierz kolumnę do analizy: ")
    szerokosc_przedzialu = int(input("Podaj szerokość przedziału: "))
    szereg = generuj_szereg_rozdzielczy(dane, kolumna, szerokosc_przedzialu)
    zapisz_do_excela(dane, szereg, kolumna)
    oblicz_statystyki(dane, kolumna)
    Q1, Q3 = oblicz_wartosci_cwiartkowe(dane, kolumna)
    oblicz_odchylenie_przecietne(dane, kolumna)
    oblicz_wariancje_odchylenie_std(dane, kolumna)
    oblicz_typowy_obszar_zmiennosci(dane, kolumna)
    oblicz_odchylenie_cwiartkowe(Q1, Q3)
    oblicz_wskazniki_asymetrii(dane, kolumna, Q1, Q3)
    if len(dane.columns) > 1:
        kolumna2 = input("Podaj drugą kolumnę: ")
        oblicz_korelacje(dane, kolumna, kolumna2)

if __name__ == "__main__":
    main()
