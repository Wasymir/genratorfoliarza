import tkinter
import random

def gen():
    wypowiedź = ''
    pula = [['Nie chce wyjść na foliarza, ale ',
             'Troche zgłębiłem i ',
             'Koniecznie przekaż dalej: ',
             'W twojej telewizji tego nie powiedzą, ale ',
             'Rząd i służba zdrowia to ukrywają, ale ',
             'Wiem z wiarygodnego źródła, że '],
            ['pewien odważny lekarz ',
             'taki jeden ratownik medyczny ',
             'brat mojej znajomej ',
             'ojciec koleżanki ',
             'znajoma pielęgniarka ',
             'kuzyn rejestratorki z przychodni '],
            ['ze szpitala covidowego, ',
             'pracuje w hurtowni leków, ',
             'z Agencji Rezerw Materiałowych, ',
             'jeździ w pogotowiu, ',
             'ze Szpitala Narodowego, ',
             'z kliniki w Berlinie, '],
            ['potajemnie powiedział(a) mi, że ',
             'wysłał(a) mi zaszyfrowaną wiadomość, że ',
             'dowiedział(a) sie w tajemnicy, że ',
             'odkrył(a), że ',
             'dostał(a) informacje, że ',
             'dzwonił(a) i powiedział, że '],
            ['w szczepionkach są mikrochipy. ',
             'szczepienia depopulują seniorów. ',
             'szczepionki zmieniają nasze dna. '
             'szczepionki były gotowe przed pandemią. ',
             'szczepionki naprawde powodują autyzm. ',
             'pandemi nie ma, a szczepionki nie są potrzebne. '],
            ['Wyłącz tv, włącz myślenie!',
             'Nie daj sobą manipulować!',
             'Nie daj się spiskowi!',
             'Używaj rozumu!',
             'Skończmy z tą pseudopandemią!',
             'Rozglyźliśmy pandemie!']]

    for tab in pula:
        wypowiedź += random.choice(tab)
    return wypowiedź

root = tkinter.Tk()
root.resizable(0,0)

text = tkinter.Text(master=root,height=5,width=50,wrap=tkinter.WORD)
text.pack()
def insertText():
    text.state = tkinter.NORMAL
    text.delete('0.0',tkinter.END)
    text.insert('0.0',gen())
    text.state = tkinter.DISABLED

button = tkinter.Button(master=root,command=insertText,text='generuj')
button.pack()
insertText()
root.mainloop()