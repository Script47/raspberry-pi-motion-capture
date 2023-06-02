import os

import dotenv


# load env vars, validate, and set defaults
def load_dotenv():
    dotenv.load_dotenv()

    if os.getenv("CAPTURE_TYPE") not in [""]:
        os.putenv("CAPTURE_TYPE", "image")
