import tkinter as tk  # Импортируем библиотеку tkinter для создания графического интерфейса
from tkinter import ttk  # Импортируем модуль ttk для работы с современными виджетами
from tkinter import filedialog  # Импортируем модуль для выбора файлов


# Создаем основное окно приложения
window = tk.Tk()
window.title("Программа с GUI")  # Устанавливаем заголовок окна

# Устанавливаем начальный размер окна (ширина x высота)
window.geometry("800x600")
window.configure(bg='#FDE7BB')  # Задаем цвет фона окна




# Создаем Canvas, чтобы разместить на нем фоновое изображение
canvas = tk.Canvas(window, width=800, height=600, highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)  # Canvas заполняет все окно и растягивается при изменении размеров



# Глобальная переменная для хранения пути к файлу
log_file_path = None



# Настраиваем стили для кнопок и меток, чтобы интерфейс выглядел красиво
style = ttk.Style()
style.configure("My.TLabel", font=("Helvetica", 14), foreground="#004D40", padding=5, background="#FDE7BB")
style.configure("My.TButton", font=("Helvetica", 12), padding=5, background="#9EDF9C", foreground="#004D40")
style.map("My.TButton", background=[('active', '#4CAF50')], foreground=[('active', '#FFFFFF')])

# Функция для записи задач и ответов в лог-файл
def log_to_file(task, answer):
    if log_file_path:
        try:
            with open(log_file_path, "a", encoding="utf-8") as log_file:
                log_file.write(f"Задача: {task}\nОтвет: {answer}\n\n")
        except Exception as e:
            result_label.config(text="Ошибка записи в файл.")
    else:
        result_label.config(text="Файл для лога не выбран!")

# Функции для обработки введенных чисел с логированием
def add_numbers_gui():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Результат: {result}")
        log_to_file(f"Сложение {num1} + {num2}", result)
    except ValueError:
        result_label.config(text="Ошибка: введите числа!")
        log_to_file("Сложение с некорректным вводом", "Ошибка: введите числа!")

def minus_numbers_gui():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Результат: {result}")
        log_to_file(f"Вычитание {num1} - {num2}", result)
    except ValueError:
        result_label.config(text="Ошибка: введите числа!")
        log_to_file("Вычитание с некорректным вводом", "Ошибка: введите числа!")

def multiplication_numbers_gui():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Результат: {result}")
        log_to_file(f"Умножение {num1} * {num2}", result)
    except ValueError:
        result_label.config(text="Ошибка: введите числа!")
        log_to_file("Умножение с некорректным вводом", "Ошибка: введите числа!")

def division_numbers_gui():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль.")
        result = num1 / num2
        result_label.config(text=f"Результат: {result}")
        log_to_file(f"Деление {num1} / {num2}", result)
    except ZeroDivisionError:
        result_label.config(text="Ошибка: деление на ноль!")
        log_to_file(f"Деление {num1} / {num2}", "Ошибка: деление на ноль!")
    except ValueError:
        result_label.config(text="Ошибка: введите числа!")
        log_to_file("Деление с некорректным вводом", "Ошибка: введите числа!")

# Функция для выбора файла
def select_file():
    global log_file_path
    log_file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Выберите файл для логирования"
    )
    if log_file_path:
        file_label.config(text=f"Выбранный файл: {log_file_path}")
        with open(log_file_path, "w", encoding="utf-8") as log_file:
            log_file.write("Лог действий программы:\n\n")  # Заголовок лога
    else:
        file_label.config(text="Файл не выбран!")


# Создаем рамку (Frame) для размещения виджетов ввода и кнопок
frame = tk.Frame(window, bg="#FFFFFF", padx=10, pady=10)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Центрируем рамку в окне


# Поля для ввода чисел
label1 = ttk.Label(frame, text="Введите первое число:", style="My.TLabel")
label1.grid(row=0, column=0, pady=5, sticky="w")  # Размещаем метку в сетке (grid)
entry1 = tk.Entry(frame, font=("Helvetica", 12), width=20)  # Поле ввода для первого числа
entry1.grid(row=0, column=1, pady=5)

label2 = ttk.Label(frame, text="Введите второе число:", style="My.TLabel")
label2.grid(row=1, column=0, pady=5, sticky="w")
entry2 = tk.Entry(frame, font=("Helvetica", 12), width=20)  # Поле ввода для второго числа
entry2.grid(row=1, column=1, pady=5)


# Кнопки для выполнения операций
add_button = ttk.Button(frame, text="Сложить", command=add_numbers_gui, style="My.TButton", cursor='hand2')
add_button.grid(row=2, column=0, pady=10, sticky="ew", columnspan=2)

minus_button = ttk.Button(frame, text="Вычесть", command=minus_numbers_gui, style="My.TButton", cursor='hand2')
minus_button.grid(row=3, column=0, pady=10, sticky="ew", columnspan=2)

multiplication_button = ttk.Button(frame, text="Умножить", command=multiplication_numbers_gui, style="My.TButton", cursor='hand2')
multiplication_button.grid(row=4, column=0, pady=10, sticky="ew", columnspan=2)

division_button = ttk.Button(frame, text="Разделить", command=division_numbers_gui, style="My.TButton", cursor='hand2')
division_button.grid(row=5, column=0, pady=10, sticky="ew", columnspan=2)


# Метка для отображения результата
result_label = ttk.Label(frame, text="Результат:", style="My.TLabel")
result_label.grid(row=6, column=0, columnspan=2, pady=10)


# Кнопка для выбора файла
file_button = ttk.Button(frame, text="Выбрать файл", command=select_file, style="My.TButton", cursor='hand2')
file_button.grid(row=7, column=0, columnspan=2, pady=10)

# Метка для отображения пути к выбранному файлу
file_label = ttk.Label(frame, text="Файл не выбран", style="My.TLabel")
file_label.grid(row=8, column=0, columnspan=2, pady=10)


# Разрешаем изменять размер окна
window.resizable(True, True)

# Запускаем главный цикл обработки событий
window.mainloop()
