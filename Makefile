.PHONY: debug
debug:
    poetry run uvicorn src.main:app --reload