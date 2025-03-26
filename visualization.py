import tkinter as tk
from tkinter import messagebox

class PageReplacementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Algorithm Visualization")

        # Algorithm Selection
        tk.Label(root, text="Select an Algorithm:", font=("Arial", 12)).pack(pady=5)
        self.algorithms = ["FIFO", "LRU", "Optimal", "LFU", "Clock"]
        self.algorithm_var = tk.StringVar(value=self.algorithms[0])
        tk.OptionMenu(root, self.algorithm_var, *self.algorithms).pack(pady=5)

        # Reference String Input
        tk.Label(root, text="Enter Reference String (comma-separated):").pack(pady=5)
        self.ref_string_entry = tk.Entry(root, width=30)
        self.ref_string_entry.pack(pady=5)

        # Start Simulation Button
        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(pady=5)

        # Frame Display for Visualization
        self.frame_display = tk.Label(root, text="", font=("Arial", 12))
        self.frame_display.pack(pady=10)

    def start_simulation(self):
        ref_string = self.ref_string_entry.get().strip()

        # Validate input: ensure it's non-empty and consists of numbers separated by commas
        if not ref_string:
            messagebox.showerror("Input Error", "Reference string cannot be empty.")
            return

        try:
            reference_string = list(map(int, ref_string.split(',')))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid reference string (comma-separated integers).")
            return

        # Process the reference string
        self.frame_display.config(text=f"Processing: {reference_string}")
        self.step_by_step_display(reference_string)

    def step_by_step_display(self, reference_string):
        self.frame_display.config(text="Processing...")
        for page in reference_string:
            self.frame_display.config(text=f"Current Page: {page}")
            self.root.update()
            time.sleep(1)  # Simulating delay

if __name__ == "__main__":
    root = tk.Tk()
    gui = PageReplacementGUI(root)
    root.mainloop()