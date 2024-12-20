import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean  # Biblioteka potrzebna do średniej geometrycznej

def wczytaj_dane():
    """Funkcja do wczytywania danych z pliku CSV."""
    plik_csv = "nvidia_data.csv"  # input("Podaj nazwę pliku CSV (np. 'dane.csv'): ")

    try:
        dane = pd.read_csv(plik_csv)
        print("Dane zostały pomyślnie wczytane.")
        return dane
    except FileNotFoundError:
        print("Nie znaleziono pliku. Upewnij się, że plik istnieje w tym samym folderze co skrypt.")
        return None

def generuj_szereg_rozdzielczy(dane, kolumna, szerokosc_przedzialu):
    """Funkcja generująca szereg rozdzielczy (liczności wystąpień) dla wybranej kolumny z ustalonym przedziałem."""
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

def zapisz_do_excela(dane, szereg, nazwa_kolumny):
    """Zapisuje dane i szereg rozdzielczy do pliku Excel."""
    with pd.ExcelWriter("nvidia_data_test.xlsx", engine='openpyxl') as writer:
        dane.to_excel(writer, sheet_name="Dane oryginalne", index=False)
        szereg_df = pd.DataFrame(szereg).reset_index()
        szereg_df.columns = [nazwa_kolumny, 'Liczność']
        szereg_df.to_excel(writer, sheet_name="Szereg rozdzielczy", index=False)
    print("Dane zapisano do pliku 'AMD_data_test.xlsx'.")

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
    """Oblicza średnią arytmetyczną, geometryczną, modę i medianę dla wybranej kolumny."""
    if kolumna not in dane.columns:
        print("Wybrana kolumna nie istnieje w danych.")
        return None

    # Średnia arytmetyczna
    srednia_arytmetyczna = round(dane[kolumna].mean(),3)
    print(f"Średnia arytmetyczna dla kolumny '{kolumna}': {srednia_arytmetyczna}")

    # Średnia geometryczna (tylko dla wartości dodatnich)
    if all(dane[kolumna] > 0):
        srednia_geometryczna = round(gmean(dane[kolumna]),3)
        print(f"Średnia geometryczna dla kolumny '{kolumna}': {srednia_geometryczna}")
    else:
        srednia_geometryczna = None
        print(f"Średnia geometryczna nie może być obliczona (kolumna '{kolumna}' zawiera wartości niedodatnie).")

    # Moda (wartość najczęściej występująca)
    moda = round(dane[kolumna].mode().iloc[0],3)
    print(f"Wartość modalna (moda) dla kolumny '{kolumna}': {moda}")

    # Mediana (wartość środkowa)
    mediana = round(dane[kolumna].median(),3)
    print(f"Wartość środkowa (mediana) dla kolumny '{kolumna}': {mediana}")

    return srednia_arytmetyczna, srednia_geometryczna, moda, mediana

def main():
    dane = wczytaj_dane()
    if dane is None:
        return

    print("Dostępne kolumny:", list(dane.columns))
    kolumna = input("Wybierz kolumnę do analizy (np. 'wiek'): ")

    if kolumna not in dane.columns:
        print("Wybrana kolumna nie istnieje w danych.")
        return

    szerokosc_przedzialu = int(input("Podaj szerokość przedziału dla szeregu rozdzielczego (np. 5): "))

    szereg = generuj_szereg_rozdzielczy(dane, kolumna, szerokosc_przedzialu)
    zapisz_do_excela(dane, szereg, kolumna)
    oblicz_statystyki(dane, kolumna)
    rysuj_histogram(dane, kolumna, szerokosc_przedzialu)


if __name__ == "__main__":
    main()
