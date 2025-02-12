import tkinter as tk
from tkinter import scrolledtext

def correct_syntax_errors(code, language):
    corrected_code = ""
    lines = code.split('\n')
    current_indentation = 0

    for line in lines:
        trimmed_line = line.strip()

        # Adjust indentation based on braces
        if trimmed_line.endswith("{"):
            current_indentation += 1

        # Preserve existing indentation
        corrected_code += "    " * current_indentation

        # Correct syntax errors and append the line
        if trimmed_line:
            if trimmed_line.startswith("}"):
                current_indentation = max(current_indentation - 1, 0)

            if trimmed_line.startswith("#"):
                corrected_code += trimmed_line
            elif trimmed_line.endswith(";") or trimmed_line.endswith("{") or trimmed_line.endswith("}"):
                corrected_code += trimmed_line
            else:
                corrected_code += trimmed_line + ";"
        else:
            corrected_code += trimmed_line

        corrected_code += "\n"

    return corrected_code

def correct_syntax_errors_gui():
    def on_submit():
        code_content = code_input.get("1.0", tk.END)
        language = language_entry.get().lower()
        corrected_code = correct_syntax_errors(code_content, language)
        corrected_output.config(state=tk.NORMAL)
        corrected_output.delete("1.0", tk.END)
        corrected_output.insert(tk.END, corrected_code)
        corrected_output.config(state=tk.DISABLED)

    root = tk.Tk()
    root.title("Syntax Error Corrector")

    language_label = tk.Label(root, text="Enter the programming language (java, c, cpp):")
    language_label.pack()

    language_entry = tk.Entry(root)
    language_entry.pack()

    code_label = tk.Label(root, text="Enter the code for review:")
    code_label.pack()

    code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    code_input.pack()

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack()

    corrected_output_label = tk.Label(root, text="Corrected Code:")
    corrected_output_label.pack()

    corrected_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, state=tk.DISABLED)
    corrected_output.pack()

    root.mainloop()

if __name__ == "__main__":
    correct_syntax_errors_gui()
