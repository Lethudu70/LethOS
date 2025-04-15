import os
import tkinter as tk
from tkinter import simpledialog

# --- Fonction Explorateur ---
def open_explorer():
    explorer = tk.Tk()
    explorer.title("LethOS File Explorer")
    explorer.geometry("850x520")

    themes = {
        "light": {"bg": "#f0f0f0", "fg": "black", "preview_bg": "#ffffff"},
        "dark": {"bg": "#2e2e2e", "fg": "white", "preview_bg": "#1e1e1e"},
    }
    current_theme = "dark"

    def apply_theme():
        theme = themes[current_theme]
        explorer.configure(bg=theme["bg"])
        listbox.configure(bg=theme["bg"], fg=theme["fg"])
        preview_text.configure(bg=theme["preview_bg"], fg=theme["fg"])
        path_entry.configure(bg=theme["preview_bg"], fg=theme["fg"], insertbackground=theme["fg"])

    current_path = tk.StringVar()
    current_path.set(os.getcwd())

    def list_directory(path):
        try:
            listbox.delete(0, tk.END)
            current_path.set(path)
            items = os.listdir(path)
            for item in items:
                full_path = os.path.join(path, item)
                icon = "📁" if os.path.isdir(full_path) else "📄"
                listbox.insert(tk.END, f"{icon} {item}")
            preview_text.delete("1.0", tk.END)
        except Exception as e:
            print(f"Error listing files: {e}")

    def open_selected():
        selected = listbox.get(tk.ACTIVE)[2:]
        full_path = os.path.join(current_path.get(), selected)
        if os.path.isdir(full_path):
            list_directory(full_path)
        else:
            try:
                os.startfile(full_path)
            except Exception as e:
                print(f"Error opening file: {e}")

    def go_back():
        parent = os.path.dirname(current_path.get())
        list_directory(parent)

    def go_to_path():
        path = path_entry.get()
        if os.path.isdir(path):
            list_directory(path)
        else:
            print("Invalid path")

    def create_folder():
        name = simpledialog.askstring("Create Folder", "Enter folder name:")
        if name:
            try:
                os.mkdir(os.path.join(current_path.get(), name))
                list_directory(current_path.get())
            except Exception as e:
                print(f"Error creating folder: {e}")

    def create_file():
        name = simpledialog.askstring("Create File", "Enter file name (e.g. notes.txt):")
        if name:
            try:
                with open(os.path.join(current_path.get(), name), 'w') as f:
                    f.write("")
                list_directory(current_path.get())
            except Exception as e:
                print(f"Error creating file: {e}")

    def delete_selected():
        selected = listbox.get(tk.ACTIVE)[2:]
        full_path = os.path.join(current_path.get(), selected)
        try:
            if os.path.isdir(full_path):
                os.rmdir(full_path)
            else:
                os.remove(full_path)
            list_directory(current_path.get())
        except Exception as e:
            print(f"Error deleting: {e}")

    def rename_selected():
        selected = listbox.get(tk.ACTIVE)[2:]
        full_path = os.path.join(current_path.get(), selected)
        new_name = simpledialog.askstring("Rename", "Enter new name:")
        if new_name:
            try:
                os.rename(full_path, os.path.join(current_path.get(), new_name))
                list_directory(current_path.get())
            except Exception as e:
                print(f"Error renaming: {e}")

    def copy_selected():
        selected = listbox.get(tk.ACTIVE)[2:]
        src = os.path.join(current_path.get(), selected)
        dest = simpledialog.askstring("Copy", "Enter full destination path (with filename):")
        if dest:
            try:
                with open(src, 'rb') as fsrc:
                    with open(dest, 'wb') as fdst:
                        fdst.write(fsrc.read())
                list_directory(current_path.get())
            except Exception as e:
                print(f"Error copying file: {e}")

    def preview_selected(event=None):
        selected = listbox.get(tk.ACTIVE)[2:]
        full_path = os.path.join(current_path.get(), selected)
        preview_text.delete("1.0", tk.END)
        if os.path.isfile(full_path) and selected.endswith(".txt"):
            try:
                with open(full_path, 'r') as f:
                    preview_text.insert(tk.END, f.read())
            except Exception as e:
                preview_text.insert(tk.END, f"Error reading file: {e}")

    def edit_selected():
        selected = listbox.get(tk.ACTIVE)[2:]
        full_path = os.path.join(current_path.get(), selected)
        if os.path.isfile(full_path) and selected.endswith(".txt"):
            editor = tk.Toplevel(explorer)
            editor.title(f"Editing: {selected}")
            editor.geometry("600x400")
            text_area = tk.Text(editor, wrap="word", font=("Arial", 12))
            text_area.pack(fill=tk.BOTH, expand=True)
            try:
                with open(full_path, 'r') as f:
                    text_area.insert(tk.END, f.read())
            except Exception as e:
                text_area.insert(tk.END, f"Error opening file: {e}")
            def save():
                try:
                    with open(full_path, 'w') as f:
                        f.write(text_area.get("1.0", tk.END))
                    editor.destroy()
                    list_directory(current_path.get())
                except Exception as e:
                    print(f"Error saving file: {e}")
            tk.Button(editor, text="Save", command=save).pack(pady=5)

    def toggle_theme():
        nonlocal current_theme
        current_theme = "dark" if current_theme == "light" else "light"
        apply_theme()

    path_frame = tk.Frame(explorer)
    path_frame.pack(fill=tk.X)
    path_entry = tk.Entry(path_frame, textvariable=current_path, font=('Arial', 12))
    path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
    tk.Button(path_frame, text="Go", command=go_to_path).pack(side=tk.RIGHT, padx=5)

    main_frame = tk.Frame(explorer)
    main_frame.pack(fill=tk.BOTH, expand=True)
    listbox = tk.Listbox(main_frame, font=("Arial", 12), width=50)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    listbox.bind("<Double-Button-1>", lambda event: open_selected())
    listbox.bind("<<ListboxSelect>>", preview_selected)

    preview_text = tk.Text(main_frame, width=40, wrap="word", font=("Arial", 10))
    preview_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(0, 5), pady=5)

    button_frame = tk.Frame(explorer)
    button_frame.pack(fill=tk.X)
    tk.Button(button_frame, text="Open", command=open_selected).pack(side=tk.LEFT, padx=4)
    tk.Button(button_frame, text="Up", command=go_back).pack(side=tk.LEFT, padx=4)
    tk.Button(button_frame, text="Create Folder", command=create_folder).pack(side=tk.LEFT, padx=4)
    tk.Button(button_frame, text="Create File", command=create_file).pack(side=tk.LEFT, padx=4)
    tk.Button(button_frame, text="Delete", command=delete_selected).pack(side=tk.LEFT, padx=4)
    tk.Button(button_frame, text="Rename", command=rename_selected).pack(side=tk.LEFT, padx=4)
    tk.Button(button_frame, text="Copy", command=copy_selected).pack(side=tk.LEFT, padx=4)
    tk.Button(button_frame, text="Edit", command=edit_selected).pack(side=tk.LEFT, padx=4)
    tk.Button(button_frame, text="🌗 Theme", command=toggle_theme).pack(side=tk.LEFT, padx=4)
    tk.Button(button_frame, text="Close", command=explorer.destroy).pack(side=tk.RIGHT, padx=4)

    list_directory(current_path.get())
    apply_theme()
    explorer.mainloop()

# Démarrage automatique
if __name__ == "__main__":
    open_explorer()
