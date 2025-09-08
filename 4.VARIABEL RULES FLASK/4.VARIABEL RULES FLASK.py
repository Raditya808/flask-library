from flask import Flask
from markupsafe import escape # Fungsi  dari modul  digunakan untuk mengamankan teks agar tidak dieksekusi sebagai HTML atau JavaScript. Ini sangat penting untuk mencegah serangan seperti XSS (Cross-Site Scripting).

app = Flask(__name__)

# dalam flask pengguna dapat menambahkan bagian variabel ke url dengan menandai dengan <contoh_variabel> 


#=======================================================
# https://flask.palletsprojects.com/en/stable/quickstart/#routing
                                                 #======
#@app.route('/user/<username>')                  #======
#def show_user_profile(username):                #======
    #return f"User {escape(username)}"           #======
                                                 #======
                                                 #======
#@app.route('/post/<int:post_id>')               #======
#def post_id(post_id):                           #======
    #return f"Post ID: {post_id}"                #======
                                                 #======
#@app.route('/path/<path:subpath>')              #======
#def show_subpath(subpath):                      #======
    #return f"Subpath: {escape(subpath)}"        #======
#=======================================================


# converter types
#============================================================
'''                                                     #====
string  | (default) accepts any text without a slash    #==== 
int     |  accepts positive inetgers                    #====     
float   | accept positive floating point values         #====
path    | like string but also accepts slashes /        #====
uuid    | accepts uuid string                           #====
'''                                                     #====
#============================================================

# contoh routing menggunakan variabel dan memanggil nama
# ini sudah dianggap sebagai str dan tidak perlu menambahkan parameter str seperti int atau float
@app.route('/pengguna/<namapengguna>')
def menampilkan_profil_pengguna(namapengguna):
    return f"Pengguna {escape(namapengguna)}"


# contoh routing dalam bentuk integer jika diakses http:127.0.0.1.5001/nilai/19
@app.route('/nilai/<int:id_nilai>')
def menampilkan_id_nilai(id_nilai):
    return f"Id nilai: {id_nilai}" # output Id nilai :angka


# contoh routing float jika diakses dengan http:127.0.0.1.5001/nilaifloat/3.14 harus bernilai float kalau angka biasa akan bernilai integer
@app.route('/nilaifloating/<float:nilaifloat>')
def menampilkan_angka_float(nilaifloat):
    return f"id nilai float: {nilaifloat}"

# uuid
@app.route('/struuid/<uuid:namauuid>')
def menampilkan_profil_uuid(namauuid):
    return f"uuid str: {namauuid}"
# http://localhost:5000/struuid/123e4567-e89b-12d3-a456-426614174000

# Ini mendefinisikan route  di aplikasi Flask.Bagian  berarti Flask akan menangkap UUID yang valid dari URL dan otomatis mengonversinya menjadi objek Fungsi ini akan dipanggil saat route tersebut diakses. Parameter  berisi UUID yang dikirim lewat URL.Ini mengembalikan string yang menampilkan UUID tersebut. Karena  adalah objek UUID, Flask akan otomatis mengubahnya jadi string saat dirender.

if __name__ == "__main__":
    app.run(debug=True, port=5001)
