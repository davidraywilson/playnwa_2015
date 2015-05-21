var mobileNav = 'closed';

function toggleMobileMenu() {

    var nav = $('#mobile-nav-wrapper');
    var social_height = $('#mobile-nav-social-icons').height();
    var menu_height = $('#mobile-nav').height() + social_height + 80;

    if (mobileNav == 'closed') {
        $(nav).animate({height: menu_height}, 400);
        mobileNav = 'open';
    }

    else {
        $(nav).animate({height: '0'}, 200);
        mobileNav = 'closed';
    }

}

function toggleSubLevel(counter) {

    var nav = $('#mobile-nav-wrapper');
    var nav_height = $('#mobile-nav-wrapper').height();
    var arrow = $('.drop-arrow.arrow-' + counter);
    var wrapper = $('.sub-level-wrapper-' + counter);
    var ht = $('.sub-level-' + counter).height();

    if (wrapper.hasClass('open')) {
        $(wrapper).animate({height: '0'}, 200);
        $(nav).animate({height: nav_height - ht}, 400)
        $(arrow).removeClass('open')
        $(wrapper).removeClass('open')
    }

    else {
        $(wrapper).animate({height: ht + 'px'}, 400);
        $(nav).animate({height: nav_height + ht}, 400)
        $(arrow).addClass('open')
        $(wrapper).addClass('open')
    }

}
