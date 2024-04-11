import sys


stdin_file = sys.stdin
stdout_file = sys.stdout
stderr_file = sys.stderr

correct_sym = [" ", "(", ")", "\n"]
oper_sym = ["+", "-", "*"]


def check_eval(line_):
    try:
        eval(line_)
        return True
    except:
        return False


def check(line_):
    for char in line_:
        if check_eval(line_):
            # Рядок №1 - перевірка чи можливо перевести символ в число
            # Рядок №2 - перевірка чи є символ дозволеним
            # Рядок №3 - усунення будь-яких випідків з пустими дужками
            if not char.isdigit() \
                    and char not in correct_sym + oper_sym \
                    or str(eval(line_)) == "()":
                return False
        else:
            return False
    return True


def my_eval(line_):
    if line_ in ["", "\n"]:  # На порожній рядок повертаємо порожній рядок
        return "\n"
    else:
        if check(line_):
            return str(eval(line_)) + "\n"
        else:
            stderr_file.write("Error")
            return False


def file_eval(file):
    for line in file:
        if my_eval(line):
            stdout_file.write(my_eval(line))
        else:
            sys.exit(1)


if __name__ == "__main__":
    file_eval(stdin_file)
