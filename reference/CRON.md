## Self-Management
You can manage your own cron jobs via shell commands:
- List: `openclaw cron list`
- Add: `openclaw cron add --name <name> --agent ws-marketing --cron "<expr>" --tz "Europe/Amsterdam" --session isolated --deliver --channel last --message "<prompt>"`
- Edit: `openclaw cron edit <name> --cron "<expr>"`
- Remove: `openclaw cron rm <name>`
- Test: `openclaw cron run <name>`