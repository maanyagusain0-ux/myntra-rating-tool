import webview

APP_URL = "https://myntra-rating-tool.streamlit.app/"

webview.create_window(
    title="Myntra Product Rating Tool",
    url=APP_URL,
    width=1400,
    height=900,
    min_size=(1000, 700),
    resizable=True
)

webview.start()