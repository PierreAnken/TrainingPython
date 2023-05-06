from flask import Flask

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    # traitement de la demande de chat ici
    pass


def chat():
    # Récupérer le message envoyé par l'utilisateur
    message = request.form['message']

    # Envoyer le message à moi et obtenir une réponse
    response = send_message(message)

    # Renvoyer la réponse à l'utilisateur
    return response
