from flask import request, Flask, redirect, url_for
import re
#myfile = "test.txt"

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    value = request.json
    k=json.dumps(value)
    print k
    with open("test.txt", 'w') as f:
        f.write(str(k))
    return "ok"

if __name__ =='__main__':
    app.run(debug=True)
