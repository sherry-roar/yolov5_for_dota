from PIL import Image
import matplotlib.pyplot as plt
import os

if __name__=='__main__':
    merge_path = r'E:\shiyan\yolov5-master\data\test1\src\images'  # 要合并的小图片所在的文件夹
    org_path = r'E:\shiyan\yolov5-master\data\test1\caijian_src\images'
    for ii in os.listdir(org_path):
        imgg=Image.open(os.path.join(org_path,ii))
        result = Image.new(imgg.mode, imgg.size)
        result.paste(imgg, box=(0, 0))
        for img in os.listdir(merge_path):
            if img[0]==ii[0]:
                imgs=Image.open(os.path.join(merge_path,img))
                cols=int(img.split("_")[-1].split('.')[0])
                rows=int(img.split("_")[-2])
                result.paste(imgs, box=(cols, rows))
        # img1 = Image.open(os.path.join(merge_path,'1_0_0.png'))
        # img2 = Image.open(os.path.join(merge_path,'1_0_800.png'))
        # img3 = Image.open(os.path.join(merge_path, '1_0_848.png'))
        # result = Image.new(img1.mode, (1000 * 2, 1000))
        # result.paste(img1, box=(0, 100))
        # result.paste(img2, box=(800, 0))
        # result.paste(img3, box=(848, 0))
        # result.paste(imgg, box=(3875, 5502))
        result.save(os.path.join(merge_path,ii))
        plt.imshow(result)
        plt.show()


