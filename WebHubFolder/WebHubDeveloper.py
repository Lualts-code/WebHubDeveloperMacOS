from WebHubFolder import WebHubMaker
import os

def open():
    os.system("python projects/" + str(input1.get()) + ".py")

WebHubMaker.window(title="WebHubDeveloper", width="250", height="50", bg="white")
input1 = WebHubMaker.input(default="Name of your Web.", fg="black", bg="white")
WebHubMaker.button(text="Open", width="0", height="0", command=open, fg="black", bg="white")
WebHubMaker.start()
