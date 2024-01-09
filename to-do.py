import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        custom_font = ("Helvetica", 12)

        self.tasks = []

        self.root.configure(bg='#333333')

        self.task_entry = tk.Entry(root, width=40, font=custom_font)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=custom_font, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=40, height=10, font=custom_font, bg='#555555', fg='white')
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, font=custom_font, bg="#FF5733", fg="white")
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, font=custom_font, bg="#3498db", fg="white")
        self.update_button.grid(row=2, column=1, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_as_complete, font=custom_font, bg="#f39c12", fg="white")
        self.complete_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_list()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            updated_text = simpledialog.askstring("Update Task", "Enter updated task:")
            if updated_text:
                self.tasks[selected_index[0]] = updated_text
                self.update_task_list()

    def mark_as_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            completed_task = f"{task} (Complete)"
            self.tasks[selected_index[0]] = completed_task
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

