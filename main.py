import logging

from fastapi import FastAPI
from nicegui import app, ui

logging.basicConfig(level=logging.DEBUG)
handler = logging.StreamHandler()
logging.getLogger().addHandler(handler)


@ui.page("/demo")
async def demo():
    logging.debug("Enable pwa mode")
    app.add_static_files("/images", "images")

    ui.add_head_html(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">'
    )
    ui.add_head_html('<meta name="apple-mobile-web-app-title" content="Beaver">')
    ui.add_head_html('<meta name="apple-mobile-web-app-capable" content="yes">')
    ui.add_head_html(
        '<meta name="apple-mobile-web-app-status-bar-style" content="black">'
    )
    ui.add_head_html('<meta name="theme-color" content="#121212">')

    # viewBox="90 90 220 220"
    ui.add_head_html(
        '<link rel="apple-touch-icon" href="/images/apple-touch-icon-v4.png">'
    )

    ui.label("Hello NiceGUI!")


fastapi_app = FastAPI()
ui.run_with(fastapi_app)
