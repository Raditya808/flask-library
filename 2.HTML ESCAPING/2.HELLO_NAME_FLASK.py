from flask import Flask, request 
from markupsafe import escape
 
app = Flask(__name__) 

# Contoh kode di web nya
#=========================================================
#@app.route("/<name>")                           #========
#def hello(name):                                #========
    #name = request.args.get("name", "Flask")    #========
    #return f"Hello, {escape(name)}!"            #========
#=========================================================



# contoh kode implementasi ke bahasa indonesia

#=============================================================================
@app.route("/<nama>")                                               #=========
def halo(nama):                                                     #=========
    nama = request.args.get("nama", "Nama kamu tidak ditemukan")    #=========
    return f"hallo, {escape(nama)}"                                 #=========
#=============================================================================

# kode ini berfungsi Membuat halaman /hello yang menyapa user 
# berdasarkan parameter name di URL, dengan aman dari XSS.
# jika di akses dengan
# http://127.0.0.1:5000/halo?nama=adit
''' maka output akan mengeluarkan hallo, adit '''


if (__name__)== "__main__":
    app.run(debug=True, port=5000)
