# COCO 1500 - Object Detection with YOLOv8

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dSmWj7r-5UMHIlQjy5MuF1gLNP2osBsM?usp=sharing)  
**Reproducible Training Notebook**

**End-to-end object detection project** built as part of my Computer Vision portfolio.

I created a clean **1,500-image subset** from the official COCO 2017 validation set using FiftyOne, imported and reviewed annotations in CVAT, and trained a YOLOv8 model on Google Colab.

---

**End-to-end object detection project** built as part of my Computer Vision portfolio.

I created a clean **1,500-image subset** from the official COCO 2017 validation set using FiftyOne, imported and reviewed annotations in CVAT, and trained a YOLOv8 model on Google Colab.

---

### 📋 Project Overview

- **Dataset**: 1,500 images from COCO 2017 (80 classes)
- **Annotation Tool**: CVAT (pre-annotations + manual review)
- **Model**: YOLOv8n (Ultralytics)
- **Training Platform**: Google Colab (T4 GPU)
- **Epochs**: 30
- **Training Time**: ~30 minutes

---

### 📊 Results

| Metric           | Value     | Notes                     |
|------------------|-----------|---------------------------|
| **mAP50**        | **0.702** | Strong performance        |
| **mAP50-95**     | **0.532** | Good for nano model       |
| **Precision**    | ~0.785    | Final value               |
| **Recall**       | ~0.628    | Final value               |
| **Best Epoch**   | **27**    | Peak mAP performance      |


### 🚀 Quick Start

```bash
git clone https://github.com/yourusername/coco-1500-object-detection-yolov8.git
cd coco-1500-object-detection-yolov8

pip install ultralytics

# Run inference
python inference.py --image test_image.jpg
```

### 📁 Project Structure

```bash
coco-1500-object-detection-yolov8/
├── README.md
├── inference.py
├── data.yaml
├── notebook/
│   └── training_coco1500.ipynb
├── weights/
│   ├── best.pt
│   └── last.pt
├── results/
│   ├── curves/
│   │   ├── BoxF1_curve.png
│   │   ├── BoxPR_curve.png
│   │   ├── BoxP_curve.png
│   │   └── BoxR_curve.png
│   ├── confusion_matrix.png
│   ├── confusion_matrix_normalized.png
│   ├── results.png
│   ├── results.csv
│   ├── args.yaml
│   └── train_batch*.jpg
└── requirements.txt
```

### 🛠️ Tech Stack

Dataset Creation: FiftyOne
Annotation: CVAT
Model: Ultralytics YOLOv8n
Training: Google Colab (T4 GPU)


### 📌 Future Improvements

Train for more epochs (50+)
Experiment with YOLOv8s or YOLOv8m
Add Gradio web demo
Try instance segmentation

### 🧠 Challenges & Solutions

| Challenge                        | Solution |
|----------------------------------|---------|
| Free CVAT tier doesn't allow full dataset export (images + annotations) | Exported annotations only, then manually combined with original images from FiftyOne export |
| Complex folder structure issues when moving between Mac → Colab | Created clean `data.yaml` and fixed paths directly in Colab |
| NMS time limit warnings during validation | Added `conf`, `iou`, and `max_det` parameters to stabilize validation |
| Initial path errors in Colab     | Dynamically updated `data.yaml` paths and restructured folders |
| Authentication issues pushing to GitHub | Used GitHub Personal Access Token for secure pushing |

This project helped me strengthen my debugging and pipeline management skills.

Made with ❤️ for my Computer Vision Portfolio
