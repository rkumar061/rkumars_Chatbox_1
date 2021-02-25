from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main_index.html')


def chat(request):
    id = (request.POST["name"])
    f = open("demofile2.txt", "a")
    f.write("[")
    f.write(id)
    f.write("]")
    f.write(" joind the chat")
    f.write("\n")
    f.close()
    fid = '(' + id + ')'
    # open and read the file after the appending:
    f = open("demofile2.txt", "r")

    return render(request, 'chat_index.html', {'names': f, 'fi': fid})


def newmsg(request):
    text = (request.POST["text"])
    name = (request.POST["name"])
    f = open("demofile2.txt", "a")
    f.write(name)
    f.write(text)
    f.write("\n")
    f.close()

    # open and read the file after the appending:
    f = open("demofile2.txt", "r")
    return render(request, 'chat_next.html', {'chats': f, 'fi': name} )


def refresh(request):
    # open and read the file after the appending:
    name = (request.POST["name"])
    f = open("demofile2.txt", "r")
    return render(request, 'chat_next.html', {'chats': f, 'fi': name}, )
