from logging import PlaceHolder
from flask import Flask, make_response, render_template, request, url_for

app = Flask(__name__)

# Kode web 1
#==================================================
#@app.route('/login',methods=['GET', 'POST']) #====
#def login():                                 #====
    #if request.method == 'POST':             #====
        #return 'do_the_login()'              #====
    #else:                                    #====
      #return 'show_login_form'               #====
#==================================================
# contoh kode jika login akan menampilkan login 
# else menampilkan form login



# Kode web 2
#===========================================================
#@app.route('/login',methods=['GET','POST'])         #======
#def login_get():                                    #======
    #return show_login_form()                        #======
                                                     #======
# tidak bisa menamakan dua nilai variabel yang sama  #======
                                                     #======
#@app.route('/login2')                               #======
#def login_post():                                   #======
    #return  do_the_login()                          #======
#===========================================================
# dua routing yang sama yang membedakan tidak ada method



# contoh kode 1 menggunakan metode 12.COOKIE dalam repo dan tidak ada variabel didalam routing 
# aturan flask menggunakan ('/') harus paling awal kalau tidak akan error

# cookie dalam tampilan web utama tanpa html

#================================================================================================
@app.route('/',methods=['GET','POST'])                                          #================
def cookie_in_http_method():                                                    #================
    if request.method == 'POST':                                                #================
                                                                                #================
        username = request.form.get('username')                                 #================
        resp = make_response(f'''                                               
        <h3>Cookie saved</h3>                                                   
        <p> hello. {username}</p>
        <a href='/'Back</a>
        ''')                                                                    #================
                                                                                #================
        resp.set_cookie('username',username)                                    #================
        return resp                                                             #================
                                                                                #================
                                                                                #================
    else:                                                                       #================
        username = request.cookies.get('username')                              #================
        return f'''                                                             
            <form method="POST" action="/">                         
                <input type="text" name="username" placeholder="Username"><br>
                <button type="submit">Submit</button>
            </form>
            {'<p>Cookie ditemukan: ' + username + '</p>' if username else ''}
        '''                                                                     #================
#================================================================================================



# kode 2 dalam html form menggunakan if statement dalam bentuk for
#=================================================================================
@app.route('/login',methods=['GET','POST'])                             #=========                   
def login():                                                            #=========
    if request.method == 'POST':                                        #=========
        return '''                                                      
        <h1> hello Login</h1>                                           
      '''                                                               #=========
    else:                                                               #=========
     return '''                                                         
  <form method="POST" action="/login">  
                                                                        
  <input type="text" name="username" placeholder="Username"><br>        
  <input type="password" name="password" placeholder="Password"><br>  
  <input type="submit" value="Login"></form>                              
                                                                    
'''                                                                     #=========  
#=================================================================================
# fungsi value="login" adalah mengisi form dengan teks / tanpa ada action maka data tidak ke kirim ke yang lain action=/login akan masuk di h1 hello world di kode python

# methods='POST' selalu di python sedangkan html adalah method='POST'
# python = method
# html = method





# kode 3 dalam form html tanpa menggunakan if statement

# adding code later
# tanpa logic if statement

# 2 routing bagian ini ketika pengguna berhasil masuk
#===============================================================================================================
@app.route('/Login1',methods=['GET','POST'])                                                            #=======
def login1():                                                                                           #=======
    return '''                                                                                          
    <h1>hello world</h1>

''' 
                                                                                                        #=======
# bagian ini ketika pengguna akan menginput username password bagian ini belum ada data dengan database #=======
                                                                                                        #=======
@app.route('/Login2',methods=['GET','POST'])                                                            #=======
def login2():                                                                                           #=======
    return '''                                                                                          
    <form method="POST" action="/Login1">                                                               

    <input type="text" name="username" PlaceHolder="Username"><br>
    <input type="password" name="password" PlaceHolder="Password"><br>
    <input type="submit" Value="submit">
'''
                                                                                                        #=======
#===============================================================================================================

# syntax menjalankan web nya 
if __name__ == '__main__':
    app.run(debug=True, port=5000)
