import pymysql
import os
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '__=s9@oixaun$x^g7-4#10wf_*7zvb8)kl1$j82fj&cyq%^o^3'

# SECURITY WARNING: don't run with debug turned on in production!

# 部署到线上时为 False; 读者在本地调试时请修改为 True
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']

# INTERNAL_IPS = ['127.0.0.1']
INTERNAL_IPS = ['127.0.0.1:8000']

# 设置默认文件默认值
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Application definition
INSTALLED_APPS = [
    # default apps
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # debug 工具
    # 'debug_toolbar',
    # Third party apps
    'bootstrap4',  # boostrap模块的应用
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 可添加需要的第三方登录
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.weibo',
    # 模板文件
    # 重改allauth样式
    'crispy_forms',

    'password_reset',  # 重置密码

    'taggit',
    'ckeditor',
    'mptt',
    'notifications',

    'article',
    'userprofile',
    'comment',
    'notice',
    'markdown',

    # 'mdeditor',
    'widget_tweaks',

    # 数据检测工具 django-extensions
    'django_extensions',

    # 拓展
    'app01',
    'chat',
    'photo',
    'sharefile',

]

# bootstrap
# CRISPY_TEMPLATE_PACK = 'bootstrap4'

# 美化
SIMPLEUI_LOGO = '../static/image/blogLogo.jpg'
SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_ICON = 'fa fa-eye'
# SIMPLEUI_HOME_QUICK = False #去掉"快捷动作"
# SIMPLEUI_HOME_ACTION = False # 去掉"最近动作"
# 修改左侧菜单首页设置
SIMPLEUI_HOME_PAGE = '/'  # 指向页面
# SIMPLEUI_HOME_TITLE = '百度欢迎你!'  # 首页标题
SIMPLEUI_HOME_ICON = 'fa fa-code'  # 首页图标

# 设置右上角Home图标跳转链接，会以另外一个窗口打开
SIMPLEUI_INDEX = '/'

MIDDLEWARE = [
    # debug toole 中间件
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 定义模板位置
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'my_blog.wsgi.application'

# Database
# 数据库的创建与连接
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# # 数据库的连接
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'blog_num_one',
#         'PASSWORD':'123456',
#         'USER':'root',
#         'POST':3306,
#         'HOST':'127.0.0.1',
#     }
# }


# Password validation
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

# Internationalization
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# 静态文件地址
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# 静态文件收集目录
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

# 发送邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # smtp服务地址
EMAIL_HOST = 'smtp.qq.com'
# # 端口默认都是25不需要修改
EMAIL_PORT = 25
# # 发送邮件的邮箱，需要配置开通SMTP
EMAIL_HOST_USER = '1963668038@qq.com'
# # 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'scqtoiaurswveagf'
# # 收件人看到的发件人
EMAIL_FROM = '博客通知'
# # 这⾥必须是True，否则发送不成功
EMAIL_USE_TLS = True
# 默认显示的发送人
DEFAULT_FROM_EMAIL = "EOSONES 博客 <1963668038@qq.com>"

# 要求用户注册时必须填写email
# ACCOUNT_EMAIL_REQUIRED = True
# 注册中邮件验证方法: "强制(mandatory)"、 "可选(optional)" 或 "否(none)" 之一
# (注册成功后，会发送一封验证邮件，用户必须验证邮箱后，才能登陆)
# ACCOUNT_EMAIL_VERIFICATION ="optional"
# 作用于第三方账号的注册
# SOCIALACCOUNT_EMAIL_VERIFICATION = 'optional' / 'mandatory' / 'none'
# 邮件发送后的冷却时间(以秒为单位)
# ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN =180
# 邮箱确认邮件的截止日期(天数)
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3

# 指定要使用的登录方法(用户名、电子邮件地址或两者之一)
# ACCOUNT_AUTHENTICATION_METHOD (="username" | "email" | "username_email")
# 登录尝试失败的次数
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT =3
# 从上次失败的登录尝试，用户被禁止尝试登录的持续时间
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =300
# 更改为True，用户一旦确认他们的电子邮件地址，就会自动登录
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True

# 更改或设置密码后是否自动退出
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE =True
# 更改为True，用户将在重置密码后自动登录
# ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
# 控制会话的生命周期，可选项还有: "False" 和 "True"
# ACCOUNT_SESSION_REMEMBER =None

# 用户注册时是否需要输入邮箱两遍
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE (=False)
# 用户注册时是否需要用户输入两遍密码
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
# 用户不能使用的用户名列表
# ACCOUNT_USERNAME_BLACKLIST =[]
# 加强电子邮件地址的唯一性
# ACCOUNT_UNIQUE_EMAIL =True
# 用户名允许的最小长度的整数
# ACCOUNT_USERNAME_MIN_LENGTH =4
# 使用从社交账号提供者检索的字段(如用户名、邮件)来绕过注册表单
# SOCIALACCOUNT_AUTO_SIGNUP =True

# 设置登录后跳转链接
# LOGIN_REDIRECT_URL (="/")
# 设置退出登录后跳转链接
# ACCOUNT_LOGOUT_REDIRECT_URL (="/")
# 用户登出是否需要确认确认(True表示直接退出，不用确认；False表示需要确认)
# ACCOUNT_LOGOUT_ON_GET =True


# 媒体文件地址
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width': 'auto',
        'height': '250px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        # 'toolbar': 'Custom',

        'toolbar': [
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Blockquote', 'Image']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'tools', 'items': ['Maximize', 'Source']},
        ],
        # 工具栏按钮
        'toolbar_Custom': [
            # 表情 代码块
            ['Smiley', 'CodeSnippet'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['NumberedList', 'BulletedList'],
            # 最大化
            ['Maximize']
        ],
        # 插件
        'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
        # 附加内容
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
        'image_folder': 'editor/images/',
        'theme': 'default',
        'preview_theme': 'github',
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': True,
            'tabSize': 4,
            'lineWrapping': True,
            'autoCloseTags': True,
            'autoCloseBrackets': True,
            'foldCode': True,
            'vimMode': False,
            'showCursorWhenSelecting': True,
            'readOnly': False,
        },
        'emoji': True,
        'search_replace': True,
        'watch': True,
        'flow_chart': True,
        'sequence_diagram': True,
        'toc': True,  # use [TOC] or [toc] to add TOC
        'tex': True,
        'task_list': True,
        'toolbar_modes': 'full',
    }
}

AUTHENTICATION_BACKENDS = (
    # 此项使 Django 后台可独立于 allauth 登录
    'django.contrib.auth.backends.ModelBackend',
    # 配置 allauth 独有的认证方法，如 email 登录
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 设置站点
SITE_ID = 1
# 重定向 url
LOGIN_REDIRECT_URL = '/'

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'verbose',
#         },
#         'file': {
#             'level': 'WARNING',
#             # 'class': 'logging.FileHandler',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'when': 'midnight',
#             'backupCount': 30,
#             'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
#             'formatter': 'verbose',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['file', 'mail_admins'],
#             'level': 'WARNING',
#             'propagate': False,
#         },
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            # 替换 "/path/to/log/file.log" 为实际日志文件的绝对路径
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    },
}

'''
django-allauth 常见设置选项

ACCOUNT_AUTHENTICATION_METHOD (="username" | "email" | "username_email") 指定要使用的登录方法(用户名、电子邮件地址或两者之一)
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS (=3) 邮箱确认邮件的截止日期(天数)
ACCOUNT_EMAIL_VERIFICATION (="optional") 注册中邮件验证方法: "强制(mandatory)"、 "可选(optional)" 或 "否(none)" 之一
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN (=180) 邮件发送后的冷却时间(以秒为单位)
ACCOUNT_LOGIN_ATTEMPTS_LIMIT (=5) 登录尝试失败的次数
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT (=300) 从上次失败的登录尝试，用户被禁止尝试登录的持续时间
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION (=False) 更改为True，用户一旦确认他们的电子邮件地址，就会自动登录
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE (=False) 更改或设置密码后是否自动退出
ACCOUNT_LOGIN_ON_PASSWORD_RESET (=False) 更改为True，用户将在重置密码后自动登录
ACCOUNT_SESSION_REMEMBER (=None) 控制会话的生命周期，可选项还有: "False" 和 "True"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE (=False) 用户注册时是否需要输入邮箱两遍
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE (=True) 用户注册时是否需要用户输入两遍密码
ACCOUNT_USERNAME_BLACKLIST (=[]) 用户不能使用的用户名列表
ACCOUNT_UNIQUE_EMAIL (=True) 加强电子邮件地址的唯一性
ACCOUNT_USERNAME_MIN_LENGTH (=1) 用户名允许的最小长度的整数
SOCIALACCOUNT_AUTO_SIGNUP (=True) 使用从社交账号提供者检索的字段(如用户名、邮件)来绕过注册表单
LOGIN_REDIRECT_URL (="/") 设置登录后跳转链接
ACCOUNT_LOGOUT_REDIRECT_URL (="/") 设置退出登录后跳转链接
ACCOUNT_LOGOUT_ON_GET (=True) 用户登出是否需要确认确认(True表示直接退出，不用确认；False表示需要确认)
'''

# 设置ASGI应用
ASGI_APPLICATION = 'my_blog.asgi.application'

# 设置通道层的通信后台 - 本地测试用
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }

# # 生产环境中使用redis做后台，安装channels_redis
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
            # "hosts": [os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1')],
        },
    },
}
