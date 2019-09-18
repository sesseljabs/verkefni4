from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

frettir = [[0,"„Upp­lýs­um ekki um smá­atriði“", "Ekk­ert flugrekstr­ar­leyfi hef­ur verið veitt af hálfu banda­rískra yf­ir­valda fyr­ir arf­taka WOW air ef marka má gagna­grunn banda­rískra yf­ir­valda. Jafn­framt hef­ur flug­mála­deild banda­ríska sam­gönguráðuneyt­is­ins ekki fengið neina um­sókn um slíkt leyfi, en þeim ber að birta það í gagna­grunn­in­um sem aðgengi­leg­ur er al­menn­ingi.", "/static/img/wow.jpg", "sigmundurad@frettir.is"], [1,"Lést eft­ir björg­un úr brenn­andi húsi", "Karl­maður, sem bjargað var úr brenn­andi húsi við Hlíðar­veg í Reykja­nes­bæ síðdeg­is á föstu­dag, lést á Land­spít­al­an­um síðar sama dag. \nÞetta staðfest­ir Svein­björn Hall­dórs­son, lög­reglu­full­trúi hjá lög­regl­unni á Suður­nesj­um, í sam­tali við mbl.is, en Vís­ir greindi fyrst frá.", "/static/img/brenn.jpg", "sigmundurbc@frettir.is"], [2,"Vaxta­lækk­an­ir skili sér í hús­næðis­verð", "Gera má ráð fyr­ir að vaxta­lækk­an­ir Seðlabanka hafi áhrif á hús­næðis­vexti al­mennt. Slík­ar vaxta­lækk­an­ir gætu þrýst hús­næðis­verði upp á við. Þetta er mat Gunn­ars Bjarna Viðars­son­ar, sér­fræðings í grein­ing­ar­deild Ari­on banka.", "/static/img/vet.jpg", "gurragris@frettir.is"], [3,"Heit­asta græn­metið hér­lend­is í dag", "Græn­meti er ekki bara græn­meti eins og þið vitið öll og nú ber svo við að sam­fé­lags­miðlar nán­ast loga vegna umræðna um það sem við get­um ein­ung­is full­yrt að sé vin­sæl­asta og eft­ir­sótt­asta græn­metið í dag: Blóm­kál!", "/static/img/kal.jpg", "sapukula@frettir.is"]]

@app.route("/")
def home():
    return render_template('main.html', frettir=frettir)

@app.route("/frett/<int:id>")
def frett(id):
    return render_template("frett.html", frettir=frettir, id=id)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    #app.run() 