import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        
        # List of tasks
        self.tasks = []
        
        # Create a frame to hold the task list
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        # Listbox to display tasks
        self.listbox = tk.Listbox(self.frame, height=10, width=40, font=("Arial", 14), selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        # Entry box to add new tasks
        self.task_entry = tk.Entry(self.root, font=("Arial", 14))
        self.task_entry.pack(pady=20)
        
        # Button to add tasks
        add_button = tk.Button(self.root, text="Add Task", font=("Arial", 14), bg="#6c63ff", fg="white", command=self.add_task)
        add_button.pack(pady=10)
        
        # Button to delete selected task
        delete_button = tk.Button(self.root, text="Delete Task", font=("Arial", 14), bg="#ff4b5c", fg="white", command=self.delete_task)
        delete_button.pack(pady=10)
        
        # Button to edit selected task
        edit_button = tk.Button(self.root, text="Edit Task", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.edit_task)
        edit_button.pack(pady=10)
        
    def add_task(self):
        """Add a new task to the list"""
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You need to enter a task.")
    
    def delete_task(self):
        """Delete the selected task from the list"""
        try:
            selected_task_index = self.listbox.curselection()[0]
            task_to_delete = self.listbox.get(selected_task_index)
            self.tasks.remove(task_to_delete)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You need to select a task first.")
    
    def edit_task(self):
        """Edit the selected task"""
        try:
            selected_task_index = self.listbox.curselection()[0]
            old_task = self.listbox.get(selected_task_index)
            new_task = simpledialog.askstring("Edit Task", f"Edit task '{old_task}'", initialvalue=old_task)
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You need to select a task first.")
    
    def update_listbox(self):
        """Update the listbox with the current list of tasks"""
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
