import pandas as pd

def wybierz_kolumny():
    # Pobierz nazwę pliku CSV od użytkownika
    plik = "Dane.csv"
    try:
        # Wczytaj plik CSV do DataFrame
        df = pd.read_csv(plik)

        # Pokaż dostępne kolumny
        print("\nDostępne kolumny w pliku CSV:")
        for i, kolumna in enumerate(df.columns):
            print(f"{i + 1}. {kolumna}")

        # Zapytaj użytkownika, które kolumny chce wybrać
        wybrane_kolumny = input("\nPodaj numery kolumn, które chcesz wybrać, oddzielając je przecinkami: ")
        wybrane_kolumny = [int(x.strip()) - 1 for x in wybrane_kolumny.split(",")]

        # Wybierz kolumny
        df_wybrane = df.iloc[:, wybrane_kolumny]

        # Zapisz wybrane kolumny do pliku Excel
        nowy_plik = input("\nPodaj nazwę pliku wyjściowego (np. 'wybrane_kolumny.xlsx'): ")
        df_wybrane.to_excel(nowy_plik, index=False, engine='openpyxl')

        print(f"Wybrane kolumny zostały zapisane w pliku {nowy_plik}")
    
    except FileNotFoundError:
        print("Nie znaleziono pliku! Sprawdź ścieżkę.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    wybierz_kolumny()
