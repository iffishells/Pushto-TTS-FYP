from flask import Flask , render_template , request , url_for ,redirect
import load_data
# importlib.reload(load_data)
# flask app
app = Flask(__name__)



audio_data = load_data.loadingdata()


@app.route('/' ,methods=[ 'POST','GET'])
def home():
    if request.method == 'POST':
        # return request.form
        path = audio_data[request.form['choosed_l']]
        print(path)
        return render_template('index.html' ,path = path,audiodb = audio_data)
    else:
        return render_template("index.html" , path = None,audiodb = audio_data)


# @app.route('/adio')
# def audio():
        
if __name__ == '__main__':
    app.debug =True
    app.port = 8080
    app.run()
