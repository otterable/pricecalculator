from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

ITEMS = {
	"Kotflügel/Fenders | blatníky set MAX1 Ventura 24\"-28\"": 8.16,
	"Bremsbelag/Bremsklotz (direkter Pin) | brzdová botka dřík MAX1 60mm": 1.64,
	"Bremsbelag/Bremsklotz (mit Gewinde) | brzdová botka závit MAX1 60 mm": 2.26,
	"Bremshebel/Bremsschalter | brzdové páky MAX1 \"V\" Alu": 6.23,
	"Reifen/Pneu | plášť CHAOYANG 26x2,10 (559-52) H-5152 27 tpi černý": 9.72,
	"Reifen/Pneu | plášť KENDA 24x1,5 (507-40) (K-184) černý": 7.91,
	"Reifen/Pneu | plášť KENDA 26x1,95 (559-50) (K-831) černý": 9.72,
	"Reifen/Pneu | plášť KENDA 26x1,95 (559-50) (K-892) černý": 9.72,
	"Reifen/Pneu | plášť KENDA 700x32C (622-32) (K-125) černý": 8.28,
	"Kotflügel/Fenders | KELLYS Blatníky KLS STORM": 8.98,
	"Kettenreiniger/Kettenputzmittel | KELLYS Čistič řetězu KLS CRYSTAL": 16.36,
	"Fahrradreiniger/Radreinigungsmittel | KELLYS Čistící prostředek KLS BIKE CLEANER náhradní náplň 1000 ml": 6.52,
	"Flaschenhalter/Getränkehalter | Košík na fľašu KLASIK čierny": 2.09,
	"Pedale/Trittflächen | Pedály Extend MTB-825A plastic": 3.32,
	"Sattel/Fahrradsitz | Sedlo SMP MTB 6370 čierne": 7.83,
	"Speichenreflektor/Radreflektor | odrazka do výpletu malá": 0.33,
	"Vorderreflektor/Frontreflektor | odrazka přední s držákem malá \"V\"": 0.86,
	"Rückreflektor/Heckreflektor | odrazka zadní s držákem malá \"V\"": 0.86,
	"Öl/Schmieröl | olej WD-40 400ml": 6.23,
	"Schraube/Bolzen | M6 x 40mm, Schwarz": 0.7055,
	"Schraube/Bolzen | M6 x 50mm, Schwarz": 0.7055,
	"Schraube/Bolzen | M5 x 12mm": 0.4,
	"Schraube/Bolzen | M5 x 16mm": 0.4,
	"Fahrradgriffe | MAX1 Gross": 2.5,
	"Fahrradgriffe | Walfort": 2.99,
	"Mutter | verschiedene Größen": 0.4,
	"Distanzstücke / Unterlegscheiben | verschiedene Größen": 0.2,
	"Fahrradschlauch/Innerreifen | Walfort Fahrradschlauch 28 x 1 5/8 x 1 3/8 ETRTO: 30-622 // 700 x 35/43c": 1.99,
	"Ständer/Fahrradständer | stojánek MAX1 středový stavitelný s podložkou 20-29\" černý": 4.75,
	"Bremsenreiniger/Bremsputzmittel | čistič brzd MAX1 Brake Cleaner 10 ml": 0.10,
	"Fahrradschlauch/Innerreifen | FISCHER Fahrradschlauch mittel in 26 Zoll | ETRO-Norm: 37/57-559 | Auto Ventil": 3.02,
	"Rückleuchte/Hecklampe | Walfort Fahrradrückleuchte": 0.99,
	"Scheinwerfer/Frontlampe | Walfort Fahrrad-Scheinwerfer": 0.99,
	"Scheinwerfer/Frontlampe | Ali Klein": 3.09,
	"Scheinwerfer/Frontlampe | Ali Big": 2.71,
	"Beleuchtungsset/Lichtset | Walfort Fahrradbeleuchtungsset": 7.99,
	"Klingel/Fahrradglocke (klein) | Kleine Fahrradklingel": 0.89,
	"Klingel/Fahrradglocke (groß) | Große Fahrradklingel": 2,
	"Sattel/Fahrradsitz (komfortabel) | Fahrradsitz, weich und angenehm": 7.99,
	"Sattel/Fahrradsitz (komfortabel) | Fahrradsitz, Ali Luxus": 13,
	"Sattel/Fahrradsitz (einfach) | Fahrradsitz, einfach": 6,
	"Schraube/Bolzen | M6 x 50mm": 0.7,
	"Schrauben/Bolzen | Fahrradreparaturset, verschiedene Größen": 0.30,
	"Handyhalter | Generic": 1.85,

}



@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == "POST" and "save" in request.form:
        with open("bikeprices.txt", "a") as f:
            f.write(f"{request.form['name']}\n")
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{request.form['totalPrice']}€\n")
        flash("Repair cost saved!")
        return redirect(url_for('index'))


    return render_template("index.html", items=ITEMS)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["password"] == "eldorado":
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash("Wrong password!")
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
