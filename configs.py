# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20815140"))
    API_HASH = getenv("API_HASH", "b3f0004748a0b8c269aa5ecf37e5fa69")
    BOT_TOKEN = getenv("BOT_TOKEN", "6564513574:AAGDqUaEmeu0m4DjLDetNc4nooVTWYT7Fzo")
    FSUB = getenv("FSUB", "MovieHouse010")
    CHID = int(getenv("CHID", "-1001841880177"))
    SUDO = list(map(int, getenv("SUDO", "6045592464").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://<OggyBot>:<Oggy>@cluster0.rwohw6y.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
