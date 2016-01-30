/**
 * Created by Truman on 1/19/16.
 */

$(document).ready(function () {
    $(".wallets").on("click", function () {
        url = "/wallet/wallet/get/" + this.id;
        $.get(url, function (data) {
            $("#wallet_name").val(data.name);
            $("#wallet_total").val(data.total);
            $("#wallet_note").val(data.note);
        })
    });
});