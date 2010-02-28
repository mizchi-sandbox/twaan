#/usr/bin/python
#encoding:utf-8

import twixy
from time import sleep

tw=twixy.Api(
    localStorage.id,
    localStorage.password,
    proxy="http://twixy53.appspot.com/api"
    )


# jQuery(document.body).ready(jQuery("#tabs").tabs())


def PostTwitter(text):
    tw.PostUpdate(test) 

last_id=0
def update():
    tl = tw.GetHomeTimeline(count=150,since_id=last_id)
    twbody = document.getElementById("twitter")

    node=document.createElement("li")
    node.innerHTML=u'<div style="background-color:black;height:1px;">.</div>'
    twbody.insertBefore(node,twbody.firstChild)
        
    for i in tl[::-1]:
        node=document.createElement("li")
        node.setAttribute("class","tw_container")
        node.innerHTML=u'<div class="icon_box"><img class="icon"src="%s"/></div><span class="username">%s</span><span class="text">%s</span>' %(i.user.profile_image_url,i.user.screen_name,i.text)
        
        twbody.insertBefore(node,twbody.firstChild)
        if i.text.find(localStorage.id) >0:
            updateReplies()
            
    global last_id
    last_id=tl[0].id
    
last_id_replies=0
def updateReplies():
    tl = tw.GetReplies(since_id=last_id_replies)
    rep    = document.getElementById("replies")
    for i in tl[::-1]:
        node=document.createElement("li")
        node.setAttribute("class","tw_container")
        node.innerHTML=u'<div class="icon_box"><img class="icon"src="%s"/></div><span class="username">%s</span><span class="text">%s</span>' %(i.user.profile_image_url,i.user.screen_name,i.text)
        rep.insertBefore(node,rep.firstChild)
    global last_id_replies
    last_id_replies=tl[0].id
    return False
    

def startup():
    window.resizeTo(1280,800)
    window.moveTo(0,0)
    update()
    sleep(1);
    updateReplies()
    # setInterval(update,1000*15)
    
kcode={
    "h":72,
    "j":74,
    "k":75,
    "l":76,
    "r":82,
    "g":71,
    "w":87,
    "e":69,
    "o":99,    
    "q":81,    
    "spc":32,    
    "cmd_r":93,    
    "cmd_l":91,    
    "shift":16,    
    "ctrl":17,    
    "1":49,    
    "2":50,    
    "3":51    
    }

k_state=[]
for i in range(200):
    k_state.append(0)
ev_cur=1
def onEvent():
    if k_state[kcode["j"]]:
        scrollBy(0,50)
    if k_state[kcode["k"]]:
        scrollBy(0,-50)
    if k_state[kcode["r"]]:
        update() 
    if k_state[kcode["1"]]:
        ev_cur=1
        jQuery("#t1").click()
    if k_state[kcode["2"]]:
        ev_cur=2
        jQuery("#t2").click()
    if k_state[kcode["3"]]:
        ev_cur=3
        jQuery("#t3").click()
    # if k_state[kcode[H]] and (ev_cur > 1))
    # 	jQuery("#t"+(--ev_cur)).click();
    # if(k_state[kcode[L] && (ev_cur < 3))
    # 	jQuery("#t"+(++ev_cur)).click();
    if k_state[kcode["w"]]:
	jQuery("span.text").css("white-space","nowrap")
    if k_state[kcode["w"]] and k_state[kcode[SHIFT]]:
	jQuery("span.text").css("white-space","normal")


    # if(k_state_before[K_STATE_G] && k_state[K_STATE_G])window.scrollTo(0,0);
    
    # if(k_state[K_STATE_G] && k_state[K_STATE_SHIFT])
    #     window.scrollTo(0,10000);
    # if(k_state[K_STATE_R] && (ev_cur==1))
    #     update();
    # if(k_state[K_STATE_R] && (ev_cur==2))updateReplies();
    if k_state[kcode["q"]] and k_state[kcode["ctrl"]]:
	window.close();

    return False 

def changeKeys(keycode,to):
    global k_state
    k_state[int(keycode)]=to
    onEvent()


# jwindow=jQuery(window).keydown
# def jQuery(window).keydown(e):
#     changeKeys(e.keyCode,1)
#     jQuery("#key_check").text(e.keyCode)
#     return False

# def jQuery(window).keyup(e):
#     changeKeys(e.keyCode,0)
#     jQuery("#key_check").text(e.keyCode)
#     return False


