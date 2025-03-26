class PageReplacementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Algorithm Visualization")

        tk.Label(root, text="Select an Algorithm:", font=("Arial", 12)).pack(pady=5)
        self.algorithms = ["FIFO", "LRU", "Optimal", "LFU", "Clock"]
        self.algorithm_var = tk.StringVar(value=self.algorithms[0])
        tk.OptionMenu(root, self.algorithm_var, *self.algorithms).pack(pady=5)

        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(pady=5)

    def start_simulation(self):
        print(f"Selected Algorithm: {self.algorithm_var.get()}")