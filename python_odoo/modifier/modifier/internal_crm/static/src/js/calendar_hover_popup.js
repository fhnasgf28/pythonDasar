odoo.define('crminternal_ktt_modifier.calendar_popup', function (require) {
    "use strict";

    const CalendarView = require('web.CalendarView');
    const Dialog = require('web.Dialog');
    const core = require('web.core');
    const QWeb = core.qweb;

    console.log("JavaScript file loaded: calendar_popup.js");
    // Override CalendarView
    CalendarView.include({
        start: function () {
            console.log("CalendarView started!");
            this._super.apply(this, arguments);
            // Trigger popup when the view loads
            this._showCustomPopup();
        },

        _showCustomPopup: function () {
            const self = this;
            console.log("Custom popup function triggered!");
            // Fetch data from the server (if needed)
            this._rpc({
                model: 'calendar.event',
                method: 'search_read',
                args: [[['start', '>=', moment().startOf('day').format()], ['start', '<=', moment().endOf('day').format()]], ['name', 'start', 'stop']],
            }).then(function (events) {
                // Render popup content using QWeb
                const content = QWeb.render('CalendarPopupTemplate', { events: events });

                // Display the popup
                new Dialog(self, {
                    title: "Today's Events",
                    size: 'medium',
                    $content: $(content),
                    buttons: [{
                        text: 'Close',
                        close: true
                    }],
                }).open();
            });
        },
    });
});
