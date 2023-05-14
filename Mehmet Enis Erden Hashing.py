import hashlib
import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def calculate_hash():
    file_path = file_path_entry.get()
    hash_algorithm = hash_algorithm_var.get()
    hash_value = calculate_file_hash(file_path, hash_algorithm)
    hash_output_entry.delete(0, tk.END)
    hash_output_entry.insert(0, hash_value)

def calculate_file_hash(file_path, hash_algorithm):
    hash_obj = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        chunk = file.read(4096)
        while chunk:
            hash_obj.update(chunk)
            chunk = file.read(4096)
    return hash_obj.hexdigest()

def verify_hash():
    file_path = file_path_entry.get()
    hash_algorithm = hash_algorithm_var.get()
    expected_hash = hash_output_entry.get()
    calculated_hash = calculate_file_hash(file_path, hash_algorithm)
    if expected_hash == calculated_hash:
        verification_label.config(text="Doğrulandı")
    else:
        verification_label.config(text="Doğrulanamadı")

root = tk.Tk()
root.title("Hash Uygulaması")

# Dosya seçme kısmı
file_path_label = tk.Label(root, text="Dosya Seç:")
file_path_label.grid(row=0, column=0)

file_path_entry = tk.Entry(root, width=50)
file_path_entry.grid(row=0, column=1, padx=10, pady=10)

file_select_button = tk.Button(root, text="Seç", command=select_file)
file_select_button.grid(row=0, column=2)

# Hash algoritma seçimi
hash_algorithm_label = tk.Label(root, text="Hash Algoritması:")
hash_algorithm_label.grid(row=1, column=0)

hash_algorithm_var = tk.StringVar(root)
hash_algorithm_choices = ['md5', 'sha1', 'sha256']  # Diğer hash algoritmalarını buraya ekleyebilirsiniz
hash_algorithm_var.set(hash_algorithm_choices[0])

hash_algorithm_menu = tk.OptionMenu(root, hash_algorithm_var, *hash_algorithm_choices)
hash_algorithm_menu.grid(row=1, column=1, padx=10, pady=10)

# Hash çıktısı hesaplama
hash_output_label = tk.Label(root, text="Hash Çıktısı:")
hash_output_label.grid(row=2, column=0)

hash_output_entry = tk.Entry(root, width=50)
hash_output_entry.grid(row=2, column=1, padx=10, pady=10)

hash_calculate_button = tk.Button(root, text="Hash Hesapla", command=calculate_hash)
hash_calculate_button.grid(row=2, column=2)

# Hash doğrulama
verify_button = tk.Button(root, text="Hash Doğrula", command=verify_hash)
verify_button.grid(row=3, column=1, pady=10)

verification_label = tk.Label(root, text="")
verification_label.grid(row=4, column=1)

root.mainloop()
