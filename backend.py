import pickle

from flask import Flask
from flask import request
app = Flask(__name__)

model = pickle.load(open('model.sav', 'rb'))

@app.route('/')
def index():
    return 'Sample Page'

@app.route('/classify', methods=['POST'])
def classify_posts():
    data = request.form
    if len(data) == 0:
        return 'OK'

    output = model.predict(data.values())

    for i in range(len(data)):
        if output[i] == 0:
            print data.values()[i].encode('utf-8'), ': Not a Spoiler'
        else:
            print data.values()[i].encode('utf-8'), ': Spoiler'

    return 'OK'

if __name__ == '__main__':
    app.run()
