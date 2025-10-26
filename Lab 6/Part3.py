import tkinter as tk
from tkinter import messagebox, filedialog

# ========================
# Node (Cell) Definition
# ========================
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = ""
        self.right = None
        self.down = None


# ========================
# Linked List Grid
# ========================
class LinkedGrid:
    def __init__(self, rows=25, cols=25):
        self.rows = rows
        self.cols = cols
        self.head = self.create_grid()

    def create_grid(self):
        start = None
        prev_row = None

        for i in range(self.rows):
            row_head = None
            prev_cell = None

            for j in range(self.cols):
                new_cell = Cell(i, j)

                if not row_head:
                    row_head = new_cell
                if prev_cell:
                    prev_cell.right = new_cell
                if prev_row:
                    up = prev_row
                    for k in range(j):
                        up = up.right
                    up.down = new_cell

                prev_cell = new_cell

            if i == 0:
                start = row_head
            prev_row = row_head

        return start

    def get_node(self, r, c):
        node = self.head
        for i in range(r):
            node = node.down
        for j in range(c):
            node = node.right
        return node

    def clear_all(self):
        node_row = self.head
        while node_row:
            node_col = node_row
            while node_col:
                node_col.value = ""
                node_col = node_col.right
            node_row = node_row.down


# ========================
# GUI Part (Tkinter)
# ========================
class ExcelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Grid (Linked List DSA Project)")

        self.rows, self.cols = 10,10
        self.grid = LinkedGrid(self.rows, self.cols)
        self.entries = []
        self.current_row = 0
        self.current_col = 0

        self.build_ui()
        self.highlight_current()

        # Bind keys for navigation
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Return>", self.save_value)

    # --------------------
    # UI Creation
    # --------------------
    def build_ui(self):
        # Column headers (A, B, C...)
        for j in range(self.cols):
            label = tk.Label(self.root, text=chr(65 + j), font=("Arial", 10, "bold"))
            label.grid(row=0, column=j + 1)

        # Row numbers (1, 2, 3...)
        for i in range(self.rows):
            label = tk.Label(self.root, text=str(i + 1), font=("Arial", 10, "bold"))
            label.grid(row=i + 1, column=0)

        # Entry boxes (cells)
        for i in range(self.rows):
            row_entries = []
            for j in range(self.cols):
                e = tk.Entry(self.root, width=10, font=("Arial", 12), justify='center')
                e.grid(row=i + 1, column=j + 1, padx=2, pady=2)
                row_entries.append(e)
            self.entries.append(row_entries)

        # Status Label
        self.status = tk.Label(self.root, text="Cell: A1", font=("Arial", 10, "italic"))
        self.status.grid(row=self.rows + 2, column=0, columnspan=self.cols + 1)

        # Buttons
        clear_btn = tk.Button(self.root, text="🧹 Clear All", command=self.clear_all, bg="orange", fg="white")
        clear_btn.grid(row=self.rows + 3, column=0, columnspan=2, pady=10)

        save_btn = tk.Button(self.root, text="💾 Save to File", command=self.save_to_file, bg="green", fg="white")
        save_btn.grid(row=self.rows + 3, column=2, columnspan=2, pady=10)

        exit_btn = tk.Button(self.root, text="❌ Exit", command=self.root.quit, bg="red", fg="white")
        exit_btn.grid(row=self.rows + 3, column=4, columnspan=1, pady=10)

    # --------------------
    # Navigation
    # --------------------
    def highlight_current(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.entries[i][j].config(bg="white")

        self.entries[self.current_row][self.current_col].config(bg="lightblue")
        self.status.config(
            text=f"Cell: {chr(65 + self.current_col)}{self.current_row + 1}"
        )

    def move_right(self, event=None):
        if self.current_col < self.cols - 1:
            self.current_col += 1
        self.highlight_current()

    def move_left(self, event=None):
        if self.current_col > 0:
            self.current_col -= 1
        self.highlight_current()

    def move_up(self, event=None):
        if self.current_row > 0:
            self.current_row -= 1
        self.highlight_current()

    def move_down(self, event=None):
        if self.current_row < self.rows - 1:
            self.current_row += 1
        self.highlight_current()

    # --------------------
    # Core Operations
    # --------------------
    def save_value(self, event=None):
        val = self.entries[self.current_row][self.current_col].get()
        node = self.grid.get_node(self.current_row, self.current_col)
        node.value = val
        print(f"Saved [{chr(65+self.current_col)}{self.current_row+1}] = {val}")

    def clear_all(self):
        self.grid.clear_all()
        for i in range(self.rows):
            for j in range(self.cols):
                self.entries[i][j].delete(0, tk.END)
        messagebox.showinfo("Cleared", "All cells have been cleared!")

    def save_to_file(self):
        # Save values from all entries into linked list before exporting
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.entries[i][j].get()
                self.grid.get_node(i, j).value = val

        # Ask where to save
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            title="Save Grid Data"
        )
        if not file_path:
            return

        with open(file_path, "w") as f:
            # Write column headers
            headers = "\t".join([chr(65 + j) for j in range(self.cols)])
            f.write("\t" + headers + "\n")

            # Write data rows
            for i in range(self.rows):
                row_label = str(i + 1)
                values = []
                for j in range(self.cols):
                    node = self.grid.get_node(i, j)
                    values.append(node.value)
                f.write(row_label + "\t" + "\t".join(values) + "\n")

        messagebox.showinfo("Saved", f"Grid data saved successfully to:\n{file_path}")


# ========================
# Run the App
# ========================
if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelApp(root)
    root.mainloop()
