from django import template
register = template.Library()

import logging
logger = logging.getLogger(__name__)


@register.filter(name='embed')
def embed(youtube_url):
    try:
        code = youtube_url.split('=')[-1]
        youtube_url = 'https://www.youtube.com/embed/' + code + '?feature=player_detailpage'
    except Exception as err:
        youtube_url = ''
        logger.error(str(err))
    return youtube_url    
