odoo.define('crminternal_ktt_modifier.calendar_view', function (require) {
    "use strict";

    var CalendarRenderer = require('calendar.CalendarRenderer');
    var core = require('web.core');
    var qweb = core.qweb;

    console.log('Custom CalendarRenderer loaded!');

    CalendarRenderer.include({
    _eventRender: function (event) {
        var result = this._super.apply(this, arguments);

        if (event.record) {
            console.log('Event record:', event.record);
        }

        if (event.record && event.record.end_duration) {
            try {
                var stopTimeFormatted = moment(event.record.end_duration).format("HH:mm");
                var timeElement = $(result).find('.fc-time');
                if (timeElement.length > 0) {
                    var currentContent = timeElement.text();
                    timeElement.text(`${currentContent} - ${stopTimeFormatted}`);
                } else {
                    var titleElement = $(result).find('.fc-title');
                    if (titleElement.length > 0) {
                        var currentContent = titleElement.text();
                        titleElement.text(`${currentContent} (${stopTimeFormatted})`);
                    }
                }
            } catch (e) {
                console.error('Error processing stop time:', e);
            }
        } else {
            console.warn('Event record or stop time is undefined:', event);
        }

        return result;
    },
});
