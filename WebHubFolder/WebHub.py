from WebHubFolder import WebHubMaker
import os

def go():
    if dropdown.get() != "WebHubDeveloper":
        os.system("python projects/" + dropdown.get() + ".py")
    else:
        os.system("python " + dropdown.get() + ".py")

WebHubMaker.window(title="WebHub", height="100", width="300", bg="white")
WebHubMaker.title(text="Welcome to WebHub", font="helvetica", fg="black", bg="white")
WebHubMaker.text(text="Welcome to WebHub this is the place to go to all\ndifferent webs!", font="helvetica", size="10", fg="black", bg="white")
dropdown = WebHubMaker.dropdown(items=["WebHubDeveloper", "Demo", "AllCommands"], default="Choos a web!", fg="black", bg="white")
WebHubMaker.text(text="", font="helvetica", size="1", fg="white", bg="white")
WebHubMaker.button(text="Go to Web!", height="0", width="0", command=go, fg="black", bg="white")

WebHubMaker.start()
