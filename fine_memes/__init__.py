import random
from importlib import metadata
from io import BytesIO

import httpx
from IPython.display import display
from PIL import Image

__version__ = metadata.version("fine_memes")


def yo(notebook=False):
    url = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzdrNGgzNW9mb2NsaHYwd3FueDNnM2pjYWYzdXNpcWNmOWM2ZXIyYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2UCt7zbmsLoCXybx6t/giphy.gif"
    response = httpx.get(url)
    img = Image.open(BytesIO(response.content))
    if notebook:
        display(img)
    else:
        img.show()
    return url


def random_meme(notebook=False):
    response = httpx.get("https://api.imgflip.com/get_memes")
    response.raise_for_status()

    result = response.json()
    memes = result["data"]["memes"]

    random_int = random.randint(0, len(memes) - 1)
    corresponding_meme = memes[random_int]

    meme_response = httpx.get(corresponding_meme["url"])

    img = Image.open(BytesIO(meme_response.content))

    if notebook:
        display(img)
    else:
        img.show()

    return corresponding_meme
