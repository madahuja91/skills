# Tech Architecture Remediation Hints

| Gap | Fix |
|-----|-----|
| Empty layers | Use package/folder stereotypes + descriptors from Discovery |
| Runtime claimed without evidence | Downgrade analysis_scope to static |
| Missing CMP IDs | Assign CMP-{slug} consistently |
| No debt score | Compute from complexity proxies: fan-in, size, deprecated tech from Discover |
