import logging
from django.http import Http404
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.template import RequestContext
from page_content.models import WebPage
from utility import set_detail_context


# Some templates need extra or special processing to retrieve additional data. This map
# defines which templates get a special controller.
TEMPLATE_CONTROLLER_MAP = {}


def view_web_page(request, a_slug, edit=None):
    current_site = get_current_site()

    try:
        # IF WE THERE IS AN ACTIVE SUPERUSER, WE NEED TO LOOK FOR ALL PAGES
        # REGARDLESS OF IT'S PUBLISHED STATE
        # THIS IS SO THEY CAN EDIT THE COPY WITH FRONT
        # BECAUSE IT'S NOT AVAILABLE FROM THE BACKEND
        try:
            if request.user.is_superuser:
                active_user = request.user

            else:
                active_user = None

        except Exception, e:
            print e
            active_user = None

        if active_user:
            page = WebPage.objects.get(slug=a_slug)

        else:
            page = WebPage.objects.get(slug=a_slug, is_published=True)

    except:
        raise Http404

    # CHECK FOR TEMPLATE OVERRIDE
    try:
        if page.template_choice != None and len(page.template_choice) > 1:

            # IF TEMPLATE OVERRIDE, REDIRECT TO CORRECT VIEW
            if TEMPLATE_CONTROLLER_MAP.has_key(page.template_choice):
                func_ptr = TEMPLATE_CONTROLLER_MAP[page.template_choice]
                return func_ptr(request, page)

    except Exception, e:
        print e
        pass

    context = {'page': page}
    set_detail_context(request, context)

    template = 'detail_page.html'

    return render_to_response(template, context, context_instance=RequestContext(request))


def get_current_site():
    try:
        # GET CURRENT SITE
        current_site = Site.objects.get_current()

    except Exception, e:
        logging.error(e)
        current_site = None

    return current_site
