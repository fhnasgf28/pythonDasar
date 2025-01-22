odoo.define('crminternal_ktt_modifier.tooltip', function (require) {
    "use strict";

    var core = require('web.core');
    var QWeb = core.qweb;

    $(document).ready(function () {
        // Menambahkan tooltip pada button dengan class tooltip-button
        $('body').on('mouseenter', '.tooltip-button', function () {
            var $button = $(this);
            var tooltipText = $button.data('tooltip');
            console.log('farhanassegaf tooltip ini dieksekusi')
            if (tooltipText) {
                // Membuat elemen tooltip
                var $tooltip = $('<div class="custom-tooltip"></div>').text(tooltipText);
                $('body').append($tooltip);

                // Menentukan posisi tooltip
                var offset = $button.offset();
                $tooltip.css({
                    top: offset.top - $tooltip.outerHeight() - 10,
                    left: offset.left + ($button.outerWidth() / 2) - ($tooltip.outerWidth() / 2)
                }).fadeIn(200);
            }
        }).on('mouseleave', '.tooltip-button', function () {
            // Menghapus tooltip saat mouse keluar dari button
            $('.custom-tooltip').remove();
        });
    });
});
