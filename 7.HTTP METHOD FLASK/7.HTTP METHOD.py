from flask import Flask, request

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




# kode 1 dalam html form menggunakan if statement dalam bentuk form
#=================================================================================
@app.route('/login',methods=['GET','POST'])                           
def login():                                                          
  if request.method == 'POST':                                        
    return '''                                                        
      <h1> hello login</h1>                                           
      '''                                                             
  else:                                                               
    return '''                                                        
  <form method="POST" action="/login">

  <input type="text" name="username" placeholder="Username"><br>      
  <input type="password" name="password" placeholder="Password"><br>  
  <input type="submit" value="Login"></form>                              
                                                                      
'''                                                                   
#=================================================================================
# fungsi value="login" adalah mengisi form dengan teks / tanpa ada action maka data tidak ke kirim ke yang lain action=/login akan masuk di h1 hello world di kode python

# methods='POST' selalu di python sedangkan html adalah method='POST'
# python = method
# html = method





# kode 2 dalam form html tanpa menggunakan if statement

# adding code later



if __name__ == '__main__':
    app.run(debug=True, port=5000)
