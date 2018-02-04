$(function () {
    $('button').click(function () {
        var advisor = $('#selectedAdvisor').val();
        $.ajax({
            url: '/advisors',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});