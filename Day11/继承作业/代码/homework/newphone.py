from homework.oldphone import Oldphone
class Newphone(Oldphone):
    def call(self,number):
        print("语音拨号中...")
        super().call(number)
        print(super().getSign(),"品牌的手机很好用！")
