import os, sys, pygst
pygst.require('0.10')
import gst, gobject
gobject.threads_init()

def get_peaks(filename):
    global do_run

    pipeline_txt = (
        'filesrc location="%s" ! decodebin ! audioconvert ! '
        'audio/x-raw-int,channels=1,rate=44100,endianness=1234,'
        'width=32,depth=32,signed=(bool)True !'
        'level name=level interval=1000000000 !'
        'fakesink' % filename)
    pipeline = gst.parse_launch(pipeline_txt)

    level = pipeline.get_by_name('level')
    bus = pipeline.get_bus()
    bus.add_signal_watch()

    peaks = []
    do_run = True

    def show_peak(bus, message):
        global do_run
        if message.type == gst.MESSAGE_EOS:
            pipeline.set_state(gst.STATE_NULL)
            do_run = False
            return
        # filter only on level messages
        if message.src is not level or \
           not message.structure.has_key('peak'):
            return
        peaks.append(message.structure['peak'][0])

    # connect the callback
    bus.connect('message', show_peak)

    # run the pipeline until we got eos
    pipeline.set_state(gst.STATE_PLAYING)
    ctx = gobject.gobject.main_context_default()
    while ctx and do_run:
        ctx.iteration()

    return peaks

def normalize(peaks):
    _min = min(peaks)
    _max = max(peaks)
    d = _max - _min
    return [(x - _min) / d for x in peaks]

if __name__ == '__main__':
    filename = os.path.realpath(sys.argv[1])
    peaks = get_peaks(filename)

    print 'Sample is %d seconds' % len(peaks)
    print 'Minimum is', min(peaks)
    print 'Maximum is', max(peaks)

    peaks = normalize(peaks)
    print peaks
