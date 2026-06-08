# Mail Gen

Simple email generation app using Python and Ollama.

## Project structure

- `app.py` - front-end script or streamlit app entrypoint
- `src/` - Python package with project logic
- `src/__init__.py` - package marker for `src`
- `tests/` - unit tests
- `requirements.txt` - Python dependencies
- `.gitignore` - files and folders Git should skip

## Git workflow

1. `git add .gitignore`
2. `git commit -m "Add .gitignore"`
3. `git push -u origin main`

## Notes

- `.gitignore` keeps generated files out of Git, like `__pycache__/`, `.pytest_cache/`, and `enu/`.
- Test code uses `monkeypatch` to replace real API calls during testing.
- The app code still uses the real API when deployed.
