from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

    imc = None
    erro = None

    if request.method == "POST":

        peso = float(request.form["peso"])
        altura = float(request.form["altura"])

        if peso <= 0:
            erro = "O peso deve ser maior que zero."

        elif altura <= 0:
            erro = "A altura deve ser maior que zero."

        else:
            imc = peso / (altura ** 2)

    return render_template(
        "index.html",
        imc=imc,
        erro=erro
    )


if __name__ == "__main__":
    app.run(debug=True)