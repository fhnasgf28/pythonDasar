odoo.define('crminternal_ktt_modifier.tooltip', function (require) {
    "use strict";

    const CalendarRenderer = require('web.CalendarRenderer');

    CalendarRenderer.include({
        /**
         * Override function to add hover tooltip for calendar events.
         */
        _renderEvent: function (event) {
            const $event = this._super.apply(this, arguments);
            const description = event.record.description;
            if (description) {
                $event.attr('title', description);  // Menambahkan tooltip sebagai atribut title
                $event.hover(
                    function () {
                        $(this).css('cursor', 'pointer');
                    },
                    function () {
                        $(this).css('cursor', 'default');
                    }
                );
            }
            return $event;
        },
    });
});