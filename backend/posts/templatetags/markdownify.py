# markdownify
from django import template
from markdown import markdown
 
register = template.Library()
 
@register.filter
def markdownify(post, truncate = False):
    body = post.body
    truncated = False
    if truncate:
        if "<!-- more -->" in body:
            text = body.split("<!-- more -->")[0].strip()
        else:
            text = body[:380]
        if len(text) < len(body):
            body = text
            truncated = True

    firstline = body.splitlines()[0]
    if "# " in firstline:
        firstline += '\n\n'
    rest = str(''.join(body.splitlines()[1:]))
    rest = rest.replace('\n\n','<br/>')
    rest = rest.replace('\n',' ')
    body = str(firstline) + rest

    html = markdown(body)
    firstline = html.splitlines()[0]
    rest = html.splitlines()[1:]
    # If first line is a header, make it link to the post
    if "<h1>" in firstline and truncate:
        firstline = '<a href="'+post.get_absolute_url()+'">'+firstline+'</a>'
    html = str(firstline) + str(''.join(rest))

    if truncated:
        html += '<a class="read-more" href="'+post.get_absolute_url()+'">Read more...</a>'
    return html

