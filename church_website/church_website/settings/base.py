from os import getenv
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'ckeditor',
    'ckeditor_uploader',
    'homepage.apps.HomepageConfig',
    'gallery.apps.GalleryConfig',
    'blog.apps.BlogConfig',
    'about.apps.AboutConfig',
    'schedule.apps.ScheduleConfig',
    'search.apps.SearchConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'church_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'church_website.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = 'static'

STATICFILES_DIRS = ['loadstatic']

MEDIA_URL = 'media/'

MEDIA_ROOT = 'media'

CONVERTING_SAVED_IMAGE = 'webp'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

CKEDITOR_UPLOAD_PATH = "uploads/post/"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_sergievskiy': [
            {
                'name': 'document',
                'items': [
                    'Source',
                    '-',
                    'Save',
                    'NewPage',
                    'Preview',
                    'Maximize',
                    'Print'
                    ]
            },
            {
                'name': 'clipboard',
                'items': [
                    'Cut',
                    'Copy',
                    'Paste',
                    'PasteText',
                    'PasteFromWord',
                    '-',
                    'Undo',
                    'Redo'
                    ]
            },
            {
                'name': 'editing',
                'items': [
                    'Find',
                    'Replace',
                    '-',
                    'SelectAll'
                    ]
            },
            '/',
            {
                'name': 'basicstyles',
                'items': [
                    'Bold',
                    'Italic',
                    'Underline',
                    'Strike',
                    'Subscript',
                    'Superscript',
                    '-',
                    'RemoveFormat'
                    ]
            },
            {
                'name': 'paragraph',
                'items': [
                    'NumberedList',
                    'BulletedList',
                    '-',
                    'Outdent',
                    'Indent',
                    '-',
                    'Blockquote',
                    '-',
                    'JustifyLeft',
                    'JustifyCenter',
                    'JustifyRight', 'JustifyBlock',
                    '-',
                    'BidiLtr',
                    'BidiRtl'
                    ]
            },
            {
                'name': 'insert',
                'items': [
                    'Image',
                    'Table',
                    'HorizontalRule',
                    'SpecialChar',
                    'PageBreak',
                    '-',
                    'Link',
                    'Unlink'
                    ]
            },
            '/',
            {
                'name': 'styles',
                'items': [
                    'Styles',
                    'Format',
                    'Font',
                    'FontSize'
                    ]
            },
            {
                'name': 'colors',
                'items': [
                    'TextColor',
                    'BGColor'
                    ]
            },
        ],
        'toolbar': 'sergievskiy',
        'width': 'full',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}
