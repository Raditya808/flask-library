from flask import Flask, request



app = Flask(__name__)


# Contoh kode di web 

#============================================================
#with app.test_request_context('/hello', method='POST'): #===
    #assert request.path == '/hello'                     #===
    #assert request.method == 'POST'                     #===
#============================================================
    
    # kode ditas hanya berjalan di terminal saja tapi 
    # dikarenakan tidak ada route yang 
    # ditentukan maka hanya menampilkan eror 404


#======================================================================
@app.route('/',methods=['GET','POST'])
def user_masuk():
    username = request.args.get("username","nama kamu ditemukan")
    if request.method == 'POST':
        username = request.form.get("username","nama kamu telah ditemukan")
        return f'''
        Halo, {username}
        '''
    else:
        return '''
        <form method='POST' action='/'>
        <input type ="text" name="username" placeholder="username">
        <input type="submit" value="kirim">
        '''
# Pengecekan data dengan request palsu (BUKAN dari browser)
with app.test_request_context('/',method='POST'):
# Flask membuat request palsu seolah-olah ada user kirim POST ke "/"

# Cek apakah path yang diakses "/" (benar → tidak error, salah →AssertionError)
    assert request.path == '/'


# Cek apakah method yang digunakan POST (benar -> tidak error, salah ->AssertionError)
    assert request.method == 'POST'
#======================================================================
# Catatan: bagian ini tidak memunculkan log Flask dan tidak tampil di browser.
# Hanya dipakai untuk testing internal dalam kode Python.
# ga tau ini fungsi nya apaan 

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # app.run(host='    
    
    
 
