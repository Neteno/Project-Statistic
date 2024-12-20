import pandas as pd
import matplotlib.pyplot as plt

def wczytaj_dane():
    """Funkcja do wczytywania danych z pliku CSV."""
    plik_csv = "Nvidia_Stock_Data.csv" #input("Podaj nazwę pliku CSV (np. 'dane.csv'): ")

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
        # Oblicz zakresy przedziałów na podstawie szerokości podanej przez użytkownika
        min_wartosc = dane[kolumna].min()
        max_wartosc = dane[kolumna].max()
        bins = list(range(int(min_wartosc), int(max_wartosc) + szerokosc_przedzialu, szerokosc_przedzialu))
        
        # Tworzenie szeregu rozdzielczego przedziałowego
        szereg = pd.cut(dane[kolumna], bins=bins, right=False).value_counts().sort_index()
    else:
        # Szereg punktowy dla danych tekstowych
        szereg = dane[kolumna].value_counts()

    print(szereg)
    return szereg

def zapisz_do_excela(dane, szereg, nazwa_kolumny):
    """Zapisuje dane i szereg rozdzielczy do pliku Excel."""
    with pd.ExcelWriter("AMD_data_test.xlsx", engine='openpyxl') as writer:
        dane.to_excel(writer, sheet_name="Dane oryginalne", index=False)
        szereg_df = pd.DataFrame(szereg).reset_index()
        szereg_df.columns = [nazwa_kolumny, 'Liczność']
        szereg_df.to_excel(writer, sheet_name="Szereg rozdzielczy", index=False)
    print("Dane zapisano do pliku 'analiza_danych.xlsx'.")

def rysuj_histogram(dane, kolumna, szerokosc_przedzialu):
    """Rysuje histogram dla wybranej kolumny z podaną szerokością przedziału i wyświetla go."""
    plt.figure(figsize=(10, 6))

    # Oblicz liczbę przedziałów i ustaw odpowiednią szerokość
    licznosti, przedzialy, _ = plt.hist(dane[kolumna], bins=range(int(dane[kolumna].min()), 
                                                      int(dane[kolumna].max()) + szerokosc_przedzialu, 
                                                      szerokosc_przedzialu), 
                                        color='skyblue', edgecolor='black')

    # Dodanie wartości liczności na słupkach
    for licz, x_wartosc in zip(licznosti, przedzialy[:-1]):
        plt.text(x_wartosc + szerokosc_przedzialu / 2, licz, str(int(licz)), 
                 ha='center', va='bottom', fontsize=9)

    # Ustawienia osi Y z większą szczegółowością (zmniejszenie liczby etykiet)
    max_licznosc = int(max(licznosti))
    krok_y = 50  # Ustawienie kroku, co ile mają się pojawiać wartości na osi Y
    plt.yticks(range(0, max_licznosc + krok_y, krok_y))  # Zwiększamy odstęp między etykietami na osi Y

    # Dodanie siatki
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Dodanie tytułów i etykiet
    plt.title(f"Histogram dla kolumny '{kolumna}' (przedziały co {szerokosc_przedzialu})")
    plt.xlabel(kolumna)
    plt.ylabel("Liczność")
    
    plt.show()
    print("Histogram został wyświetlony.")


def main():
    dane = wczytaj_dane()
    if dane is None:
        return

    print("Dostępne kolumny:", list(dane.columns))
    kolumna = input("Wybierz kolumnę do analizy (np. 'wiek'): ")

    if kolumna not in dane.columns:
        print("Wybrana kolumna nie istnieje w danych.")
        return

    # Pobierz szerokość przedziału od użytkownika
    szerokosc_przedzialu = int(input("Podaj szerokość przedziału dla szeregu rozdzielczego (np. 5): "))

    szereg = generuj_szereg_rozdzielczy(dane, kolumna, szerokosc_przedzialu)
    zapisz_do_excela(dane, szereg, kolumna)
    rysuj_histogram(dane, kolumna, szerokosc_przedzialu)

if __name__ == "__main__":
    main()
