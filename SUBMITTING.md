# How to submit — with a Pull Request

You've never done this before, and that's fine — every step is here.
A **fork** is your own copy of this repository on GitHub. A **branch**
is where your changes live. A **Pull Request (PR)** asks to bring your
branch's changes into the original repository.

> Everywhere you see `<your-username>` below, replace the whole thing
> — angle brackets included — with your actual GitHub username. Typing
> `<your-username>` literally into a command will not work.

## 1. Install Git

- **Windows:** install [Git for Windows](https://git-scm.com/download/win). Use "Git Bash" (installed alongside it) as your terminal for the rest of these steps.
- **macOS:** open Terminal and run `git --version` — if it's not installed, macOS will prompt you to install it.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) or your distro's package manager.

Confirm it worked:
```
git --version
```

## 2. Create a GitHub account

If you don't have one, sign up at [github.com](https://github.com).

## 3. Configure Git with your name and email

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 4. Set up how Git will sign you in

Your first push in step 10 will ask you to prove it's really you. Set
this up now so it doesn't surprise you later.

- **Windows:** Git for Windows includes Git Credential Manager. The
  first time you push, a browser tab opens — sign in to GitHub there
  and approve it. After that, Git remembers you.
- **macOS / Linux:** GitHub no longer accepts your account password
  for `git push`. The easiest fix is the [GitHub CLI](https://cli.github.com/):
  install it, then run:
  ```
  gh auth login
  ```
  Choose **GitHub.com**, **HTTPS**, and **Login with a web browser**,
  then follow the prompts. This also makes Git itself remember your
  login for future pushes.

## 5. Fork this repository

Go to this repository's GitHub page —
`https://github.com/PythonADI/python-127-homework-9` — and click
**Fork** (top right). Use the default settings. This creates your own
copy at `https://github.com/<your-username>/python-127-homework-9`.

## 6. Clone YOUR fork

```
git clone https://github.com/<your-username>/python-127-homework-9.git
cd python-127-homework-9
```

## 7. Create a branch named after your GitHub username

```
git checkout -b <your-username>
```

Expected output: `Switched to a new branch '<your-username>'`.

## 8. Create your folder and build your project

Create a folder inside `submissions/` named after your GitHub
username:

```
mkdir -p submissions/<your-username>
```

Now open [EXERCISES.md](EXERCISES.md) and do Part 1 and Part 2. Your
whole Django project goes **inside this folder**, so you end up with:

```
submissions/<your-username>/manage.py
submissions/<your-username>/pyproject.toml
submissions/<your-username>/uv.lock
submissions/<your-username>/my_site/
submissions/<your-username>/pages/
submissions/<your-username>/templates/
```

**Only your own folder.** Do not edit `README.md`, `EXERCISES.md`,
`SUBMITTING.md`, or any other student's folder.

## 9. Check your project before committing

From inside your folder:

```
cd submissions/<your-username>
uv run python manage.py runserver
```

Open <http://127.0.0.1:8000/>, <http://127.0.0.1:8000/about/> and
<http://127.0.0.1:8000/hobbies/>. Every page must open and the menu
must work. Stop the server with **Ctrl + C**, then go back to the root
of the repository:

```
cd ../..
git status
```

`git status` must **not** list `.venv/` or `db.sqlite3` — the
repository's `.gitignore` hides them. `.venv` is huge, and everyone
creates their own with `uv sync`.

## 10. Commit and push your branch

```
git add submissions/<your-username>
git commit -m "Add homework 9"
git push -u origin <your-username>
```

If this is your first push, it will ask you to sign in (see step 4) —
follow the prompt, then the push completes.

## 11. Open the Pull Request

GitHub will print a link after the push, and also show a
"Compare & pull request" banner on your fork's page — click either
one. Or open one manually from
`https://github.com/PythonADI/python-127-homework-9/compare`:

- **base repository:** `PythonADI/python-127-homework-9`, branch `main`
- **head repository:** `<your-username>/python-127-homework-9`, branch `<your-username>`

**Title:** `Homework 9 - Your Name` (your real name).

Fill in the checklist in the PR description template, then click
**Create pull request** (not "Create draft pull request").

## 12. Wait for review

You don't have write access to the original repository, so you can't
push to it directly — only a Pull Request can bring your changes in.
Your instructor is automatically requested as a reviewer.

If they ask for changes, make them on the **same branch** and push
again:

```
git add submissions/<your-username>
git commit -m "Address review feedback"
git push
```

Don't open a second PR — this one updates automatically.
