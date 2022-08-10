import tornado .web #line:2
import tornado .httpserver #line:3
import tornado .ioloop #line:4
import tornado .websocket as ws #line:5
from tornado .options import define ,options #line:6
import time #line:7
import redis #line:8
import threading #line:9
from threading import Lock ,Thread #line:10
import asyncio #line:11
import os #line:12
define ('port',default =6006 ,help ='port to listen on')#line:14
handles =[]#line:16
class RedisHelper :#line:18
    def __init__ (O0OO0OO0O00O00OOO ):#line:20
        O0OO0OO0O00O00OOO .__O00OOO00OOOOOOO0O =redis .Redis (host ='172.0.0.1')#line:30
        O0OO0OO0O00O00OOO .chan_sub1 ='cutting_running_32_1'#line:34
        O0OO0OO0O00O00OOO .chan_sub2 ='cutting_running_32_2'#line:35
        O0OO0OO0O00O00OOO .chan_pub ='UI_Setting'#line:36
    def public (OO000OO00OO0OO000 ,OOOOOO0O0O0OOOO00 ):#line:38
        OO000OO00OO0OO000 .__O00OOO00OOOOOOO0O .publish (OO000OO00OO0OO000 .chan_pub ,OOOOOO0O0O0OOOO00 )#line:41
        return True #line:42
    def subscribe (O0O00000O0OOOOOO0 ):#line:44
        OOOOO00OOOO0O00O0 =O0O00000O0OOOOOO0 .__O00OOO00OOOOOOO0O .pubsub ()#line:47
        OOOOO00OOOO0O00O0 .subscribe (O0O00000O0OOOOOO0 .chan_sub1 )#line:50
        OOOOO00OOOO0O00O0 .subscribe (O0O00000O0OOOOOO0 .chan_sub2 )#line:51
        OOOOO00OOOO0O00O0 .parse_response ()#line:54
        return OOOOO00OOOO0O00O0 #line:57
ps =RedisHelper ().subscribe ()#line:65
class web_socket_handler (ws .WebSocketHandler ):#line:68
    ""#line:71
    @classmethod #line:72
    def route_urls (OOO00OO000OO00000 ):#line:73
        return [(r'/',OOO00OO000OO00000 ,{}),]#line:74
    def simple_init (OOO000000OOO0OO0O ):#line:76
        OOO000000OOO0OO0O .last =time .time ()#line:77
        OOO000000OOO0OO0O .stop =False #line:78
        handles .append (OOO000000OOO0OO0O )#line:79
    def open (O00OO0O0O0OOO00OO ):#line:81
        ""#line:84
        O00OO0O0O0OOO00OO .simple_init ()#line:85
        print ("New client connected")#line:86
        O00OO0O0O0OOO00OO .write_message ("You are connected")#line:87
    def on_message (O000O00OOOOOO0O0O ,OOO0OO0000O0O000O ):#line:90
        ""#line:93
        print ("received message {}".format (OOO0OO0000O0O000O ))#line:94
        O000O00OOOOOO0O0O .write_message ("You said {}".format (OOO0OO0000O0O000O ))#line:95
        O000O00OOOOOO0O0O .last =time .time ()#line:96
        RedisHelper ().public (OOO0OO0000O0O000O )#line:97
    def on_close (O0O0OOOO00O00OOO0 ):#line:99
        ""#line:102
        print ("connection is closed")#line:103
        handles .remove (O0O0OOOO00O00OOO0 )#line:104
        O0O0OOOO00O00OOO0 .loop .stop ()#line:105
    def check_origin (OOO0OOO00OO0OO000 ,OOO000O000OOO0OOO ):#line:108
def initiate_server ():#line:111
    O0O00000000OOOO0O =tornado .web .Application (web_socket_handler .route_urls ())#line:113
    OO0O00OO000O00OO0 =tornado .httpserver .HTTPServer (O0O00000000OOOO0O )#line:115
    OO0O00OO000O00OO0 .listen (options .port )#line:116
    OO00OOO0OOO000000 =threading .Thread (target =work1 ,daemon =True )#line:117
    OO00OOO0OOO000000 .start ()#line:118
    tornado .ioloop .IOLoop .instance ().start ()#line:120
def work1 ():#line:122
   O000O00O00OO0O0O0 =len (handles )#line:123
   asyncio .set_event_loop (asyncio .new_event_loop ())#line:124
   for OO00O0O0O00O0OO00 in ps .listen ():#line:125
            if OO00O0O0O00O0OO00 ['type']=='message':#line:126
                print (OO00O0O0O00O0OO00 ['data'])#line:127
                for O0OO00O0O0OO0000O in handles :#line:128
                  if (O0OO00O0O0OO0000O ):#line:129
                    O0OO00O0O0OO0000O .write_message ("You said {}".format (OO00O0O0O00O0OO00 ['data']))#line:130
if __name__ =='__main__':#line:134
    initiate_server ()#line:135
