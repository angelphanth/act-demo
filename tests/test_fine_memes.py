from fine_memes import random_meme, yo


def test_random_meme():
    meme = random_meme(notebook=True)

    assert meme["name"]
    assert meme["url"].startswith("http")


def test_yo():
    url = yo(notebook=True)

    assert (
        url
        == "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzdrNGgzNW9mb2NsaHYwd3FueDNnM2pjYWYzdXNpcWNmOWM2ZXIyYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2UCt7zbmsLoCXybx6t/giphy.gif"
    )
