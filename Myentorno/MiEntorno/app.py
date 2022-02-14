from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/index.html/')
def inicio():
    return render_template("index.html")
    

@app.route('/sumar')
def suma():
    return render_template("sumar.html")

@app.route('/menu')
def menu():
    return render_template("index.html")

@app.route('/resta')
def resta():
    return render_template("restar.html")

@app.route('/multiplica')
def multiplica():
    return render_template("multiplica.html")

@app.route('/divide')
def division():
    return render_template("division.html")

@app.route('/accionDividir',methods=["POST"])
def accionDividir():
    numero1=int(request.form.get("numero1"))
    numero2=int(request.form.get("numero2"))
    divide=numero1/numero2
    return render_template("resultadoDivision.html",numero1=numero1,numero2=numero2,divide=divide)

@app.route('/accionMultiplicar',methods=["POST"])
def accionMultiplicar():
    numero1=int(request.form.get("numero1"))
    numero2=int(request.form.get("numero2"))
    mult=numero1*numero2
    return render_template("resultadoMult.html",numero1=numero1,numero2=numero2,mult=mult)


@app.route('/accionSumar',methods=["POST"])
def accionSumar():
    numero1=int(request.form.get("numero1"))
    numero2=int(request.form.get("numero2"))
    suma=numero1+numero2
    return render_template("resultado.html",numero1=numero1,numero2=numero2,suma=suma)

@app.route('/accionRestar',methods=["POST"])
def accionRestar():
    numero1=int(request.form.get("numero1"))
    numero2=int(request.form.get("numero2"))
    resta=numero1-numero2
    return render_template("resultadoResta.html",numero1=numero1,numero2=numero2,resta=resta)

app.run('0.0.0.0',8081, debug=True)