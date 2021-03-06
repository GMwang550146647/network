"""

1.工厂模式：
    1.定义接口来创建对象，但是工厂不负责创建对象，而是由子类完成
    2.Factory方法的创建是通过继承，而不是实例化完成
    3.设计具有定制性，可以返回相同的实例或者子类，而不是某种类型的对象
2.类别：
    1.简单工厂模式
        特点
            工厂创建不同类型的对象，而不是直接将对象实例化
    2.工厂方法模式
        特点
            允许接口创建对象，但用哪个类创建对象，由子类决定
        优点
            灵活性大，代码通用，不是单纯实例化某个类，而是根据接口
            松耦合，创建对象和使用对象的代码分开，客户端不需要关系传递什么参数，和实例化什么类，降低维护成本
    3.抽象工厂模式
        特点
            创建一系列相关的对象，无需指定/公开其具体类接口，该模式提供其他工厂的对象，在内部创建其他对象
            相当于 嵌套版本的工厂方法模式！
"""