# App

**TODO: Add description**

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `app` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:app, "~> 0.1.0"}
  ]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at [https://hexdocs.pm/app](https://hexdocs.pm/app).

```bash
$ curl -i -H 'X-API-TOKEN: 2231443b8fb511c7b6a0eb25a62577320bac69b6' -H 'X-MARKETPLACE-ID: momox_de' 'https://api.momox.de/api/v4/offer/?ean=9783527507993'
HTTP/2 200
date: Mon, 25 Jan 2021 09:00:36 GMT
content-type: application/json
content-length: 508
set-cookie: __cfduid=d1dc06e528b32b9b90139cc2255b5c88d1611565236; expires=Wed, 24-Feb-21 09:00:36 GMT; path=/; domain=.momox.de; HttpOnly; SameSite=Lax
allow: GET, HEAD, OPTIONS
x-platform: VM
x-frame-options: SAMEORIGIN
vary: Cookie
set-cookie: django_language=de; expires=Tue, 25 Jan 2022 09:00:36 GMT; Max-Age=31536000; Path=/
set-cookie: media_mx_ec=86506410a8cf43adb9d8c00bcc9bca4a; Domain=momox.de; expires=Fri, 24 Jan 2025 09:00:36 GMT; Max-Age=126144000; Path=/; SameSite=Lax
cf-cache-status: DYNAMIC
cf-request-id: 07da5f18d7000006014db95000000001
expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
server: cloudflare
cf-ray: 6170ce07b9ab0601-FRA

{"status":"offer","price":"4.12","reference_price":null,"reference_price_date":null,"currency":"eur","demand_rating":4,"warehouse_status":2,"product":{"ean":"9783527507993","type":"book","title":"Die 5 Dysfunktionen eines Teams","description":"Buch von Lencioni, Patrick M.\n(Gebundene Ausgabe, 1. Auflage, 186 Seiten)\nWiley-VCH Verlag GmbH & Co. KGaA, September 2014","image_url":"https://images.momox.de/media/legacy/9783527507993.jpg","amazon_url":"https://amazon.de/gp/produc

```

```bash
curl -iL 'https://www.medimops.de/produkte-C0/?fcIsSearch=1&searchparam=9783423209694'
```
