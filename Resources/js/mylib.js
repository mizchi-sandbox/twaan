updateUserConfig=function(){
    localStorage.id=jQuery("input")[0].value
    localStorage.password=jQuery("input")[1].value
};

jQuery(function() {
    jQuery("#tabs").tabs();
j});

jQuery(document.body).keydown(function(e){
    return changeKeys(e.keyCode,1);
});
jQuery(document.body).keyup(function(e){
    return changeKeys(e.keyCode,0);
});

