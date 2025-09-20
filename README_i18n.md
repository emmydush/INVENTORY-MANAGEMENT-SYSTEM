# Internationalization (i18n) Implementation

This document describes the multilingual support implementation for the Inventory Management System.

## Supported Languages

The system currently supports three languages:
1. English (en)
2. French (fr)
3. Kinyarwanda (rw)

## Implementation Details

### 1. Django Settings Configuration

The following settings were added to `settings.py`:

```python
# Internationalization
LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
    ('fr', 'Français'),
    ('rw', 'Kinyarwanda'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
```

### 2. URL Configuration

Language switching URLs were added to `urls.py`:

```python
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    # ... existing URL patterns
)
```

### 3. Template Implementation

Language switching is implemented in `templates/base.html` with a dropdown menu:

```html
<!-- Language Selector -->
<li class="nav-item dropdown">
    <a class="nav-link text-white dropdown-toggle" href="#" id="languageDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-globe me-1" viewBox="0 0 16 16">
            <path d="M8 1a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm2 4a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm-2 2a2 2 0 1 0 0 4 2 2 0 0 0 0-4Z"/>
        </svg>
        {{ LANGUAGE_CODE|upper }}
    </a>
    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="languageDropdown">
        <li><a class="dropdown-item {% if LANGUAGE_CODE == 'en' %}active{% endif %}" href="{% url 'set_language' 'en' %}">English</a></li>
        <li><a class="dropdown-item {% if LANGUAGE_CODE == 'fr' %}active{% endif %}" href="{% url 'set_language' 'fr' %}">Français</a></li>
        <li><a class="dropdown-item {% if LANGUAGE_CODE == 'rw' %}active{% endif %}" href="{% url 'set_language' 'rw' %}">Kinyarwanda</a></li>
    </ul>
</li>
```

### 4. Translation Files

Translation files are located in the `locale/` directory with the following structure:
- `locale/en/LC_MESSAGES/django.po` (English translations)
- `locale/fr/LC_MESSAGES/django.po` (French translations)
- `locale/rw/LC_MESSAGES/django.po` (Kinyarwanda translations)

Compiled binary files:
- `locale/en/LC_MESSAGES/django.mo`
- `locale/fr/LC_MESSAGES/django.mo`
- `locale/rw/LC_MESSAGES/django.mo`

## Adding New Languages

To add a new language:

1. Add the language code to the `LANGUAGES` setting in `settings.py`
2. Create a new directory in `locale/` with the language code
3. Create `LC_MESSAGES` subdirectory
4. Create or copy the `django.po` file with translations
5. Compile the translations to `django.mo` file

## Updating Translations

To update translations:

1. Edit the appropriate `.po` file in `locale/[language]/LC_MESSAGES/`
2. Run the compilation script: `python compile_translations.py`
3. Restart the server to see changes

## Testing Language Switching

Language switching can be tested by accessing URLs with language prefixes:
- English: `/en/dashboard/`
- French: `/fr/dashboard/`
- Kinyarwanda: `/rw/dashboard/`