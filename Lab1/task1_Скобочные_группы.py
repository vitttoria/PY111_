def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    brackets = "(){}[]"  # Строка из видов скобок
    opening, closing = brackets[::2], brackets[1::2]  # Считываем четные и нечетные символы (как открывающие и
    # закрывающие скобки)
    stack = []
    for character in brackets_row:  # элемент в строке
        if character in opening:  # если элемент совпадает с opening
            stack.append(opening.index(character))  # добавляем элемент с стэк, как открывающую скобку
        elif character in closing:  # если элемент совпадает с closing
            if stack and stack[-1] == closing.index(character):  # если
                stack.pop()
            else:
                return False
    if not stack == []:
        return False
    elif brackets_row == "":
        return True
    elif not stack:
        return True


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets("(())"))  # True
    print(check_brackets("(()("))  # False
    print(check_brackets("("))  # False
    print(check_brackets(")"))  # False
