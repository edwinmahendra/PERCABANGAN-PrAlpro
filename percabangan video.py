#Edwin Mahendra 71200541

'''
Kumi akan melakukan sign up akun sosial media barunya.
Kemudian setelah melakukan sign up, ia akan login. Ada beberapa kondisi yang harus dipenuhi:
-Jika ketika 'sign up', username = password maka program akan mengeluarkan 'Username dan Password harus berbeda
    Jika username dan password jumlah karakternya kurang dari 7 dan lebih dari 12
    maka outputnya 'Username dan Password harus berisi 8-12 karakter'
-Jika ketika 'login', Kumi salah memasukkan password dan username maka
    program akan memngeluarkan ouput 'Username dan Password anda salah'
    -Jika Kumi salah memasukkan username maka
    program akan memngeluarkan ouput 'Username anda salah'
    -Jika Kumi salah memasukkan password maka
    program akan memngeluarkan ouput 'Password anda salah'
    -Jika semua kondisi bernilai benar maka
    program akan memngeluarkan ouput 'Selamat datang!'
'''

print('===SELAMAT DATANG===')
print()
print('Silakan sign up')
print()

username=input('Masukkan username = ')
password=input('Masukkan password = ')

n=len(username)
o=len(password)

print()
if (username!=password):
    if (n >= 7 and n <= 12) and (o >= 7 and o <= 12):
        if (n>=7 and n<=12):
            if ((o>=7 and o<=12)):
                print('Username dan Password anda terverifikasi. Tekan enter untuk login')
                k=input()
                print('=== LOGIN ===')
                print()
                x=input('Masukkan username = ')
                y=input('Masukkan password = ')
                if x==username and y==password:
                    if x==username:
                        if y==password:
                            print('Selamat datang!')
                        else:
                            print('Password anda salah')
                    else:
                        print('Username anda salah')
                else:
                    print('Username dan Password anda salah')
            else:
                print('Password harus berisi 7-12 karakter')
        else:
            print('Username harus berisi 7-12 karakter')
    else:
        print('Username dan Password harus berisi 8-12 karakter')
else:
    print('Username dan Password harus berbeda')
