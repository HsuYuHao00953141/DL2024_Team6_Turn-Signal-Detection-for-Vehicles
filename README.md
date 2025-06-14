# 🚗 Turn Signal Detection for Vehicles  
深度學習概論｜第六組 專題成果  

## 📌 專案簡介
本專案旨在偵測「轉彎車輛是否有打方向燈」，結合監視器影像與深度學習模型，協助實現智慧交通執法系統。模型可判斷車輛是否打開左轉燈、右轉燈，或未使用方向燈，並能應用於多種車輛類型辨識，作為交通違規判定的依據。

## 🎯 專案目標
- 偵測轉彎車輛方向燈狀態：左轉、右轉、未打燈  
- 應對多樣車種，增強模型泛化能力  
- 可佈署於實際監視影像應用場景中  

---

## 📁 專案結構說明

| 資料夾/檔案 | 說明 |
|-------------|------|
| [`YOLOv7_training_result`](./YOLOv7_training_result) | 使用 YOLOv7 模型的訓練結果、模型參數與輸出檔案 |
| [`YOLOv12_training_result`](./YOLOv12_training_result) | 使用 YOLOv12 模型的訓練記錄、圖表與最終模型 |
| [`tool_code`](./tool_code) | 影像切割、標註轉換與預處理等自訂工具程式 |
| [`Dataset`](./Dataset) | 資料集說明與標註策略（原始圖片未包含於本專案） |

---

## 🧾 資料集介紹

- **來源**：來自嘉義市實際路口（林森東路、民族路、民生南路）之監視器畫面（CCTV）  
- **處理流程**：透過 YOLO 偵測後切片成靜態圖，並手動標記方向燈狀態  
- **標註方式**：
  - **大框 (Case1)**：涵蓋整台車輛（含輪胎與燈號），提升判斷準確率  
  - **小框 (Case2)**：僅針對燈號位置，結果不穩定，已棄用  
- **最終標籤類別**：左轉、右轉、未打燈（三類）
- **label class**: "turn_right = 0"、"trurn_left = 1"、"turn_without_light = 2"

---

## 🔗 YOLO 原始碼來源

本專案使用以下開源 YOLO 模型進行訓練與測試：

- [YOLOv12 - by sunsmarterjie](https://github.com/sunsmarterjie/yolov12)  
- [YOLOv7 - by WongKinYiu](https://github.com/WongKinYiu/yolov7)

感謝原始開發者提供高效的物件偵測框架，使本專題得以順利實作與推進。

---

## 🧪 模型實驗與比較

| 模型版本 | Backbone | Optimizer | Epochs | mAP@0.5:0.95 |
|----------|----------|-----------|--------|--------------|
| YOLOv7-tiny | YOLOv7 | SGD | 50 | 中等表現 |
| YOLOv12n   | YOLOv12 | SGD | 50 | 表現最佳 ✅ |

- YOLOv12 表現略優於 YOLOv7，故作為最終部署版本  
- 水平翻轉資料增強已關閉，保留影像方向資訊以提升方向燈判別準確率  

---

## 📈 模型成效與貢獻

- **準確率**：
  - 普通轎車方向燈辨識達 **90%** 準確率  
  - 特殊車種辨識約 **20%**，有待樣本增強
- **質化貢獻**：
  - 可辨識左右方向燈與無打燈狀態
  - 已具備一定泛化能力，可應用於不同時段與路況
- **未來展望**：
  - 擴增貨車與特殊車種樣本
  - 強化夜間/雨天等環境影像資料
  - 透過影像前處理提升泛化性

---

## 📸 測試成果展示

- 正確辨識案例：
  - ✅ 無打燈車輛辨識  
    <img src="./YOLOv12_detect_result/turn-left-without-light1.gif" width="300"/>  
    <img src="./YOLOv12_detect_result/turn-left-without-light2.gif" width="300"/>

  - ✅ 左右打燈車輛辨識  
    <img src="./YOLOv12_detect_result/turn-left-with-light.gif" width="300"/>  
    <img src="./YOLOv12_detect_result/turn-right-with-light.gif" width="300"/>

- 錯誤案例：
  - ❌ 特殊車種誤判方向燈  
    <img src="./YOLOv12_detect_result/error-detect1.gif" width="300"/>  
    <img src="./YOLOv12_detect_result/error-detect2.gif" width="300"/>  
    <img src="./YOLOv12_detect_result/error-detect3.gif" width="300"/>

---

## 🛠 技術細節

- 框架：PyTorch, YOLOv7/YOLOv12
- 開發工具：Google Colab, Python
- 模型部署：透過 `.pt` 權重檔進行推論，可配合 OpenCV 或 Flask API 擴展應用

---

## 👨‍💻 團隊成員
第六組｜許育豪、余謝宗倫、鄭朝元、林群振、黃冠彰、黃鼎鈞

---

如需更多資料與模型分析，請參閱各子資料夾內的訓練報告 (`*.pdf`)。
