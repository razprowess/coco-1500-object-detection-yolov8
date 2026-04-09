from ultralytics import YOLO
import argparse
from pathlib import Path
import cv2
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="YOLOv8 Inference Script")
    parser.add_argument('--image', type=str, required=True, help='Path to test image')
    parser.add_argument('--model', type=str, default='results/best.pt', 
                       help='Path to trained model')
    parser.add_argument('--conf', type=float, default=0.25, help='Confidence threshold')
    parser.add_argument('--save', action='store_true', help='Save output image')
    
    args = parser.parse_args()

    # Load model
    model = YOLO(args.model)
    
    # Run inference
    results = model(args.image, conf=args.conf, save=args.save)
    
    # Show result
    print(f"✅ Detection completed on: {args.image}")
    print(f"   → Detected {len(results[0].boxes)} objects")
    
    # Optional: Display image with matplotlib
    if args.save:
        output_path = "runs/detect/predict/" + Path(args.image).name
        print(f"   → Output saved to: {output_path}")

if __name__ == "__main__":
    main()
