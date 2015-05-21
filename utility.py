# Used to clean strings of special characters
import string
import logging
from django.contrib.sites.models import Site
from django.http import Http404
from navigation.models import PrimaryNavigation
from site_content.models import Logo, SiteColor, SocialLink, Instagram


def set_detail_context(request, a_context):
    # CHECK FOR ADMIN USER
    active_user = None
    try:
        if request.user.is_superuser:
            active_user = request.user

    except Exception, e:
        print e

    a_context['active_user'] = active_user

    try:
        # GET CURRENT SITE
        current_site = Site.objects.get_current()

    except Exception, e:
        logging.error(e)
        current_site = None

    if current_site:
        try:
            # GET LOGO FOR CURRENT SITE
            logo = Logo.objects.get(site=current_site)
            a_context['logo'] = logo

        except Exception, e:
            logging.error(e)

        try:
            # GET COLOR FOR CURRENT SITE
            site_color = SiteColor.objects.get(site=current_site)
            a_context['site_color'] = site_color

        except Exception, e:
            logging.error(e)

        try:
            # GET PRIMARY NAV FOR CURRENT SITE
            nav_links = PrimaryNavigation.get_published_objects()
            a_context['nav_links'] = nav_links

        except Exception, e:
            logging.error(e)

        try:
            # GET SOCIAL LINKS FOR CURRENT SITE
            social_links = SocialLink.get_published_objects_for_site(current_site)
            a_context['social_links'] = social_links

        except Exception, e:
            logging.error(e)

        try:
            # GET INSTAGRAM NAME FOR CURRENT SITE
            instagram = Instagram.objects.get(site=current_site)
            a_context['instagram'] = instagram

        except Exception, e:
            logging.error(e)

    else:
        raise Http404


allchars = string.maketrans('', '')


def makefilter(keep):
    delchars = allchars.translate(allchars, keep)

    def thefilter(s):
        return s.translate(allchars, delchars)

    return thefilter


stringFilter = makefilter('abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890. ')
