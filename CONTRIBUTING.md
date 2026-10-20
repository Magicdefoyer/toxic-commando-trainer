# Contributing to toxic-commando-trainer

Thanks for your interest in the John Carpenter's Toxic Commando Trainer project.

## Ground rules
- This is a community modding / cheat-research project for **John Carpenter's Toxic Commando** (single-player offline use only).
- Do not submit code that targets other players in multiplayer sessions.
- All memory offsets must be documented with the game build number they were verified against.

## Workflow
1. Fork the repo and create a feature branch: `feat/esp-box-height` or `fix/aob-scan-crash`.
2. Run `pip install -r requirements.txt` and `pytest tests/`.
3. Keep PRs focused — one feature or offset update per PR.
4. Update `docs/offsets.md` when touching `cheat-core/offsets.py`.

## Offset submissions
If you have fresh offsets for a new game patch, open an issue titled `offsets: build <build_id>` with the AOB signatures and the resulting pointers.