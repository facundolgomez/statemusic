from flask import Flask, request

app = Flask(__name__)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    with open("code.txt", "w") as f:
        f.write(code)
        
    return f"Se ha recibido el codigo para obtener el token"
    
app.run(port=8888)
