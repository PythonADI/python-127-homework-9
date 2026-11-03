# როგორ გავაგზავნოთ — Pull Request-ით

ეს არასდროს გაგიკეთებიათ და არაუშავს — ყველა ნაბიჯი აქ არის. **Fork**
არის ამ რეპოზიტორის თქვენი საკუთარი ასლი GitHub-ზე. **Branch** არის
ადგილი, სადაც თქვენი ცვლილებები ინახება. **Pull Request (PR)** სთხოვს
თქვენი branch-ის ცვლილებების შერწყმას ორიგინალ რეპოზიტორთან.

> ყველგან, სადაც ხედავთ `<your-username>`-ს, ჩაანაცვლეთ ის — კუთხოვანი
> ფრჩხილების ჩათვლით — თქვენი რეალური GitHub username-ით. `<your-username>`-ის
> სიტყვასიტყვით აკრეფა ბრძანებაში არ იმუშავებს.

## 1. დააინსტალირეთ Git

- **Windows:** დააინსტალირეთ [Git for Windows](https://git-scm.com/download/win). გამოიყენეთ "Git Bash" ტერმინალად შემდეგი ნაბიჯებისთვის.
- **macOS:** გახსენით Terminal და გაუშვით `git --version` — თუ არ არის დაინსტალირებული, macOS შემოგთავაზებთ დაინსტალირებას.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) ან თქვენი დისტრიბუტივის პაკეტების მენეჯერი.

დარწმუნდით რომ იმუშავა:
```
git --version
```

## 2. შექმენით GitHub ანგარიში

თუ არ გაქვთ, დარეგისტრირდით [github.com](https://github.com)-ზე.

## 3. დააკონფიგურირეთ Git თქვენი სახელით და ელფოსტით

```
git config --global user.name "თქვენი სახელი"
git config --global user.email "you@example.com"
```

## 4. მოაწყვეთ შესვლის (sign-in) მეთოდი

პირველი push-ი (მე-10 ნაბიჯში) მოგთხოვთ დამტკიცებას, რომ ეს მართლა
თქვენ ხართ. მოაწყვეთ ეს ახლა, რომ მოგვიანებით არ გაგიკვირდეთ.

- **Windows:** Git for Windows შეიცავს Git Credential Manager-ს. პირველი
  push-ისას გაიხსნება ბრაუზერის ჩანართი — შედით იქ GitHub-ზე და
  დაადასტურეთ. ამის შემდეგ Git დაიმახსოვრებს თქვენ.
- **macOS / Linux:** GitHub-მა შეწყვიტა ანგარიშის პაროლის მიღება
  `git push`-ისთვის. უმარტივესი გამოსავალია [GitHub CLI](https://cli.github.com/):
  დააინსტალირეთ და გაუშვით:
  ```
  gh auth login
  ```
  აირჩიეთ **GitHub.com**, **HTTPS**, და **Login with a web browser**,
  შემდეგ მიჰყევით ინსტრუქციებს. ეს ასევე დააფიქსირებს თქვენს
  შესვლას მომავალი push-ებისთვის.

## 5. Fork-ი გაუკეთეთ ამ რეპოზიტორს

გადადით ამ რეპოზიტორის GitHub გვერდზე —
`https://github.com/PythonADI/python-127-homework-9` — და დააჭირეთ
**Fork**-ს (ზედა მარჯვენა კუთხეში). გამოიყენეთ ნაგულისხმევი
პარამეტრები. ეს შექმნის თქვენს საკუთარ ასლს:
`https://github.com/<your-username>/python-127-homework-9`.

## 6. Clone გაუკეთეთ თქვენს fork-ს

```
git clone https://github.com/<your-username>/python-127-homework-9.git
cd python-127-homework-9
```

## 7. შექმენით branch თქვენი GitHub username-ის სახელით

```
git checkout -b <your-username>
```

მოსალოდნელი შედეგი: `Switched to a new branch '<your-username>'`.

## 8. შექმენით თქვენი საქაღალდე და ააწყვეთ პროექტი

შექმენით საქაღალდე `submissions/`-ის შიგნით, დასახელებული თქვენი
GitHub username-ით:

```
mkdir -p submissions/<your-username>
```

ახლა გახსენით [EXERCISES_ka.md](EXERCISES_ka.md) და შეასრულეთ
ნაწილი 1 და ნაწილი 2. თქვენი მთლიანი Django პროექტი იქმნება **ამ
საქაღალდის შიგნით**, რომ საბოლოოდ გქონდეთ:

```
submissions/<your-username>/manage.py
submissions/<your-username>/pyproject.toml
submissions/<your-username>/uv.lock
submissions/<your-username>/my_site/
submissions/<your-username>/pages/
submissions/<your-username>/templates/
```

**მხოლოდ თქვენი საკუთარი საქაღალდე.** არ შეცვალოთ `README.md`,
`EXERCISES.md`, `SUBMITTING.md`, ან სხვა სტუდენტის საქაღალდე.

## 9. შეამოწმეთ პროექტი commit-მდე

თქვენი საქაღალდის შიგნიდან:

```
cd submissions/<your-username>
uv run python manage.py runserver
```

გახსენით <http://127.0.0.1:8000/>, <http://127.0.0.1:8000/about/> და
<http://127.0.0.1:8000/hobbies/>. ყველა გვერდი უნდა იხსნებოდეს და მენიუ
უნდა მუშაობდეს. გააჩერეთ სერვერი **Ctrl + C**-ით, შემდეგ დაბრუნდით
რეპოზიტორის ძირში:

```
cd ../..
git status
```

`git status`-ში **არ** უნდა ჩანდეს `.venv/` ან `db.sqlite3` —
რეპოზიტორის `.gitignore` მათ მალავს. `.venv` ძალიან დიდია და ყველა
თავისას ქმნის `uv sync`-ით.

## 10. Commit და push გაუკეთეთ თქვენს branch-ს

```
git add submissions/<your-username>
git commit -m "Add homework 9"
git push -u origin <your-username>
```

თუ ეს თქვენი პირველი push-ია, მოგთხოვთ შესვლას (იხილეთ მე-4 ნაბიჯი) —
მიჰყევით მითითებას, შემდეგ push დასრულდება.

## 11. გახსენით Pull Request

GitHub push-ის შემდეგ დაბეჭდავს ბმულს, ასევე გამოჩნდება
"Compare & pull request" ბანერი თქვენი fork-ის გვერდზე — დააჭირეთ
რომელიმეს. ან გახსენით ერთი ხელით
`https://github.com/PythonADI/python-127-homework-9/compare`-დან:

- **base repository:** `PythonADI/python-127-homework-9`, branch `main`
- **head repository:** `<your-username>/python-127-homework-9`, branch `<your-username>`

**სათაური:** `Homework 9 - თქვენი სახელი` (თქვენი რეალური სახელი).

შეავსეთ checklist PR-ის აღწერაში, შემდეგ დააჭირეთ
**Create pull request**-ს (არა "Create draft pull request").

## 12. დაელოდეთ განხილვას

თქვენ არ გაქვთ write წვდომა ორიგინალ რეპოზიტორზე, ამიტომ ვერ
დააგზავნით პირდაპირ — მხოლოდ Pull Request-ს შეუძლია თქვენი
ცვლილებების შეტანა. ინსტრუქტორი ავტომატურად ემატება როგორც
reviewer.

თუ ცვლილებებს მოითხოვენ, გააკეთეთ ისინი იმავე branch-ზე და
თავიდან push გაუკეთეთ:

```
git add submissions/<your-username>
git commit -m "Address review feedback"
git push
```

არ გახსნათ მეორე PR — ეს ავტომატურად განახლდება.
