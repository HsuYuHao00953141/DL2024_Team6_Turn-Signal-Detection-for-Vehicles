import cv2

def get_images_from_video(video_name, time_F, video_images):
    #video_images = []
    vc = cv2.VideoCapture(video_name)
    c = 1
    
    if vc.isOpened(): #判斷是否開啟影片
        rval, video_frame = vc.read()
    else:
        rval = False

    while rval:   #擷取視頻至結束
        rval, video_frame = vc.read()
        if(c % time_F == 0): #每隔幾幀進行擷取
            video_images.append(video_frame)
        c = c + 1
    vc.release()
    
    return video_images

time_F = 2 #time_F越小，取樣張數越多
#video_name = 'D:/download/20220126_墾丁出水口右側/GoPro 8 Black/GHAL0507.avi' #影片名稱
video_list = ["D:\\UnderWater_data\\GHCD0710\\GHCD0710_new.mp4"]

video_images = []
for video_name in video_list:
    video_images = get_images_from_video(video_name, time_F, video_images) #讀取影片並轉成圖片
    n = 1
    for i in range(0, len(video_images)): #顯示出所有擷取之圖片
        cv2.imwrite('D:\\UnderWater_data\\GHCD0710\\GHCD0710_images\\GHCN0710_%d.jpg'%(i+n), video_images[i])
        print(i+n)

#cv2.destroyAllWindows()