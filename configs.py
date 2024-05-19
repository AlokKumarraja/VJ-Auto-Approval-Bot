# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27505575"))
    API_HASH = getenv("API_HASH", "03bbc5e15dbddfb03fb953435b5eb028
    ")
    BOT_TOKEN = getenv("BOT_TOKEN", "7057278544:AAF9ucctewpepKskpJ5HFUAebi5bNeTTIRU")
    FSUB = getenv("FSUB", "VJ_Botz")
    CHID = int(getenv("CHID", "-1001623633000"))
    SUDO = list(map(int, getenv("SUDO", "6168162777").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://animebhau60:F66EK72xqzfumHR7@cluster0.mgupyii.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
