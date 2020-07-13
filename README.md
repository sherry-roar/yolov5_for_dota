## YOLOv5 for DOTAv1.5 datasets
***
Orginal project site:

1. DOTA dataset:https://captain-whu.github.io/DOTA/dataset.html  
2. YOLOv5:https://github.com/ultralytics/yolov5

### Feature
Training models for detecting ships in aerial images.

This project can extract images containing ships that its gsd
is greater than 0.1 and less than 0.5 in the DOTA dataset,
and crop these aerial images into 800*800 pieces for training.

![avatar](./ship_detection.png)
The recognition effect is as shown above.

### How to train your own model
***
0. install dependencies
```
pip install -U -r requirements.txt
```
1. Put training images into `.\data\src\img`,label txt into `.\data\src\otxt`
2. Run `python caijian.py`
to crop images into pieces
3. Run ```python train_crop.py``` to select images that are ships(or others)
4. Run ```first.py``` and ```voc_label.py``` to Convert dota label format 
to yolo label format
5. Modify configs in `.\data\icon.yaml` and `.\models\yolov5*.yaml`
6. Run to train your own model
```
python train.py --data icon.yaml --cfg  yolov5*.yaml --weights yolov5*.pt --batch-size 16
```
**NOTICE: Remember to modify the path in some files.**

***
### Inference
Run
```
python detect.py --source ./inference/images/ --weights best.pt --conf 0.4
```

### Others
You can also train a models to recognize the rotation of these ships
by using these project below:  
1. R2CNN:https://github.com/yangxue0827/R2CNN_FPN_Tensorflow
![avatar](./2.jpg)
2. YOLT:https://github.com/CosmiQ/yolt
![avatar](./3.png)