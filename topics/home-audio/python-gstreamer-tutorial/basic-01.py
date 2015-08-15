#!/usr/bin/env python

import gi
gi.require_version('Gst', '1.0')
from gi.repository import GObject, Gst

GObject.threads_init()
Gst.init(None)

url = "http://docs.gstreamer.com/media/sintel_trailer-480p.webm"
pipeline = Gst.parse_launch("playbin uri=%s" % url)
   
# Start playing 
pipeline.set_state (Gst.State.PLAYING)
   
# Wait until error or EOS 
bus = pipeline.get_bus()
msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS)
   
# Free resources 
pipeline.set_state(Gst.State.NULL)
