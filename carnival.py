#!/usr/bin/python3

import bottle
from bottle import get, post, put, request
import unicornhat

unicornhat.brightness(0.2)

@get('/brightness')
def get_brightness():
    return "{}\n".format(unicornhat.get_brightness())

@put('/brightness')
def put_brightness():
    r = request.body.read()
    print(">> [{}]".format(r))
    unicornhat.brightness(float(r))
    unicornhat.show()


@put('/off')
def set_off():
    unicornhat.off()
    return "ok"

@put('/test')
def test():
    unicornhat.set_all(0,255,0)
    unicornhat.show()
    return "ok"

@get('/leds')
def get_leds():
    return {'leds': unicornhat.get_pixels()}

def main():
    bottle.run(host='0.0.0.0', port=8082)


if __name__ == '__main__':
    main()
