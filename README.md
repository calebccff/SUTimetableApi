# Import your timetable with filters
This simply allows you to use the calender export feature from SU timetable and only have events from your house / group shown

## Instructions
1. Go to https://science.swansea.ac.uk/intranet/attendance/timetable/2019/09/30?department=CSCI&level=1
2. At the bottom is a hyperlink [timetable.ics](https://science.swansea.ac.uk/intranet/attendance/timetable/student_calendar/SOME_HASH/timetable.ics). Grab the `SOME_HASH` part.
3. Browse to http://connolly.tech/api/SOME_HASH?group=X:Y, replacing `SOME_HASH` with the hash you just copied. Also modify the `group=` part to represent your house/group as follows:

| Group | Turing | Lovelace | Babbage |
|-------|--------|----------|---------|
| A     | T:A    | L:A      | B:A     |
| B     | T:A    | L:B      | B:B     |

4. Try browsing to the URL in your browser, if it's valid it will be a page full of text, if it isn't there will be an error telling you what is wrong. If you receive an error 404, make sure you're using HTTP not HTTPS, Firefox likes to aggressively redirect to HTTP on Linux. I'm working on a fix, in the meantime test in a different browser.
4. Now go to import the timetable. [Here for Google Calendar](https://calendar.google.com/calendar/r/settings/addbyurl) and [here for Outlook Calendar](https://outlook.office365.com/calendar/). For outlook click import calendar on the left and then click "from web".
5. Paste the URL you created, it takes ~10 seconds to add (The URL in the format `http://connolly.tech/api/SOME_HASH?group=X:Y`)
6. Wait for it to update on your phone, and that's it.