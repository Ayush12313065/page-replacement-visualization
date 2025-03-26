import tkinter as tk

class PageReplacementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Algorithm Visualization")

        self.label = tk.Label(root, text="Welcome to Page Replacement Simulator", font=("Arial", 14))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(pady=5)

    def start_simulation(self):
        print("Simulation Started...")  # Placeholder for future implementation

if __name__ == "__main__":
    root = tk.Tk()
    gui = PageReplacementGUI(root)
    root.mainloop()