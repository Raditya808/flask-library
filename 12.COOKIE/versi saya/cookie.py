from flask import Flask , render_template, request, make_response

app = Flask(__name__)


@app.route('/Cookies', methods=['GET','POST'])
def get_cookies():
   

    if request.method == 'POST':

        namapengguna = request.form.get('namapengguna')

        resp = make_response(f'''
        <h3>Cookie tersimpan</h3>
        <p> halo vroh {namapengguna}</p>
        <a href="/Cookies"Home</a>
        ''')
   
        resp.set_cookie('namapengguna',namapengguna)
        return resp
    
                

    else:
        namapengguna = request.cookies.get('namapengguna')
        return render_template('cookiie.html',namapengguna=namapengguna)


if __name__ == '__main__':
    app.run(debug=True)
# contoh reouting tanpa tambahan menggunakan app = Flask(__name__,template_folder='templates')
