from django.db import models

# Create your models here.
"""
1.创建表结构：
    1.1.ORM无法操作到数据库级别的命令，只能操作到数据表，所以第一步需要在数据库中创建表空间
        create database 数据库名称 default charset=utf8; # 防止编码问题，指定为 utf8
        create database mysite default charset=utf8;
    1.2.配置settings文件
        DATABASES = { 
            'default': 
            { 
                'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
                'NAME': 'runoob', # 数据库名称
                'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1 
                'PORT': 3306, # 端口 
                'USER': 'root',  # 数据库用户名
                'PASSWORD': '123456', # 数据库密码
            }  
        }
    1.3.settings同级目录下设置
        # 告诉 Django 使用 pymysql 模块连接 mysql 数据库：
        import pymysql
        pymysql.version_info = (1, 4, 13, "final", 0)
        pymysql.install_as_MySQLdb()
    1.4.定义模型
        1.表定义
            class Test(models.Model):
                name = models.CharField(max_length=20)
        2.创建表
            # python manage.py migrate   # 创建表结构
            # python manage.py makemigrations [app] # 让 Django 知道我们在我们的模型有一些变更
            # python manage.py migrate [app]   # 创建表结构
        3.数据操作
        
"""


# 1.4.1.表定义
class UserInfo(models.Model):
    '''
    create table app_userinfo(
        id int primary key auto_increment,
        name varchar(30),
        password varchar(30),
        hobby varchar(60),
        normal varchar(30),
    )
    #具体查看https://www.cnblogs.com/clschao/articles/10427807.html
    '''
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    hobby = models.CharField(max_length=60)
    normal = models.CharField(max_length=30, default='No')
    roles = models.ManyToManyField(to='Role')

    def __str__(self):
        s = f"Id: {self.id}; Username: {self.username}; Password: {self.password}; Hobby: {self.hobby}; Normal: {self.normal};"
        return s


class Permission(models.Model):
    url = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    menus=models.ForeignKey('Menu',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        s = f"url: {self.url}; title: {self.title};"
        return s

class Menu(models.Model):
    url=models.CharField(max_length=32)
    title=models.CharField(max_length=32)
    def __str__(self):
        s = f"url: {self.url}; title: {self.title};"
        return s

class Role(models.Model):
    name = models.CharField(max_length=12)
    permission = models.ManyToManyField(to='Permission')

    def __str__(self):
        s = f"name: {self.name};"
        return s


# 1.4.2.数据库基本操作:单表操作
class SingleTableManagement():
    def __init__(self):
        pass

    def insert(self, ):
        """
        1.insert
        """

        # 方式1
        test1 = UserInfo(username='feifei', password='gmwang', hobby=['C++'])
        test1.save()
        # 方式2
        # new_obj=UserInfo.objects.create(id=100,username='gmwang',password='gmwnag')
        # 方式3： 批量插入
        users = []
        for i in range(10):
            useri = {'username': 'gmwang_{}'.format(i), 'password': 'gmwang_{}'.format(i), 'hobby': ['C++', 'Python'],
                     'normal': 'yes'}
            users.append(UserInfo(**useri))
        UserInfo.objects.bulk_create(users)

    def select(self, ):
        """
        2.Select
        """
        user_table = UserInfo.objects.all()  # ->选全部

        seleted_rows = UserInfo.objects.filter(id=1)  # ->where
        # seleted_row=UserInfo.objects.get(id=1) #获取一个,不存在会抛出异常
        for rowi in user_table:
            print(rowi)

    def update(self):
        """
        3.update
        """
        # 方式1
        # test2 = UserInfo.objects.get(id=2)
        # test2.username = 'gmwang1'
        # test2.save()
        # 方式2
        UserInfo.objects.filter(id=2).update(username='gmwang1')
        # 方式3
        obj, created = UserInfo.objects.update_or_create(
            username='gmwang9909',  # 查找筛选条件（如果找不到就添加，找到就更新default的内容）
            defaults={"hobby": ['Python']}  # 要修改的值
        )

    def delete(self):
        """
        4.delete
        """
        # 方式1
        # test4 = UserInfo.objects.get(id=100)
        # test4.delete()
        # 方式2
        UserInfo.objects.filter(id=6).delete()

    def other_query(self):
        # 5.一般查询技巧
        # 5.1.exclude -> 排除某些行
        excluded = UserInfo.objects.all().exclude(id=6)  # ->排除id==6的
        # 5.2.values -> 选择特定列
        selected_columns = UserInfo.objects.all().values('id', 'username')  # ->只选取id 和username列
        # 5.3.order_by -> 排序
        ordered_list = UserInfo.objects.all().order_by('id').reverse()
        # 5.4.exists ->查询是否存在
        exists = UserInfo.objects.all().exclude(id=6).exists()
        # 5.5.distinct ->去重
        distinct = UserInfo.objects.all().values('username').distinct()
        print([item['username'] for item in distinct])

        # 6.基于双下划线的模糊查询
        # UserInfo.objects.filter(price__in=[100,200,300]) #price值等于这三个里面的任意一个的对象
        # UserInfo.objects.filter(price__gt=100)  #大于，大于等于是price__gte=100，别写price>100，这种参数不支持
        # UserInfo.objects.filter(price__lt=100)
        # UserInfo.objects.filter(price__range=[100,200])  #sql的between and，大于等于100，小于等于200
        # UserInfo.objects.filter(title__icontains="python") #不区分大小写
        # UserInfo.objects.filter(title__startswith="py") #以什么开头，istartswith  不区分大小写
        # UserInfo.objects.filter(pub_date__year=2012)
        result = UserInfo.objects.filter(username__contains="gmwang")  # title值中包含gmwang的
        print(result)

    def run(self):
        self.insert()
        self.select()
        self.delete()
        self.update()
        self.other_query()


def user_add(username, password, hobby, normal):
    new_user = UserInfo(username=username, password=password, hobby=hobby, normal=normal)
    new_user.save()


def user_login(username, password):
    users = UserInfo.objects.filter(username=username, password=password)
    user=users[0]
    print(user.roles.values("permission__url").distinct())
    return True if users else False


def get(*args, **kwargs):
    user_table = UserInfo.objects.all()
    return user_table


def edit(id, **kwargs):
    UserInfo.objects.filter(id=id).update(**kwargs)
    updated_user = UserInfo.objects.filter(id=id)
    return updated_user[0]


def delete(**kwargs):
    UserInfo.objects.filter(**kwargs).delete()


'''

<1> CharField
        字符串字段, 用于较短的字符串.
        CharField 要求必须有一个参数 maxlength, 用于从数据库层和Django校验层限制该字段所允许的最大字符数.

<2> IntegerField
       #用于保存一个整数.

<3> DecimalField
        一个浮点数. 必须 提供两个参数:

        参数    描述
        max_digits    总位数(不包括小数点和符号)
        decimal_places    小数位数
                举例来说, 要保存最大值为 999 (小数点后保存2位),你要这样定义字段:

                models.DecimalField(..., max_digits=5, decimal_places=2)
                要保存最大值一百万(小数点后保存10位)的话,你要这样定义:

                models.DecimalField(..., max_digits=17, decimal_places=10) #max_digits大于等于17就能存储百万以上的数了
                admin 用一个文本框(<input type="text">)表示该字段保存的数据.

<4> AutoField
        一个 IntegerField, 添加记录时它会自动增长. 你通常不需要直接使用这个字段;
        自定义一个主键：my_id=models.AutoField(primary_key=True)
        如果你不指定主键的话,系统会自动添加一个主键字段到你的 model.

<5> BooleanField
        A true/false field. admin 用 checkbox 来表示此类字段.

<6> TextField
        一个容量很大的文本字段.
        admin 用一个 <textarea> (文本区域)表示该字段数据.(一个多行编辑框).

<7> EmailField
        一个带有检查Email合法性的 CharField,不接受 maxlength 参数.

<8> DateField
        一个日期字段. 共有下列额外的可选参数:
        Argument    描述
        auto_now    当对象被保存时(更新或者添加都行),自动将该字段的值设置为当前时间.通常用于表示 "last-modified" 时间戳.
        auto_now_add    当对象首次被创建时,自动将该字段的值设置为当前时间.通常用于表示对象创建时间.
        （仅仅在admin中有意义...)

<9> DateTimeField
         一个日期时间字段. 类似 DateField 支持同样的附加选项.

<10> ImageField
        类似 FileField, 不过要校验上传对象是否是一个合法图片.#它有两个可选参数:height_field和width_field,
        如果提供这两个参数,则图片将按提供的高度和宽度规格保存.    
<11> FileField
     一个文件上传字段.
     要求一个必须有的参数: upload_to, 一个用于保存上载文件的本地文件系统路径. 这个路径必须包含 strftime #formatting,
     该格式将被上载文件的 date/time
     替换(so that uploaded files don't fill up the given directory).
     admin 用一个<input type="file">部件表示该字段保存的数据(一个文件上传部件) .

     注意：在一个 model 中使用 FileField 或 ImageField 需要以下步骤:
            （1）在你的 settings 文件中, 定义一个完整路径给 MEDIA_ROOT 以便让 Django在此处保存上传文件.
            (出于性能考虑,这些文件并不保存到数据库.) 定义MEDIA_URL 作为该目录的公共 URL. 要确保该目录对
             WEB服务器用户帐号是可写的.
            （2） 在你的 model 中添加 FileField 或 ImageField, 并确保定义了 upload_to 选项,以告诉 Django
             使用 MEDIA_ROOT 的哪个子目录保存上传文件.你的数据库中要保存的只是文件的路径(相对于 MEDIA_ROOT).
             出于习惯你一定很想使用 Django 提供的 get_<#fieldname>_url 函数.举例来说,如果你的 ImageField
             叫作 mug_shot, 你就可以在模板中以 {{ object.#get_mug_shot_url }} 这样的方式得到图像的绝对路径.

<12> URLField
      用于保存 URL. 若 verify_exists 参数为 True (默认), 给定的 URL 会预先检查是否存在( 即URL是否被有效装入且
      没有返回404响应).
      admin 用一个 <input type="text"> 文本框表示该字段保存的数据(一个单行编辑框)

<13> NullBooleanField
       类似 BooleanField, 不过允许 NULL 作为其中一个选项. 推荐使用这个字段而不要用 BooleanField 加 null=True 选项
       admin 用一个选择框 <select> (三个可选择的值: "Unknown", "Yes" 和 "No" ) 来表示这种字段数据.

<14> SlugField
       "Slug" 是一个报纸术语. slug 是某个东西的小小标记(短签), 只包含字母,数字,下划线和连字符.#它们通常用于URLs
       若你使用 Django 开发版本,你可以指定 maxlength. 若 maxlength 未指定, Django 会使用默认长度: 50.  #在
       以前的 Django 版本,没有任何办法改变50 这个长度.
       这暗示了 db_index=True.
       它接受一个额外的参数: prepopulate_from, which is a list of fields from which to auto-#populate
       the slug, via JavaScript,in the object's admin form: models.SlugField
       (prepopulate_from=("pre_name", "name"))prepopulate_from 不接受 DateTimeFields.

<13> XMLField
        一个校验值是否为合法XML的 TextField,必须提供参数: schema_path, 它是一个用来校验文本的 RelaxNG schema #的文件系统路径.

<14> FilePathField
        可选项目为某个特定目录下的文件名. 支持三个特殊的参数, 其中第一个是必须提供的.
        参数    描述
        path    必需参数. 一个目录的绝对文件系统路径. FilePathField 据此得到可选项目.
        Example: "/home/images".
        match    可选参数. 一个正则表达式, 作为一个字符串, FilePathField 将使用它过滤文件名. 
        注意这个正则表达式只会应用到 base filename 而不是
        路径全名. Example: "foo.*\.txt^", 将匹配文件 foo23.txt 却不匹配 bar.txt 或 foo23.gif.
        recursive可选参数.要么 True 要么 False. 默认值是 False. 是否包括 path 下面的全部子目录.
        这三个参数可以同时使用.
        match 仅应用于 base filename, 而不是路径全名. 那么,这个例子:
        FilePathField(path="/home/images", match="foo.*", recursive=True)
        ...会匹配 /home/images/foo.gif 而不匹配 /home/images/foo/bar.gif

<15> IPAddressField
        一个字符串形式的 IP 地址, (i.e. "24.124.1.30").
<16> CommaSeparatedIntegerField
        用于存放逗号分隔的整数值. 类似 CharField, 必须要有maxlength参数.



'''
"""
(1)null
 
如果为True，Django 将用NULL 来在数据库中存储空值。 默认值是 False.
 
(1)blank
 
如果为True，该字段允许不填。默认为False。
要注意，这与 null 不同。null纯粹是数据库范畴的，而 blank 是数据验证范畴的。
如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的。
 
(2)default
 
字段的默认值。可以是一个值或者可调用对象。如果可调用 ，每有新对象被创建它都会被调用，如果你的字段没有设置可以为空，那么将来如果我们后添加一个字段，这个字段就要给一个default值
 
(3)primary_key
 
如果为True，那么这个字段就是模型的主键。如果你没有指定任何一个字段的primary_key=True，
Django 就会自动添加一个IntegerField字段做为主键，所以除非你想覆盖默认的主键行为，
否则没必要设置任何一个字段的primary_key=True。
 
(4)unique
 
如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
 
(5)choices
由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，<br>而且这个选择框的选项就是choices 中的选项。
(6)db_index
　　如果db_index=True 则代表着为此字段设置数据库索引。


DatetimeField、DateField、TimeField这个三个时间字段，都可以设置如下属性。

(7)auto_now_add
    配置auto_now_add=True，创建数据记录的时候会把当前时间添加到数据库。

(8)auto_now
    配置上auto_now=True，每次更新数据记录的时候会更新该字段，标识这条记录最后一次的修改时间。
"""
