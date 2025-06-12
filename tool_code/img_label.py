import os
import shutil

# ==== 手動設定路徑與起始編號 ====
image_folder = '/home/hsu/Desktop/DL/dataset_unorder/img'
label_folder = '/home/hsu/Desktop/DL/dataset_unorder/label'
output_image_folder = '/home/hsu/Desktop/DL/dataset/img'
output_label_folder = '/home/hsu/Desktop/DL/dataset/labels'
start_index = 1  # <<< 從這個數字開始命名

# 建立輸出資料夾
os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_label_folder, exist_ok=True)

# 取得所有圖片檔，僅保留有對應 label 的
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
image_files.sort()
valid_pairs = []

for img_file in image_files:
    name, ext = os.path.splitext(img_file)
    label_path = os.path.join(label_folder, name + '.txt')
    if os.path.exists(label_path):
        valid_pairs.append((img_file, name + '.txt'))

# 開始重新命名並輸出
for i, (img_file, lbl_file) in enumerate(valid_pairs):
    new_index = start_index + i
    new_image_name = f"{new_index}.jpg"
    new_label_name = f"{new_index}.txt"

    # 複製圖片
    shutil.copyfile(os.path.join(image_folder, img_file), os.path.join(output_image_folder, new_image_name))

    # 複製 label
    shutil.copyfile(os.path.join(label_folder, lbl_file), os.path.join(output_label_folder, new_label_name))

print(f"✅ 已重新命名並輸出 {len(valid_pairs)} 對 img + label，從 {start_index} 開始到 {start_index + len(valid_pairs) - 1}")
