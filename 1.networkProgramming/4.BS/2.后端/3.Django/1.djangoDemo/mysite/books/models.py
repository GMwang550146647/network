from django.db import models

"""
多对一：ForeignKey  ：外键约束
一对一：OneToOneField ：外键约束加上unique约束
多对多：ManyToManyField： 添加一个表，创建两个id的对应关系
"""


# 比较常用的信息放到这个表里面
class Author(models.Model):
    """
    1.Author 和 AuthorDetail 是一对一关系
    """

    # 默认会创建 id列
    # nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # 与AuthorDetail建立一对一的关系，一对一的这个关系字段写在两个表的任意一个表里面都可以
    # 就是foreignkey+unique，只不过不需要我们自己来写参数了，并且orm会自动帮你给这个字段名字拼上一个_id，数据库中字段名称为authorDetail_id
    # authorDetail = models.OneToOneField(to="AuthorDetail", to_field="nid", on_delete=models.CASCADE)
    # 默认对应AuthorDetail 的id字段，然后on_delete=models.CASCADE
    authorDetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)

    def __str__(self):
        return f"id: {self.id} || name: {self.name} ||  age: {self.age} ||  authorDetail_id: {self.authorDetail_id}"


# 不常用的放到这个表里面
class AuthorDetail(models.Model):
    # 默认会创建 id列
    # nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)

    def __str__(self):
        return f"id: {self.id} || birthday: {self.birthday} ||  telephone : {self.telephone} ||  addr : {self.addr}|| "


class Publish(models.Model):
    """
    2.Publish 和 Book 是一对多关系
    """
    # 默认会创建 id列
    # nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return f"id: {self.id} || name: {self.name} ||  city: {self.city} ||  email: {self.email}"


class Book(models.Model):
    """
    3.Book 和 Author 是多对多
    """
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)  # (在多的一方设置这个属性列)
    # 1.多对多 方式1：自动生成多对多表
    # authors = models.ManyToManyField(to='Author')
    # """authors=models.ManyToManyField(to='Author') 会自动创建以下表"""
    # 自动生成的第三张表我们是没有办法添加其他字段的
    # class Book_Author(models.Model):
    #     book_id=models.ForeignKey(to='Book')
    #     author_id=models.ForeignKey(to='Author')
    # 2. 多对多 方式2：自定义生成多对多表(可以自定义表其他列)
    author = models.ManyToManyField(to='Author', through='Book_Author', through_fields=("book", "author"))

    # through_fields接受一个2元组（'field1'，'field2'）：
    # 其中field1是定义ManyToManyField的模型外键的名（author），field2是关联目标模型（book）的外键名。
    def __str__(self):
        return f"id: {self.id} || title : {self.title} ||  publishDate: {self.publishDate}||  price : {self.price} ||  publish_id: {self.publish_id}"


class Book_Author(models.Model):
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    info = models.CharField(max_length=100)

    class Meta:
        unique_together = ('author', 'book')

    def __str__(self):
        return f"id: {self.id} || book_id: {self.book_id} ||  author_id: {self.author_id} ||  info: {self.info}"
