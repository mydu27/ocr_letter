from sqlalchemy import Column, Integer, String
from app.plugins.private.orm import Common, db


class Ocr(Common, db.Model):
    """Ocr 识别字母记录表"""

    id = Column(Integer, primary_key=True, autoincrement=True, comment='自增id')
    file_path = Column(String(200),
                       nullable=False,
                       index=True,
                       unique=True,
                       comment="图片保存路径")
    file_md5 = Column(String(200),
                      nullable=False,
                      index=True,
                      unique=True,
                      comment="图片计算的md5值")
    result = Column(String(500),
                    nullable=False,
                    index=True,
                    unique=True,
                    comment="识别出来的letter字符串用，隔开")


# class Letters(Base):
#     __tablename__ = "chinese_words"

#     word = Column(String(128), primary_key=True)
#     eng_id = Column(Integer, ForeignKey('words.id'), primary_key=True)
