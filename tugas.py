from flask import Flask, request
from base import save_to_base

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'EMPTY itu kosong'

@app.route('/loho' , methods = ['GET', 'POST'])
def paket():
    if request.method == 'GET':
        return 'hayo ka GET ya'
    elif request.method == 'POST':
        return 'kali ini ga kaget kan'

@app.route('/ware', methods=['GET', 'POST'])
def kuota():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    save_to_base(kecepatan=kecepatan, latitude=latitude, longitude=longitude)
    return{
        "kecepatan": 90,
        "latitude": 6.2088,
        "longitude": 106.8456
    }

if __name__ == '__main__':
    app.run(debug=True)
