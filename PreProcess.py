import os
import random
import shutil
import argparse

def crossVal(img_path, seg_path, folder, val_per):
    for i in range(int(folder)):
        data_path = "./VOC_"+ str(i)
        train_path = os.path.join(data_path, "JPEGImages")
        train_seg_path = os.path.join(data_path, "SegmentationClass")
        if not os.path.isdir(train_path):
            os.makedirs(train_path)
            os.makedirs(train_seg_path)
        val_path = os.path.join(data_path, "val")
        val_seg_path = os.path.join(data_path, "val_seg")
        if not os.path.isdir(val_path):
            os.makedirs(val_path)
            os.makedirs(val_seg_path)
        #val_per = 0.1
        data_list = os.listdir(img_path)
        val_len = int(len(data_list) * val_per)
        val_list = random.sample(data_list, val_len)
        train_list = list(set(data_list) - set(val_list))
        print(val_list)
        print(train_list)
        for train_data in train_list:
            shutil.copy(os.path.join(img_path, train_data), train_path)
            shutil.copy(os.path.join(seg_path, train_data), train_seg_path)
        for val_data in val_list:
            shutil.copy(os.path.join(img_path, val_data), val_path)
            shutil.copy(os.path.join(seg_path, val_data), val_seg_path)
        
        #print(data_path)
        save_path = os.path.join(data_path, "ImageSets/Segmentation")
        #print(save_path)
        if not os.path.isdir(save_path):
            os.makedirs(save_path)
        train_path = data_path + "/JPEGImages"
        val_path = data_path + "/val"

        train_list = os.listdir(train_path)
        val_list = os.listdir(val_path)

        ftrainval = open(os.path.join(save_path,'trainval.txt'), 'w')  
        ftrain = open(os.path.join(save_path,'train.txt'), 'w')  
        fval = open(os.path.join(save_path,'val.txt'), 'w')  

        for train_data in train_list: 
            train_name = train_data.split(".png")[0] + '\n' 
            ftrain.write(train_name)
            ftrainval.write(train_name)  
        for val_data in val_list:
            val_name = val_data.split(".png")[0] + '\n' 
            fval.write(val_name)
            ftrainval.write(val_name)  

        ftrainval.close()  
        ftrain.close()  
        fval.close()

def moveVal(folder):
    for i in range(0, folder):
        img_path = os.path.join("./VOC_" + str(i), "JPEGImages")
        seg_path = os.path.join("./VOC_" + str(i), "SegmentationClass")
        val_path = os.path.join("./VOC_" + str(i), "val")
        val_seg_path = os.path.join("./VOC_" + str(i), "val_seg")
        #os.rename(os.path.join(data_path, "train"), os.path.join(data_path, "JPEGImages"))
        #os.rename(os.path.join(data_path, "train_seg"), os.path.join(data_path, "SegmentationClass"))
        val_list = os.listdir(val_path)
        for val_img in val_list:
            shutil.copy(os.path.join(val_path, val_img), img_path)
            shutil.copy(os.path.join(val_seg_path, val_img), seg_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Preprocess.")
    parser.add_argument("--img_path")
    parser.add_argument("--seg_path")
    parser.add_argument("-folder", default=5, type=int)
    parser.add_argument("-val_per", default=0.2, type = float)
    args = parser.parse_args()

    crossVal(args.img_path, args.seg_path, args.folder, args.val_per)
    moveVal(args.folder)
