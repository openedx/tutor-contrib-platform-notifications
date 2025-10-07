.DEFAULT_GOAL := help
.PHONY: docs
SRC_DIRS = ./tutornotifications

# Warning: These checks are not necessarily run on every PR.
test: test-lint test-types test-format  # Run some static checks.

test-format: ## Run code formatting tests
	hatch run quality:test-format

test-lint: ## Run code linting tests
	hatch run quality:test-lint

test-types: ## Run type checks.
	hatch run quality:test-types

format: ## Format code
	hatch run quality:format

fix-lint: ## Fix lint errors automatically
	hatch run quality:fix-lint

version: ## Print the current tutor-cairn version
	@python -c 'import io, os; about = {}; exec(io.open(os.path.join("tutornotifications", "__about__.py"), "rt", encoding="utf-8").read(), about); print(about["__version__"])'

ESCAPE = 
help: ## Print this help
	@grep -E '^([a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/@               $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' | tr '@' '\n' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'
