from db.models import Tweet
from db.database import db_session
from datetime import datetime

t1 = Tweet(name="さぼてん", content="今日はいい天気！", position_x='12.3', position_y='12.3', created_at=datetime(2020 , 1 , 1 , 12 , 30 , 20))
t2 = Tweet(name="ほりしょー", content="jackの活動日です！", position_x='1.3', position_y='2.3', created_at=datetime(2020 , 1 , 1 , 13 , 30 , 20))
t3 = Tweet(name="きゃん", content="課題に追われてる。。。", position_x='11.3', position_y='9.3', created_at=datetime(2020 , 1 , 1 , 14 , 30 , 20))
t4 = Tweet(name="てっぴー", content="軽音行ってくる", position_x='4.3', position_y='7.3', created_at=datetime(2020 , 1 , 1 , 15 , 30 , 20))
t5 = Tweet(name="赤い色素", content="テスト多すぎるよ〜〜", position_x='10.3', position_y='1.6', created_at=datetime(2020 , 1 , 1 , 16 , 30 , 20))
t6 = Tweet(name="ずおちゃん", content="部活で疲れた〜", position_x='3.3', position_y='5.3', created_at=datetime(2020 , 1 , 1 , 17 , 30 , 20))

db_session.add(t1)
db_session.add(t2)
db_session.add(t3)
db_session.add(t4)
db_session.add(t5)
db_session.add(t6)
db_session.commit()