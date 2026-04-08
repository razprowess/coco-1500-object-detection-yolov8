# COCO 1500 - Object Detection with YOLOv8

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
text├── notebook/              # Google Colab training notebook
├── results/               # Training graphs + best.pt
├── inference.py           # Inference script
├── data.yaml
└── README.md

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


Made with ❤️ for my Computer Vision Portfolio
