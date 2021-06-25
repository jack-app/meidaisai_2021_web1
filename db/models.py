from sqlalchemy import Column, Integer, String, Text, DateTime, desc
from sqlalchemy.ext.hybrid import hybrid_property
from db.database import Base, db_session
from datetime import datetime

class Tweet(Base):
    '''
    ~~~ 使い方 ~~~
    1. まずはこのライブラリをインポート
        # main.py
        from db.models import Tweet
    2. Tweet全部取得したい時
        Tweet.all() # 配列で得られる。
    3. Tweet作成したい時（データを保存したい時）
        t = Tweet(name='名前', content='内容', position_x='座標X', position_y='座標Y') # インスタンス化
        t.save() # 保存
    
    ~~~ 各属性たち ~~~
    tweet.name            # (String型)   投稿者の名前
    tweet.content         # (String型)   投稿内容
    tweet.position_x      # (String型)   座標X
    tweet.position_y      # (String型)   座標Y
    tweet.created_at      # (datetime型) 投稿時刻
    tweet.created_at_text # (String型)   投稿時刻
    '''

    __tablename__ = 'tweets' 
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    content = Column(Text)
    position_x = Column(String(128))
    position_y = Column(String(128))
    created_at = Column(DateTime)

    def __init__(self, name=None, content=None, position_x = None, position_y = None, created_at=None):
        self.name = name
        self.content = content
        self.created_at = created_at
        self.position_x = position_x
        self.position_y = position_y
        self.created_at = datetime.now()
    def __repr__(self):
        return '<Tweet { id = %r, name = %r, content = %r, created_at = %r}>' % (self.id, self.name, self.content, self.created_at)
    
    @classmethod
    def all(cls):
        return db_session.query(cls).order_by(desc(cls.created_at)).all()
    
    @classmethod
    def get_positions(cls):
        return db_session.query(cls.position_x, cls.position_y).all()

    def save(self):
        db_session.add(self)
        db_session.commit()
        return True

    @hybrid_property
    def created_at_text(self):
        return self.created_at.strftime("%Y/%m/%d %H:%M:%S")