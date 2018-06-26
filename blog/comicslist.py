from .models import Post

def comicsFill():
    for i in range(30):
        me = User.objects.get(username="patience")
        Post.objects.create(author=me, title="", text="", comic="%d" % i)
