"""
抽象类： 规定了一系列的方法，并规定了必须由继承类实现的方法。由于有抽象方法的存在，
		所以抽象类不能实例化。可以将抽象类理解为毛坯房，门窗，墙面的样式由你自己来定，
		所以抽象类与作为基类的普通类的区别在于约束性更强
接口类：与抽象类很相似，表现在接口中定义的方法，必须由引用类实现，但他与抽象类的根本区别在于用途：
		与不同个体间沟通的规则，你要进宿舍需要有钥匙，这个钥匙就是你与宿舍的接口，
		你的舍友也有这个接口，所以他也能进入宿舍，你用手机通话，那么手机就是你与他人交流的接口

区别于关联:
	接口是抽象类的变体，接口中所有的方法都是抽象的，而抽象类中可以有非抽象方法，
	抽象类是声明方法的存在而不去实现它的类

	接口定义方法，没有实现的代码，而抽象类可以实现部分方法

	接口中基本数据类型为static而抽象类不是
"""
import abc #利用abc模块实现抽象类


class All_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass

# class Txt(All_file):
#     pass
#
# t1=Txt() #报错,子类没有定义抽象方法



class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

class Sata(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')


wenbenwenjian=Txt()

yingpanwenjian=Sata()

jinchengwenjian=Process()

#这样大家都是被归一化了,也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()

print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)



# 做出一个良好的抽象
class Payment(object):
    #规定了一个兼容接口
    def pay(self):
        pass

#微信支付
class WeChatPay(object):
    def pay(self,money):
        print('微信支付了%s'%money)

#支付宝支付
class AliPay(object):
    def pay(self,money):
        print('支付宝支付了%s'%money)

#苹果支付
class ApplePay(object):
    def pay(self,money):
        print('苹果支付了%s'%money)


def pay(obj,money):
    obj.pay(money)

weixin = WeChatPay()
alipay = AliPay()
applepay = ApplePay()

#调用者无需关心具体实现细节，可以一视同仁的处理实现了特定接口的所有对象
pay(weixin,100)
pay(alipay,200)
pay(applepay,300)