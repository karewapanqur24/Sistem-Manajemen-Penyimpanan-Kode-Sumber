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


    def edit_snippet(self):
        index = simpledialog.askinteger("Input", "Masukkan indeks snippet kode:")
        title = simpledialog.askstring("Input", "Masukkan judul kode baru:")
        code = simpledialog.askstring("Input", "Masukkan kode baru:")
        if title and code:
            self.code_management.update(index, title, code)
            messagebox.showinfo("Info", f"Snippet kode pada indeks {index} telah diperbarui.")
