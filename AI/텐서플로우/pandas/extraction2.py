import pandas as pd

# 키, 몸무게, 유형, 데이트 프레임 생성하기
tbl = pd.DataFrame({"weight": [80.0,70.4,65.5,45.9,51.2],
                    "height" : [170,180,155,143,154],
                    "type" : ["f","n","n","t","t"]})

# (0부터 세었을 때) 2~3번째 데이터 출력
print("tbl[2:4]\n", tbl[2:4])

# (0부터 세었을 때) 3번째 이후의 데이터 출력하기
print("tbl[3:]\n", tbl[3:])