from __future__ import annotations

from aiohttp import web, ClientSession
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.http import KEY_AUTHENTICATED, HomeAssistantView
import logging
_LOGGER = logging.getLogger(__name__)

DOMAIN = "imageproxy"


def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up a skeleton component."""
    hass.http.register_view(imageproxy(config['imageproxy']))

class imageproxy(HomeAssistantView):
    """Camera view to serve an image."""

    url = "/imageproxy/{image}"
    name = "api:imageproxy:image"
    requires_auth = False

    def __init__(self, config: ConfigType) -> None:
        self.config = config

    async def get(self, request: web.Request, image: str) -> web.StreamResponse:

        if not request[KEY_AUTHENTICATED] or request.query.get("token") in self.config.accesstokens:
            raise web.HTTPUnauthorized()

        try:
            async with ClientSession() as session:
                async with session.get(self.config.resources[image]) as resp:
                    return web.Response(body=await resp.content.read(), content_type=resp.content_type)
        except Exception as e:
            _LOGGER.error(e)
            return web.Response(status=500)