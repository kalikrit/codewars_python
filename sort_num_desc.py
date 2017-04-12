
def descending_order(num):
    """
    на входе число 1233456
    на выходе получаем число с цифрами исходного числа, отсортированными в обратном порядке 6543321
    """
    return int("".join(sorted(str(num), reverse=True)))

