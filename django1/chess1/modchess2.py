from django.http import HttpResponse
def displayrows():
    row1="<div class=row2><div class=black2 >&#9820;</div> <div class=white1 >&#9822;</div><div class=black2 >&#9821;</div> <div class=white1>&#9819;</div><div class=black2 >&#9818;</div> <div class=white1 >&#9821;</div><div class=black2 >&#9822;</div> <div class=white1>&#9820;</div></div>"
    row2="<div class=row2><div class=white1 >&#9817;</div><div class=black2 >&#9817;</div> <div class=white1 >&#9817;</div><div class=black2>&#9817;</div> <div class=white1 >&#9817;</div><div class=black2>&#9817;</div> <div class=white1 >&#9817;</div><div class=black2>&#9817;</div> </div>"
    row3="<div class=row2><div class=black2 ></div> <div class=white1 ></div><div class=black2></div> <div class=white1></div><div class=black2 ></div> <div class=white1 ></div><div class=black2></div> <div class=white1></div></div>"
    row4="<div class=row2><div class=black2 ></div> <div class=white1 ></div><div class=black2></div> <div class=white1></div><div class=black2 ></div> <div class=white1 ></div><div class=black2></div> <div class=white1></div></div>"
    row5="<div class=row2><div class=black2 ></div> <div class=white1 ></div><div class=black2></div> <div class=white1></div><div class=black2 ></div> <div class=white1 ></div><div class=black2></div> <div class=white1></div></div>"
    row6="<div class=row2><div class=black2 ></div> <div class=white1 ></div><div class=black2></div> <div class=white1></div><div class=black2 ></div> <div class=white1 ></div><div class=black2></div> <div class=white1></div></div>"
    row7="<div class=row2><div class=black2 >&#9823;</div> <div class=white1>&#9823;</div><div class=black2>&#9823;</div> <div class=white1>&#9823;</div><div class=black2>&#9823;</div> <div class=white1>&#9823;</div><div class=black2>&#9823;</div> <div class=white1>&#9823;</div></div>"
    row8="<div class=row2><div class=white1 >&#9814;</div><div class=black2>&#9816;</div> <div class=white1>&#9815;</div><div class=black2>&#9813;</div> <div class=white1>&#9812;</div><div class=black2>&#9815;</div> <div class=white1>&#9816;</div><div class=black2>&#9814;</div> </div>"
    list1=row1+row2+row3+row4+row5+row6+row7+row8
    return (list1)
    