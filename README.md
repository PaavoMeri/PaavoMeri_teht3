# pilvipalvelut_tehtava3

Toiminnallisuus 

Projektin käyttöönotto: Aloita asentamalla tarvittavat Linux-paketit komennoilla: 
“sudo apt install python3-pip" ja “pip3 install django”. Seuraavaksi tuo projekti Githubista esimerkiksi komennolla “git clone https://github.com/PaavoMeri/PaavoMeri_teht3.git”. Hakeudu seuraavaksi kansioon jossa manage.py tiedosto sijaitsee, tässä kansiossa voit luoda superuser käyttäjän komennolla “python3 manage.py createsuperuser” tämä on tärkeää että pääset kirjautumaan Djangon admin hallintasivuun. Nyt palvelimen voi käynnistää komennolla “python3 manage.py runserver”. Nettisivun pitäisi olla nyt saatavilla osoitteesta localhost:8000 . Django:n admin hallintapaneeliin pääsee osoitteesta localhost:8000/admin . Muista, että tuotantokäytössä on suositeltavaa käyttää WSGI-palvelinta yhdessä verkkopalvelimen kanssa. Tämä tarjoaa paremman suorituskyvyn, vakauden ja turvallisuuden verrattuna Django:n sisäänrakennettuun kehityspalvelimeen.  
