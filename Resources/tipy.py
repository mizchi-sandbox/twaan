#/usr/bin/python
#encoding:utf-8

import simplejson
import twixy
from time import sleep

tw=twixy.Api(
    "your_id",
    "your_password"
    )
interval=60
last_id=0
def update():
    tl = tw.GetHomeTimeline(count=150,since_id=last_id)
    twbody=document.getElementById("twitter")
        
    for i in tl:
        node=document.createElement("li")
        node.setAttribute("class","tw_container")
        node.innerHTML=u'<div class="icon_box"><img class="icon"src="%s"/></div><div class="mes_box"><a name="%s"/><span class="username">%s</span><span class="text">%s</span></div>' %(i.user.profile_image_url,i.id,i.user.screen_name,i.text)
        twbody.insertBefore(node,twbody.firstChild)
        
    global last_id
    last_id=tl[0].id


def startup():
    update()
    window.resizeTo(1200,800)
    window.moveTo(0,0)
    setInterval(update,1000*interval)
