from django.http import Http404, HttpResponseRedirect

from navigation.models import PrimaryNavigation, UrlRedirect
from page_content.views import view_web_page


def default(request):
    path = request.path.rstrip('/')

    # Look for navigation links
    try:
        nav = PrimaryNavigation.objects.get(url_search_target=path, is_published=True)

        if nav.link_type == 'page':
            return view_web_page(request, nav.page.slug)


    except PrimaryNavigation.DoesNotExist:
        pass


    # Look for a redirect
    try:
        redirect = UrlRedirect.objects.get(from_url=path)
        return HttpResponseRedirect(redirect.to_url)

    except UrlRedirect.DoesNotExist:
        pass

    # Look for a page slug that matches if the url is one level deep
    split_url = request.path.strip('/').split('/')
    if len(split_url) < 2:
        try:
            return view_web_page(request, split_url[0])
        except:
            pass


    # if we fall through this far then we don't know what this url is
    raise Http404