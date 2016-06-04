import json
from browser.html import *
from browser import document, window
from browser.ajax import ajax
from browser.websocket import WebSocket


restaurant_list = document['restaurant-list']


def main():
    ws = WebSocket('ws://' + window.location.host + '/status/')
    ws.bind('open', on_open)
    ws.bind('message', on_message)

def on_open(evt):
    print('Starting...')
    request = ajax()
    request.open('GET', '/start/', True)
    request.send()

def on_message(evt):
    obj = json.loads(evt.data)
    if obj.get('type') == 'console':
        print(obj['value'])
    else:
        # print(obj['name'])
        li = LI()
        url = obj.get('url')
        if not url:
            try:
                url = obj['menu']['url']
            except KeyError:
                pass
        if url:
            li <= A(obj['name'], href=url)
        else:
            li <= B(obj['name'])
        li <= DIV(obj['location']['address'])
        categories = (c['shortName'] for c in obj['categories'])
        li <= DIV('Category: ' + ', '.join(categories))
        li <= DIV('Rating: %s' % obj['rating'])
        restaurant_list <= li


main()
