import logging

from nicegui import app, ui

logging.basicConfig(level=logging.DEBUG)
handler = logging.StreamHandler()
logging.getLogger().addHandler(handler)


@ui.page("/demo")
async def demo():
    logging.debug("Enable pwa mode")
    app.add_static_files("/images", "images")

    ui.add_head_html('<meta name="apple-mobile-web-app-title" content="Beaver">')
    ui.add_head_html('<meta name="apple-mobile-web-app-capable" content="yes">')
    ui.add_head_html(
        '<link rel="apple-touch-icon" href="/images/apple-touch-icon-v4.png">'
    )

    ui.label("Hello NiceGUI!")


ui.run(port=5001, uvicorn_logging_level="info")
