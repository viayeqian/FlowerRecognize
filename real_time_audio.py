# -*- coding: utf-8 -*-
#实时调用百度语音库，语音录入识别
import speech_recognition as sr
import logging
logging.basicConfig(level=logging.DEBUG)

#while True:
def search():
    
    while True:
        r = sr.Recognizer()
        #麦克风
        mic = sr.Microphone()
        
        logging.info('录音中')
        with mic as source:
            #去噪声
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        
        logging.info('录音结束，识别中.....')
        test = r.recognize_google(audio,language='cmn-Hans-CN',show_all=True)
        if isinstance(test,list):
            print("没有听清哦")
            return ""
        else:
            #查看一下输入的语音是是不是正确
            print(test['alternative'][0]['transcript'])
            return test['alternative'][0]['transcript']
        #print(test)
        logging.info('end')

if __name__ == "__main__":
    search()