from WebHubFolder import WebHubMaker

WebHubMaker.window(title="AllCommands", height="auto", width="auto")
WebHubMaker.title(text="AllCommands", font="helvetica")
WebHubMaker.text(text="from WebHubFolder import WebHubMaker", font="helvetica", size="15", fg="orange", bg="white")
WebHubMaker.text(text="WebHubMaker.window(title=\"[title]\", height=\"[height]\", width=\"[width]\")\nWebHubMaker.window(title=\"[title]\", height=\"auto\", width=\"auto\")", font="helvetica", size="15", fg="red", bg="white")
WebHubMaker.text(text="WebHubMaker.title(text=\"[text]\", font=\"[font]\")", font="helvetica", size="15", fg="orange", bg="white")
WebHubMaker.text(text="WebHubMaker.text(text=\"[text]\", font=\"[font]\", size=\"[size]\", fg=\"[fg]\", bg=\"bg\")", font="helvetica", size="15", fg="red", bg="white")
WebHubMaker.text(text="WebHubMaker.link(text=\"[text]\", link=\"[link]\")", size="15", font="helvetica", fg="orange", bg="white")
WebHubMaker.text(text="WebHubMaker.dropdown(items=\"[items]\", default=\"[default]\")\ndropdown1 = WebHubMaker.dropdown(items=\"[items]\", default=\"[default]\")\ndropdown1.get()", size="15", font="helvetica", fg="red", bg="white")
WebHubMaker.text(text="WebHubMaker.button(text=\"[text]\", height=\"[height]\", width=\"[width]\", command=\"[command]\")", size="15", font="helvetica", fg="orange", bg="white")
WebHubMaker.text(text="WebHubMaker.start()", font="helvetica", size="15", fg="red", bg="white")

WebHubMaker.start()
