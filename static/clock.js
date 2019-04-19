function getClock()
{
    var d=new Date();
    var s=d.getSeconds();
    var m=d.getMinutes();
    var h=d.getHours();
    if (s<10) {s="0" + s}
    if (m<10) {m="0" + m}
    document.getElementById("clock").innerHTML= "<b> " + h + ":" + m + ":" + s + "</b> "
    setTimeout("getClock()",1000);
}
getClock();
