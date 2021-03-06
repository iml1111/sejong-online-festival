from datetime import datetime

EXHIBITIONS = [
    {
        "name": "늘혬코러스",
        "banner_photo": "/uploads/늘혬코러스_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "중앙밴드동아리",
        "type": "video_youtube",
        "post": "2020 늘혬코러스 / 세종대학교 'Hi-Light' 온택트 축제",
        "contents": ["https://www.youtube.com/watch?v=N6JZefArSkI"],
        "created_at": datetime.now(),
        "__version__": 2,
    },
    {
        "name": "The BLACK",
        "banner_photo": "/uploads/더블랙_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "The BLACK",
        "type": "gallery_grid",
        "post": "음악을 즐길 수 있는 동아리원 상시 모집. 페메주세요!",
        "contents": ["더블랙%s.png" % str(i) for i in range(1, 9)],
        "created_at": datetime.now(),
        "__version__": 2,
    },
    {
        "name": "세종극회",
        "banner_photo": "/uploads/세종극회_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "세종극회",
        "type": "gallery_normal",
        "post": "",
        "contents": ["극회%s.png" % str(i) for i in range(1, 5)],
        "created_at": datetime.now(),
        "__version__": 2,
    },
    {
        "name": "BAMBOO",
        "banner_photo": "/uploads/bamboo_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "BAMBOO",
        "type": "gallery_normal",
        "post": "",
        "contents": [],
        "created_at": datetime.now(),
        "__version__": 1,
    },
    {
        "name": "한울림",
        "banner_photo": "/uploads/한울림_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "한울림",
        "type": "gallery_grid",
        "post": "",
        "contents": [],
        "created_at": datetime.now(),
        "__version__": 1,
    },
    {
        "name": "디자인 이노베이션 전시회",
        "banner_photo": "/uploads/디자인_이노베이션_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "이노베이션",
        "type": "video_youtube",
        "post": "",
        "contents": [],
        "created_at": datetime.now(),
        "__version__": 1,
    },
    {
        "name": "소리더하기",
        "banner_photo": "/uploads/소리더하기_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "소리더하기",
        "type": "video_youtube",
        "post": "",
        "contents": [],
        "created_at": datetime.now(),
        "__version__": 1,
    },
    {
        "name": "OVERFLOW",
        "banner_photo": "/uploads/overflow_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "소리더하기",
        "type": "gallery_grid",
        "post": "",
        "contents": [],
        "created_at": datetime.now(),
        "__version__": 1,
    },
    {
        "name": "친환경 챌린지 EX",
        "banner_photo": "/uploads/지도제보챌린지_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "지도제보챌린지",
        "type": "gallery_normal",
        "post": "",
        "contents": [],
        "created_at": datetime.now(),
        "__version__": 1,
    },
    {
        "name": "아이코리아",
        "banner_photo": "/uploads/아이코리아_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "아이코리아",
        "type": "gallery_normal",
        "post": "",
        "contents": [],
        "created_at": datetime.now(),
        "__version__": 1,
    },
    {
        "name": "인터페이스",
        "banner_photo": "/uploads/인터페이스_배너.png",
        "owner_id": "exhibition_admin",
        "owner_name": "컴퓨터 학술 동아리",
        "type": "video_youtube",
        "post": "",
        "contents": [],
        "created_at": datetime.now(),
        "__version__": 1,
    },
]