from homework.oldphone import Oldphone
from homework.newphone import Newphone
phone1 = Oldphone()
phone2 = Newphone()
print("旧手机：")
phone1.call(1234556)
print("")
phone2.setSign("oppo")
print("新手机：")
phone2.call(1234124)