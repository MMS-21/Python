#!/usr/bin/env python3
"""
PDF Organizer GUI
-----------------
A user-friendly tool to merge, split, compress, or extract text from PDFs.
"""

import os
from pathlib import Path
from tkinter import (
    Tk, Frame, Label, Button, filedialog, messagebox, StringVar, OptionMenu, Text, END
)
from PyPDF2 import PdfMerger, PdfReader, PdfWriter


def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    return f"Merged {len(pdf_files)} files → {output_path}"


def split_pdf(input_pdf, output_folder):
    reader = PdfReader(input_pdf)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        output_file = output_folder / f"{Path(input_pdf).stem}_page{i}.pdf"
        with open(output_file, "wb") as f:
            writer.write(f)
    return f"Split complete! {len(reader.pages)} pages saved in {output_folder}"


def extract_text(input_pdf, output_file):
    reader = PdfReader(input_pdf)
    text_content = ""
    for page in reader.pages:
        text_content += (page.extract_text() or "") + "\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text_content)
    return f"Extracted text saved to {output_file}"


def compress_pdf(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    return f"Compressed PDF saved as {output_pdf}"


class PDFOrganizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("📄 PDF Organizer Tool")
        master.geometry("600x500")
        master.resizable(False, False)

        self.selected_files = []
        self.output_path = StringVar()
        self.action = StringVar(value="Merge PDFs")

        # UI Elements
        Label(master, text="Select PDF Files:", font=("Arial", 12, "bold")).pack(pady=5)
        Button(master, text="📂 Browse Files", command=self.browse_files).pack()

        Label(master, text="Select Action:", font=("Arial", 12, "bold")).pack(pady=10)
        options = ["Merge PDFs", "Split PDF", "Extract Text", "Compress PDF"]
        OptionMenu(master, self.action, *options).pack()

        Label(master, text="Choose Output Path:", font=("Arial", 12, "bold")).pack(pady=10)
        Button(master, text="📁 Choose Output Folder", command=self.choose_output).pack()

        Button(
            master, text="🚀 Process", command=self.process_pdfs,
            bg="#4CAF50", fg="white", padx=20, pady=5, font=("Arial", 11, "bold")
        ).pack(pady=15)

        Label(master, text="Output Log:", font=("Arial", 12, "bold")).pack(pady=5)
        self.log_box = Text(master, height=12, width=70, wrap="word", bg="#f9f9f9")
        self.log_box.pack(padx=10, pady=5)

    def browse_files(self):
        if self.action.get() == "Merge PDFs":
            files = filedialog.askopenfilenames(
                title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")]
            )
            self.selected_files = list(files)
        else:
            file = filedialog.askopenfilename(
                title="Select a PDF File", filetypes=[("PDF Files", "*.pdf")]
            )
            self.selected_files = [file] if file else []

        self.log(f"Selected: {', '.join(self.selected_files) if self.selected_files else 'None'}")

    def choose_output(self):
        if self.action.get() == "Extract Text":
            path = filedialog.asksaveasfilename(
                title="Save Extracted Text As", defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")]
            )
        elif self.action.get() == "Split PDF":
            path = filedialog.askdirectory(title="Select Output Folder")
        else:
            path = filedialog.asksaveasfilename(
                title="Save Output As", defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")]
            )
        if path:
            self.output_path.set(path)
            self.log(f"Output path set to: {path}")

    def process_pdfs(self):
        try:
            if not self.selected_files:
                messagebox.showwarning("Warning", "Please select at least one PDF file.")
                return

            action = self.action.get()
            result_message = ""

            if action == "Merge PDFs":
                output = self.output_path.get() or "merged_output.pdf"
                result_message = merge_pdfs(self.selected_files, output)

            elif action == "Split PDF":
                output = self.output_path.get() or "split_pages"
                result_message = split_pdf(self.selected_files[0], output)

            elif action == "Extract Text":
                output = self.output_path.get() or "extracted_text.txt"
                result_message = extract_text(self.selected_files[0], output)

            elif action == "Compress PDF":
                output = self.output_path.get() or f"compressed_{Path(self.selected_files[0]).name}"
                result_message = compress_pdf(self.selected_files[0], output)

            self.log(result_message)
            messagebox.showinfo("Success", result_message)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")
            self.log(f"❌ Error: {e}")

    def log(self, text):
        self.log_box.insert(END, text + "\n")
        self.log_box.see(END)

if __name__ == "__main__":
    root = Tk()
    app = PDFOrganizerGUI(root)
    root.mainloop()