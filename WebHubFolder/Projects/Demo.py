from WebHubFolder import WebHubMaker

WebHubMaker.window(title="Demo", height="100", width="225", bg="red")
WebHubMaker.title(text="This is a demo!", font="helvetica", fg="yellow", bg="red")
WebHubMaker.text(text="This size is 15.", font="helvetica", size="15", fg="black", bg="red")
WebHubMaker.link(text="You also can use links!", link="https://google.com", size="12", font="helvetica", bg="red")
WebHubMaker.dropdown(items=["Or", "dropdown", "menu's."], default="Or", fg="yellow", bg="red")

WebHubMaker.start()
