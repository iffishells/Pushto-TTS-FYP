from flask import Flask , render_template , request , url_for ,redirect
import load_data
# importlib.reload(load_data)
# flask app


app = Flask(__name__)

# audio_data = load_data.loadingdata()

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")
    
@app.route('/about')
def about():
    return 'this is about page'




if __name__ == '__main__':
    app.run(debug=True,port=8080)
