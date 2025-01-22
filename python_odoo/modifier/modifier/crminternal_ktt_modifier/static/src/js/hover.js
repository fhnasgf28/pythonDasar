odoo.define('crminternal_ktt_modifier.CalendarView', function (require) {
    "use strict";

    const CalendarRenderer = require('calendar.CalendarRenderer');
    console.log('maseh farhanasseinidd')
    CalendarRenderer.include({
        events: _.extend({}, CalendarRenderer.prototype.events, {
            'mouseenter .o_calendar_event': '_onHoverEvent',
            'mouseleave .o_calendar_event': '_onLeaveEvent',
        }),

        _onHoverEvent: function (ev) {
            ev.stopPropagation();
            const $target = $(ev.currentTarget);

            if (!$target.data('popover-initialized')) {
                $target.popover({
                    content: this._getPopoverContent($target),
                    html: true,
                    trigger: 'manual',
                    placement: 'top'
                });
                $target.data('popover-initialized', true);
            }
            $target.popover('show');
        },

        _onLeaveEvent: function (ev) {
            const $target = $(ev.currentTarget);
            $target.popover('hide');
        },

        _getPopoverContent: function ($target) {
            const eventData = $target.data('event-data') || {};
            return `<strong>${eventData.title || 'No Title'}</strong><br>${eventData.description || 'No Description'}`;
        }
    });

