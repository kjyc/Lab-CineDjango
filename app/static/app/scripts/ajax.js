$(function () {
    $('#new_pelicula').on('submit', function (e) {
        e.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            url: '/new_pelicula/',
            type: 'POST',
            data: formData,
            processData: false,  // tell jQuery not to process the data
            contentType: false,
            dataType: 'JSON',
            success: function (response) {
                alert(response.message);
            }
        });
        return false;
    });
});