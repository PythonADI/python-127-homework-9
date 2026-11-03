# Exercises

In class we built `first_web` together. Now you build one **on your
own**, from an empty folder, and add a few pages to it.

Your whole Django project lives inside your own folder:
`submissions/<your-github-username>/`. Follow [SUBMITTING.md](SUBMITTING.md)
steps 1–8 first (fork, clone, branch, create the folder), then come
back here.

## Before you start

You need **uv** installed. Check in the terminal:

```
uv --version
# uv 0.7.5 ...
```

If you get "command not found", install it from
<https://docs.astral.sh/uv/getting-started/installation/> and open a
**new** terminal.

## How a request travels

Keep this picture in mind. Every page you add needs all three parts:

```
browser asks for /about/
        │
        ▼
urls.py      →  "/about/ belongs to about_view"
        │
        ▼
views.py     →  about_view(request) prepares the data
        │
        ▼
templates/   →  about.html turns the data into HTML
        │
        ▼
browser shows the page
```

---

## Part 1 — Set up the project (step by step)

Run every command in the terminal. Lines starting with `#` show what
you should see.

### Step 1. Go into your folder and create a Python project

From the root of the repository:

```
cd submissions/<your-username>
uv init
```

`uv init` creates a Python project right here: `pyproject.toml`,
`README.md`, `.python-version` and a `main.py`. Delete `main.py` —
Django does not need it.

**From now on, run every command from inside
`submissions/<your-username>/`.**

### Step 2. Install Django

```
uv add django
```

This creates a `.venv` folder (the project's own Python) and writes
Django into `pyproject.toml`. Open `pyproject.toml` and check:

```toml
dependencies = [
    "django>=5.2",
]
```

### Step 3. Create the Django project

```
uv run django-admin startproject my_site .
```

**Do not forget the dot `.` at the end.** It means "create it here".
Without it you get an extra folder inside your folder.

You now have:

```
submissions/<your-username>/
├── manage.py          ← you run every Django command through this
├── my_site/
│   ├── settings.py    ← project settings
│   ├── urls.py        ← the list of addresses
│   ├── asgi.py
│   └── wsgi.py
├── pyproject.toml
└── uv.lock
```

### Step 4. Run it for the first time

```
uv run python manage.py migrate
uv run python manage.py runserver
# Starting development server at http://127.0.0.1:8000/
```

Open <http://127.0.0.1:8000/> in your browser. You should see the
green rocket. 🚀

`migrate` creates the database file `db.sqlite3`. `runserver` keeps
running until you press **Ctrl + C** in the terminal. Stop it now.

### Step 5. Create an app

A project is the whole website. An **app** is one part of it. Ours
will be called `pages`:

```
uv run python manage.py startapp pages
```

Now tell the project the app exists. In `my_site/settings.py` add
`'pages'` to the end of `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
]
```

### Step 6. Create the templates folder

Next to `manage.py`, create a folder called `templates`. Then, in
`my_site/settings.py`, find `TEMPLATES` and fill in `DIRS`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
        ...
```

Your folder now looks like this:

```
submissions/<your-username>/
├── manage.py
├── my_site/
├── pages/
│   ├── views.py
│   └── ...
└── templates/
```

### Step 7. Your first page

**The template** — `templates/home.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Site</title>
</head>
<body>
    <h1>Welcome to my site</h1>
</body>
</html>
```

**The view** — `pages/views.py`:

```python
from django.shortcuts import render


def home_view(request):
    return render(request, "home.html")
```

**The URL** — `my_site/urls.py`:

```python
from django.contrib import admin
from django.urls import path
from pages.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
]
```

Run the server again and open <http://127.0.0.1:8000/>. You should see
**Welcome to my site** instead of the rocket.

✅ **Part 1 is done** when your home page shows up.

---

## Part 2 — Exercises

For each new page you need: a **template**, a **view**, and a **path**
in `urls.py`.

### Exercise 1 — About page

Make a page at `/about/` that shows a short text about you.

Hint: copy `home.html` to `about.html`, write `about_view`, and add
`path('about/', about_view, name="about")`.

### Exercise 2 — Send data to the template

A view can send a **dictionary** to the template. Each key becomes a
variable you can print with `{{ }}`:

```python
def about_view(request):
    context = {"name": "Nina", "city": "Tbilisi", "age": 19}
    return render(request, "about.html", context)
```

```html
<h1>About {{ name }}</h1>
<p>{{ name }} is {{ age }} years old and lives in {{ city }}.</p>
```

Change your `about_view` so your name, city and age come from the
dictionary, not from the HTML.

### Exercise 3 — `if` in a template

Templates have their own `if`. It uses `{% %}` and must be closed with
`{% endif %}`:

```html
{% if age >= 18 %}
    <p>I am an adult.</p>
{% else %}
    <p>I am not an adult yet.</p>
{% endif %}
```

Add this to `about.html`. Change `age` in the view and refresh the page
to see both branches.

### Exercise 4 — List of hobbies

Make a page at `/hobbies/`. In the view, build a **list of
dictionaries** (just like Workshop 8):

```python
def hobbies_view(request):
    hobbies = [
        {"name": "Football", "hours": 4},
        {"name": "Chess", "hours": 2},
        {"name": "Guitar", "hours": 3},
    ]
    return render(request, "hobbies.html", {"hobbies": hobbies})
```

In the template, loop with `{% for %}`. Read a dictionary key with a
**dot**: `hobby.name`, not `hobby["name"]`.

```html
<ul>
{% for hobby in hobbies %}
    <li>{{ hobby.name }} - {{ hobby.hours }} hours a week</li>
{% endfor %}
</ul>
<p>I have {{ hobbies|length }} hobbies.</p>
```

Use your own hobbies (at least 3).

### Exercise 5 — Navigation menu

Add a menu to **every** page so you can click between them. Use the
`name=` you gave each path:

```html
<nav>
    <a href="{% url 'home' %}">Home</a> |
    <a href="{% url 'about' %}">About</a> |
    <a href="{% url 'hobbies' %}">Hobbies</a>
</nav>
```

`{% url 'about' %}` becomes `/about/`. If you later change the address
in `urls.py`, the links still work.

✅ **Part 2 is done** when you can click Home → About → Hobbies and
back, and every page shows its data.

---

## Bonus (optional)

1. **No hobbies yet.** Inside the `for` loop add `{% empty %}` with a
   message. Make the list empty and check the message shows.
2. **Total hours.** In `hobbies_view` count the total hours with a loop
   (the accumulator from Workshop 4) and show it on the page.
3. **One menu, not three.** Copying the `<nav>` into every page is
   repetitive. Look up `{% extends %}` and `{% block %}` in the
   [Django template docs](https://docs.djangoproject.com/en/5.2/ref/templates/language/#template-inheritance),
   make a `base.html` with the menu, and have every page extend it.

---

## Common errors

| You see | Why | Fix |
|---------|-----|-----|
| `TemplateDoesNotExist at /` | Django cannot find the HTML file | Check `DIRS` in `settings.py`, that `templates/` is **next to `manage.py`**, and the file name is spelled the same in the view |
| `Page not found (404)` | No path matches the address | Check `urls.py`. `'about/'` has a slash at the end and **no** slash at the start |
| `NameError: name 'about_view' is not defined` | `urls.py` does not know the view | Add it to the `from pages.views import ...` line |
| `NoReverseMatch` | `{% url 'abuot' %}` uses a name that does not exist | Match the `name=` in `urls.py` exactly |
| `{{ name }}` shows nothing | The key is not in the context dictionary | Check the spelling of the key in the view |
| `That port is already in use` | Another `runserver` is still running | Find that terminal and press **Ctrl + C** |
| `No module named 'django'` | You ran `python` instead of `uv run python` | Always start commands with `uv run` |
| `can't open file 'manage.py'` | You are in the wrong folder | `cd submissions/<your-username>` first |

## Quick reference

| Task | Command / code |
|------|----------------|
| New Python project here | `uv init` |
| Install Django | `uv add django` |
| Create Django project | `uv run django-admin startproject my_site .` |
| Create app | `uv run python manage.py startapp pages` |
| Create database | `uv run python manage.py migrate` |
| Start server | `uv run python manage.py runserver` |
| Stop server | **Ctrl + C** |
| View | `def about_view(request): return render(request, "about.html", context)` |
| URL | `path('about/', about_view, name="about")` |
| Print a variable | `{{ name }}` |
| Dictionary key | `{{ hobby.name }}` |
| If | `{% if ... %} ... {% else %} ... {% endif %}` |
| Loop | `{% for x in items %} ... {% endfor %}` |
| Link | `<a href="{% url 'about' %}">About</a>` |
