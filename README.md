# Python-project(Matrix_Calculation_Project)
# 목차
- [프로젝트 선정](#프로젝트-기획-동기)
- [전체 코드 실행 과정](#전체-코드-실행-과정)
- [코드 설명](#코드-설명)
- [의의]#(의의)
- 
# 프로젝트 기획 동기
####
 평소 파이썬에 대한 경험이 많지 않아 계산기 프로젝트에 대해 관심이 있었습니다. 또한 연세대학교 합격 전에 편입준비 과정에서 선형대수학에 큰 흥미를 느껴 이것이 파이썬으로 어떻게 구현되고 계산되는지 궁금했었습니다. 인공지능과 반도체 칩에 대한 전 세계적인 관심이 해가 거듭할수록 커지는 만큼 선형대수학도 이에 많이 사용된다고 익히 들었습니다. 인공신경망에 대한 계산, (SVD) Singular Value Decomposition의 이용, eigenvalue-eigenvector등의 원리가 적용된다고 알고 있습니다. 실생활에서의 인공지능에서 이런 값들에 대한 빠른 계산이 필요할 것이고 이를 손으로 직접 계산하기에는 분명 무리가 있을 것입니다. 따라서 행렬의 입력을 통해 입력되면 원하는 결과를 선택하여 도출하는 행렬 계산기 프로그램((Matrix_Calculation_Project)을 기획하게 되었습니다.

# 전체 코드 실행 과정
####
1. main.py파일에서 실행 - 2.행렬입력 - 3. 원하는 기능 선택 - 4. 결과출력


# 코드 설명
####
먼저 코드수정의 효율성을 위해 main.py , matrix_opertation.py , menu.py 파일로 분리해 파일을 생성하였습니다.

[matrix_operation.py]

<첫째> 

numpy를 import하고 먼저 행렬을 입력받기 위한 함수를 정의하였습니다.

<img width="664" alt="스크린샷 2024-06-20 오후 9 21 04" src="https://github.com/Choi-Yoonseo/Python-project/assets/163809985/4462d2ee-deb1-4df0-bce6-b208dcef3131">

<둘째> 

eigenvalue, svd, rank, basis_transformation, trace의 기능을 위한 numpy의 하위모듈인 선형대수관련 함수를 사용하기 위해 np.linalg를 사용하였습니다.

np.linalg.eig(matrix) (eignvalue-eigenvector)

np.linalg.svd(matrix) (Singular Value Decomposition)

np.linalg.matrix_rank(matrix) (rank)

np.linalg.inv(alpha) (inverse matrix)

np.dot(beta,alpha) (inner product)

np.trace(matrix) (trace)

<img width="415" alt="스크린샷 2024-06-20 오후 9 24 36" src="https://github.com/Choi-Yoonseo/Python-project/assets/163809985/577b5910-07bd-4f18-b732-77120106da76">

[menu.py]

원하는 기능 선택을 위해 정의한 함수가 담긴 파일을 형성하였습니다.

<img width="482" alt="스크린샷 2024-06-20 오후 9 32 41" src="https://github.com/Choi-Yoonseo/Python-project/assets/163809985/7e7774a9-fb32-4241-aa8c-1f588e96c731">

[main.py]

<첫째>
numpy를 import하고 matrix_operation.py파일로부터 정의된 함수들을 호출하였습니다. 또한 menu선택을 위해 menu파일로부터 import하였습니다.

<img width="858" alt="스크린샷 2024-06-20 오후 9 33 43" src="https://github.com/Choi-Yoonseo/Python-project/assets/163809985/6e03615b-70b4-4898-a8d0-9c47a9f24766">

<둘째>
main함수를 정의하고 사용자가 원할 때 종료하기 위해 무한루프안에 menu기능을 정의하였습니다. 

<img width="478" alt="스크린샷 2024-06-20 오후 9 38 10" src="https://github.com/Choi-Yoonseo/Python-project/assets/163809985/c822e765-eb4d-41c8-b81e-dd07b1f89050">

<1번 기능 - 행렬의 덧셈>

두 행렬을 입력받아 행렬의 덧셈을 출력합니다.

<2번 기능 - 행렬의 뺄셈>

두 행렬을 입력받아 행렬의 뺄셈을 출력합니다.

<3번 기능 - 행렬의 내적>

두 행렬을 입력받아 행렬의 내적을 출력합니다.

<4번 기능 - 전치행렬(Transpose)>

한 행렬을 입력받아 행렬의 전치행렬을 출력합니다.

<img width="496" alt="스크린샷 2024-06-20 오후 9 40 28" src="https://github.com/Choi-Yoonseo/Python-project/assets/163809985/6aaf0f80-73e4-419a-bc9f-c09867a2ecbd">

<5번 기능 - 역행렬>

한 행렬을 입력받아 역행렬을 출력하고 역행렬이 존재하지 않은 경우를 위해 역행렬이 존재하지 않는 출력도 입력하였습니다.

<6번 기능 - 행렬식>

한 행렬을 입력받아 해당 행렬의 행렬식을 출력합니다.

<7번 기능 - eigenvalue, eigenvector>

한 행렬을 입력받아 고유치(eigenvalue), (고유벡터)eigenvector 를 출력합니다.

<8번 기능 - Singular Value Decomposition>

한 행렬을 입력받아 특이값과 U행렬(AAt를 직교대각화 시키는 행렬), Vt(AtA를 직교대각화 시키는 행렬)을 각각 출력합니다.

<9번 기능 - rank>

한 행렬을 입력받아 행렬의 계수 rank를 출력합니다.

<10번 기능 - 기저 변환 행렬(추이행렬)>

알파공간의 기저행렬과 베타공간의 기저행렬을 입력 받고 역행렬을 가지는 경우에 알파와 베타 공간사이의 기저변환행렬을 출력합니다.

역행렬이 존재하지 않는 경우 기저변환행렬이 존재하지 않음도 출력합니다.

<img width="314" alt="스크린샷 2024-06-20 오후 9 48 44" src="https://github.com/Choi-Yoonseo/Python-project/assets/163809985/9b1751a5-dae0-4177-bf9a-9ee49daa51f3">

<11번 기능 - trace>

한 행렬을 입력받아 행렬의 대각합(trace)를 출력합니다.

<12번 기능 - 프로그램 종료>

사용자가 종료를 원하면 12번을 입력하여 프로그램을 종료합니다.

<img width="328" alt="스크린샷 2024-06-20 오후 9 50 46" src="https://github.com/Choi-Yoonseo/Python-project/assets/163809985/2d0d223a-d3ac-4026-88f8-0f7cde20a779">

마지막 if __name__ == "__main__":
    main() 로 마무리 합니다.

# 의의
####
이 프로젝트를 위해 numpy모듈을 조사하면서 생각보다 프로그램의 편의성을 위해 이미 형성되어있는 모듈들이 상당히 많음을 알수 있었습니다. 앞으로 다른 프로젝트를 진행할때도 처음부터 자신이 코드를 다 만드는 것이 아니라 관련된 모듈을 import하여 사용하면서 코드의 효율성을 높이는 부분으로 방향성이 향해야 함을 깨달았습니다. 또한 평소에 하던 것은 코드의 길이가 길지 않아서 하나의 파이썬 파일에 다 코드를 작성했습니다. 하지만 이번 프로젝트에서 코드가 길어지면서 오류 발생시 수정하는 과정에서 파일이 하나로 되어있다보니 수정에 어려움을 겪었습니다. 이때 파일을 적절한 개수로 나누어 수정을 진행하였는데 오류가 있는 부분을 직관적으로 파악할 수 있었습니다. 모듈적으로 지식도 쌓고 프로젝트를 하는 과정에서 파일 수정에 관한 팁도 얻으면서 뜻깊은 프로젝트 시간이었습니다.
