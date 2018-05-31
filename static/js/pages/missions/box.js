$(document).ready(function() {

    /* Flags */
    $("a[id^=capture-file-flag-button]").click(function() {
        $("#capture-file-flag-uuid").val($(this).data("uuid"));
    });

    $("#capture-file-flag-submit").click(function() {
        $("#capture-file-flag-form").submit();
    });

    $("a[id^=capture-text-flag-button]").click(function() {
        $("#capture-text-flag-uuid").val($(this).data("uuid"));
    });

    $("#capture-text-flag-submit").click(function() {
        $("#capture-text-flag-form").submit();
    });

    /* Hints */
    $("a[id^=purchase-hint-button]").click(function() { 
        $("#purchase-hint-uuid").val($(this).data("uuid"));
        var price = $(this).data("price");
        if (price === "0") {
            var bank = $("#hintbanking").val();
            if (bank == 'true') {
                $("#purchase-hint-text").text("Would you like to purchase this hint for $"+price+"?");
            } else {
                $("#purchase-hint-text").text("Would you like to take this hint for -"+price+" points?");
            }
        } else {
            //If the cost is 0, then skip the dialog and just give the hint
            $("#purchase-hint-form").submit();
        }
    });

    $("#purchase-hint-submit").click(function() {
        $("#purchase-hint-form").submit();
    });

});
