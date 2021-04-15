import copy
import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, TIMESTAMP
from contextlib import contextmanager
from libs.error import NotFound


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class Common(object):
    """orm通用操作"""

    create_time = Column(TIMESTAMP, default=datetime.datetime.now)
    status = Column(SmallInteger, default=1)

    _privacy_fields = {'status'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def direct_add_(self):
        """添加事务"""
        db.session.add(self)
        return self

    def direct_commit_(self):
        """提交"""
        self.direct_add_()
        db.session.commit()
        return self

    def direct_update_(self):
        """更新"""
        db.session.commit()
        return self

    def set_attrs(self, attrs_dict):
        """批量更新模型的字段数据
        :param attrs_dict: {field:value}
        :return: self
        """
        for key, value in attrs_dict.items():
            setattr(self, key, value)
        return self

    def to_dict_(self, fields: set = None, funcs: list = None) -> dict:
        """返回字典表数据
        :param funcs: 序列化后需要被调用的函数
        :param fields: 允许被序列化的字段
        :return: dict({'field_name': field_value})
        """
        result = dict()
        if fields is None:
            fields = set(name.name for name in self.__table__._columns)
        for column in fields:
            value = getattr(self, column)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            result[column] = value
        # 通过funcs 添加额外的数据内容
        if funcs:
            for func in funcs:
                func, args, kwargs = func
                getattr(self, func)(result, *args, **kwargs)
        return result

    def serialization(self,
                      increase: set = None,
                      remove: set = None,
                      funcs: list = None) -> dict:
        """序列化指定字段
        :param funcs: 序列化后需要调用的函数名与参数,示例:('func_name', tuple(), dict())
        :param increase: 需要(出增加/显示)的序列化输的字段
        :param remove: 需要(去除/隐藏)的序列化输出的字段
        :return: dict({'field_name': field_value})
        """
        if increase is None:
            increase = set()
        if remove is None:
            remove = set()
        if funcs is None:
            funcs = list()

        fields = copy.copy(self._privacy_fields)  # 拷贝默认隐藏字段,不影响到全局模型的序列化输出
        all_field = set(name.name
                        for name in self.__table__._columns)  # 获得模型所有字段
        fields = fields - increase  # 取消被隐藏的字段
        fields = fields | remove  # 追加需要被隐藏的字段

        all_field = all_field - fields  # 从模型原型所有的可序列化字段中 去除需要被隐藏的字段
        return self.to_dict_(fields=all_field, funcs=funcs)  # 开始序列化
