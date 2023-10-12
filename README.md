Tehtävä 3 - Labran palveluiden ja asetusten keskitetty esittäminen 
Paavo Meri 


Johdanto 
Tämä raportti kuvaa Djangolla toteutetun hallintasivuston arkkitehtuuria ja toimintaa, joka kokoaa yhteen kaikki labran laitteet ja työkalut. 


Arkkitehtuuri 
Projektin tietokannassa on kolme päämallia: Kategoria, Kohde ja SivunLataukset. Kategoria tallentaa eri laite- ja palvelu kategoriat. Kohde tallentaa yksittäiset laitteet ja palvelut, sillä on forgein key joka yhdistää jokaisen kohteen Kategoria malliin. Jokaisella kohteella voi olla nimi, IP-osoite, linkki ja tunnistetiedot. SivunLataukset tallentaa tiedot jokaisesta sivun latauksesta ja IP-osoitteista. 

Projektilla on yksi näkymä nimeltään index se hakee tietokannasta kaikki tiedot ja lähettää ne index.html templaatin käytettäväksi, se näyttää Kategoriat ja niihin liittyvät Kohteet dynaamisesti. 


Toiminnallisuus 
Projektin käyttöönotto: Aloita asentamalla tarvittavat Linux-paketit komennoilla: 
“sudo apt install python3-pip" ja “pip3 install django”. Seuraavaksi tuo projekti Githubista esimerkiksi komennolla “git clone https://github.com/PaavoMeri/PaavoMeri_teht3.git”. Hakeudu seuraavaksi kansioon jossa manage.py tiedosto sijaitsee, tässä kansiossa voit luoda superuser käyttäjän komennolla “python3 manage.py createsuperuser” tämä on tärkeää että pääset kirjautumaan Djangon admin hallintasivuun. Nyt palvelimen voi käynnistää komennolla “python3 manage.py runserver”. Nettisivun pitäisi olla nyt saatavilla osoitteesta localhost:8000 . Django:n admin hallintapaneeliin pääsee osoitteesta localhost:8000/admin . Muista, että tuotantokäytössä on suositeltavaa käyttää WSGI-palvelinta yhdessä verkkopalvelimen kanssa. Tämä tarjoaa paremman suorituskyvyn, vakauden ja turvallisuuden verrattuna Django:n sisäänrakennettuun kehityspalvelimeen.  
Hallintasivun pääsivulla on yksinkertaisesti lista kaikista laitteista ja palveluista, ne päivittyy dynaamisesti jos kohteita lisätään. Kohteiden lisääminen tapahtuu Django:n admin sivulta, kirjauduttuasi sinne sivun vasemmasta laidasta löytyy Kategoriat, Kohteet ja Sivun Lataukset.  

 
Johtopäätökset 
Tämä projekti tarjoaa tehokkaan ja keskitetyn tavan esittää labran laitteet ja työkalut, sen voisi laittaa esimerkiksi Active Directoryä käyttämällä labrassa olevien Windows työasemien selainten kotisivuksi. Django tarjoaa joustavan ja tehokkaan tavan muokata ja laajentaa sovellusta tarpeen mukaan. 
