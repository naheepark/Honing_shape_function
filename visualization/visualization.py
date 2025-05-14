import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import glob

# 한글 폰트 설정
mpl.rc('font', family='Malgun Gothic')
mpl.rcParams['axes.unicode_minus'] = False

# .gen 파일 목록 가져오기
gen_files = glob.glob(r"C:\Users\박나희\Desktop\Honing_shape_function\*.gen")

# 저장할 폴더 경로
save_folder = r"C:\Users\박나희\Desktop\Honing_shape_function\visualization\graph"
os.makedirs(save_folder, exist_ok=True)

for gen_file in gen_files:
    x, y = [], []

    with open(gen_file, "r", encoding="cp949") as f:
        lines = f.readlines()

    data_lines = lines[1:-2]

    for line in data_lines:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        x_val, y_val = map(float, parts)
        x.append(x_val)
        y.append(y_val)

    # 그래프 그리기
    plt.figure()
    plt.plot(x, y, marker='o', linestyle='--', linewidth=0.7, markersize=2)
    plt.xlabel("X 값")
    plt.ylabel("Y 값")
    plt.title(os.path.basename(gen_file))  # 제목은 전체 파일명

    plt.grid(True)

    # 파일명만 추출해서 저장
    filename = os.path.splitext(os.path.basename(gen_file))[0]
    save_path = os.path.join(save_folder, filename + ".png")
    plt.savefig(save_path, dpi=300)
    plt.close()
