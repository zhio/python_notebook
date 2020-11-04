# classmethod和staticmethod

python 面向对象编程中,类中定义的方法可以是@staticmethod装饰的静态方法，可以是@classmethod装饰的类方法，还有不带装饰器的实例方法。

## classmethod

带有classmethod装饰器的是类方法，定义操作类的方法，而不是操作实例的方法，类方法的第一个参数是类本身，约定使用`cls`代表当前类。

示例：

```python
class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day=day, month=month, year=year)
        return date1


if __name__ == '__main__':
    date = Date()
    print(date.from_string("11-09-2012").day)  # 11
    print(date.from_string("11-09-2012").month) # 9
    print(date.from_string("11-09-2012").year)  # 2012
```

classmethod使用场景：可以预处理类，重构一个类时，无需更新构造器代码，重写一个classmethod方法，返回所需要的实例。

## staticmethod

带有classmethod装饰器的是静态方法，第一个参数不是特殊的值，参数可有可无，其实和普通函数一样，只是在类中的定义体中。

示例：

```python
class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day=day, month=month, year=year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


if __name__ == '__main__':
    date = Date()
    print(date.from_string("11-09-2012").day)
    print(date.from_string("11-09-2012").month)
    print(date.from_string("11-09-2012").year)
    print(date.is_date_valid("11-09-2012"))  # True
```

## 两者区别

classmethod第一个参数是`cls`代表当前类，staticmethod参数可有可无。