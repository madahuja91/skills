# Integration Remediation Hints

| Gap | Fix |
|-----|-----|
| Missed file/FTP/batch | Search for `.ctl`, scheduler XML, `ftp`, `JMS`, `MQ`, `Axis`, `WSDL` |
| Sync/async unclear | Default hybrid + low confidence; cite retry/queue evidence |
| Fake latency metrics | Remove metrics or mark monitoring unavailable |
