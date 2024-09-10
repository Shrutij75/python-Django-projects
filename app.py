from flask import Flask, render_template, request,redirect,url_for

# create a simple flask application
app = Flask(__name__)  # initialize the flask class, and it's the entry point

@app.route("/", methods=['GET'])
def welcome():
    return "<h1>Welcome to my flask application</h1>"

@app.route("/index", methods=['GET'])
def index():
    return "<h2>Welcome to my first index page!!!</h2>"


@app.route("/success/<int:score>", methods=['GET'])
def success(score):
    return "<h2>The person is passed and has the score"+str(score)


@app.route("/fail/<int:score>", methods=['GET'])
def fail(score):
    return "<h2>The person is failed and has the score"+str(score)


@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html', score=None)
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        avg = (maths + science + history) / 3
        res=" "
        if avg>=50:
            res="success"
        else:
            res="fail"
            
        return redirect(url_for(res,score=avg))
        # return render_template('form.html', score=avg)

if __name__ == "__main__":
    app.run(debug=True)

