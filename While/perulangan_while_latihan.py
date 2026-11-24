password = ""

while password!="123456":
    password = input("Masukkan Password: ")
    
    if password != "123456":
        print("password salah, silahkan coba lagi")
    else:
        print("Password benar")
    
print("login berhasil")