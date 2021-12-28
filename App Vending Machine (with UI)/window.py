# Vending Machine Program
# KU1102 - 23 / Kelompok 4/ 2021-2022

# Kamus
# 1) Class
#   VendingItems                                    : class
#   Nasi, Manis                                     : sub-class (anak class)
#   self.code, self.name, self.lauk, self.isi       : str
#   self.price, self.stock, self.kalori, self.time  : int
# 2) Menu
#   item1, item2, ..., item9                        : object
#   menu                                            : array [item1, item2, ..., item9] of object
# 3) Appp
#   balance, num1, temp, amount, current1, jumlah   : int
#   var                                             : object
#   code, current, timer                            : str
# 4) Interface
#   all entries                                     : entry, str
#   all buttons                                     : button
#   all images                                      : img
#   all canvas                                      : canvas

# Libraries external
from tkinter import *
import time
import pygame
import winsound

# ---- Declare Data ---- #

class VendingItems:
    def __init__(self, code, name, price, stock, kalori,  time):     # Method untuk inisialisasi info produk
        self.code = code        # kode pemilihan produk
        self.name = name        # nama produk
        self.price = price      # harga produk
        self.stock = stock      # jumlah produk yang tersedia
        self.kalori = kalori    # besar kalori dalam kkal
        self.time = time        # waktu untuk pemanasan makanan dalam detik

# ---- AKHIR KELAS UTAMA -------- #

# Anak class khusus untuk jenis item makanan nasi yang memiliki isi lauk berbeda-beda
class Nasi(VendingItems):
    def __init__(self, code, name, price, stock, lauk, kalori, time):
        super().__init__(code, name, price, stock, kalori, time)    # memanggil method dari class utama
        self.lauk = lauk

# ----- AKHIR KELAS NASI ---- #

# Anak class khusus untuk jenis item makanan manis
class Manis(VendingItems):
    def __init__(self, code, name, price, stock, isi, kalori, time):
        super().__init__(code, name, price, stock, kalori, time)
        self.isi = isi

# ----- AKHIR KELAS MANIS ------ #

# -------------------------------- #

item1 = Nasi('A1', 'Nasi Goreng', 20000, 5, 'Sosis', 250, 120)
item2 = Nasi('A2', 'Nasi Uduk', 20000, 3, 'Ayam Suwir', 260, 120)
item3 = Nasi('A3', 'Nasi Kuning', 15000, 5, ' Ayam Suwir', 300, 120)
item4 = Nasi('B1', 'Nasi Kucing', 15000, 11, 'Teri',220, 120)
item5 = Nasi('B2', 'Nasi Bakar', 15000, 2, 'Ayam Suwir', 280, 120)
item6 = Nasi('B3', 'Nasi Liwet', 10000, 0, 'Tempe & Telur Dadar', 200, 120)
item7 = Manis('C1', 'Roti Isi Cokelat', 10000, 7, 'Selai Cokelat', 300, 30)
item8 = Manis('C2', 'Roti Isi Kacang', 10000, 8, 'Selai Kacang', 300, 30)
item9 = Manis('C3', 'Roti Isi Keju', 10000, 4, 'Keju Krim', 320, 30)

menu = [item1, item2, item3, item4, item5, item6, item7, item8, item9]

# ---- Open App Tkinter ---- #

window = Tk() # Open libraries tkinter
window.title('Vending Machine') # Set nama app
window.geometry("1080x720") # Set ukuran app
icon = PhotoImage(file='icon/logo.png') # Set icon app
window.tk.call('wm', 'iconphoto', window._w, icon)  # Set icon app
# window.iconbitmap('icon/logo.ico') # ALTERNATIF, Ubah ini menjadi bukan comments jika logo.png 2 line code di atas tidak bisa
window.configure(bg = "#f5f6f8") # Set bg app
winsound.PlaySound('audio/sound.wav', winsound.SND_ALIAS | winsound.SND_LOOP |winsound.SND_ASYNC) # Set lagu saat membuka app

# Declare balance awal
balance = 0

# Layer main_window
def main_window():
    # Global variabel
    global background, background_img, img0, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12
    global b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12
    global entry0_img, entry1_img, entry2_img, entry3_img, entry4_img, entry5_img, entry6_img, entry7_img, entry8_img, entry9_img, entry10_img, entry11_img, entry12_img, entry13_img
    global entry0_bg, entry1_bg, entry2_bg, entry3_bg, entry4_bg, entry5_bg, entry6_bg, entry7_bg, entry8_bg, entry9_bg, entry10_bg, entry11_bg, entry12_bg, entry13_bg

    # Buttons/ Entry/ Lain-lain ---------------------------------------------------------------
    
    # Fungsi untuk update stok makanan yang ada di layar (interface)
    def stock_update():
        # Dalam setiap entry data lama dihapus, diupdate dengan data baru
        # Entry.delete() -> menghapus data yang ada di entry
        # Entry.insert() -> memasukkan data ke entry
        entry13.delete(0, END)
        entry13.insert(0, item1.stock)
        entry12.delete(0, END)
        entry12.insert(0, item2.stock)
        entry11.delete(0, END)
        entry11.insert(0, item3.stock)
        entry10.delete(0, END)
        entry10.insert(0, item4.stock)
        entry9.delete(0, END)
        entry9.insert(0, item5.stock)
        entry8.delete(0, END)
        entry8.insert(0, item6.stock)
        entry7.delete(0, END)
        entry7.insert(0, item7.stock)
        entry6.delete(0, END)
        entry6.insert(0, item8.stock)
        entry5.delete(0, END)
        entry5.insert(0, item9.stock)

    # Fungsi untuk screen awal(starter) dan juga perpindahan screen dari main_window ke popup
    def screen(code):
        # Screen awal
        if code == 'start':
            entry4.delete(0, END)
            entry4.insert(0, 'Selamat datang, mau pesan apa?')
        # PopUp
        if code == 'wait':
            # Definisikan global untuk sisa balance, agar saat balik lagi ke main_window, balance masih ada
            global balance
            balance = int(entry1.get())
            entry4.delete(0, END)
            entry4.insert(0, 'Makanan sedang dimasak...')
            # Timer berdasarkan waktu memasak masing2 item.code
            countdown(var.time * amount)
            # Sesuai dengan item.code yang ada
            if var.code == 'A1':
                pop_up_nasigoreng()
            elif var.code == 'A2':
                pop_up_nasiuduk()
            elif var.code == 'A3':
                pop_up_nasikuning()
            elif var.code == 'B1':
                pop_up_nasikucing()
            elif var.code == 'B2':
                pop_up_nasibakar()
            elif var.code == 'B3':
                pop_up_nasiliwet()
            elif var.code == 'C1':
                pop_up_roticoklat()
            elif var.code == 'C2':
                pop_up_rotikacang()
            elif var.code == 'C3':
                pop_up_rotikeju()

    # Mendefinisikan fungsi dari button (A, B, C, 1, 2, 3) dan print ke layar (interface)
    def button_click1(number):
        current = entry3.get()
        # Di set agar input max nya 3 character saja
        if len(current) > 2:
            return
        else:
            entry3.delete(0, END)
            entry3.insert(0, current + number)

    # Mendefinisikan fungsi dari button uang (10.000, 20.000, 50.000, 100.000)
    def button_click2(number):
        current = entry1.get()
        num1 = int(current)
        res = num1 + number
        # Di set agar balance max dari user 200.000 saja
        if res > 200000:
            return
        else:
            entry1.delete(0, END)
            entry1.insert(0, str(res))
            entry0.delete(0, END)
            entry0.insert(0, str(res))

    # Mendefinisikan fungsi dari button delete (menghapus entry dari button_click1)
    def button_delete():
        current = entry3.get()[:-1]
        entry3.delete(0, END)
        entry3.insert(0, current)

    # Fungsi mendeteksi item.code yang diinput user
    def code_enter(current):
        check = True
        for item in menu:
            if item.code == current:
                # Definisikan global untuk item yang dipesan
                global var
                var = item
                check = True
                entry4.delete(0, END)
                # Jika stok item yang dipilih 0, suruh pilih lainnya
                if var.stock == 0:
                    entry4.insert(0, 'Stok 0, pilih lainnya')
                    return
                # Jika tidak, lanjut ke check_amount
                else:
                    entry4.insert(0, 'Masukkan Jumlah')
                    return
            # Jika tidak ada, check False
            else:
                check = False
        # Jika False, user disuruh input ulang kode, print ke backend
        if not check:
            entry4.delete(0, END)
            entry4.insert(0, 'Pilih kode item yang tersedia')
            print(f'User memilih item <{current}>, tidak tersedia.')
            return

    # Fungsi untuk mengecek jumlah yang ingin user input
    def check_amount(item, current):
        entry3.delete(0, END)
        # Jika user memasukkan integer, lanjut
        try:
            current1 = int(entry1.get())
            # Definisikan global untuk sisa balance
            global temp
            temp = current1
            current = int(current)
            # Jika user menginput 0, tidak terjadi apa2
            if current == 0:
                return
            elif item.stock >= current:
                # Defnisikan global untuk jumlah yang user inginkan
                global amount
                amount = current
                entry4.delete(0, END)
                # Jika balance >= item yang dikalkulasi, maka lanjut
                if amount * var.price <= temp:
                    # Hitung price nya (update balance)
                    calculate_price(var, amount)
                    # Update stok yang ada
                    print('Sisa stok: ')
                    for item in menu:
                        # print ke backend
                        print(f'{item.name} = {item.stock}')
                    print('---------------------------------------------------------------')
                    entry4.delete(0, END)
                    stock_update()
                    # Transisi ke popup window masing2 makanan
                    screen('wait')
                # Jika tidak, user diminta memasukkan kekurangan uangnya
                else:
                    entry4.insert(0, f'Masukkan Uang: {amount * var.price - temp}')
                return
            # Jika misal user memasukkan tidak sesuai stok, user disuruh input ulang
            else:
                entry4.delete(0, END)
                entry4.insert(0, 'Lihat stok, pilih ulang')
                # Print ke backend sisa stok
                print(f'Stok {item.name} yang tersedia: {item.stock}')
                return
        # Jika tidak, user harus memasukkan jumlah yg benar
        except ValueError:
            entry3.delete(0, END)

    # Fungsi untuk menghitung price (jumlah pesanan user * harga tiap makanan) + update balance, kembalian
    def calculate_price(item, jumlah):
        jumlah = int(jumlah)
        current = int(entry1.get())
        # Definisikan global untuk sisa balance
        global temp
        temp = current
        # Jika balance < harga yang ditentukan, return False
        if jumlah * item.price > current:
            return False
        # Selain itu hitung, kurangi dengan balance, dan update stok yang ada, print ke backend
        else:
            current -= jumlah * item.price
            print(f'User memesan {item.name} sebanyak {jumlah}.')
            item.stock -= jumlah
            entry4.delete(0, END)
            entry1.delete(0, END)
            entry1.insert(0, str(current))
            entry0.delete(0, END)
            entry0.insert(0, str(current))
            return True

    # Mendefinisikan button enter dengan berbagai macam fungsi, dilihat dari entry yang ada
    def button_enter():
        # Jika entry awal, maka user harus memasukkan code
        if entry4.get() == 'Selamat datang, mau pesan apa?' or entry4.get() == 'Stok 0, pilih lainnya' or entry4.get() == 'Pilih kode item yang tersedia':
            current = entry3.get()
            # Jika sesuai lanjut ke code_enter (untuk dicek item.code nya)
            code_enter(current)
            entry3.delete(0, END)
            return
        # Jika entry disuruh masukkan jumlah, maka user harus memasukkannya
        elif entry4.get() == 'Masukkan Jumlah' or entry4.get() == 'Lihat stok, pilih ulang':
            current = entry3.get()
            # Jika sesuai lanjut ke check_amount (untuk dicek ketersediaan stok dan lain2)
            check_amount(var,current)
            entry3.delete(0, END)
            return
        # Jika entry disuruh masukkan uang kekurangan dari user
        elif entry4.get() == f'Masukkan Uang: {amount * var.price - temp}' or entry4.get() == f'Uang kurang {amount * var.price - temp}':
            # Jika uang sudah cukup, lanjut ke calculate_price
            if calculate_price(var, amount):
                print('Sisa stok: ')
                for item in menu:
                    print(f'{item.name} = {item.stock}')
                print('---------------------------------------------------------------')
                entry4.delete(0, END)
                stock_update()
                screen('wait')
            # Jika tidak, meminta user memasukkan uang kekurangannya
            else:
                entry4.delete(0, END)
                entry4.insert(0, f'Uang kurang {amount * var.price - temp}')   
        entry3.delete(0, END)

    # Fungsi untuk timer saat menunggu makanan dimasak
    def countdown(t):
        while t > -1:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            entry2.config(text=timer)
            window.update()
            time.sleep(1)
            t -= 1

    # Mendefinisikan tombol claim, untuk mereset semuanya (user mengambil kembalian dan quit program) (user tidak ingin memesan lagi)
    def claim():
        global balance
        # Print ke backend, kembalian yang diterima user
        print(f'User menerima kembalian {entry0.get()}.')
        # reset ke interface awal
        balance = 0
        layer_claim()
        print('---------------------------------------------------------------')

    # GUI/ Interface ---------------------------------------------------------------------------

    canvas = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------
    
    background_img = PhotoImage(file = f"background/mainbg.png") # Set background
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    # Buttons ----------------------------------------------------------------------------------

    img0 = PhotoImage(file = f"buttons/img0.png") # Set button
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:[sound_buttons(), claim()], # Set commands dari button
        relief = "flat")

    b0.place(
        x = 903, y = 633,
        width = 119,
        height = 51)

    img1 = PhotoImage(file = f"buttons/img1.png") # Set button
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click2(100000)], # Set commands dari button
        relief = "flat")

    b1.place(
        x = 849, y = 554,
        width = 140,
        height = 50)

    img2 = PhotoImage(file = f"buttons/img2.png") # Set button
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click2(50000)], # Set commands dari button
        relief = "flat")

    b2.place(
        x = 695, y = 553,
        width = 140,
        height = 50)

    img3 = PhotoImage(file = f"buttons/img3.png") # Set button
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click2(20000)], # Set commands dari button
        relief = "flat")

    b3.place(
        x = 849, y = 489,
        width = 140,
        height = 50)

    img4 = PhotoImage(file = f"buttons/img4.png") # Set button 
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click2(10000)], # Set commands dari button
        relief = "flat")

    b4.place(
        x = 695, y = 489,
        width = 140,
        height = 50)

    img5 = PhotoImage(file = f"buttons/img5.png") # Set button
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_delete()], # Set commands dari button
        relief = "flat")

    b5.place(
        x = 695, y = 280,
        width = 140,
        height = 60)

    img6 = PhotoImage(file = f"buttons/img6.png") # Set button
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_enter()], # Set commands dari button
        relief = "flat")

    b6.place(
        x = 851, y = 280,
        width = 140,
        height = 60)

    img7 = PhotoImage(file = f"buttons/img7.png") # Set button
    b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click1('3')], # Set commands dari button
        relief = "flat")

    b7.place(
        x = 911, y = 218,
        width = 74,
        height = 50)

    img8 = PhotoImage(file = f"buttons/img8.png") # Set button
    b8 = Button(
        image = img8,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click1('2')], # Set commands dari button
        relief = "flat")

    b8.place(
        x = 806, y = 218,
        width = 74,
        height = 50)

    img9 = PhotoImage(file = f"buttons/img9.png") # Set button
    b9 = Button(
        image = img9,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click1('1')], # Set commands dari button
        relief = "flat")

    b9.place(
        x = 701, y = 218,
        width = 74,
        height = 50)

    img10 = PhotoImage(file = f"buttons/img10.png") # Set button
    b10 = Button(
        image = img10,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click1('C')], # Set commands dari button
        relief = "flat")

    b10.place(
        x = 911, y = 151,
        width = 74,
        height = 50)

    img11 = PhotoImage(file = f"buttons/img11.png") # Set button
    b11 = Button(
        image = img11,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click1('B')], # Set commands dari button
        relief = "flat")

    b11.place(
        x = 806, y = 151,
        width = 74,
        height = 50)

    img12 = PhotoImage(file = f"buttons/img12.png") # Set button
    b12 = Button(
        image = img12,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), button_click1('A')], # Set commands dari button
        relief = "flat")

    b12.place(
        x = 701, y = 151,
        width = 74,
        height = 50)

    # Entry ----------------------------------------------------------------------------------

    entry0_img = PhotoImage(file = f"textbox/img_textBox0.png") # Set entry
    entry0_bg = canvas.create_image(
        773.0, 660.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#e1e1e1",
        highlightthickness = 0,
        font = ('Poppins', 11))

    entry0.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry0.place(
        x = 683.0, y = 645,
        width = 180.0,
        height = 28)

    entry1_img = PhotoImage(file = f"textbox/img_textBox1.png") # Set entry
    entry1_bg = canvas.create_image(
        841.5, 455.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#e1e1e1",
        highlightthickness = 0,
        font = ('Poppins', 11))

    entry1.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry1.place(
        x = 683.0, y = 440,
        width = 317.0,
        height = 28)

    entry2_img = PhotoImage(file = f"textbox/img_textBox2.png") # Set entry
    entry2_bg = canvas.create_image(
        881.0, 381.0,
        image = entry2_img)

    entry2 = Label(
        bd = 0,
        bg = "#e0e0e0",
        highlightthickness = 0,
        font = ('Poppins', 11, 'bold'))

    entry2.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry2.place(
        x = 856.0, y = 366,
        width = 50.0,
        height = 28)

    entry3_img = PhotoImage(file = f"textbox/img_textBox3.png") # Set entry
    entry3_bg = canvas.create_image(
        981.5, 113.0,
        image = entry3_img)

    entry3 = Entry(
        bd = 0,
        bg = "#e1e1e1",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins', 11))

    entry3.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry3.place(
        x = 963.0, y = 98,
        width = 37.0,
        height = 28)

    entry4_img = PhotoImage(file = f"textbox/img_textBox4.png") # Set entry
    entry4_bg = canvas.create_image(
        793.0, 113.0,
        image = entry4_img)

    entry4 = Entry(
        bd = 0,
        bg = "#e1e1e1",
        highlightthickness = 0,
        font = ('Poppins', 11))

    entry4.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry4.place(
        x = 683.0, y = 98,
        width = 220.0,
        height = 28)

    entry5_img = PhotoImage(file = f"textbox/img_textBox5.png") # Set entry
    entry5_bg = canvas.create_image(
        438.0, 483.5,
        image = entry5_img)

    entry5 = Entry(
        bd = 0,
        bg = "#e76b38",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins', 11))

    entry5.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry5.place(
        x = 430.0, y = 470,
        width = 16.0,
        height = 25)

    entry6_img = PhotoImage(file = f"textbox/img_textBox6.png") # Set entry
    entry6_bg = canvas.create_image(
        262.0, 483.5,
        image = entry6_img)

    entry6 = Entry(
        bd = 0,
        bg = "#e76b38",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins',11))

    entry6.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry6.place(
        x = 254.0, y = 470,
        width = 16.0,
        height = 25)

    entry7_img = PhotoImage(file = f"textbox/img_textBox7.png") # Set entry
    entry7_bg = canvas.create_image(
        83.0, 483.5,
        image = entry7_img)

    entry7 = Entry(
        bd = 0,
        bg = "#e76b38",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins', 11))

    entry7.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry7.place(
        x = 75.0, y = 470,
        width = 16.0,
        height = 25)

    entry8_img = PhotoImage(file = f"textbox/img_textBox8.png") # Set entry
    entry8_bg = canvas.create_image(
        438.0, 281.5,
        image = entry8_img)

    entry8 = Entry(
        bd = 0,
        bg = "#e76b38",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins', 11))

    entry8.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry8.place(
        x = 430.0, y = 268,
        width = 16.0,
        height = 25)

    entry9_img = PhotoImage(file = f"textbox/img_textBox9.png") # Set entry
    entry9_bg = canvas.create_image(
        262.0, 279.5,
        image = entry9_img)

    entry9 = Entry(
        bd = 0,
        bg = "#e76b38",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins', 11))

    entry9.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry9.place(
        x = 254.0, y = 266,
        width = 16.0,
        height = 25)

    entry10_img = PhotoImage(file = f"textbox/img_textBox10.png") # Set entry
    entry10_bg = canvas.create_image(
        83.0, 279.5,
        image = entry10_img)

    entry10 = Entry(
        bd = 0,
        bg = "#e76b38",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins', 11))

    entry10.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry10.place(
        x = 75.0, y = 266,
        width = 16.0,
        height = 25)

    entry11_img = PhotoImage(file = f"textbox/img_textBox11.png") # Set entry
    entry11_bg = canvas.create_image(
        438.0, 79.5,
        image = entry11_img)

    entry11 = Entry(
        bd = 0,
        bg = "#e76b38",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins', 11))

    entry11.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry11.place(
        x = 430.0, y = 66,
        width = 16.0,
        height = 25)

    entry12_img = PhotoImage(file = f"textbox/img_textBox12.png") # Set entry
    entry12_bg = canvas.create_image(
        262.0, 79.5,
        image = entry12_img)

    entry12 = Entry(
        bd = 0,
        bg = "#e76b38",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins', 11))

    entry12.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry12.place(
        x = 254.0, y = 66,
        width = 16.0,
        height = 25)

    entry13_img = PhotoImage(file = f"textbox/img_textBox13.png") # Set entry
    entry13_bg = canvas.create_image(
        86.0, 77.5,
        image = entry13_img)

    entry13 = Entry(
        bd = 0,
        bg = "#e76b38",
        highlightthickness = 0,
        justify = 'center',
        font = ('Poppins', 11))

    entry13.bind('<Button-1>', lambda e: 'break') # Set agar entry tidak bisa dimanipulasi user

    entry13.place(
        x = 78.0, y = 64,
        width = 16.0,
        height = 25)

    # Saat mulai langsung ke screen start dan update stock
    # Jangan lupa balance dan kembalian yang sebelumnya tetap/ tidak berubah
    screen('start')
    stock_update()
    entry0.insert(0, f'{balance}')
    entry1.insert(0, f'{balance}')

# Layer cara kerja
def carakerja():
    global bg_carakerja, background10, img_carakerja, b_carakerja 

    canvas10 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas10.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_carakerja = PhotoImage(file = f"background/carakerja.png") # Set background
    background10 = canvas10.create_image(
        540.0, 360.0,
        image=bg_carakerja)
    
    # Buttons ----------------------------------------------------------------------------------

    img_carakerja = PhotoImage(file = f"buttons/img_mengerti.png") # Set button
    b_carakerja = Button(
        image = img_carakerja,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_carakerja.place(
        x = 803, y = 546,
        width = 151,
        height = 66)

# Layer claim
def layer_claim():
    global bg_claim, background11, img_claim, b_claim 

    canvas11 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas11.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_claim = PhotoImage(file = f"background/claim.png")  # Set background
    background11 = canvas11.create_image(
        540.0, 360.0,
        image=bg_claim)
    
    # Buttons ----------------------------------------------------------------------------------

    img_claim = PhotoImage(file = f"buttons/img_x.png") # Set button
    b_claim = Button(
        image = img_claim,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_claim.place(
        x = 768, y = 275,
        width = 25,
        height = 23)

# Layer popup nasigoreng
def pop_up_nasigoreng():
    bell()
    global bg_nasgor, background1, img_nasgor, b_nasgor 

    canvas1 = Canvas( # Set canvas awal 
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas1.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_nasgor = PhotoImage(file = f"background/bg_nasigoreng.png") # Set background
    background1 = canvas1.create_image(
        540.0, 360.0,
        image=bg_nasgor)
    
    # Buttons ----------------------------------------------------------------------------------

    img_nasgor = PhotoImage(file = f"buttons/img_ok.png") # Set button
    b_nasgor = Button(
        image = img_nasgor,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_nasgor.place(
        x = 470, y = 443,
        width = 140,
        height = 60)

# Layer popup nasiuduk
def pop_up_nasiuduk():
    bell()
    global bg_nasiuduk, background2, img_nasiuduk, b_nasiuduk 

    canvas2 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas2.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_nasiuduk = PhotoImage(file = f"background/bg_nasiuduk.png") # Set background
    background2 = canvas2.create_image(
        540.0, 360.0,
        image=bg_nasiuduk)
    
    # Buttons ----------------------------------------------------------------------------------

    img_nasiuduk = PhotoImage(file = f"buttons/img_ok.png") # Set button
    b_nasiuduk = Button(
        image = img_nasiuduk,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_nasiuduk.place(
        x = 470, y = 443,
        width = 140,
        height = 60)

#Layer popup nasikuning
def pop_up_nasikuning():
    bell()
    global bg_nasikuning, background3, img_nasikuning, b_nasikuning 

    canvas3 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas3.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_nasikuning = PhotoImage(file = f"background/bg_nasikuning.png") # Set background
    background3 = canvas3.create_image(
        540.0, 360.0,
        image=bg_nasikuning)
    
    # Buttons ----------------------------------------------------------------------------------

    img_nasikuning = PhotoImage(file = f"buttons/img_ok.png") # Set button
    b_nasikuning = Button(
        image = img_nasikuning,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_nasikuning.place(
        x = 470, y = 443,
        width = 140,
        height = 60)

# Layer popup nasikucing
def pop_up_nasikucing():
    bell()
    global bg_nasikucing, background4, img_nasikucing, b_nasikucing 

    canvas4 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas4.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_nasikucing = PhotoImage(file = f"background/bg_nasikucing.png") # Set background
    background4 = canvas4.create_image(
        540.0, 360.0,
        image=bg_nasikucing)
    
    # Buttons ----------------------------------------------------------------------------------

    img_nasikucing = PhotoImage(file = f"buttons/img_ok.png") # Set button
    b_nasikucing = Button(
        image = img_nasikucing,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_nasikucing.place(
        x = 470, y = 443,
        width = 140,
        height = 60)

# Layer popup nasibakar
def pop_up_nasibakar():
    bell()
    global bg_nasibakar, background5, img_nasibakar, b_nasibakar 

    canvas5 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas5.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_nasibakar = PhotoImage(file = f"background/bg_nasibakar.png") # Set background
    background5 = canvas5.create_image(
        540.0, 360.0,
        image=bg_nasibakar)
    
    # Buttons ----------------------------------------------------------------------------------

    img_nasibakar = PhotoImage(file = f"buttons/img_ok.png") # Set button
    b_nasibakar = Button(
        image = img_nasibakar,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_nasibakar.place(
        x = 470, y = 443,
        width = 140,
        height = 60)

# Layer popup nasiliwet
def pop_up_nasiliwet():
    bell()
    global bg_nasiliwet, background6, img_nasiliwet, b_nasiliwet 

    canvas6 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas6.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_nasiliwet = PhotoImage(file = f"background/bg_nasiliwet.png") # Set background
    background6 = canvas6.create_image(
        540.0, 360.0,
        image=bg_nasiliwet)
    
    # Buttons ----------------------------------------------------------------------------------

    img_nasiliwet = PhotoImage(file = f"buttons/img_ok.png") # Set button
    b_nasiliwet = Button(
        image = img_nasiliwet,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_nasiliwet.place(
        x = 470, y = 443,
        width = 140,
        height = 60)

# Layer popup roticoklat
def pop_up_roticoklat():
    bell()
    global bg_roticoklat, background7, img_roticoklat, b_roticoklat 

    canvas7 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas7.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_roticoklat = PhotoImage(file = f"background/bg_roticoklat.png") # Set background
    background7 = canvas7.create_image(
        540.0, 360.0,
        image=bg_roticoklat)
    
    # Buttons ----------------------------------------------------------------------------------

    img_roticoklat = PhotoImage(file = f"buttons/img_ok.png") # Set button
    b_roticoklat = Button(
        image = img_roticoklat,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_roticoklat.place(
        x = 470, y = 443,
        width = 140,
        height = 60)

# Layer popup rotikacang
def pop_up_rotikacang():
    bell()
    global bg_rotikacang, background8, img_rotikacang, b_rotikacang 

    canvas8 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas8.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_rotikacang = PhotoImage(file = f"background/bg_rotikacang.png") # Set background
    background8 = canvas8.create_image(
        540.0, 360.0,
        image=bg_rotikacang)
    
    # Buttons ----------------------------------------------------------------------------------

    img_rotikacang = PhotoImage(file = f"buttons/img_ok.png") # Set button
    b_rotikacang = Button(
        image = img_rotikacang,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_rotikacang.place(
        x = 470, y = 443,
        width = 140,
        height = 60)

# Layer popup rotikeju
def pop_up_rotikeju():
    bell()
    global bg_rotikeju, background9, img_rotikeju, b_rotikeju 

    canvas9 = Canvas( # Set canvas awal
        window,
        bg = "#f5f6f8",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas9.place(x = 0, y = 0)

    # Background -------------------------------------------------------------------------------

    bg_rotikeju = PhotoImage(file = f"background/bg_rotikeju.png") # Set background
    background9 = canvas9.create_image(
        540.0, 360.0,
        image=bg_rotikeju)
    
    # Buttons ----------------------------------------------------------------------------------

    img_rotikeju = PhotoImage(file = f"buttons/img_ok.png") # Set button
    b_rotikeju = Button(
        image = img_rotikeju,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [sound_buttons(), main_window()], # Set commands dari button
        relief = "flat")

    b_rotikeju.place(
        x = 470, y = 443,
        width = 140,
        height = 60)

# Open pygame libraries untuk suara
pygame.mixer.init()

# Suara saat makanan jadi
def bell():
    pygame.mixer.music.load('audio/bell.wav')
    pygame.mixer.music.play(loops=0)

# Suara saat mengklik tombool
def sound_buttons():
    pygame.mixer.music.load('audio/buttons.wav')
    pygame.mixer.music.play(loops=0)

# Call carakerja
carakerja()
# Window unresizable
window.resizable(False, False)
window.mainloop()