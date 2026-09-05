# group25082026
https://www.jetbrains.com/pycharm/download/?section=windows

git config --global user.name "Axel F"
git config --global user.email "Axel@gmail.com"

git init
git remote add origin ###git@github.com:smartguy-coder/group25082026.git###
git pull origin main

- uv init app
- cd app
- uv sync
- uv add pytest
- Ctrl-Alt-l
- uv run -m pytest .
- uv run -m pytest . -v
- uv run -m pytest . -s
- uv run -m pytest . -v -s
- uv run -m pytest tests\test_model_bank_account_1.py::TestBankAccountATMMashine -v -s


Налаштування (сучасний шлях — Rulesets):

Репозиторій → Settings → Rules → Rulesets → New ruleset → New branch ruleset
Назва довільна, Enforcement status: Active
Target branches → Add target → Include default branch (або явно main)
Увімкни Require a pull request before merging — щоб не можна було пушнути в main напряму в обхід перевірок
Увімкни Require status checks to pass → Add checks → знайди і додай pytest
Create
