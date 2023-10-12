from random import randint
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
MAX_GEN = 50
MIN_K = 5
MAX_K = 15
def divide_in_matrix(m: list[list[int]]) -> list[list[float]]:
    new_m = []
    for row in m:
        divider = max(row)
        new_m.append([(i / divider) for i in row])
    return new_m
def gen_matrix(rows: int, columns: int) -> list[list[int]]:
    m = []
    for _ in range(rows):
        m.append([randint(0, MAX_GEN) for _ in range(columns)])
    return m
def matrix_to_str(matrix: list[list[int | float]]) -> str:
    out = ""
    max_el_length = 1
    for row in matrix:
        r_el_l = list(map(lambda i: len(str(round(i, 2))), [el for el in row]))
        if (new_max := max(r_el_l)) > max_el_length:
            max_el_length = new_max
    row_templ = ("{:<{width}} " * len(matrix[0])) + "\n"
    for row in matrix:
        out += row_templ.format(
            *[ round(el, 2) for el in row],
            width=max_el_length
        )
    return out.strip()
def gen_message(
        m_a: list[list[int | float]],
        m_b: list[list[int | float]],
        m_a_b: list[list[int | float]]
):
    m_a_str = matrix_to_str(m_a)
    m_b_str = matrix_to_str(m_b)
    m_a_b_str = matrix_to_str(m_a_b)
    return f"Matrix A:\n{m_a_str}\nMatrix B:\n{m_b_str}\nMatrix A*B:\n{m_a_b_str}"
def multiply_matrices(
        m_a: list[list[int | float]],
        m_b: list[list[int | float]]
) -> list[list[int | float]]:
    if len(m_a[0]) != len(m_b):
        raise Exception("Unable to perform multipy of matrices")
    m_c = [
        [
            sum(
                a * b for a, b in zip(a_row, b_col)
            ) for b_col in zip(*m_b)
        ] for a_row in m_a
    ]
    return m_c
def read_file() -> str:
    with open(INPUT_FILE, "r") as file:
        info = file.read()
    return info
def write_file(message: str):
    with open(OUTPUT_FILE, "w") as file:
        file.write(message)
def main():
    size_a_str = read_file()
    n, m = tuple(map(int, size_a_str.split()))
    matrix_a = gen_matrix(rows=n, columns=m)
    div_matrix_a = divide_in_matrix(matrix_a)
    k = randint(5, 15)
    matrix_b = gen_matrix(rows=m, columns=k)
    matrix_a_b = multiply_matrices(div_matrix_a, matrix_b)
    message = gen_message(matrix_a, matrix_b, matrix_a_b)
    write_file(message)
if __name__ == "__main__":
    main()