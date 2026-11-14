# Git & GitHub – Software Engineering class demo

This is a small educational repository used in the presentation.

## Requirements
- Git 2.23 or newer (for `git switch`)
- Python 3.10 or newer

## Run the tests
From the project root:

```bash
python -m unittest discover -s tests -v
```

Expected result: 6 tests pass.

## Repository contents
- `src/auth.py`: small illustrative login validation function
- `tests/test_auth.py`: six unit-test methods
- `docs/requirements.md`: sample requirement identifiers
- `.github/workflows/tests.yml`: GitHub Actions workflow for unit tests
- `.gitignore`: ignores local Python files and `.env`

## GitHub setup
Create an empty repository on GitHub, then from this directory run:

```bash
git init
git branch -M main
git add .
git commit -m "chore: initialize demo"
git remote add origin <REPO_URL>
git push -u origin main
```

Replace `<REPO_URL>` with the URL of your repository.

## Important security note
`src/auth.py` is deliberately simple and is only for teaching Git, testing, and regression testing. It is not secure authentication code and must not be used for real passwords or production login systems. Never commit credentials, tokens, private keys, or `.env` files.

## Development workflow

- Create a feature branch before making changes.
- Run unit tests before committing.
- Commit changes with a descriptive message.
- Push the feature branch to GitHub.
- Open a Pull Request to merge changes into main.
