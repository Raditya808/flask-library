from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index' 

@app.route('/login')
def login():
    return 'ini page login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    
app.run(debug=True, port=5000)
   
#===============================================
# url_for('index')                 
# → Membangun URL untuk fungsi view bernama 'index'
# → Hasil: '/' atau '/index' tergantung definisi route
#===============================================

# url_for('login')                 
# → Membangun URL untuk fungsi view bernama 'login'
# → Hasil: '/login'
#===============================================

# url_for('login', next='/')       
# → Menambahkan query string ke URL login
# → Hasil: '/login?next=/'
#===============================================

# url_for('profile', username='John Doe') 
# → Membangun URL dengan parameter dinamis 'username'
# → Hasil: '/profile/John%20Doe' (otomatis di-escape)
#===============================================

# secara ringkas kode ini berfungsi membangun url otomatis dengan url for()
# dan bisa diakses di web ketika di copy 

