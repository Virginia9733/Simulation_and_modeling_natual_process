import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from subprocess import call

img_root = '/Users/virginiali/PycharmProjects/Simulation_and_modeling_natual_process/png/'
out_root = '/Users/virginiali/PycharmProjects/Simulation_and_modeling_natual_process/png/Flow_around_a_cylinder.avi'
fps = 20  # 帧率
size = (640, 480)
fourcc = VideoWriter_fourcc(*"MJPG")  # 支持jpg
videoWriter = cv2.VideoWriter(out_root, fourcc, fps, size)
im_names = os.listdir(img_root)
print(len(im_names))
for im_name in range(len(im_names) - 2):
    string = img_root + 'frame' + str(im_name) + '.png'
    print(string)
    frame = cv2.imread(string)
    frame = cv2.resize(frame, size)  # 注意这里resize大小要和视频的一样
    videoWriter.write(frame)

videoWriter.release()

dir = out_root.strip(".avi")
command = "ffmpeg -i %s.avi %s.mp4" % (dir, dir)  # 使用ffmped将avi压缩为mp4,注意两个的路径
call(command.split())
