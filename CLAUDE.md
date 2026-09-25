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
- **`libs/py-libs`** — git submodule + uv workspace member providing the shared `py_libs` package (`Select`, `Clipboard`, `Notification`, …). Use it instead of local helpers: `from py_libs.Select import Select`.
- **`libs/`** — `buffer.py` (`addToClipBoardFile`: copies a file's contents via `xclip`, no py_libs equivalent). Other modules there are legacy and unused.
- **`classes/`** — `SortFiles` (sort files by extension).

## Key Patterns

- Clipboard: `py_libs.Clipboard.write()` (also sends a desktop notification with the copied text — so no separate `notify-send`). Exception: `generatePassword.py` keeps `pyperclip` + a generic notification so the password isn't shown in the notification
- Selection menus: `py_libs.Select` (`select_fzf_one`, `select_multiple`, `select_questionary`, …)
- Rich library used for colored output (`from rich import print`) and table formatting
- Scripts are Linux-specific (uses `notify-send`, `xclip`, apt package management)

## Dependencies

Managed with `uv` (see `pyproject.toml`). Key libraries: `rich`, `pyperclip`, `simple-term-menu`, `questionary`, `pyfzf`, `plyer`, `termcolor`, `numpy`/`numba`.
