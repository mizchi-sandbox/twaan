window.resizeTo(1200,800);
window.moveTo(0,0);

var key=[];
var key_before=[];

//keycode
const KEY_J=74;
const KEY_K=75;
const KEY_R=82;
const KEY_G=71;
const KEY_Q = 81;
const KEY_SPC=32;
const KEY_CMD_L =91;
const KEY_CMD_R =93;
const KEY_SHIFT =16;
const KEY_CTRL=17;

doEvent=function(){
    if(key[KEY_J])window.scrollBy(0,30);
    if(key[KEY_K])window.scrollBy(0,-30);
    if(key_before[KEY_G] && key[KEY_G])window.scrollTo(0,0);
    
    if(key[KEY_G] && key[KEY_SHIFT])
	window.scrollTo(0,10000);
    if(key[KEY_R])update();
    if(key[KEY_Q] && key[KEY_CTRL])
	window.close();

    return false;
}

changeKey=function(kcode,to){
    key[kcode]=to;
    doEvent();
    key_before=key;
}

$(window).keydown(function(e){
    changeKey(e.keyCode,1);
    $("#key_check").text(e.keyCode);
    return false;
});
$(window).keyup(function(e){
    changeKey(e.keyCode,0);
    $("#key_check").text(e.keyCode);
    return false;
});
