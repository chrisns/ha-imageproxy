# Simple image proxy custom component for home assistant

Will probably do more than just images

## Installation

add this repo into your `custom_components`

add to your `configuration.yaml` something like

```yaml
imageproxy:
  resources:
    google: https://www.google.com/logos/doodles/2021/seasonal-holidays-2021-6753651837109324.3-ladc.gif
    googleagain: https://www.google.com/logos/doodles/2021/seasonal-holidays-2021-6753651837109324.3-ladc.gif
  accesstokens:
    - bez!tvq9wdw5WZV8mny
    - trw7czy_dhf.yub8XTP
```

restart home assistant

You should now be able to navigate to

- http://localhost:8123/imageproxy/google?token=bez!tvq9wdw5WZV8mny
- http://localhost:8123/imageproxy/googleagain?token=bez!tvq9wdw5WZV8mny

and see the image proxied via home assistant

This is really handy if you use nabu casa or other means to expose your home assitant outside of your network