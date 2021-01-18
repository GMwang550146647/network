from django.db import models
import random
from django.db.models import Avg, Max, Min, Sum, Count

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
    # related_name就是隐藏的名字，反向查询的时候用！
    authorDetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE, related_name='author')

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
    comments = models.IntegerField(default=1)
    good = models.IntegerField(default=1)
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
        return f"id: {self.id} || title : {self.title} ||  publishDate: {self.publishDate}|| good: {self.good}|| comments: {self.comments}|| price : {self.price} ||  publish_id: {self.publish_id}"


class Book_Author(models.Model):
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    info = models.CharField(max_length=100)

    class Meta:
        unique_together = ('author', 'book')

    def __str__(self):
        return f"id: {self.id} || book_id: {self.book_id} ||  author_id: {self.author_id} ||  info: {self.info}"


class MultiTableManagement():
    def __init__(self, no=0):
        self.no = no

    def insert(self):
        '''1.一对一'''
        authors = []
        books = []

        for i in range(2):
            # 方式1: 指定对象
            new_ad = AuthorDetail.objects.create(birthday='2020-11-01', telephone=f'32904802{i}', addr=f'地球{i}')
            a1 = Author.objects.create(name=f'gmwang_{i}{self.no}', age=40 + i, authorDetail=new_ad)
            # 方式2: 指定id
            new_ad = AuthorDetail.objects.create(birthday='2020-11-02', telephone='32904999238', addr=f'月球{i}')
            a2 = Author.objects.create(name=f'feifei_{i}{self.no}', age=18 + i, authorDetail_id=new_ad.id, )
            authors.extend([a1, a2])

        '''2.多对一'''
        publisher = ['醒目猪出版社', 'feifei出版社']
        for i, publisher_i in enumerate(publisher):
            new_p = Publish.objects.create(name=publisher_i, city=f'广东_{i}', email=f'{publisher_i}@edu.com', )
            # 方式1 ： 指定对象
            b1 = Book.objects.create(title=f'好书_{i}{self.no}', publishDate='2010-10-11', price=98, publish=new_p)
            # 方式2 :  指定id   指向跟方式1同样的new_publish对象
            b2 = Book.objects.create(title=f'坏书_{i}{self.no}', publishDate='2010-10-03', price=98,
                                     publish_id=new_p.id, )
            books.extend([b1, b2])

        '''3.多对多'''
        # 方式1： 指定id->通过表格对象
        mapper = [(random.randint(0, len(authors) - 1), random.randint(0, len(books) - 1)) for i in range(5)]
        mapper = list(set(mapper))
        mapper_list = [[f'info_{i}'] + list(item) for i, item in enumerate(mapper)]
        mapper_dict = [{'author_id': authors[i[1]].id, 'book_id': books[i[2]].id, 'info': i[0]} for i in mapper_list]
        for info_i in mapper_dict:
            Book_Author.objects.create(**info_i)

        # 方式2： 指定对象->通过表格对象 ->重复添加会报unique error
        # mapper_dict = [{'author': authors[i[1]], 'book': books[i[2]], 'info': i[0]} for i in mapper_list]
        # for info_i in mapper_dict:
        #     Book_Author.objects.create(**info_i)

        # 方式3： 指定id->不通过表格对象，从book_obj入手(重复加入无效，但是不报错)
        # book_obj = Book.objects.get(id=1)
        book_obj = Book.objects.filter(id=1).first()
        book_obj.author.add(*[item.id for item in authors])
        # 由于author 里面没有book 对象，所以不能从author_obj入手！
        # author_obj=Author.objects.get(id=1)
        # author_obj.book.add(*[1,2])

        # 方式4： 指定对象->不通过表格对象 ->重复添加"不"会报unique error
        book_obj = Book.objects.get(id=1)
        book_obj = Book.objects.filter(id=1).first()
        book_obj.author.add(*authors)

    def select_nested_query(self):
        '''正向查询与反向查询'''
        # 当前类有foreign key的，查改foreignkey 就是正向，反之就是反向
        '''1.基于对象的跨表查询： 子查询'''
        # 1. 一对一（由于一对一的表格两个表都会有对方的外键，所以两个表都能直接调用对方）
        # 正向 : 查看Author 对应的 AuthorDetail 的某个内容(例如id)
        author_obj = Author.objects.filter(name='gmwang', ).first()
        author_detail_id = author_obj.authorDetail_id  # 这里其实是连表查询(定义类的时候有这个，所有直接index)
        print(f'author_obj:{author_obj}')
        print(f'author_detail:{author_obj.authorDetail}')
        # 反向 : 根据查出来的id 通过AuthorDetail 把 对应的Author查出来
        author_detail_obj = AuthorDetail.objects.filter(id=author_detail_id).first()
        target = author_detail_obj.author
        print(f'target:{target}')

        # 2.多对一（由于多对一表，只有创建外键表才有对方的外键，所以只能单向访问，反向就要遍历filter）
        # 正向
        book_obj = Book.objects.filter(title='好睇嘅书').first()
        publish_id = book_obj.publish_id
        print(f'book_obj:{book_obj}')
        print(f"book_publish:{book_obj.publish}")
        # 反向
        publish_obj = Publish.objects.filter(id=publish_id).first()
        books = Book.objects.filter(publish_id=publish_obj.id)
        print(f'target1:{books}')
        books = publish_obj.book_set.all()  # 这个能直接提取素有的book
        print(f'target2:{books}')

        # 3.多对多
        # 正向
        book_obj = Book.objects.get(title='唔好睇嘅书')
        print(book_obj.author.all())
        # 反向 -> 反向要加个set
        author_obj = Author.objects.get(name='gmwanggmwang')
        print(author_obj.book_set.all())

    def select_join_query(self):
        '''2.基于双下划线的跨表查询： 连表join'''
        # 1. 一对一（由于一对一的表格两个表都会有对方的外键，所以两个表都能直接调用对方）
        # 正向 : 通过 "当前表属性名__外键表属性名" 进行values,filter访问其属性
        combined_obj = Author.objects.filter(authorDetail__telephone='18312030404', ) \
            .values('name', 'authorDetail__telephone').first()
        print(f'combined_obj:{combined_obj}')
        # 反向 : 可以通过"当前表属性名__外键表属性名"直接进行filter和values
        combined_obj = AuthorDetail.objects.filter(author__name='gmwang').values('author__name', 'telephone').first()
        print(f'combined_obj:{combined_obj}')

        # 2.多对一（由于多对一表，只有创建外键表才有对方的外键，所以只能单向访问，反向就要遍历filter）
        # 正向
        combined_obj = Book.objects.filter(publish__name='傻猪出版社').values("title", "publish__name")
        print(f'combined_obj:{combined_obj}')
        # 反向
        combined_obj = Publish.objects.filter(book__title='唔好睇嘅书').values("book__title", 'name')
        print(f'combined_obj:{combined_obj}')

        # 3.多对多
        # 正向
        combined_obj = Book.objects.filter(author__name='gmwang').values('author__name', 'title')
        print(combined_obj)
        # 反向 -> 反向要加个set
        combined_obj = Author.objects.filter(book__title='唔好睇嘅书').values('name', 'book__title')
        print(combined_obj)

        # 多表
        obj = Book.objects.filter(publish__name='咧猪猪出版社', author__name='gmwang').values('title', 'publish__name',
                                                                                        'author__name')
        print(obj)

    def agg_query(self):
        # 1.聚合
        price = Book.objects.aggregate(avg=Avg('price'), max=Max('price'), min=Min('price'))
        print(price)
        # 2.分组
        # 2.1.根据本表字段进行分组聚合(不指定values就默认用id分组)
        grouped = Book.objects.values('publish_id').annotate(avg=Avg('price'))
        print(grouped)
        # 2.2.根据外键字段进行分组聚合
        grouped = Publish.objects.annotate(avg=Avg('book__price')).values('id', 'avg')
        print(grouped)

    def F_query(self):
        from django.db.models import F
        # 1.计算两属性列之间的计算大小关系
        objs = Book.objects.filter(comments__gt=F('good'))
        print(objs)
        # 2.更新（自加）
        Book.objects.filter(id=5).update(comments=F('comments') + 100)

    def Q_query(self):
        from django.db.models import Q
        # 1.由于filter都是进行AND操作的，如果要进行OR操作可以用Q查询
        bookList = Book.objects.filter(Q(author__name="gmwang") | Q(author__name="feifei"))
        # 2.更复杂的多层嵌套
        bookList = Book.objects.filter(Q(author__name="yuan") & ~Q(publishDate__year=2017)).values_list("title")
        # 可以进行Q嵌套，多层Q嵌套等，其实工作中比较常用
        bookList = Book.objects.filter(
            Q(Q(author__name="yuan") & ~Q(publishDate__year=2017)) & Q(id__gt=6)).values_list("title")
        # 3.注意q查询必须在前面  （也是and的关系，但是Q必须写在前面)
        bookList = Book.objects.filter(Q(publishDate__year=2016) | Q(publishDate__year=2017), title__icontains="python")

    def raw_query(self):
        # 1.ORM自带的
        ret = Book.objects.raw('select * from books_book where comments > %s', params=[10, ])
        print(ret)
        for result_i in ret:
            print(result_i)
        # 2.连接数据库
        from django.db import connection, connections
        cursor = connection.cursor()  # cursor = connections['default'].cursor()
        cursor.execute('select * from books_book where comments > %s', params=[10, ])
        for result_i in cursor.fetchall():
            print(result_i)

    def update(self):
        """1.一对一，多对一 一样"""
        Author.objects.filter(id=2).update(
            name='gmwanggmwang',
            age='1000',
            authorDetail=AuthorDetail.objects.create(birthday='1001-01-01', addr='gz', telephone='19242380')
        )
        """2.多对多"""
        book_obj = Book.objects.get(id=2)
        book_obj.author.set(['1', '2'])  # 删除所有,然后重新设定为 1，2

    def delete(self):
        '''1.一对一 以及 一对多：表A关联表B,删除表A不影响表B，删除表B会级联删除A中的记录（如果设置了级联CASCADE'''
        # Author.objects.get(id=10).delete()  #->不会影响AuthorDetail
        # AuthorDetail.objects.get(id=10).delete()  #-> 同时删除Author中的对应记录

        '''2.多对多删除   -> 多次删除没关系，不报错，查不到就不删除'''
        book_obj = Book.objects.get(id=1)
        book_obj.author.remove(*[61, 62])  # 清除特定的id
        # book_obj.author.clear()          #删除所有
        # book_obj.author.set(['1','2'])          #删除所有,然后重新设定为 1，2

    def run(self):
        # self.insert()
        # self.select_nested_query()
        # self.select_join_query()
        self.agg_query()
        self.Q_query()
        self.F_query()
        self.raw_query()
        # self.update()
        # self.delete()
