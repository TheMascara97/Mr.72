import pyautogui,cv2,time,easyocr,ddddocr

def now_ui():
    if photo_compare(780,430,340,130,'./login.png') ==1:
        return 0
    else:
        return 1
def login_click():
    ui_click(920,605)
    time.sleep(3)
    ui_click(920,605)
    pyautogui.write('admin',interval=0.25)
    ui_click(960,690)
    time.sleep(3)
    ui_click(80,200)
    time.sleep(1)
    ui_click(80,950)
    time.sleep(1)
    ui_click(80,750)
    time.sleep(3)
    ui_click(987,213)
    time.sleep(2)
def ui_click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.leftClick()
def upload(now_version):
    if now_version==1:
        version_file='D:\ota\high\ota.swu'
    else:
        version_file='D:\ota\low\ota.swu'
    pyautogui.write(version_file,interval=0.25)
    pyautogui.press('enter')
def photo_compare(x=0,y=0,i=0,j=0,compare_file='./version_h.png'):
    screenshot = pyautogui.screenshot(region=(x,y,i,j),imageFilename='./now_ph.png')
    image1 = cv2.imread('./now_ph.png')
    image2 = cv2.imread(compare_file)
    hist_img1 = cv2.calcHist([image1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    hist_img1[255, 255, 255] = 0 #ignore all white pixels
    cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_img2 = cv2.calcHist([image2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    hist_img2[255, 255, 255] = 0  #ignore all white pixels
    cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    # Find the metric value
    metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
    # print(round(metric_val, 2))
    return int(round(metric_val, 2))
def version_compare():
    screenshot = pyautogui.screenshot(region=(310,310,200,30),imageFilename='./now_ph.png')
    # 创建EasyOCR Reader
    ocr = ddddocr.DdddOcr(beta=True)
    with open("./now_ph.png", 'rb') as f:
        image = f.read()
    text = ocr.classification(image)
    print(text)
    return text
def error_ph(num):
    # screenshot = pyautogui.screenshot(region=(310,310,200,30),imageFilename='./第{}次版本错误.png'.format(num))   #版本号截图
    screenshot = pyautogui.screenshot(region=(0,0,1920,1080),imageFilename='./第{}次版本错误.png'.format(num))
    
if __name__=='__main__':
    ver_num=0
    hight ='1O2'
    low = '1o1'
    for i in range(1,1001):
        print('------------------------------------第{}次测试------------------------------------------'.format(i))
        if i ==1:
            login_click()
        ui_click(987,213)
        version = version_compare()
        if hight in version:
            ver_num=0
            print('高-->低')
        elif version=='':
            if now_ui()==0:
                print('识别到了登录页面，重新进入并跳过该次测试')
                login_click()
                continue
            else:
                print('未知问题,升级失败')
                error_ph(i)
                break
        else:
            ver_num=1
            print('低-->高')
        ui_click(600,440)
        time.sleep(3)
        upload(ver_num)
        time.sleep(5)
        ui_click(700,440)
        time.sleep(2)
        ui_click(1120,620)
        time.sleep(10)
        if photo_compare(800,570,300,40,'./upgradesing.png')>0.9:
            print('开始升级')
        else:
            if now_ui()==0:
                print('识别到自动退出到了登录页面，跳过本次测试')
                login_click()
                continue
            else:
                print('未知问题,升级失败')
                error_ph(i)
                break
        for j in range(20):
            if j == 10:
                ui_click(920,605)
                pyautogui.hotkey('f5')
                time.sleep(10)
            if photo_compare(780,430,340,130,'./login.png')>0.9:
                print('识别到登录界面')
                login_click()
                break
            time.sleep(30)
        #790 490    1140  650    upgradesing
        version = version_compare()
        if ver_num==0:
            if low in version:
                print('高-->低升级成功')
            else:
                error_ph(i)
                print('高-->低升级失败')
        elif version =='':
            if now_ui()==0:
                print('识别到了登录页面，重新进入检测测试结果')
                login_click()
                if ver_num==0:
                    if low in version_compare():
                        print('高-->低升级成功')
                    else:
                        error_ph(i)
                        print('高-->低升级失败')
                else:
                    if hight in version_compare():
                        print('低-->高升级成功')
                    else:
                        error_ph(i)
                        print('低-->高升级失败')
            else:
                print('未知问题,升级失败')
                error_ph(i)
                break
        else:
            if hight in version:
                print('低-->高升级成功')
            else:
                error_ph(i)
                print('低-->高升级失败')
