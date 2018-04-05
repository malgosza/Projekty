from flask import Flask

#klasa przedstawiajaca aplikacje, czyli stworzy serwer
apka=Flask(__name__)

#dekorator - '@...'
@apka.route("/")
def stronaStartowa():
    return "<h1>Moja Apka</h1>"

@apka.route("/omnie")
def oMnie():
    return "<h1>Ja</h1>"

#postawi serwer
if __name__ == '__main__':
    apka.run(debug=True)