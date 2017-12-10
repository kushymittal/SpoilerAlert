import pickle

from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

model = pickle.load(open('model.sav', 'rb'))

@app.route('/')
def index():
    return 'Sample Page'

@app.route('/classify', methods=['POST'])
def classify_posts():
    print request

    data = request.form
    if len(data) == 0:
        return 'OK'

    output = model.predict(data.values())

    for i in range(len(data)):
        if output[i] == 0:
            print data.values()[i].encode('utf-8'), ': Not a Spoiler'
        else:
            print data.values()[i].encode('utf-8'), ': Spoiler'

    return ','.join([str(x) for x in output])

if __name__ == '__main__':
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context=context)
    #app.run(ssl_context='adhoc')
    #app.run()
