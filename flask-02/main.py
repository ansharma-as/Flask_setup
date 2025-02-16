from flask import Flask , redirect , url_for , render_template
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success():
    return "Pass"

@app.route('/fail/<int:score>')
def fail():
    return "failed"

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if(marks<30):
        return 'fail'
    else:
        return 'successs'
    return redirect(url_for(result, score=marks))


if __name__ == '__main__':
    app.run(debug=True)