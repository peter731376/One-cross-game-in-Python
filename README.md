# One-cross-game-in-Python

This game exercise from my Python course at school
I wrote the file ristinolla.py
Tehtävän kuvaus
Kirjoita moduuliin ristinolla luokka Ristinolla, jonka avulla kaksi käyttäjää voi pelata ristinollaa 4x4-kokoisella ruudukolla.

Huomaa, että moduulin nimi pitää kirjoittaa pienellä alkukirjaimella. Vastaavasti luokan nimi pitää kirjoittaa isolla alkukirjaimella. Tämä on yleisesti käytetty nimeämiskäytäntö, jota myös Goblin vaatii käytettävän (muuten ohjelmasi tarkistus ei toimi).

Pelin kulku
Pelissä on 4x4-kokoinen ruudukko, johon kaksi pelaaja sijoittaa vuoron perään omia merkkejään (ensimmäinen pelaaja "ristejä" eli käytännössä X-kirjaimia ja toinen pelaaja nollia) vapaana oleviin ruutuihin. Yhdellä vuorolla saa sijoittaa yhden merkin. Se pelaaja voittaa, joka saa ensimmäiseksi aikaan omista merkeistään koostuvan neljän merkin pituisen pystyrivin, vaakarivin tai ruudukon lävistäjän. Jos ruudukko tulee täyteen, mutta kummallakaan pelaajalla ei ole neljän merkin pituista suoraa, peli päättyy ratkaisemattomaan.

Tässä ohjelmassa ruutujen paikkoja merkitään X- ja Y-koordinaateilla, joiden arvo vaihetelee nollasta kolmeen. Koordinaatit alkavat vasemmasta alakulmasta. X-koordinaatit kasvavat oikealle ja Y-koordinaatit ylöspäin.

Huomaa, että tässä pelissä on kaksi käyttäjää, jotka pelaavat keskenään. Tietokone ei siis pelaa käyttäjää vastaan, vaan se vain pitää kirjaa pelin tilanteesta ja vuorossa olevasta pelaajasta.

Luokan Ristinolla kuvaus
Määrittele Ristinolla-luokassa metodien ulkopuolella (mutta luokan sisällä) seuraavat vakiot:

    PELAAJA1 = 1
    PELAAJA2 = 2
    RATKAISEMATON = 3
    MERKKI1 = 1
    MERKKI2 = -1
    TYHJA = 0
    EI_LOYDY = 0
    KESKEN = 0
    KOKO = 4
    MERKIT = ['_', 'X', '0']
Voit käyttää näitä vakiota muualla luokassasi ja sen ulkopuolella kuvaamaan esimerkiksi vuorossa olevaa pelaajaa, ruudussa olevaa merkkiä tai pelin voittajaa tai sitä, että pelillä ei ole voittajaa. Näitä vakioita voi käyttää esimerkiksi kirjoittamalla Ristinolla.PELAAJA1.
Ristinolla-oliolla on syytä olla kentät, jotka sisältävät pelaajien nimet sekä peliruudukon tilanteen. Peliruudukon tilannetta voi kuvata kaksiulotteisella listalla, jossa jokainen alilista kuvaa yhtä riviä peliruudukolla ja alilistan alkio yksittäistä ruutua tällä rivillä. Voit miettiä itse, millä edellä annetuista vakioista kuvaat mitäkin tilannetta (tyhjä, 1. pelaajan merkki, 2. pelaajan merkki) ruuduissa. Valitsemalla alkiot sopivasti voit kuitenkin helpottaa tarvittavia tarkistuksia ja ruudukon tilanteen tulostamista.

Kirjoita sitten luokkaan seuraavat metodit

__init__(self, nimi1, nimi2)
Metodi luo uuden Ristinolla-olion. Pelaajien nimet annetaan parametrina. Ruudukon tilannetta kuvaava lista alustetaan kuvaamaan tyhjää ruudukkoa.
kerro_pelaaja1(self)
Metodi palauttaa ensimmäisen pelaajan nimen
kerro_pelaaja2(self)
Metodi palauttaa toisen pelaajan nimen
lisaa_merkki(self, x_koord, y_koord, pelaaja)
Metodi lisää vuorossa olevan pelaajan merkin ruudukossa parametrina annettujen koordinaattien mukaiseen ruutuun, jos se on mahdollista. Vuorossa olevaa pelaajaa kuvaava vakio on annettu kolmantena parametrina. Merkin lisääminen ei ole mahdollista, jos ruudussa on jo merkki tai vähintään toinen koordinaateista on sallitun välin 0-3 ulkopuolella. Metodi palauttaa arvon True, jos merkin lisääminen onnistuu ja arvon False, jos merkin lisääminen ei onnistu.
peli_paattynyt(self)
Metodi tutkii, onko peli jo päättynyt (siksi että jompi kumpi pelaajista on saanut neljän merkin pituisen suoran tai ruudukko on tullut täyteen). Jos peli on jo päättynyt, metodi palauttaa joko arvon Ristinolla.PELAAJA1, Ristinolla.PELAAJA2 tai Ristinolla.RATKAISEMATON sen mukaan, kummalla pelaajista on suora tai onko peli päättynyt ratkaisemattomaan. Jos peli ei ole vielä päättynyt, metodi palauttaa arvon Ristinolla.KESKEN. Tälle metodille kannattaa määritellä apumetodeita, jotka tutkivat erilaisia mahdollisia tilanteita (ruudukosta löytyy voiton ratkaiseva vaakarivi, pystyrivi tai lävistäjä, ruudukko on täynnä). Saat miettiä itse nämä apumetodit.
__str__(self)
Metodi palauttaa merkkijonon, joka sisältää peliruudukon tilanteen siten, että kukin rivi on esitetty omalla rivillään vasemmasta yläkulmasta alkaen. Jos ruutu on tyhjä, sitä vastaavalla paikalla on _ (alaviiva); jos ruudussa on ensimmäisen pelaajan merkki, sitä vastaavalla paikalla on X, jos ruudussa on toisen pelaajan merkki, sitä vastaavalla paikalla on 0 (nolla). Huomaa, että metodi ei tulosta mitään, vaan se vain palauttaa tilannetta vastaavan merkkijonon. Saat merkkijonoon rivinvaihtoja lisäämällä siihen "\n"-merkkejä sopiviin kohtiin. Esimerkki mahdollisesta peliruudukosta:
_X0_
XX0_
_X0_
____
Huomaa, että viimeisen rivin loppuun ei tule rivinvaihtomerkkiä.
Luokan testaaminen
Kun olet kirjoittanut luokan valmiiksi, voit testata sitä pelaamalla ristinollaa ohjelman annetun testiohjelman avulla. Älä tee mitään muutoksia pelaa_ristinollaa-ohjelmaan. Jos Eclipse valittaa virheistä tässä ohjelmassa, kysymys on todennäköisesti siitä, että sinun Ristinolla-luokastasi puuttuu vielä sellaisia ominaisuuksia, joita pelaa_ristinollaa-moduulin ohjelma käyttää. Huomaa, että kaikki käyttäjältä pyydettävät syötteet pyydetään pelaa_ristinollaa-ohjelmassa samoin kuin kaikki tulostukset tehdään siellä. Sinun luokkasi ei pidä lukea käyttäjän syötettä eikä tulostaa käyttäjälle mitään.

Virhetilanteiden käsittely
Valmiiksi annettu ohjelma pelaa_ristinollaa huolehtii virhetilanteiden käsittelystä, kunhan sinun luokkasi metodit palauttavat yllä annettujen ohjeiden mukaiset arvot.

Ohjelman palautus
Kun luokkasi näyttää toimivan oikein, palauta Gobliniin tiedosto ristinolla.py. Tiedostossa saa olla ainoastaan luokka Ristinolla, ei valmiina annettua pelaa_ristinollaa-ohjelmaa.

Vinkki
Ohjelman testaaminen kaikissa tilanteissa voi tuntua työläältä 4x4-laudalla. Jos muutat vakion Ristinolla.KOKO arvoksi väliaikaisesti 3, voit testata ohjelmasi toimintaa aluksi 3x3-laudalla (edellytyksenä on tosin se, että olet kirjoittanut luokan muuten järkevästi niin, että se käyttää hyväkseen annettuja vakioita). Näin todennäköisesti huomaat suurimman osan mahdollisista virheistä. Kun olet korjannut ne, voit vaihtaa vakioksi takaisin 4 ja testata luokkasi toimintaa suuremmalla laudalla.

Huomautus kaksiulotteisen listan alustamisesta
Kun kaksiulotteisen listan alkioille annetaan alkuarvoja, voi Python-tulkki toimia tavalla, jota ei tule etukäteen ajatelleeksi. Tarkastallaan seuraavaa esimerkkitapausta (käskyt ja niiden tulostukset on esitetty niin, että käskyt on annettu suoraan Python-tulkille): Luodaan lista, joka sisältää kaksi alilistaa, joissa on kummassakin neljä alkiota:

>>> lista1 = [[0, 0, 0, 0], [0, 0, 0, 0]]
Tällainen lista toimii odotetulla tavalla, esimerkiksi
>>> print(lista1)
[[0, 0, 0, 0], [0, 0, 0, 0]]
>>> lista1[1][2] = 5
>>> print(lista1)
[[0, 0, 0, 0], [0, 0, 5, 0]]
Jos sen sijaan listan alkuarvot annetaankin vähän eri tavalla

>>> lista2 = [[0, 0, 0, 0]] * 2
toimiikin näin luotu lista toisin, esimerkiksi:
>>> print(lista2)
[[0, 0, 0, 0], [0, 0, 0, 0]]
>>> lista2[1][2] = 5
>>> print(lista2)
[[0, 0, 5, 0], [0, 0, 5, 0]]
Tässä tapauksessa molempien alilistojen kolmas alkio on muuttunut, vaikka ohjelmoija kuvitteli muuttaneensa vain jälkimmäisen alilistan yhtä alkiota. Tämä johtuu siitä, että jälkimmäisellä tavalla luotu lista ei sisälläkään kahta erillistä neljän alkion alilistaa, vaan sama neljän alkion alilista on lista2n alkiona kahteen kertaa. Jos tähän alilistaan tehdään jossain kohdassa muutos, näkyy muutos kaikissa kohdissa, joissa tämä sama alilista esiintyy. Ole siis tarkkana, että teet peliruudukkoa luodessasi jokaiselle rivin oman listan.
Esimerkkejä testiohjelman suorituksesta:
[ohjelman suoritus alkaa]
Tervetuloa pelaamaan ristinollaa 4x4-ruudukolla.
Ruutujen koordinaatit annetaan muodossa X:Y.
Koordinaatit alkavat vasemmasta alakulmasta nollasta.
Kuka on ensimmainen pelaaja?
Tiina Teekkari
Kuka on toinen pelaaja?
Sampo Sahkolainen
Pelitilanne nyt:
____
____
____
____
Vuorossa on Tiina Teekkari.
Mihin ruutuun merkki lisataan?
1:2
Pelitilanne nyt:
____
_X__
____
____
Vuorossa on Sampo Sahkolainen.
Mihin ruutuun merkki lisataan?
2:1
Pelitilanne nyt:
____
_X__
__0_
____
Vuorossa on Tiina Teekkari.
Mihin ruutuun merkki lisataan?
2:1
Valitsemaasi ruutuun ei voi lisata merkkia.
Mihin ruutuun merkki lisataan?
0:2
Pelitilanne nyt:
____
XX__
__0_
____
Vuorossa on Sampo Sahkolainen.
Mihin ruutuun merkki lisataan?
2:2
Pelitilanne nyt:
____
XX0_
__0_
____
Vuorossa on Tiina Teekkari.
Mihin ruutuun merkki lisataan?
1:1
Pelitilanne nyt:
____
XX0_
_X0_
____
Vuorossa on Sampo Sahkolainen.
Mihin ruutuun merkki lisataan?
2:3
Pelitilanne nyt:
__0_
XX0_
_X0_
____
Vuorossa on Tiina Teekkari.
Mihin ruutuun merkki lisataan?
1:3
Pelitilanne nyt:
_X0_
XX0_
_X0_
____
Vuorossa on Sampo Sahkolainen.
Mihin ruutuun merkki lisataan?
-1:0
Valitsemaasi ruutuun ei voi lisata merkkia.
Mihin ruutuun merkki lisataan?
2:0
Peli on paattynyt. Pelilaudan tilanne lopuksi:
_X0_
XX0_
_X0_
__0_
Voittaja on Sampo Sahkolainen
[ohjelman suoritus päättyy]
[ohjelman suoritus alkaa]
Tervetuloa pelaamaan ristinollaa 4x4-ruudukolla.
Ruutujen koordinaatit annetaan muodossa X:Y.
Koordinaatit alkavat vasemmasta alakulmasta nollasta.
Kuka on ensimmainen pelaaja?
Riina Raksalainen
Kuka on toinen pelaaja?
Teemu Teekkari
Pelitilanne nyt:
____
____
____
____
Vuorossa on Riina Raksalainen.
Mihin ruutuun merkki lisataan?
2:2
Pelitilanne nyt:
____
__X_
____
____
Vuorossa on Teemu Teekkari.
Mihin ruutuun merkki lisataan?
1:1
Pelitilanne nyt:
____
__X_
_0__
____
Vuorossa on Riina Raksalainen.
Mihin ruutuun merkki lisataan?
3:0
Pelitilanne nyt:
____
__X_
_0__
___X
Vuorossa on Teemu Teekkari.
Mihin ruutuun merkki lisataan?
2:1
Pelitilanne nyt:
____
__X_
_00_
___X
Vuorossa on Riina Raksalainen.
Mihin ruutuun merkki lisataan?
3:1
Pelitilanne nyt:
____
__X_
_00X
___X
Vuorossa on Teemu Teekkari.
Mihin ruutuun merkki lisataan?
3:2
Pelitilanne nyt:
____
__X0
_00X
___X
Vuorossa on Riina Raksalainen.
Mihin ruutuun merkki lisataan?
1:2
Pelitilanne nyt:
____
_XX0
_00X
___X
Vuorossa on Teemu Teekkari.
Mihin ruutuun merkki lisataan?
3:3
Pelitilanne nyt:
___0
_XX0
_00X
___X
Vuorossa on Riina Raksalainen.
Mihin ruutuun merkki lisataan?
0:3
Pelitilanne nyt:
X__0
_XX0
_00X
___X
Vuorossa on Teemu Teekkari.
Mihin ruutuun merkki lisataan?
0:0
Pelitilanne nyt:
X__0
_XX0
_00X
0__X
Vuorossa on Riina Raksalainen.
Mihin ruutuun merkki lisataan?
0:1
Pelitilanne nyt:
X__0
_XX0
X00X
0__X
Vuorossa on Teemu Teekkari.
Mihin ruutuun merkki lisataan?
0:2
Pelitilanne nyt:
X__0
0XX0
X00X
0__X
Vuorossa on Riina Raksalainen.
Mihin ruutuun merkki lisataan?
1:0
Pelitilanne nyt:
X__0
0XX0
X00X
0X_X
Vuorossa on Teemu Teekkari.
Mihin ruutuun merkki lisataan?
1:3
Pelitilanne nyt:
X0_0
0XX0
X00X
0X_X
Vuorossa on Riina Raksalainen.
Mihin ruutuun merkki lisataan?
2:0
Pelitilanne nyt:
X0_0
0XX0
X00X
0XXX
Vuorossa on Teemu Teekkari.
Mihin ruutuun merkki lisataan?
2:3
Peli on paattynyt. Pelilaudan tilanne lopuksi:
X000
0XX0
X00X
0XXX
Peli paattyi tasapeliin.
[ohjelman suoritus päättyy]
