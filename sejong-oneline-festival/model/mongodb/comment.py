from datetime import datetime
from pymongo import IndexModel, DESCENDING, ASCENDING
from .base import Model
from bson.objectid import ObjectId


class Comment(Model):

    VERSION = 1

    @property
    def index(self) -> list:
        return [
            IndexModel([
                ('content_id', ASCENDING), 
                ('created_at', ASCENDING)
            ])
        ]

    @property
    def schema(self) -> dict:
        return {
            'author_id': None, # 작성자 id
            'author_name': None, # 작성자 이름
            'author_major': None, # 작성자 학과
            'content_id': None, # 연결된 이벤트 id
            'comment': None, # 댓글 내용
            'created_at': datetime.now(),
            '__version__': self.VERSION
        }
    def commit_comment(self,document:dict) -> dict:
        self.col.insert_one(self.schemize(document))

    def get_comment(self,document:str,_skip: int, _limit: int) ->list :
        return list(self.col.find({'content_id':ObjectId(document)})
        .sort([('_id', DESCENDING)])
        .skip(_skip)
        .limit(_limit)
        )

    def upsert_config(self, document: list):
        self.col.drop()
        self.col.insert_many(
            document
        )
    