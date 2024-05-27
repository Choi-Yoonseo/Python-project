def menu():
    print("\n행렬 계산기 리스트")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 전치 행렬 (Transpose)")
    print("5. 역행렬")
    print("6. 행렬식 (determinant)")
    print("7. 고유치 및 고유벡터 계산 (eigenvalue, eigenvector)")
    print("8. 특이값 분해 (Singular Value Decomposition)")
    print("9. rank")
    print("10. 기저 변환 행렬(추이행렬) 계산")
    print("11. trace")
    print("12. 프로그램 종료")

def get_choice():
    choice = input("선택하세요: ")
    return choice
