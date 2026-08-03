# Contributing to Agent Body Skills

Thanks for improving the Agent Body Skill catalog.

## Add or update a Skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Use lowercase letters, digits, and hyphens in `<skill-name>`; keep it under 64 characters.
3. Add YAML frontmatter containing only `name` and `description`.
4. Make `name` exactly match the directory name.
5. Make `description` explain both what the Skill does and when an agent should use it.
6. Keep the body procedural and concise. Put large API references in `references/`.
7. Never commit API keys, tokens, customer data, or environment-specific secrets.
8. Run the local validation command before opening a pull request:

   ```bash
   python .github/scripts/validate_skills.py
   ```

## Pull requests

Describe the user-facing capability, the MCP server/tool names involved, and any behavior or safety changes. Add or update examples when they clarify triggering or result handling.
