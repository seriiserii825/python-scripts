# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A collection of standalone Python CLI utility scripts for web development workflows. Each top-level `.py` file is an independent tool invoked through a numbered menu in `main.py`. The scripts automate tasks like font conversion, project scaffolding, git mirroring, password generation, and CSS calculations.

## Running

```bash
# Uses uv for dependency management (Python 3.10+)
uv run python main.py
```

Individual scripts can also be run directly: `uv run python <script>.py`

## Architecture

- **`main.py`** — Entry point. Displays a numbered menu and dispatches to individual tool functions.
- **Top-level scripts** — Each file exports a single function (e.g., `aspectRatio()`, `generatePassword()`) that `main.py` imports and calls. Scripts are interactive, using `input()` for user prompts.
- **`libs/`** — Shared utility modules: file operations (`file.py`, `createFile.py`), clipboard (`buffer.py` using `pyperclip`/`xclip`), terminal selection menus (`select.py` using `simple-term-menu`), directory helpers, and Rich table formatting (`richTable.py`).
- **`classes/`** — OOP wrappers: `Select` (multi-backend selection: fzf, questionary, term-menu), `SortFiles` (sort files by extension).

## Key Patterns

- Clipboard integration via `pyperclip` and Linux `xclip`/`notify-send` for results
- Terminal menus use `simple-term-menu` (in `libs/select.py`) and `questionary`/`fzf` (in `classes/Select.py`)
- Rich library used for colored output (`from rich import print`) and table formatting
- Scripts are Linux-specific (uses `notify-send`, `xclip`, apt package management)

## Dependencies

Managed with `uv` (see `pyproject.toml`). Key libraries: `rich`, `pyperclip`, `simple-term-menu`, `questionary`, `pyfzf`, `plyer`, `termcolor`, `numpy`/`numba`.
