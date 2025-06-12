# 🧰 工具程式說明 (`tool_code/`)

本資料夾包含輔助本專案資料處理與標註轉換所需的自製工具腳本，適用於監視器影像切割、標籤轉換與清洗等前處理流程。

---

## 📄 工具腳本列表

| 檔名 | 功能說明 |
|------|----------|
| `get_images_from_video.py` | 從監視器影片中擷取畫面，轉為圖片序列（切片影像） |
| `json_to_txt.py` | 將 LabelMe 格式的 JSON 標註轉為 YOLO 格式的 TXT 標註 |
| `change_labelme_lebel.py` | 更改 LabelMe 標註中的標籤名稱（label name 替換） |
| `change_txt_label.py` | 直接批次修改 YOLO TXT 標註檔中的類別 ID 或名稱 |
| `find_error_txt_label.py` | 檢查 YOLO 標註 TXT 是否存在錯誤格式或類別值超出範圍 |
| `img_label.py` | 繪製圖片上的標註框（根據 YOLO 標註檔繪圖） |
| `tool.py` | 綜合工具腳本，可整合執行多項前處理步驟 |


