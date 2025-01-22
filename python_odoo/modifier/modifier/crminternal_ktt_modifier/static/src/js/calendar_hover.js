odoo.define('crminternal_ktt_modifier.calendar_hover', function (require) {
    "use strict";

    var core = require('web.core');
    var ajax = require('web.ajax');
    var CalendarRenderer = require('web.CalendarRenderer');
    var CalendarView = require('web.CalendarView');
    var viewRegistry = require('web.view_registry');

    console.log('farhanassegaf file javascrpt ini di eksekusi')

    var CustomCalendarRenderer = CalendarRenderer.extend({
        events: _.extend({}, CalendarRenderer.prototype.events, {
            'mouseover .o_calendar_record': '_onActivityHover',
            'mouseout .o_calendar_record': '_onActivityHoverOut',
        }),

        _onActivityHover: function (event) {
            event.stopPropagation(); // Stop event propagation to prevent default click behavior

            var self = this;
            var eventId = $(event.currentTarget).data('id');

            if (!eventId) return;

            ajax.jsonRpc('/get/calendar/event/details', 'call', {
                'event_id': eventId
            }).then(function (data) {
                if (data) {
                    // Create tooltip element if it doesn't exist
                    if (!$('#calendar-event-tooltip').length) {
                        $('body').append('<div id="calendar-event-tooltip" style="position: absolute; background: white; border: 1px solid black; padding: 10px; display: none; z-index: 1000;"></div>');
                    }

                    // Fill tooltip with data
                    var tooltipContent = '<b>' + data.name + '</b><br>';
                    tooltipContent += 'Start: ' + data.start + '<br>';
                    if (data.stop) {
                        tooltipContent += 'End: ' + data.stop + '<br>';
                    }
                    tooltipContent += 'Responsible: ' + (data.user_id || 'N/A') + '<br>';
                    tooltipContent += 'Privacy: ' + data.privacy + '<br>';
                    tooltipContent += 'Description: ' + (data.description || 'No Description') + '<br>';

                    $('#calendar-event-tooltip').html(tooltipContent);

                    // Position tooltip
                    var top = $(event.currentTarget).offset().top + $(event.currentTarget).outerHeight();
                    var left = $(event.currentTarget).offset().left;
                    $('#calendar-event-tooltip').css({
                        'top': top + 'px',
                        'left': left + 'px',
                    });

                    // Show tooltip
                    $('#calendar-event-tooltip').show();
                }
            });
        },

        _onActivityHoverOut: function (event) {
            // Hide tooltip
            $('#calendar-event-tooltip').hide();
        },
    });

    var CustomCalendarView = CalendarView.extend({
        config: _.extend({}, CalendarView.prototype.config, {
            Renderer: CustomCalendarRenderer,
        }),
    });

    viewRegistry.add('custom_calendar_view', CustomCalendarView);
});