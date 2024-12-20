# Project-Statistic
# **Analiza statystyczna danych giełdowych**

## **Opis projektu**

Ten projekt ma na celu przeprowadzenie analizy statystycznej danych giełdowych przy użyciu dwóch plików CSV zawierających informacje o akcjach dwóch różnych firm (np. NVIDIA i AMD). Program oferuje szereg funkcjonalności umożliwiających obliczenie podstawowych statystyk, wizualizację danych w formie histogramów oraz analizę korelacji między danymi.

## **Funkcjonalności**

1. **Wczytywanie danych z plików CSV**  
   Program wczytuje dane z dwóch plików CSV dostarczonych przez użytkownika. Upewnia się, że dane są dostępne i wyświetla dostępne kolumny.

2. **Obliczanie statystyk dla wybranych kolumn**  
   Dla wybranej kolumny z każdego pliku program oblicza:
   - Średnią arytmetyczną
   - Średnią geometryczną (jeśli wszystkie wartości są dodatnie)
   - Modę
   - Mediana
   - Pierwszy i trzeci kwartyl (Q1, Q3)
   - Odchylenie przeciętne
   - Wariancję i odchylenie standardowe
   - Typowy obszar zmienności
   - Odchylenie ćwiartkowe
   - Klasyczny i pozycyjny wskaźnik asymetrii

3. **Tworzenie histogramów**  
   Program rysuje histogramy dla wybranej kolumny z każdego pliku, umożliwiając wizualną analizę rozkładu danych.

4. **Obliczanie korelacji między plikami**  
   Obliczana jest korelacja Pearsona dla wybranej kolumny z obu plików, co pozwala określić zależność między danymi.

## **Technologie użyte w projekcie**

- **Język programowania**: Python
- **Biblioteki**:
  - `pandas`: Wczytywanie i manipulacja danymi
  - `numpy`: Obliczenia matematyczne
  - `scipy.stats`: Obliczanie średniej geometrycznej
  - `matplotlib`: Tworzenie wizualizacji (histogramów)

## **Wymagania**

Przed uruchomieniem programu upewnij się, że masz zainstalowane poniższe biblioteki:
- `pandas`
- `numpy`
- `matplotlib`
- `scipy`

Aby zainstalować wymagane biblioteki, wykonaj komendę:
```bash
pip install pandas numpy matplotlib scipy
```

## **Instrukcja użytkowania**

1. Umieść dwa pliki CSV z danymi w folderze z programem.
2. Uruchom program w terminalu:
   ```bash
   python Program.py
   ```
3. Podaj nazwy plików oraz wybierz kolumnę wspólną do analizy.
4. Określ szerokość przedziału dla histogramów.
5. Program automatycznie wyświetli wyniki statystyczne, histogramy oraz korelację między danymi.

## **Struktura projektu**

```
Project-Statistic/
│
├── Program.py        # Główny plik programu
├── NVIDIA.csv        # Przykładowy plik z danymi akcji NVIDIA
├── AMD.csv           # Przykładowy plik z danymi akcji AMD
└── README.md         # Dokumentacja projektu
```

## **Przykładowe dane**

- `NVIDIA.csv` i `AMD.csv` to przykładowe pliki zawierające dane o notowaniach giełdowych w formacie CSV.
- Użytkownik może zastąpić te pliki swoimi danymi.

## **Możliwe rozszerzenia**

- Dodanie obsługi większej liczby plików.
- Wprowadzenie analizy regresji lub innych zaawansowanych metod statystycznych.
- Eksport wyników analizy do pliku PDF lub CSV.

## **Licencja**

Ten projekt jest dostępny na licencji MIT. Szczegóły w pliku `LICENSE`.

---

Możesz umieścić powyższy opis w pliku `README.md` w swoim repozytorium GitHuba! Jeśli chcesz, mogę pomóc Ci go poprawić lub rozbudować. 😊
