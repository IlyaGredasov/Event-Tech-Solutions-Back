PYBIN = "python"

run_linter:
	ruff check

fix_linter:
	ruff check --fix

load_fixtures:
	$(PYBIN) src/manage.py loaddata src/fixtures/groups.json
