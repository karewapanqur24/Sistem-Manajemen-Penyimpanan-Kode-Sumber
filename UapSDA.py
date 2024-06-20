import csv
import tkinter as tk
from tkinter import simpledialog, messagebox

class CodeSnippet:
    def _init_(self, title, code):
        self.title = title
        self.code = code

class CodeManagement:
    def _init_(self):
        self.data = []
        self.load_data()

    def load_data(self):
        try:
            with open('code_data.csv', 'r') as f:
                reader = csv.reader(f)
                self.data = [CodeSnippet(row[0], row[1]) for row in reader]
        except FileNotFoundError:
            self.data = []

    def save_data(self):
        with open('code_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for snippet in self.data:
                writer.writerow([snippet.title, snippet.code])

    def create(self, title, code):
        self.data.append(CodeSnippet(title, code))
        self.save_data()

    def read(self, index):
        if index < len(self.data):
            return self.data[index]
        return None

    def update(self, index, title, code):
        if index < len(self.data):
            self.data[index] = CodeSnippet(title, code)
            self.save_data()

    def delete(self, index):
        if index < len(self.data):
            del self.data[index]
            self.save_data()

    def search(self, title):
        for i, snippet in enumerate(self.data):
            if snippet.title == title:
                return i
        return -1

    def sort_by_title(self):
        self.data.sort(key=lambda snippet: snippet.title)
        self.save_data()

class CodeManagementApp:
    def _init_(self, root):
        self.code_management = CodeManagement()
        self.root = root
        self.root.title("Sistem Manajemen Kode")

        
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self.root, text="Tambah Snippet Kode", command=self.add_snippet).pack(fill=tk.X)
        tk.Button(self.root, text="Lihat Semua Snippet Kode", command=self.display_all).pack(fill=tk.X)
        tk.Button(self.root, text="Lihat Snippet Kode Berdasarkan Indeks", command=self.view_snippet).pack(fill=tk.X)
        tk.Button(self.root, text="Ubah Snippet Kode", command=self.edit_snippet).pack(fill=tk.X)
        tk.Button(self.root, text="Hapus Snippet Kode", command=self.delete_snippet).pack(fill=tk.X)
        tk.Button(self.root, text="Cari Snippet Kode", command=self.search_snippet).pack(fill=tk.X)
        tk.Button(self.root, text="Urutkan Snippet Kode Berdasarkan Judul", command=self.sort_snippets).pack(fill=tk.X)
        tk.Button(self.root, text="Keluar", command=self.root.quit).pack(fill=tk.X)

    def add_snippet(self):
        title = simpledialog.askstring("Input", "Masukkan judul kode:")
        code = simpledialog.askstring("Input", "Masukkan kode:")
        if title and code:
            self.code_management.create(title, code)
            messagebox.showinfo("Info", f"Snippet kode dengan judul '{title}' telah ditambahkan.")

    def display_all(self):
        snippets = ""
        for i, snippet in enumerate(self.code_management.data):
            snippets += f"Indeks: {i}, Judul: {snippet.title}\nKode:\n{snippet.code}\n\n"
        messagebox.showinfo("Semua Snippet Kode", snippets)

    def view_snippet(self):
        index = simpledialog.askinteger("Input", "Masukkan indeks snippet kode:")
        snippet = self.code_management.read(index)
        if snippet:
            messagebox.showinfo("Snippet Kode", f"Judul: {snippet.title}\nKode:\n{snippet.code}")
        else:
            messagebox.showwarning("Warning", "Indeks tidak valid.")

    def edit_snippet(self):
        index = simpledialog.askinteger("Input", "Masukkan indeks snippet kode:")
        title = simpledialog.askstring("Input", "Masukkan judul kode baru:")
        code = simpledialog.askstring("Input", "Masukkan kode baru:")
        if title and code:
            self.code_management.update(index, title, code)
            messagebox.showinfo("Info", f"Snippet kode pada indeks {index} telah diperbarui.")

    def delete_snippet(self):
        index = simpledialog.askinteger("Input", "Masukkan indeks snippet kode:")
        self.code_management.delete(index)
        messagebox.showinfo("Info", f"Snippet kode pada indeks {index} telah dihapus.")

    def search_snippet(self):
        title = simpledialog.askstring("Input", "Masukkan judul kode yang dicari:")
        index = self.code_management.search(title)
        if index != -1:
            messagebox.showinfo("Info", f"Snippet kode dengan judul '{title}' ditemukan pada indeks {index}.")
        else:
            messagebox.showwarning("Warning", "Snippet kode tidak ditemukan.")

    def sort_snippets(self):
        self.code_management.sort_by_title()
        messagebox.showinfo("Info", "Semua snippet kode telah diurutkan berdasarkan judul.")

if _name_ == "_main_":
    root = tk.Tk()
    app = CodeManagementApp(root)
    root.mainloop()
