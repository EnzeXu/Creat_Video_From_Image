import os
import cv2
from tqdm import tqdm


def creat_video_from_images(input_dir, output_path, fig_size, fps=5):
    file_dir = input_dir
    file_names = os.listdir(file_dir)
    file_names = [item for item in file_names if ".png" in item and "sw" not in item]
    file_names.sort()
    print("{} files: {}".format(len(file_names), file_names))
    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MJPG'), fps, fig_size)
    # video = cv2.VideoWriter('outputs/test.mp4', fourcc, 5, (16000, 4800))
    for i in tqdm(range(len(file_names))):
        img = cv2.imread('{}/{}'.format(file_dir, file_names[i]))
        img = cv2.resize(img, fig_size)
        video.write(img)
    video.release()


if __name__ == "__main__":
    creat_video_from_images("data/ModelBYCC_Cluster_origin_id=11_2022-09-11-01-33-58", "outputs/test.avi", (16000, 4800))
    pass
