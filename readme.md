# url shortener

#### installation
- clone this repo
- create virtual env
- install requirements:
```bash
pip3 install -r url_shortener/requirements.txt
```
- make sure redis is working on host from [settings.py](https://github.com/annbgn/url_shortener/blob/master/app/app/settings.py#L88)

#### usage
- run locally (if no redis_url is specified, fall back to default local redis url):
```bash
RESIS_URL=some_value python url_shortener/app/app/manage.py runserver
```
- send a request with a url to shorten, get short url in response
```bach
curl -X POST "localhost:8000/get_short" -d '{"url":"http://google.com/"}' -H 'Content-Type: application/json'
```
```bash
{"short_url": "localhost:8000/redirect/75634539-4342-4021-b58d-65dfdced2827"}
```
- you can be redirected to original long url by requesting the short url from response above. note that cache stores key-value pair for 1h and if it's expired, you'll get 410 status code
```bash
curl -X GET "localhost:8000/redirect/75634539-4342-4021-b58d-65dfdced2827" -vvv --location
```
