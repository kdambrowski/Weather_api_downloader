Opis projektu
Celem projektu jest wykonanie zadań rekrutacyjnych z pliku Zadanie.docx,
które posiada poniższe założenia:


1. Proszę o napisanie kodu w Pythonie, który będzie łączył się do darmowego API (https://www.weatherapi.com/docs/).
W celu wykonania zadania, trzeba założyć konto i wygenerować swój klucz do autoryzacji. Etapy zadania:

a. Przygotuj plik konfiguracyjny z 10 dowolnymi miastami.

b. Napisz kod w Python, pozwalający na pobranie z pliku konfiguracyjnego informacje dla jakich miast będziemy pobierać
dane z API

c. Napisz kod w Python, który będzie pozwalał na pobieranie danych o aktualnej pogodzie dla wskazanych w pliku
konfiguracyjnym miast. Dodatkowe informacje
c.i. Otrzymane dane zapisz lokalnie w postaci JSON z podziałem na foldery Year/Month/Day/City
c.ii. W przypadku wielokrotnego  uruchomienia w ciągu dnia, pliki nie powinny się nadpisywać, tylko powinno być wiele
plików per jeden dzień.

d. Napisz kod w pythonie, który będzie pozwalał na pobieranie prognozy pogody dla wskazanych w pliku konfiguracyjnym
miast. Dodatkowe Informacje:
d.i. Otrzymane dane zapisz lokalnie w postaci JSON z podziałem na foldery Year/Month/Day/City
d.ii. W przypadku wielokrotnego  uruchomienia w ciągu dnia, pliki nie powinny się nadpisywać tylko powinno być wiele
plików per jeden dzień.

e. Wykonaj proszę porównanie, za pomocą dowolnej biblioteki pythonowej, jak dane na temat prognozy pokryły się z danymi
aktualnymi. Porównanie temperatury, siły i kierunku wiatru, ciśnienie i wilgotność. Okres porównania jest dowolny może
to być kilka godzin.

f. Zadanie dodatkowe, zaproponuj wskaźnik wyliczany na podstawie porównywanych danych z punktu „e”, który będzie
wskazywał na poziom pokrycia się prognozy z danymi rzeczywistymi.


Uruchomienie
Aby uruchomić kod należy wykonać poniższe punkty.
1. rozpakować pliki zawarte w Kacper_D_Ramp_zadanie.zip do lokalizacji docelowej
    gdzie będą gromadzone wygenerowane dane,
2. zainstalować niezbędne biblioteki poprzez wykonanie komendy  pip install -r requirements.txt w CMD będąc we wskazanej
    w pkt 1 lokalizacji, lub zainstalować je ręcznie,
3. sprawdzić ustawienia w pliku setings.py i wprowadzić dane odpowiednie dla wymagań
4. uruchomić skrypt z pliku main.py poprzez komendę python3 Demo.py w CMD
5. patrzeć i korzystać z generowanych danych

Dodatkowe uwagi:
1. w terminalu mogą pojawić sie warningi odnośnie SettingWithCopyWarning .loc[row_indexer,col_indexer] = value instead
użyte w skrypcie funkcje celowo wykorzystują poprzednią metodę przypisywania danych, dlatego proszę o pominięcie tych
informacji
2. dla zadania e. w który należy wykonac porównanie wartość waiting_time = 60 z modułu setings.py jest podawana
w sekundach, a w związku z treścią zadania aktualne dane będą pobierane z API na bierząco w interwałach co waiting_time
3. skrypt z Querami do zadań związanymi z SQL jest dołączony jako plik tekstowy o nazwie SQL.txt dodatkowo został
 wygenerowany dodatkowy plik SQL_script.sql jako plik zabezpieczający
4. Wszystkie query zostąły zapisane w MySQL (MySQL Workbench 8.0)
