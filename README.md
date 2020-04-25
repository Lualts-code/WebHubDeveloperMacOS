# WebHubDeveloper
WebHub for developers.

WebHub is a Hub for Webs.

#All commands

from WebHubFolder import WebHubMaker

WebHubMaker.window(title="[title]", height="[height]", width="[width ]")
WebHubMaker.window(title="[title]", height="auto", width="auto")

WebHubMaker.title(text="[text]", font="[font]")

WebHubMaker.text(text="[text]", font="[font]", size="[size]", fg="[fg]", bg="[bg]")

WebHubMaker.link(text="[text]", link="link")

WebHubMaker.dropdown(items="[items]", default="[default]")
dropdown1 = WebHubMaker.dropdown(items="[items]", default="[default]")
dropdown1.get()

WebHubMaker.button(text="[text]", height="[height]", width="width", command="[command]")

WebHubMaker.start()
