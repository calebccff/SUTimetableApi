# Import your timetable with filters
This simply allows you to use the calender export feature from SU timetable and only have events from your house / group shown.

#### I would encourage you not to rely on this service, not only is it up to 12 hours behind the original calendar, it is just running on a VPS which could well go down and cause you not to receive updates at all. [See the FAQ](#FAQ).

## Instructions
1. Go to https://science.swansea.ac.uk/intranet/attendance/timetable
2. At the bottom is a hyperlink [timetable.ics](https://science.swansea.ac.uk/intranet/attendance/timetable/student_calendar/SOME_HASH/timetable.ics). Grab the `SOME_HASH` part.
3. Browse to http://connolly.tech/api/SOME_HASH?group=X:Y, replacing `SOME_HASH` with the hash you just copied. Also modify the `group=` part to represent your house/group as follows:

| Group | Turing | Lovelace | Babbage |
|-------|--------|----------|---------|
| A     | T:A    | L:A      | B:A     |
| B     | T:B    | L:B      | B:B     |

4. Try browsing to the URL in your browser, if it's valid it will be a page full of text, if it isn't there will be an error telling you what is wrong. If you receive an error 404, or something about 'Unable to connect', make sure you're using HTTPS, NOT HTTP!.
4. Now go to import the timetable. [Here for Google Calendar](https://calendar.google.com/calendar/r/settings/addbyurl) and [here for Outlook Calendar](https://outlook.office365.com/calendar/). For outlook click import calendar on the left and then click "from web".
5. Paste the URL you created, it takes ~10 seconds to add (The URL in the format `http://connolly.tech/api/SOME_HASH?group=X:Y`)
6. Wait for it to update on your phone, and that's it. **Please note it can take up to 10 minutes to appear on your phone after it's been imported**

## FAQ
### Will changes made to the timetable be updated?
Yes, if the original swansea timetable changes, yours will too. Note that this process [can take up to 12 hours](https://support.google.com/calendar/answer/37100?hl=en&ref_topic=1672445)

### An important lecture was missing! It's YOUR fault
I take no responsibilities for any issues here, I highly recommend that you still regularly check the original timetable found [here](https://science.swansea.ac.uk/intranet/attendance/timetable). Your failure to do this is not my responsibility.

### I see you changed it to show model names instead of codes, what if I prefer codes?!
Add `&codes_not_numbers=1` to the end of your URL and you'll get the codes instead of the names.