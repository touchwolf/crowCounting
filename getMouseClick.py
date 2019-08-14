import cv2

def click_save(img_name, lst_name):
    img = cv2.imread(img_name)
    shape = img.shape[:2]
    lst_name = lst_name
    mlist = []
    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x,y)
            print(xy)
            cv2.circle(img, (x,y), 5, (0,0,255), thickness=-1)
            # cv2.putText(img, xy, (x,y), cv2.FONT_HERSHEY_PLAIN,
            #             1.0, (0,0,0), thickness=1)
            cv2.imshow("image", img)
            mlist.append(xy)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)
    print(shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    with open(lst_name, 'w') as fin:
        fin.write(str(shape)+'\n')
        #fin.write(str(mlist))
        for i in range(len(mlist)):
            fin.write(mlist[i]+'\n')
if __name__ == '__main__':
    click_save('C:/Users/sh/Desktop/_models/IMG_1123.jpg', 'C:/Users/sh/Desktop/_models/IMG_1123.lst')