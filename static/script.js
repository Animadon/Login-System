$(document).ready(function(){

    $("#register").on('click', function() {
        var username = $("#register_username").val();
        var password = $('#register_password').val();
    
        $.ajax({
            url: '/register',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({'username': username, 'password': password}),
            success: function(response) {
                alert(response.status);
            },
            error: function(response) { // FIX: Added the necessary error handler
                alert(response.responseJSON.status);
            }
        });
    });

    $("#login").on('click', function() {
        var username = $("#login_username").val();
        var password = $("#login_password").val();

        $.ajax({
            url: '/login',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({'username':username, 'password':password}),
            success: function(response) {
                alert(response.status)
                window.location.reload()

            },
            error: function(response) {
                alert(response.responseJSON.status);
            }
        })
            
    })
});