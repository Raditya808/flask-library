from flask import Flask , request, render_template 

app = Flask(__name__)
#========================================================================
#                                                                       =
# contoh routing pertama menggunakan file templates dari hhtml          =
#                                                                       =
#========================================================================
def valid_login(username, password):                    #================
    return username == 'admin' and password == 'secret' #================
                                                        #================
                                                        #================
def log_the_user_in(username):                          #================
    return f'Logged in as {username}'                   #================
                                                        #================
#========================================================================
@app.route('/',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
#========================================================================
#                                                                       =
# contoh tanpa menggunakan file templates                               =
# isue dengan kode error tidak keluar di web                            =
#========================================================================
def valid_Login(namapengguna, sandi):                   #================                   
    return namapengguna == 'admin' and sandi == '12345' #================
                                                        #================
                                                        #================
def user_login(namapengguna):                           #================
    return f'''                                         
                                                                
    <h1>Welcome to website using flask without templates html file
    '''                                                 #================
#========================================================================
@app.route('/login', methods=['GET','POST'])
def masuk():
    error = None
    if request.method == "POST":
        if valid_Login(request.form['namapengguna'],
                       request.form['sandi']):
            return user_login(request.form['namapengguna'])

        else:
            error = 'invalid nama pengguna / sandi'
        
    return f'''
      <form method="POST" action="/login">
    {f'<p style="color: red">{error}</p>' if error else ''}
    Nama: <input type="text" placeholder="Nama pengguna" 
    name="namapengguna"><br>
    password: <input type="password" placeholder="sandi" 
    name="sandi"><br>
    <input type="submit" value="submit">
    </form>
        ''' 
#========================================================================

if __name__ == '__main__':
    app.run(debug=True, port=5000)

 # kode ini membuat suatu web aplikasi sederhana dengan Flask 
 # yang menangani login.
 # dengan key yang bernama username dan password
 # dengan nama admin dan password sebagai secret
 
 # jika salah memasuukan nick dan password 
 # maka akan terjadi error di kode html

