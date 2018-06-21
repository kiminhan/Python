from PIL import Image
import numpy as np
import os, re
# 파일 경로 지정하기
search_dir = "./image/101_ObjectCategories"
cache_dir = "./image/cache_avhash"

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)

# 이미지 데이터를 Average Hash로 변환하기 ---(*1)
def average_hash(fname, size = 16):
    fname2 = fname[len(search_dir):]

    # 이미지 캐시하기 (오류버젼)
    #cache_file = cache_dir + "/" + fname2.replace('/','_') + ".csv"
    #print(cache_file)
    #if not os.path.exists(cache_file): # 해시 생성하기
    #    img = Image.open(fname)  # 이미지 데이터 열기
    #    img = img.convert('L').resize((size, size), Image.ANTIALIAS)
    #    pixels = np.array(img.getdata()).reshape((size, size))
    #    avg = pixels.mean()
    #    px = 1 * (pixels > avg)
    #    np.savetxt(cache_file, px, fmt = "%.0f", delimiter=",")
    #else: # 캐시돼 있다면 읽지 않기
    #    px = np.loadtxt(cache_file, delimiter=",")
    #return px

    cache_file = cache_dir + fname2.replace('jpg', 'csv')# 기존 코드 의도가 파악되지 않아서 수정. (cache_avhash폴더 안에 물체별 폴더와 이미지파일 명이 문자열로 저장됨.)

    folder_name=fname2[1:].find('/') + 1        # 이미지가 저장된 폴더 이름 저장하기 위한 변수(find 함수로 '/'문자의 위치를 파악)
    if(folder_name==0):                         # '/' 문자가 없으면 Null값을 저장하는데 chair같은 지정된 폴더의 이미지가 아닌 모든 폴더를 찾을 때는 폴더 구분이 \문자가 된다.
        folder_name = fname2[1:].find('\\') + 1 # 이 부분은 fname2에서 이미지가 저장된 폴더 이름을 추출(find 함수로 '/'문자의 위치를 파악)
    folder_name = fname2[:folder_name]          # 폴더명의 길이정보를 가지고 문자열 인덱싱으로 추출

    if not os.path.exists(cache_file):         ## 해시 생성하기 (해당 경로에 파일이 없다면 실행)(존재하면 true 없으면 false 이나, not 이 붙었으니 반대)
        img = Image.open(fname)
        img = img.convert("L").resize((size, size), Image.ANTIALIAS)
        pixels = np.array(img.getdata()).reshape((size, size))
        avg = pixels.mean()
        px = 1 * (pixels > avg)
        if not os.path.exists(cache_dir+folder_name):        # 결과를 저장하는 경로에 폴더가 없는 경우
            print(cache_dir+folder_name)                     # 폴더 경로 확인을 위한 (불필요한)체크
            os.mkdir(cache_dir+folder_name)                  # 폴더 생성
        np.savetxt(cache_file, px, fmt="%.0f", delimiter=",")
    else:                                                  ### 캐시돼 있다면 읽지 않기
        px = np.loadtxt(cache_file, delimiter=",")
    return px

# 해밍 거리 구하기
def hamming_dist(a, b):
    aa = a.reshape(1, -1) # 1차원 배열로 변환하기
    ab = b.reshape(1, -1)
    dist = (aa != ab).sum()
    return dist

# 모든 폴더에 처리 적용하기
def enum_all_files(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            fname = os.path.join(root, f)
            if re.search(r'\.(jpg|jpeg|png)$', fname):
                yield fname

# 이미지 찾기
def find_image(fname, rate):
    src = average_hash(fname)
    for fname in enum_all_files(search_dir):
        dst = average_hash(fname)
        diff_r = hamming_dist(src, dst) / 256
        # print("[check] ",fname)
        if diff_r < rate:
            yield (diff_r, fname)

# 찾기
srcfile = search_dir + "/chair/image_0016.jpg"
html = ""
sim = list(find_image(srcfile, 0.25))
sim = sorted(sim, key=lambda x:x[0])
for r, f in sim:
    print(r, ">", f)
    s = '<div style="float:left;"><h3>[차이:' + str(r) + '-' + \
        os.path.basename(f) + ']</h3>' + '<p><a href="' + f + '"><img src="' + \
        f + '"width=400' + '</a></p></div>'
    html += s

# HTML로 출력하기
html = """<html><head><meta charset="utf8"></head>
<body><h3>원래 이미지</h3><p>
<img src='{0}' width=400></p>{1}
</body></html>""".format(srcfile, html)
with open("./avhash-search-output.html","w", encoding="utf-8") as f:
    f.write(html)
print("ok")