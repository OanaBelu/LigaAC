"""Construiește două clase: o clasă “Student” care moștenește o clasă “Persoană” și
încearcă să construiești un Catalog (array/vector) care să conțină mai multe
obiecte de tip Student.
○ Un Student are: medie_generala, nume_facultate;
○ O Persoană are: nume, prenume, varsta;
○ Construiește și o metodă (funcție) în interiorul clasei “Student” care să
schimbe media generală a studentului."""


# clasa parinte (de baza)
class Person:
    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta


# clasa copil (mosteneste Person, si implicit toate atributele acesteia)
class Student(Person):
    def __init__(self, medie_generala, nume_facultate, nume, prenume, varsta):
        # super() reprezinta clasa parinte, in cazul nostru Person
        # deci practic aici apelam constructorul clasei parinte
        super().__init__(nume, prenume, varsta)
        self.medie_generala = medie_generala
        self.nume_facultate = nume_facultate

    def schimba_media_generala(self, medie_generala_noua):
        self.medie_generala= medie_generala_noua


"""Construiește trei clase: o clasă “Mașină”, o clasă “Șofer” și o clasă “Motor”.
Avem nevoie ca o Mașină să aibe un Șofer și un Motor.
○ Un Șofer are: nume, data_nașterii;
○ Un Motor are: cai_putere;
○ O Mașină are: marcă, model, an_fabricație;

○ Construiește o metodă (funcție) în clasa Mașină în care să afișezi detaliile
despre mașină și șoferul care o conduce dacă motorul ei are peste 105 cai
putere."""

"""Construiește două clase: o clasă “Spital” și una “Medic”. Avem nevoie ca un
Spital să poată avea mai mulți medici.
○ Un Spital are: nume, număr_medici, specializare , medici (array cu
obiecte de tip Medic);
○ Un Medi are: nume, prenume, post;
○ Construiește o metodă (funcție) în clasa Spital care sa îți afișeze toți
medicii dintr-un spital.
○ Construiește o metodă (funcție) în clasa Medic în care să poți modifica
numele medicului."""


class Hospital:
    pass


class Doctor:
    pass
