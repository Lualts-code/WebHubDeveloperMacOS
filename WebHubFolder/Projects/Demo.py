from WebHubFolder import WebHubMaker

WebHubMaker.window(title="Demo", height="100", width="225")
WebHubMaker.title(text="This is a demo!", font="helvetica")
WebHubMaker.text(text="This size is 15.", font="helvetica", size="15", fg="black", bg="white")
WebHubMaker.link(text="You also can use links!", link="https://google.com", size="12", font="helvetica")
WebHubMaker.dropdown(items=["Or", "dropdown", "menu's."], default="Or")

WebHubMaker.start()
