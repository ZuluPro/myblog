from xml.dom import minidom
from datetime import datetime
from requests_oauthlib import OAuth1Session
from django.core.files.storage import Storage
from django.core.cache import caches
from django.conf import settings


class FileNotFound(Exception):
    """Can't find file."""


class FileSaveError(Exception):
    """Can't save file."""


class AuthenticationError(Exception):
    """Can't make an action due to authentication."""


class FlickrStorage(Storage):
    """
    Storage for handle Flickr's photo with Django Storage API.
    """
    SIZES = 'mstzb'
    API_ENDPOINT = 'https://api.flickr.com/services/rest/'
    API_POST_URL = 'https://up.flickr.com/services/upload/'
    IMG_URL_TEMPLATE = "https://farm{farm}.staticflickr.com/{server}/{id}_"\
                       "{originalsecret}_o.{originalformat}"
    THUMB_URL_TEMPLATE = "https://farm{farm}.staticflickr.com/{server}/{id}_"\
                         "{secret}.jpg"

    def __init__(self, api_key, api_secret=None, oauth_token=None,
                 oauth_token_secret=None, user_id=None):
        """
        :param api_key: User's API key
        :type api_key: str

        :param api_secret: User's API secret
        :type api_secret: str

        :param oauth_token: Oauth access token
        :type oauth_token: str

        :param oauth_token_secret: Oauth access token secret
        :type oauth_token_secret: str

        :param user_id: User ID, if you want to list its directory by default
        :type user_id: str
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.oauth_session = OAuth1Session(
            client_key=api_key, client_secret=api_secret,
            signature_method=u'HMAC-SHA1', signature_type=u'AUTH_HEADER',
            resource_owner_key=oauth_token,
            resource_owner_secret=oauth_token_secret)
        self.user_id = user_id
        self._request_default_params = {
            'api_key': self.api_key,
            'format': 'json',
            'nojsoncallback': '1'
        }
        self.cache = caches[settings.FLICKR_CACHE]

    def _make_request_params(self, method, options=None):
        """
        Create a dictionary from minimum parameters needed for request API and
        given data.

        :param method: Method used, example 'flickr.people.getPublicPhotos'
        :type method: str

        :param options: Parameters to add to request
        :type method: dict

        :return: Request parameters
        :rtype: dict
        """
        options = options or {}
        params = self._request_default_params.copy()
        params['method'] = method
        params.update(options)
        return params

    def listdir(self, path=None, original=True, size='m'):
        """
        List user's photos. What is considered by Django as a path is here a
        user ID.

        :param path: User's ID, example: '73509042@N00', default: User ID
                     defined at instanciation

        :param original: Get original files URLs
        :type original: bool

        :param size: It defines the wanted size if original is false or
                     unavailable
        :type size: str

        :return: A list of 2 tuples, the 1st is empty, the second contains URLs
        :rtype: list of 2 tuples
        """
        user_id = path or self.user_id
        if not user_id:
            raise ValueError("You must either specify a user ID at "
                             "storage instanciation or at listdir "
                             "launching")
        wanted_size = 'url_o' if original else 'url_%s' % size
        fallback_size = 'url_%s' % size if original else 'url_m'
        extras = ','.join([wanted_size, fallback_size])
        params = self._make_request_params('flickr.people.getPublicPhotos',
                                           {'user_id': user_id,
                                            'extras': extras})
        response = self.oauth_session.get(self.API_ENDPOINT, params=params)
        urls = [pho.get(wanted_size, pho[fallback_size])
                for pho in response.json()['photos']['photo']]
        return ([], urls)

    def list_image_and_thumb(self, path=None, size='m'):
        """
        List user's photos with original and thumbnail URLs.

        :param path: User's ID, example: '73509042@N00', default: User ID
                     defined at instanciation
        :type path: str

        :param original: Get original files URLs
        :type original: bool

        :param size: Wanted size
        :type size: str

        :return: A list of tuple, all tuple is composed by original URL and
                 thumbnail URL
        :rtype: list of tuple
        """
        user_id = path or self.user_id
        if not user_id:
            raise ValueError("You must either specify a user ID at "
                             "storage instanciation or at "
                             "list_image_and_thumb launching.")
        size = 'url_%s' % size
        params = self._make_request_params('flickr.people.getPublicPhotos',
                                           {'user_id': user_id,
                                            'extras': 'url_o,url_m,%s' % size})
        response = self.oauth_session.get(self.API_ENDPOINT, params=params)
        urls = [(pho[size], pho.get('url_o', pho['url_m']))
                for pho in response.json()['photos']['photo']]
        return urls

    def _get_file_info(self, photo_id):
        """
        Get informations for a single photo.

        :param photo_id: ID of the desired file
        :type photo_id: str

        :returns: Response data
        :rtype: dict

        :raises: :class:`.FileNotFound` if can't find file
        """
        params = self._make_request_params('flickr.photos.getInfo',
                                           {'photo_id': photo_id})
        response = self.oauth_session.get(self.API_ENDPOINT,
                                          params=params).json()
        if response['stat'] == 'fail':
            raise FileNotFound("Can't find '%s'" % photo_id)
        return response

    def created_time(self, name):
        photo = self._get_file_info(name)['photo']
        return datetime.fromtimestamp(float(photo['dateuploaded']))

    def exists(self, name):
        try:
            self._get_file_info(name)
            return True
        except FileNotFound:
            return False

    def modified_time(self, name):
        photo = self._get_file_info(name)['photo']
        return datetime.fromtimestamp(float(photo['dates']['lastupdate']))

    def _save(self, name, content):
        """
        Uploads a photo to Flickr and returns its ID.

        :param name: Desired file name on Flickr database
        :type name: str

        :param content: File to upload
        :type content: :class:`django.core.files.base.File`

        :return: File's name
        :rtype: str

        :raises: FileSaveError: If unable to upload image
        """
        if not self.oauth_token:
            raise AuthenticationError("You must be authenticated with oAuth "
                                      "for upload files.")
        params = self._request_default_params.copy()
        params.update({
            'title': name,
            # 'description': description,
            # 'tags': tags,
            # 'is_public': is_public,
            'is_public': 1,
            # 'is_friend': is_friend,
            # 'is_family': is_family,
            # 'safety_level': safety_level,
            # 'content_type': content_type,
            # 'hidden': hidden
        })
        response = self.oauth_session.post(self.API_POST_URL, params=params,
                                           files={'photo': content.file})
        # TODO: Make clear XML Parsing
        if not (response.status_code == 200 and 'stat="ok"' in response.content):
            raise FileSaveError("Unable to save file: %s" % response.content)
        xmldoc = minidom.parseString(response.content)
        photo_id = xmldoc.getElementsByTagName('photoid')[0].firstChild.nodeValue
        return photo_id

    def _format_url(self, photo, original=True, size='m'):
        """
        Format a photo's URL from its attributes.

        :param photo: Photo attributes
        :type photo: dict

        :param original: Get original file URL
        :type original: bool

        :param size: Wanted size
        :type size: str

        :return: URL
        :rtype: str
        """
        if original:
            if 'originalsecret' not in photo:
                raise ValueError("Only photo owner can get original URL")
            url = self.IMG_URL_TEMPLATE.format(**photo)
        else:
            if size not in self.SIZES:
                raise ValueError("Bad image size, allowed are %s" % self.SIZES)
            url = self.THUMB_URL_TEMPLATE.format(**photo)
        return url

    # XXX: Maybe we shouldn't cache
    def url(self, name, original=True, size='m'):
        """
        Get url of a photo with desired size.

        :param name: ID of the desired file
        :type name: str

        :param original: Get original file URL
        :type original: bool

        :param size: Wanted size
        :type size: str

        :return: URL
        :rtype: str
        """
        cache_key = "%s-%s" % (name, 'o' if original else size)
        cached_url = self.cache.get(cache_key, None)
        if cached_url:
            return cached_url
        photo = self._get_file_info(name)['photo']
        url = self._format_url(photo, original, size)
        self.cache.set(cache_key, url)
        return url

    def get_available_name(self, name, max_length=None):
        """
        Useless with Flickr as any name can be given.
        """
        return name