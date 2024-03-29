var action_menu_status = 'closed';

// CLOSE USER ACTIONS ON PAGE LOAD
$(window).ready(function() {
    var menu_wrap = $('#user-actions-menu');
    var app_wrap = $('#user-actions-menu #all-apps');
    var wrap_bottom = '-' + $(app_wrap).height() - 80;
    $(menu_wrap).animate({bottom: wrap_bottom}, 300);
    var action_menu_status = 'closed';
});

function toggleUserActions() {

    var menu_wrap = $('#user-actions-menu');

    if (action_menu_status == 'closed') {

        $(menu_wrap).animate({bottom: 0}, 300);
        action_menu_status = 'open'

    }

    else {

        var menu_wrap = $('#user-actions-menu');
        var app_wrap = $('#user-actions-menu #all-apps');
        var wrap_bottom = '-' + $(app_wrap).height() - 80;
        $(menu_wrap).animate({bottom: wrap_bottom}, 300);
        action_menu_status = 'closed'

    }

}


function displayManageWindow(link) {
    var mask = $('#mask');
    var dialog = $('#user-manage-dialog');
    var dialog_content = $('#user-manage-content');

    var iframe = document.createElement('iframe');
    iframe.frameBorder = 0;
    iframe.id = 'admin-frame';
    iframe.setAttribute('src', link);
    $(dialog_content).html(iframe);

    $('body').css('overflow','hidden');
    $(mask).fadeIn(600);

    setTimeout(
        function () {
            $(dialog).show();
            $(dialog).animate({left: '0'}, 800)
        }, 300
    );
}


function hideManageWindow() {
    var mask = $('#mask');
    var dialog = $('#user-manage-dialog');

    $('body').css('overflow','visible');
    $(dialog).animate({left: '-9999px'}, 600);

    setTimeout(
        function () {
            $(mask).fadeOut(600);
            $(dialog).fadeOut(600)
        }, 400
    );
}


function saveManageWindow() {
    location.reload();
}


function ajaxError(xhr, options, thrownError) {
    alert(xhr.status);
    alert(thrownError);
}
