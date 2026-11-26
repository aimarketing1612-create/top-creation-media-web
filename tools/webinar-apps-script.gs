/**
 * TCM webinar sign-ups -> Google Sheet + Google Calendar.
 *
 * SETUP (5 minutes, free):
 *  1. Create a Google Sheet named "TCM Webinar Sign-ups".
 *  2. Extensions > Apps Script. Delete the sample code, paste this whole file, Save.
 *  3. Deploy > New deployment > type "Web app".
 *       Execute as: Me.   Who has access: Anyone.
 *     Click Deploy, allow the permissions, and copy the Web app URL.
 *  4. Send that URL to your developer (or paste it as lead_endpoint in tools/blocks_webinar.py).
 *
 * What happens on every sign-up:
 *  - A row is added to the sheet: time, name, WhatsApp, session, language, page.
 *  - One calendar event per session is created on your calendar (if it does not exist yet),
 *    and each sign-up is added to that event's description, so you see who is coming.
 */
var CALENDAR_ID = 'primary';           // or a specific calendar's ID
var EVENT_TITLE = 'TCM Free AI Marketing Class';

function doPost(e) {
  var p = e.parameter || {};
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Signed up', 'Name', 'WhatsApp', 'Session', 'Session start (ISO)', 'Language', 'Page', 'WhatsApp link']);
    }
    var phone = String(p.phone || '').replace(/\D/g, '');
    sheet.appendRow([new Date(), p.name || '', "'" + phone, p.session || '', p.start || '', p.lang || '', p.page || '',
                     phone ? 'https://wa.me/' + phone : '']);

    if (p.start && p.end) {
      var start = new Date(p.start), end = new Date(p.end);
      var cal = CalendarApp.getCalendarById(CALENDAR_ID) || CalendarApp.getDefaultCalendar();
      var events = cal.getEvents(start, end).filter(function (ev) { return ev.getTitle() === EVENT_TITLE; });
      var ev = events.length ? events[0] : cal.createEvent(EVENT_TITLE, start, end, { description: 'Sign-ups:\n' });
      ev.setDescription(ev.getDescription() + '\n' + (p.name || '') + '  +' + phone);
    }
    return ContentService.createTextOutput('ok');
  } finally {
    lock.releaseLock();
  }
}
