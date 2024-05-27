import numpy as np
from matrix_operations import m, eigenvalues_vectors, svd, matrix_rank, basis_transformation_matrix,matrix_trace
from menu import menu
print("행렬 계산기를 실행합니다.")


def main():
    while True:
        menu()
        a = input("선택하세요: ")

        if a == '1':
            matrix1 = m("첫 번째 행렬을 입력하세요:")
            matrix2 = m("두 번째 행렬을 입력하세요:")
            print(f"덧셈 결과 : \n {matrix1 + matrix2}\n")

        elif a == '2':
            matrix1 = m("첫 번째 행렬을 입력하세요:")
            matrix2 = m("두 번째 행렬을 입력하세요:")
            print(f"뺄샘 결과 : \n {matrix1 - matrix2}\n")

        elif a == '3':
            matrix1 = m("첫 번째 행렬을 입력하세요:")
            matrix2 = m("두 번째 행렬을 입력하세요:")
            print(f"곱셈 결과:{np.dot(matrix1, matrix2)}\n")

        elif a == '4':
            matrix = m("행렬을 입력하세요")
            print(f"전치 행렬 결과:{np.transpose(matrix)}\n")

        elif a == '5':
            matrix = m("행렬을 입력하세요")
            try:
                print(f"역행렬 결과 : {np.linalg.inv(matrix)}\n")
            except np.linalg.LinAlgError:
                print("역행렬이 존재하지 않습니다.")

        elif a == '6':
            matrix = m("행렬을 입력하세요")
            print(f"결과 : {np.linalg.det(matrix)}\n")

        elif a == '7':
            matrix = m("행렬을 입력하세요")
            eigenvalues, eigenvectors = eigenvalues_vectors(matrix)
            print(f"고유치 : {eigenvalues}\n")
            print(f"고유벡터: {eigenvectors}\n")
        
        elif a == '8':
            matrix = m("행렬을 입력하세요")
            U, S, Vt = svd(matrix)
            print(f"U 행렬 : {U}\n")
            print(f"특이값 : {S}\n")
            print(f"Vt 행렬 : {Vt}\n")

        elif a == '9':
            matrix = m("행렬을 입력하세요")
            rank = matrix_rank(matrix)
            print(f"rank:{rank}\n")
            print(f"행공간의 차원과 열공간의 차원은 {rank}입니다.\n")

        elif a == '10':
            alpha = m("alpha 기저 행렬 입력 :")
            beta = m("beta 기저 행렬 입력 :")
            try:
                P = basis_transformation_matrix(alpha, beta)
                print(f"기저 변환 행렬 (P):\n{P}\n")
            except np.linalg.LinAlgError:
                print("입력된 기저 행렬 중 하나가 역행렬을 가지지 않습니다.\n")

        elif a == '11':
            matrix = m("행렬을 입력하세요")
            t = matrix_trace(matrix)
            print(f"행렬의 trace는 {t}입니다.\n")

        elif a == '12':
            print("프로그램을 종료합니다.")
            break    
        
        else:
            print("잘못된 접근입니다.")
            continue

if __name__ == "__main__":
    main() 