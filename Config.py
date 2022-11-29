import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "8192152"))
    API_HASH = os.environ.get("API_HASH", "2931e14598cd0f0763236bc84ee4bd6d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5097632527:AAGGPLeEE7v7rt3wyLfeqKm0_kac_EU0eMc")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBuwcNZfSIZtHcovJztCRqeZViFKB0oiRMLg0ZE9q3y2TtlBdoyUQB0FjB9_QOhawU9qdI4LHFYLL_39CYceLKGr7F0n2mL-iXiPLoZAryhfqJh3azXfBWcsSWLf9XH3cxW9QiWTzaokEaIl8Pj8i3apfCwzyAhSqwX5yTNJCmKT5v7VyTGL0kyyXTYqonpK4YCu07d8WwHf20XR1IusaRpoGQ70a8WZRL-mDfZ-r1w42Z_fWYurJ1yiJxydt15HSYmrNXgpcsu1weqpLkPMAWi4_f1jEaFjO_xeulML0ft9BqoWyLXnuE4Qu5W6WDnu52UbEDTK3pHm30qpM9Mr-FyYw=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Myselfmusicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5101751343")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
