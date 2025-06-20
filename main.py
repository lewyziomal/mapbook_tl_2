# from utils.model import users
# from utils.controller import get_user_info, add_user, remove_user, update_user, get_map,get_coordinates
#
#
# def main():
#     print('===========MENU============')
#     print('0 - zakończ program ')
#     print('1 - wyswietl co u znajomych ')
#     print('2 - dodaj noego uzytkownika')
#     print('3 - usun uzytkownika  ')
#     print('4 - edytuj uzytkownika ')
#     print('5 - przygotuj mape znajomych  ')
#     print('===========MENU============')
#
#     while True:
#         choice: str = input("Wybierz opcje MENU: ")
#         if choice == '0':
#             break
#         if choice == '1':
#             get_user_info(users)
#         if choice == '2':
#             add_user(users)
#         if choice == '3':
#             remove_user(users)
#         if choice == '4':
#             update_user(users)
#         if choice == '5':
#             get_map(users)
#     get_user_info(users)
#
#
# if __name__ == "__main__":
#     main()


from cProfile import Profile
from tkinter import *

import tkintermapview
from geocoder import location

users: list = []


def add_user():
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    post = entry_liczba_postow.get()
    users.append({"name": name, "surmane:": surname, "location": location, "posts": post})
    print(users)
    show_users()

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_imie.focus()


def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx,
                                      f'{idx + 1} {user['name']} {user["surmane:"]} {user["location"]} {user["posts"]}')


def remove_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    print(i)
    users.pop(i)
    show_users()


def edit_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    print(i)
    entry_imie.insert(0, users[i]['name'])
    entry_nazwisko.insert(0, users[i]['surname'])
    entry_miejscowosc.insert(0, users[i]['location'])
    entry_liczba_postow.insert(0, users[i]['posts'])
    button_dodaj_uzytkownika.config(text="Zapisz", command=lambda: update_user(i))


def update_user(i):
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    post = entry_liczba_postow.get()
    users[i]['name'] = name
    users[i]['surname'] = surname
    users[i]['location'] = location
    users[i]['posts'] = post
    button_dodaj_uzytkownika.config(text="Dodaj", command=add_user)




def delete_user():


root = Tk()

root.title('mapbook_tl_2')
root.geometry('1200x700')

ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szcegoly_obiektow = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szcegoly_obiektow.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_obiektow

label_lista_obiektow = Label(ramka_lista_obiektow, text='Lista Znajomych')
label_lista_obiektow.grid(row=0, column=0, )

listbox_lista_obiektow = Listbox(ramka_lista_obiektow)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text='Pokaż szczególy')
button_pokaz_szczegoly.grid(row=3, column=0)

button_usun_obiekt = Button(ramka_lista_obiektow, text='Usuń znajomego', command=remove_user)
button_usun_obiekt.grid(row=3, column=1)

button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_user)
button_edytuj_obiekt.grid(row=3, column=2)

# ramka_formularz

label_formularz = Label(ramka_formularz, text='Formularz')
label_formularz.grid(row=0, column=1, columnspan=3)

label_imie = Label(ramka_formularz, text='Imie')
label_imie.grid(row=2, column=0, sticky=W)

label_nazwisko = Label(ramka_formularz, text='Nazwisko')
label_nazwisko.grid(row=3, column=0, sticky=W)

label_miejscowosc = Label(ramka_formularz, text='Miejscowosc')
label_miejscowosc.grid(row=4, column=0, sticky=W)

label_liczba_postow = Label(ramka_formularz, text='Liczba postow')
label_liczba_postow.grid(row=5, column=0, sticky=W)

entry_imie = Entry(ramka_formularz)
entry_imie.grid(row=2, column=1)
entry_nazwisko = Entry(ramka_formularz)
entry_nazwisko.grid(row=3, column=1)
entry_miejscowosc = Entry(ramka_formularz)
entry_miejscowosc.grid(row=4, column=1)
entry_liczba_postow = Entry(ramka_formularz)
entry_liczba_postow.grid(row=5, column=1)

button_dodaj_uzytkownika = Button(ramka_formularz, text='Dodaj uzytkownika', command=add_user)
button_dodaj_uzytkownika.grid(row=6, column=1, columnspan=2)

# ramka_szczegoly_obiektow

label_szczegoly_uzytkownika = Label(ramka_szcegoly_obiektow, text='Pokaż szczegóły:')
label_szczegoly_uzytkownika.grid(row=0, column=0)

label_imie_szczegoly_uzytkwnika = Label(ramka_szcegoly_obiektow, text='Imie: ')
label_imie_szczegoly_uzytkwnika.grid(row=1, column=0)

label_imie_szczegoly_uzytkwnika_wartosc = Label(ramka_szcegoly_obiektow, text='........ ')
label_imie_szczegoly_uzytkwnika_wartosc.grid(row=1, column=1)

label_nazwisko_szczegoly_uzytkwnika = Label(ramka_szcegoly_obiektow, text='Nazwisko: ')
label_nazwisko_szczegoly_uzytkwnika.grid(row=1, column=2)

label_nazwisko_szczegoly_uzytkwnika_wartosc = Label(ramka_szcegoly_obiektow, text='........ ')
label_nazwisko_szczegoly_uzytkwnika_wartosc.grid(row=1, column=3)

label_miejscowosc_szczegoly_uzytkwnika = Label(ramka_szcegoly_obiektow, text='Miejscowosc: ')
label_miejscowosc_szczegoly_uzytkwnika.grid(row=1, column=4)

label_miejscowosc_szczegoly_uzytkwnika_wartosc = Label(ramka_szcegoly_obiektow, text='........ ')
label_miejscowosc_szczegoly_uzytkwnika_wartosc.grid(row=1, column=5)

label_liczba_postow_szczegoly_uzytkwnika = Label(ramka_szcegoly_obiektow, text='Liczba postów: ')
label_liczba_postow_szczegoly_uzytkwnika.grid(row=1, column=6)

label_liczba_postow_szczegoly_uzytkwnika_wartosc = Label(ramka_szcegoly_obiektow, text='........ ')
label_liczba_postow_szczegoly_uzytkwnika_wartosc.grid(row=1, column=7)

# ramka_mapa

map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=470)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)

root.mainloop()
