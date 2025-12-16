# Log Sources

This project processes logs generated directly by the operating system.

Raw log files are not included in the repository for security and privacy reasons.

---

## Windows

- Source: Windows Event Viewer → Security
- Events: Authentication attempts, logon activity, access control
- Export method:

```powershell
wevtutil qe Security /f:text > security.log
