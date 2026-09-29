from fine_memes import random_meme


def test_random_meme():
    meme = random_meme(notebook=True)

    assert meme["name"]
    assert meme["url"].startswith("http")
