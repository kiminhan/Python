# if = 상수,변수,조건식 - 평가 후에 - True, False
# if 후에 and, or로 조건을 늘릴 수 있다. 자주 사용

if 1: # 참과 거짓으로 나누기 때문에 성립 (0이 아닌 숫자는 참)
    print("OK")
if "hello": # 같은 이유에서
    print("OK")

if '': # 아무것도 없을때는 거짓이기 때문에 프린트는 안함 하지만 에러는 x
    print("OK")
if 0: # 같은 이유에서
    print("OK")

if None: # 같은 이유에서 (거짓)
    print("OK")
