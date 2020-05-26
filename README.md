# Versions

OS: MacOS
Python: 3.8
WebHubMaker: 1.0

# All the commands

from WebHubFolder import WebHubMaker

WebHubMaker.window(title="[title]", height="[height]", width="[width]", bg="[bg]")
WebHubMaker.window(title="[title]", height="auto", width="auto", bg="[bg]")

WebHubMaker.title(text="[text]", font="[font]", fg="[fg]", bg="[bg]")

WebHubMaker.text(text="[text]", font="[font]", size="[size]", fg="[fg]", bg="[bg]")

WebHubMaker.link(text="[text]", link="link", bg="[bg]")

WebHubMaker.dropdown(items="[items]", default="[default]", fg="[fg]", bg="[bg]")
dropdown1 = WebHubMaker.dropdown(items="[items]", default="[default]", fg="[fg]", bg="[bg]")
dropdown1.get()

WebHubMaker.button(text="[text]", height="[height]", width="width", command="[command]", fg="[fg]", bg="[bg]")

WebHubMaker.input(default="[default]", fg="[fg]", bg="[bg]")
input1 = WebHubMaker.input(default="[default]", fg="[fg]", bg="[bg]")
input1.get()

WebHubMaker.start()
