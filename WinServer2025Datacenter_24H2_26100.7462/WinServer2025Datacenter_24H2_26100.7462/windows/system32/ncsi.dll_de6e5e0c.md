# Binary Specification: ncsi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ncsi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `de6e5e0c3129a27536f2c3afdf878a0a71953a41cdb2054f46825399f8aa3bcf`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NcsiAllocateAndGetConnectivityStatusSet` | `0xF570` | 39 | UnwindData |  |
| 10 | `NcsiPerformReprobe` | `0x2F700` | 752 | UnwindData |  |
| 4 | `NcsiFreeConnectivityStatusSet` | `0x38870` | 52 | UnwindData |  |
| 8 | `NcsiNotifySessionChange` | `0x38C00` | 150 | UnwindData |  |
| 2 | `NcsiDeregisterConnectivityStatusChange` | `0x509F0` | 147 | UnwindData |  |
| 3 | `NcsiDeregisterDiagnosticsInfoChange` | `0x50A90` | 110 | UnwindData |  |
| 5 | `NcsiGetCaptivePortalHosts` | `0x50B10` | 507 | UnwindData |  |
| 6 | `NcsiGetWebProbeConfig` | `0x50D20` | 411 | UnwindData |  |
| 9 | `NcsiPerformRefresh` | `0x50ED0` | 523 | UnwindData |  |
| 11 | `NcsiRegisterConnectivityStatusChange` | `0x510F0` | 210 | UnwindData |  |
| 12 | `NcsiRegisterDiagnosticsInfoChange` | `0x511D0` | 195 | UnwindData |  |
| 13 | `NcsiUpdateClientPresence` | `0x512A0` | 1,106 | UnwindData |  |
| 7 | `NcsiIdentifyUserSpecificProxies` | `0x546D0` | 88 | UnwindData |  |
