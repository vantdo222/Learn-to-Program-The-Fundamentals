import tkinter
import a1
import time
import math

def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    
    return time_2-time_1


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    
    return (time_2-time_1)/3600


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    
    return hours+(minutes/60)+(seconds/3600)


def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24



### Write your get_hours function definition here:

def get_hours(seconds):
    """ (int) -> int

    Return the number of hours that have elapsed since midnight, as seen on a 24-hour clock
 
    >>> get_hours (3800)
    1
    >>> get_hours (8000)
    2
    """
    return to_24_hour_clock(seconds//3600)

### Write your get_minutes function definition here:

def get_minutes(seconds):
    """ (int) -> int

    Return the number of minutes that have elapsed since midnight as seen on a clock
    
    >>> get_minutes(3800)
    3
    >>> get_minutes (8000)
    13
    """

    return (seconds//60 - get_hours(seconds)*60)%60

### Write your get_seconds function definition here:

def get_seconds(seconds):
    """ (int) -> int

    Return the number of hours in the specified number of seconds.
    
    >>> get_seconds(3800)
    20
    >>> get_seconds(8000)
    20
    """
    
    return (seconds - get_minutes(seconds)*60 - get_hours(seconds)*3600)


def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    
    return to_24_hour_clock(time-utc_offset)


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """

    return to_24_hour_clock(time+utc_offset)


# The list of expected functions in a student submission.
EXPECTED_FNS = ['hours_difference',
                'to_float_hours',
                'get_hours',
                'get_minutes',
                'get_seconds',
                'time_to_utc',
                'time_from_utc']


# Make fake empty functions for ones that students haven't written yet.
for f in EXPECTED_FNS:
    if not hasattr(a1, f):
        print(f, "is missing in a1.py.")
        a1.__dict__[f] = lambda *x: 0


# The list of the world's time zones.
REAL_ZONES = [
    'local', 'UTC-12.0',  'UTC-11.0',  'UTC-10.0',  'UTC-9.5',  'UTC-9.0',
    'UTC-8.0',  'UTC-7.0',  'UTC-6.0',  'UTC-5.0',  'UTC-4.5',  'UTC-4.0',
    'UTC-3.5',  'UTC-3.0',  'UTC-2.0',  'UTC-1.0',  'UTC+0.0',  'UTC+1.0',
    'UTC+2.0',  'UTC+3.0',  'UTC+3.5',  'UTC+4.0',  'UTC+4.5',  'UTC+5.0',
    'UTC+5.5',  'UTC+5.75',  'UTC+6.0',  'UTC+6.5',  'UTC+7.0',  'UTC+8.0',
    'UTC+8.75',  'UTC+9.0',  'UTC+9.5',  'UTC+10.0',  'UTC+10.5',  'UTC+11.0',
    'UTC+11.5',  'UTC+12.0',  'UTC+12.75',  'UTC+13.0',  'UTC+14.0']


class Clock(object):

    '''A clock with a UTC offset.'''

    def __init__(self, tk, zone=None, **kargs):
        '''A 200x200 pixel clock in a particular time zone. tk is the tkiner
        instance; kargs contains the x and y location of the clock in the main
        window.'''

        self.width = 200
        self.height = 200
        self.internal_frame = tkinter.Frame(
            tk, borderwidth=3, relief=tkinter.GROOVE)

        self.canvas = tkinter.Canvas(
            self.internal_frame, width=self.width, height=self.height)
        self.canvas.grid()

        self.canvas.after(300, self.refresh)

        if time.daylight:
            dlt = time.altzone
        else:
            dlt = time.timezone

        self.diff = a1.hours_difference(dlt, 0)

        self.local_offset = self.diff
        self.now = time.time()          # Allow fast-forwarding
        self.interval = 500

        self.var = tkinter.StringVar(self.internal_frame)
        self.var.set('local')
        option = tkinter.OptionMenu(self.internal_frame, self.var, *REAL_ZONES)
        option.grid(sticky='ew')
        self.internal_frame.grid(**kargs)
        self.time_scale = 1

        def callback(*args):
            if self.var.get() == 'local':
                self.diff = self.local_offset
            else:
                try:
                    self.diff = float(self.var.get()[3:])
                except:
                    self.diff = 0

        self.var.trace("w", callback)
        self.var.set(zone)

    def _draw_hand(self, degrees, length, **kw):
        '''Draw a clock hand on this Clock at angle degrees length pixels
        long. kw contains information about the hand colour and shape of
        the hand.'''

        angle = math.radians(degrees - 90)
        self.canvas.create_line(self.width / 2, self.height / 2,
                                math.cos(angle) * length + self.width / 2,
                                math.sin(angle) * length + self.width / 2,
                                **kw)

    def refresh(self, forced=False):
        '''Redraw the clock. If forced is True, display it now. If forced is
        False, register a redraw for later.'''

        self.now = self.now + self.interval / 1000 * self.time_scale
        self.canvas.delete(tkinter.ALL)

        # Draw the clock rim.
        self.canvas.create_oval(10, 10, self.width - 10,
                                self.height - 10, width=2, fill="#334455")

        # Draw the tick marks around the clock.
        for i in range(0, 12):
            angle = math.radians(i / 12 * 360)
            outer_length = 90
            inner_length = 80
            self.canvas.create_line(
                math.cos(angle) * inner_length + self.width / 2,
                math.sin(angle) * inner_length + self.width / 2,
                math.cos(angle) * outer_length + self.width / 2,
                math.sin(angle) * outer_length + self.width / 2,
                fill='white', width=3
            )

        # Draw a light or dark face depending on whether it's before noon or
        # after.
        utc_hour = (self.now / 60 / 60) % 24
        hour = int(a1.time_from_utc(utc_hour, self.diff))
        self.canvas.create_oval(15, 15, self.width - 15, self.height - 15,
                                width=2, fill="#e0e8ff" if hour < 12 else "#334")

        hands_colour = "black" if hour < 12 else "white"

        # Draw the hour hand.
        hours_angle = (hour % 12) / 12 * 360
        self._draw_hand(hours_angle, 30, arrow=tkinter.FIRST,
                        arrowshape=(50, 2, 2), fill=hands_colour)
        self._draw_hand(hours_angle + 180, 5, fill=hands_colour)

        # Draw the minute hand.
        minutes_angle = a1.get_minutes(int(self.now)) / 60 * 360
        if a1.time_from_utc(0, self.diff) % 1 == 0.5:
            minutes_angle += 180
        elif a1.time_from_utc(0, self.diff) % 1 == 0.75:
            minutes_angle += 270
        self._draw_hand(minutes_angle, 30, arrow=tkinter.FIRST,
                        arrowshape=(80, 2, 2), fill=hands_colour)
        self._draw_hand(minutes_angle + 180, 5, fill=hands_colour)

        # Draw the second hand.
        seconds_angle = int(a1.get_seconds(int(self.now))) / 60 * 360
        self._draw_hand(seconds_angle, 70, fill='red',
                        width=2, arrow=tkinter.FIRST, arrowshape=(70, 9, 2))
        self._draw_hand(seconds_angle + 180, 18, fill='red',
                        arrow=tkinter.LAST, arrowshape=(8, 5, 5), width=2)
        self._draw_hand(seconds_angle + 180, 20, fill='red')

        # Draw the four larger tick marks at noon, 3, 6, and 9.
        for i in range(0, 12, 3):
            angle = math.radians(i / 12 * 360)
            outer_length = 90
            inner_length = 70
            self.canvas.create_line(
                math.cos(angle) * inner_length + self.width / 2,
                math.sin(angle) * inner_length + self.width / 2,
                math.cos(angle) * outer_length + self.width / 2,
                math.sin(angle) * outer_length + self.width / 2,
                width=5
            )

        if not forced:
            self.canvas.after(self.interval, self.refresh)


if __name__ == '__main__':
    tk = tkinter.Tk()

    # The main window.
    frame = tkinter.Frame(tk)

    # Make a list of 4 clocks and add them to the main window.
    canvases = []
    for x in range(4):
        canvases.append(Clock(frame,
                              zone=['local', 'UTC-4.0', 'UTC+0.0', 'UTC+12.0'][x], row=0, column=x))

    def slow():
        '''Halve the speed of the clocks.'''
        for canvas in canvases:
            canvas.time_scale /= 2
            canvas.refresh(forced=True)

    # Add the Slow motion button to the window and register the slow function as the
    # one to be called when the button is clicked.
    tkinter.Button(frame, text='Slow motion',
                   command=slow).grid(row=3, column=0)

    def normal_speed():
        '''Set the speed of the clocks back to normal.'''
        for canvas in canvases:
            canvas.time_scale = 1
            canvas.refresh(forced=True)

    # Add the Normal speed button to the window and register the normal_speed
    # function as the one to be called when the button is clicked.
    tkinter.Button(frame, text='Normal speed',
                   command=normal_speed).grid(row=3, column=1)

    def speed():
        '''Double the speed of the clocks.'''
        for canvas in canvases:
            canvas.time_scale *= 2
            canvas.refresh(forced=True)

    # Add the Fast forward button to the window and register the speed
    # function as the one to be called when the button is clicked.
    tkinter.Button(frame, text='Fast forward',
                   command=speed).grid(row=3, column=2)

    frame.pack()

    tk.mainloop()
