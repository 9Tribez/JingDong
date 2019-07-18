class Settings:
    # CAT是请求商品索引页的一个参数的值，同一种类的商品CAT值相同且固定

    # 手机
    # CAT = '9987,653,655'

    # 笔记本电脑
    # CAT = '670,671,672'

    # 二手笔记本电脑
    # CAT = '13765,13769,13770'

    # 数码相机
    CAT = '652,654,831'

    # 索引(表示：前INDEX页商品)
    INDEX = 10

    # 数据库URI
    MONGO_URI = 'mongodb://127.0.0.1:27017'
    # 数据库名称
    MONGO_DB = 'JingDong_Products'
    # 数据库的集合名称
    MONGO_COLLECTIONS = 'cameras'
