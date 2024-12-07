from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

# Dosya yolu, verilerin kaydedileceği yer
DATA_FILE = 'messages.txt'

@app.route('/')
def index():
    # Ana sayfayı döndür
    return '''
    <form action="/submit" method="POST">
        <input type="text" name="name" placeholder="Adınız" required>
        <input type="text" name="phone" placeholder="Numaranız" required>
        <textarea name="message" rows="5" placeholder="Mesajınız" required></textarea>
        <input type="submit" value="Mesaj Gönder">
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    # Formdan gelen verileri al
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']

    # Verileri dosyaya yaz
    with open(DATA_FILE, 'a') as f:
        f.write(f'Ad: {name}, Telefon: {phone}, Mesaj: {message}\n')

    # Başarıyla gönderim sonrası kullanıcıyı yönlendir
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return 'Mesajınız başarıyla gönderildi!'

if __name__ == '__main__':
    # Sunucuyu çalıştır
    app.run(debug=True)