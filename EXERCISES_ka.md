# სავარჯიშოები

კლასში ერთად ავაწყვეთ `first_web`. ახლა თქვენ ააწყობთ პროექტს
**დამოუკიდებლად**, ცარიელი საქაღალდიდან, და დაამატებთ რამდენიმე გვერდს.

თქვენი მთლიანი Django პროექტი ინახება თქვენს საკუთარ საქაღალდეში:
`submissions/<your-github-username>/`. ჯერ შეასრულეთ
[SUBMITTING_ka.md](SUBMITTING_ka.md)-ის 1–8 ნაბიჯები (fork, clone,
branch, საქაღალდის შექმნა), შემდეგ დაბრუნდით აქ.

## სანამ დაიწყებთ

გჭირდებათ დაინსტალირებული **uv**. შეამოწმეთ ტერმინალში:

```
uv --version
# uv 0.7.5 ...
```

თუ ხედავთ "command not found", დააინსტალირეთ
<https://docs.astral.sh/uv/getting-started/installation/>-დან და
გახსენით **ახალი** ტერმინალი.

## როგორ მოგზაურობს მოთხოვნა

დაიმახსოვრეთ ეს სურათი. ყოველ ახალ გვერდს სამივე ნაწილი სჭირდება:

```
ბრაუზერი ითხოვს /about/-ს
        │
        ▼
urls.py      →  "/about/ ეკუთვნის about_view-ს"
        │
        ▼
views.py     →  about_view(request) ამზადებს მონაცემებს
        │
        ▼
templates/   →  about.html მონაცემებს HTML-ად აქცევს
        │
        ▼
ბრაუზერი აჩვენებს გვერდს
```

---

## ნაწილი 1 — პროექტის შექმნა (ნაბიჯ-ნაბიჯ)

ყველა ბრძანება გაუშვით ტერმინალში. `#`-ით დაწყებული ხაზები აჩვენებს,
რა უნდა დაინახოთ.

### ნაბიჯი 1. შედით თქვენს საქაღალდეში და შექმენით Python პროექტი

რეპოზიტორის ძირიდან:

```
cd submissions/<your-username>
uv init
```

`uv init` ქმნის Python პროექტს აქვე: `pyproject.toml`, `README.md`,
`.python-version` და `main.py`. წაშალეთ `main.py` — Django-ს ის არ
სჭირდება.

**ამიერიდან ყველა ბრძანება გაუშვით
`submissions/<your-username>/`-ის შიგნიდან.**

### ნაბიჯი 2. დააინსტალირეთ Django

```
uv add django
```

ეს ქმნის `.venv` საქაღალდეს (პროექტის საკუთარი Python) და ჩაწერს
Django-ს `pyproject.toml`-ში. გახსენით `pyproject.toml` და შეამოწმეთ:

```toml
dependencies = [
    "django>=5.2",
]
```

### ნაბიჯი 3. შექმენით Django პროექტი

```
uv run django-admin startproject my_site .
```

**არ დაგავიწყდეთ წერტილი `.` ბოლოში.** ის ნიშნავს "შექმენი აქ".
მის გარეშე თქვენს საქაღალდეში ზედმეტი საქაღალდე გაჩნდება.

ახლა გაქვთ:

```
submissions/<your-username>/
├── manage.py          ← Django-ს ყველა ბრძანებას ამით უშვებთ
├── my_site/
│   ├── settings.py    ← პროექტის პარამეტრები
│   ├── urls.py        ← მისამართების სია
│   ├── asgi.py
│   └── wsgi.py
├── pyproject.toml
└── uv.lock
```

### ნაბიჯი 4. გაუშვით პირველად

```
uv run python manage.py migrate
uv run python manage.py runserver
# Starting development server at http://127.0.0.1:8000/
```

გახსენით <http://127.0.0.1:8000/> ბრაუზერში. უნდა დაინახოთ მწვანე
რაკეტა. 🚀

`migrate` ქმნის მონაცემთა ბაზის ფაილს `db.sqlite3`. `runserver`
მუშაობს მანამ, სანამ ტერმინალში არ დააჭერთ **Ctrl + C**-ს. ახლა
გააჩერეთ.

### ნაბიჯი 5. შექმენით აპლიკაცია (app)

პროექტი არის მთელი ვებსაიტი. **აპლიკაცია** არის მისი ერთი ნაწილი.
ჩვენსას დავარქმევთ `pages`:

```
uv run python manage.py startapp pages
```

ახლა უთხარით პროექტს, რომ აპლიკაცია არსებობს. `my_site/settings.py`-ში
დაამატეთ `'pages'` `INSTALLED_APPS`-ის ბოლოს:

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

### ნაბიჯი 6. შექმენით templates საქაღალდე

`manage.py`-ის გვერდით შექმენით საქაღალდე სახელად `templates`. შემდეგ
`my_site/settings.py`-ში იპოვეთ `TEMPLATES` და შეავსეთ `DIRS`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
        ...
```

თქვენი საქაღალდე ახლა ასე გამოიყურება:

```
submissions/<your-username>/
├── manage.py
├── my_site/
├── pages/
│   ├── views.py
│   └── ...
└── templates/
```

### ნაბიჯი 7. თქვენი პირველი გვერდი

**Template** — `templates/home.html`:

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

**View** — `pages/views.py`:

```python
from django.shortcuts import render


def home_view(request):
    return render(request, "home.html")
```

**URL** — `my_site/urls.py`:

```python
from django.contrib import admin
from django.urls import path
from pages.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
]
```

ხელახლა გაუშვით სერვერი და გახსენით <http://127.0.0.1:8000/>. რაკეტის
ნაცვლად უნდა დაინახოთ **Welcome to my site**.

✅ **ნაწილი 1 დასრულებულია**, როცა თქვენი მთავარი გვერდი გამოჩნდება.

---

## ნაწილი 2 — სავარჯიშოები

ყოველ ახალ გვერდს სჭირდება: **template**, **view** და **path**
`urls.py`-ში.

### სავარჯიშო 1 — About გვერდი

შექმენით გვერდი `/about/` მისამართზე, რომელიც თქვენზე მოკლე ტექსტს
აჩვენებს.

მინიშნება: დააკოპირეთ `home.html` როგორც `about.html`, დაწერეთ
`about_view` და დაამატეთ `path('about/', about_view, name="about")`.

### სავარჯიშო 2 — მონაცემების გადაცემა template-ში

View-ს შეუძლია template-ს გადასცეს **ლექსიკონი (dictionary)**. ყოველი
გასაღები ხდება ცვლადი, რომელსაც `{{ }}`-ით დაბეჭდავთ:

```python
def about_view(request):
    context = {"name": "Nina", "city": "Tbilisi", "age": 19}
    return render(request, "about.html", context)
```

```html
<h1>About {{ name }}</h1>
<p>{{ name }} is {{ age }} years old and lives in {{ city }}.</p>
```

შეცვალეთ თქვენი `about_view` ისე, რომ თქვენი სახელი, ქალაქი და ასაკი
ლექსიკონიდან მოდიოდეს და არა HTML-იდან.

### სავარჯიშო 3 — `if` template-ში

Template-ებს საკუთარი `if` აქვთ. ის იყენებს `{% %}`-ს და უნდა
დაიხუროს `{% endif %}`-ით:

```html
{% if age >= 18 %}
    <p>I am an adult.</p>
{% else %}
    <p>I am not an adult yet.</p>
{% endif %}
```

დაამატეთ ეს `about.html`-ში. შეცვალეთ `age` view-ში და განაახლეთ
გვერდი, რომ ორივე შემთხვევა ნახოთ.

### სავარჯიშო 4 — ჰობების სია

შექმენით გვერდი `/hobbies/` მისამართზე. View-ში ააწყვეთ
**ლექსიკონების სია** (ზუსტად როგორც მე-8 ვორქშოფში):

```python
def hobbies_view(request):
    hobbies = [
        {"name": "Football", "hours": 4},
        {"name": "Chess", "hours": 2},
        {"name": "Guitar", "hours": 3},
    ]
    return render(request, "hobbies.html", {"hobbies": hobbies})
```

Template-ში გამოიყენეთ `{% for %}` ციკლი. ლექსიკონის გასაღები
წაიკითხეთ **წერტილით**: `hobby.name` და არა `hobby["name"]`.

```html
<ul>
{% for hobby in hobbies %}
    <li>{{ hobby.name }} - {{ hobby.hours }} hours a week</li>
{% endfor %}
</ul>
<p>I have {{ hobbies|length }} hobbies.</p>
```

გამოიყენეთ თქვენი საკუთარი ჰობები (მინიმუმ 3).

### სავარჯიშო 5 — ნავიგაციის მენიუ

დაამატეთ მენიუ **ყველა** გვერდზე, რომ მათ შორის გადასვლა შეძლოთ.
გამოიყენეთ `name=`, რომელიც თითოეულ path-ს დაარქვით:

```html
<nav>
    <a href="{% url 'home' %}">Home</a> |
    <a href="{% url 'about' %}">About</a> |
    <a href="{% url 'hobbies' %}">Hobbies</a>
</nav>
```

`{% url 'about' %}` ხდება `/about/`. თუ მოგვიანებით `urls.py`-ში
მისამართს შეცვლით, ბმულები მაინც იმუშავებს.

✅ **ნაწილი 2 დასრულებულია**, როცა შეგიძლიათ დააჭიროთ Home → About →
Hobbies და უკან, და ყველა გვერდი თავის მონაცემებს აჩვენებს.

---

## ბონუსი (არასავალდებულო)

1. **ჰობები ჯერ არ არის.** `for` ციკლის შიგნით დაამატეთ `{% empty %}`
   შეტყობინებით. სია გააცარიელეთ და შეამოწმეთ, რომ შეტყობინება ჩანს.
2. **ჯამური საათები.** `hobbies_view`-ში ციკლით დაითვალეთ ჯამური
   საათები (აკუმულატორი მე-4 ვორქშოფიდან) და აჩვენეთ გვერდზე.
3. **ერთი მენიუ და არა სამი.** `<nav>`-ის ყველა გვერდზე კოპირება
   განმეორებაა. მოძებნეთ `{% extends %}` და `{% block %}`
   [Django template-ების დოკუმენტაციაში](https://docs.djangoproject.com/en/5.2/ref/templates/language/#template-inheritance),
   შექმენით `base.html` მენიუთი და ყველა გვერდმა გააფართოოს (extend)
   ის.

---

## გავრცელებული შეცდომები

| ხედავთ | რატომ | გამოსწორება |
|--------|-------|-------------|
| `TemplateDoesNotExist at /` | Django ვერ პოულობს HTML ფაილს | შეამოწმეთ `DIRS` `settings.py`-ში, რომ `templates/` არის **`manage.py`-ის გვერდით**, და რომ ფაილის სახელი view-ში ზუსტად ისევე წერია |
| `Page not found (404)` | არცერთი path არ ემთხვევა მისამართს | შეამოწმეთ `urls.py`. `'about/'`-ს ბოლოში აქვს დახრილი ხაზი და დასაწყისში **არ** აქვს |
| `NameError: name 'about_view' is not defined` | `urls.py`-მ არ იცის ეს view | დაამატეთ ის `from pages.views import ...` ხაზში |
| `NoReverseMatch` | `{% url 'abuot' %}` იყენებს სახელს, რომელიც არ არსებობს | ზუსტად დაამთხვიეთ `urls.py`-ში მითითებულ `name=`-ს |
| `{{ name }}` არაფერს აჩვენებს | ეს გასაღები context ლექსიკონში არ არის | შეამოწმეთ გასაღების მართლწერა view-ში |
| `That port is already in use` | სხვა `runserver` ჯერ კიდევ მუშაობს | იპოვეთ ის ტერმინალი და დააჭირეთ **Ctrl + C**-ს |
| `No module named 'django'` | გაუშვით `python` და არა `uv run python` | ბრძანებები ყოველთვის დაიწყეთ `uv run`-ით |
| `can't open file 'manage.py'` | არასწორ საქაღალდეში ხართ | ჯერ `cd submissions/<your-username>` |

## სწრაფი ცნობარი

| ამოცანა | ბრძანება / კოდი |
|---------|-----------------|
| ახალი Python პროექტი აქ | `uv init` |
| Django-ს ინსტალაცია | `uv add django` |
| Django პროექტის შექმნა | `uv run django-admin startproject my_site .` |
| აპლიკაციის შექმნა | `uv run python manage.py startapp pages` |
| მონაცემთა ბაზის შექმნა | `uv run python manage.py migrate` |
| სერვერის გაშვება | `uv run python manage.py runserver` |
| სერვერის გაჩერება | **Ctrl + C** |
| View | `def about_view(request): return render(request, "about.html", context)` |
| URL | `path('about/', about_view, name="about")` |
| ცვლადის დაბეჭდვა | `{{ name }}` |
| ლექსიკონის გასაღები | `{{ hobby.name }}` |
| If | `{% if ... %} ... {% else %} ... {% endif %}` |
| ციკლი | `{% for x in items %} ... {% endfor %}` |
| ბმული | `<a href="{% url 'about' %}">About</a>` |
