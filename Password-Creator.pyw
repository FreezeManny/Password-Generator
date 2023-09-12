import tkinter
import customtkinter

import random

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
specialCharacters = "!@#$%^&*()_-+={[}|:;<>"

def createRandomPassword(length, withUppercase, withLowercase, withNumbers, withSpecialCharacters):

    uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    specialCharacters = "!@#$%^&*()_-+={[}|:;<>"

    allCharactersUsed = ""

    password = ""

    if(withUppercase == 1):
        allCharactersUsed += uppercaseLetters
    if(withLowercase == 1):
        allCharactersUsed +=lowercaseLetters
    if(withNumbers == 1):
        allCharactersUsed += numbers
    if(withSpecialCharacters == 1):
        allCharactersUsed += specialCharacters


    for i in range(length):

        password += allCharactersUsed[random.randint(0, len(allCharactersUsed)-1)]
    return password


def copyToClipboard(text):
    
        r = tkinter.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.password_length = 20

        self.password = ""

        # configure window
        self.title("Password Generator")
        self.resizable(False, False)
        self.after_idle(self.updatePassword)

        # configure grid layout
        #self.grid_columnconfigure(1, weight=1)
        #self.grid_rowconfigure(0, weight=1)

        self.password_length_frame = customtkinter.CTkFrame(self)
        self.password_length_frame.grid(row=0, column=0, padx=5, pady=5)

        self.password_length_label = customtkinter.CTkLabel(self.password_length_frame, text="Password Length:")
        self.password_length_label.grid(row=0, column=0)

        self.password_length_value_label = customtkinter.CTkLabel(self.password_length_frame, text=self.password_length)
        self.password_length_value_label.grid(row=0, column=1)

        self.password_length_slider = customtkinter.CTkSlider(self.password_length_frame, from_=4, to=40, command=self.lenghtSliderChange)
        self.password_length_slider.grid(row=1, column=0, columnspan=2)
        self.password_length_slider.set(self.password_length)


        self.options_frame = customtkinter.CTkFrame(self)
        self.options_frame.grid(row=0, column=1, padx=5, pady=5)

        self.uppercase_letters_checkbox = customtkinter.CTkCheckBox(self.options_frame, text="Uppercase Letters", command=self.checkboxChange)
        self.uppercase_letters_checkbox.grid(row=0, column=0, sticky="w", padx=1, pady=2)
        self.uppercase_letters_checkbox.select()

        self.lowercase_letters_checkbox = customtkinter.CTkCheckBox(self.options_frame, text="Lowercase Letters", command=self.checkboxChange)
        self.lowercase_letters_checkbox.grid(row=1, column=0, sticky="w", padx=1, pady=2)
        self.lowercase_letters_checkbox.select()

        self.numbers_checkbox = customtkinter.CTkCheckBox(self.options_frame, text="Numbers", command=self.checkboxChange)
        self.numbers_checkbox.grid(row=2, column=0, sticky="w", padx=1, pady=2)
        self.numbers_checkbox.select()

        self.special_Characters_checkbox = customtkinter.CTkCheckBox(self.options_frame, text="Special Characters", command=self.checkboxChange)
        self.special_Characters_checkbox.grid(row=3, column=0, sticky="w", padx=1, pady=2)
        self.special_Characters_checkbox.select()


        self.button_output_frame = customtkinter.CTkFrame(self)
        self.button_output_frame.grid(row=0, column=2, padx=5, pady=5)

        self.password_label = customtkinter.CTkLabel(self.button_output_frame, text="Password: ")
        self.password_label.grid(row=0, column=0)

        self.generated_password_label = customtkinter.CTkLabel(self.button_output_frame, text="")
        self.generated_password_label.grid(row=1, column=0, sticky="w", padx=5, pady=2)

        self.regenerate_btn = customtkinter.CTkButton(self.button_output_frame, text="Regenerate", command=self.regenerate)
        self.regenerate_btn.grid(row=2, column=0, padx=1, pady=2)

        self.copy_btn = customtkinter.CTkButton(self.button_output_frame, text="copy", command=self.copy)
        self.copy_btn.grid(row=3, column=0, padx=1, pady=2)


    def lenghtSliderChange(self, value):
        self.password_length = round(value)
        self.password_length_value_label.configure(text=self.password_length)
        self.updatePassword()
        #print(self.password_length)

    def checkboxChange(self):
        #print("Checkbox changed")
        self.updatePassword()

    def regenerate(self):
        self.updatePassword()

    def copy(self):
        copyToClipboard(self.password)

    def copyAndClose(self):
        copyToClipboard(self.password)
        self.destroy()

    def updatePassword(self):
        self.password = createRandomPassword(self.password_length, self.uppercase_letters_checkbox.get(), self.lowercase_letters_checkbox.get(), self.numbers_checkbox.get(), self.special_Characters_checkbox.get())
        self.generated_password_label.configure(text=self.password)
        copyToClipboard(self.password)



        


if __name__ == "__main__":
    app = App()
    app.mainloop()
