from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>Welcome to my web application</h1>
<p>Click <a href="/project">here</a> to go to the project page</p>
<p>Click <a href="/about">here</a> to go to the about page</p>''' # rute web utama tanpa slash dengan dua rute dibawah 

@app.route('/project')
def project():
    return 'the project page'

@app.route('/about')
def about():
    return 'the about page'


if __name__ == '__main__':
    app.run(debug=True, port=5000)

# url kanonik untuk projects titik akhir memiliki garis miring hal ini mirip dengan folder dalam file sistem jika kita mengakses dalam port 127.0.0.1:5000/projects 
# maka secara langsung flask akan mengarah ke url dengan slash didepan /projects/

# URL kanonik untuk abouttitik akhir tidak memiliki garis miring di akhir. Hal ini mirip dengan nama jalur berkas. Mengakses URL dengan garis miring di akhir ( /about/) akan menghasilkan kesalahan 404 "Tidak Ditemukan". Hal ini membantu menjaga URL tetap unik untuk sumber daya ini, sehingga mesin pencari dapat menghindari pengindeksan halaman yang sama dua kali.
