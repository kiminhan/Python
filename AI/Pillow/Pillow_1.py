from PIL import Image
import numpy as np

# 이미지 데이터를 Average Hash로 변환하기
def average_hash(fname, size = 16):
    img = Image.open(fname) # 이미지 데이터 열기
    img = img.convert('L') # 그레이스케일로 변환하기
    img = img.resize((size, size), Image.ANTIALIAS)

# 리사이즈하기
    pixel_data = img.getdata() # 픽셀 데이터 가져오기
    pixels = np.array(pixel_data) # Numpy 배열로 변환하기
    pixels = pixels.reshape((size, size)) # 2차원 배열로 변환하기
    avg = pixels.mean() # 평균 구하기
    diff = 1 * (pixels > avg) # 평균보다 크면 1, 작으면 0으로 변환하기
    return diff

def np2hash(ahash):
    bhash = []
    for nl in ahash.tolist():
        s1 = [str(i) for i in nl]
        s2 = "".join(s1)    # 리스트(s1)을 문자열로 변환
        i= int(s2, 2)   # 이진수를 정수로 변환
        bhash.append("%04x" % i) # 출력양식(4칸 맞춤 (꽉 차지 않은 경우 0으로 채움), 16진수)
        return "".join(bhash)

    # Average Hash 출력하기

# ahash = average_hash("background.jpg")
ahash = average_hash("light.jpg")
print(ahash)
print(np2hash(ahash))