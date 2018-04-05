from flask import Flask
from flask import render_template
#klasa przedstawiajaca aplikacje, czyli stworzy serwer
apka=Flask(__name__)

def dajZwierzakaZbazyDanych():
    return " dzik"

#dekorator - '@...'
@apka.route("/")
def stronaStartowa():

    return render_template('stronaStartowa.html',message="Moja tresc", zwierzak=dajZwierzakaZbazyDanych())

@apka.route("/omnie")
def oMnie():
    return "<h1>Ja</h1>"

#postawi serwer
if __name__ == '__main__':
    apka.run(debug=True)