import pickle

from flask import Flask
from flask import request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#from OpenSSL import SSL 
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('alice.key')
#context.use_certificate_file('alice.crt')

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

    return 'OK'

if __name__ == '__main__':
    #context = ('alice.crt', 'alice.key')
    #app.run(ssl_context=context)
    app.run()
