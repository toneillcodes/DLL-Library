# Binary Specification: ncsi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ncsi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b9c7935e22959d3cdea9a4383a008e5e7396de219f064d1d9a4d455c55d2d57e`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NcsiAllocateAndGetConnectivityStatusSet` | `0xF900` | 39 | UnwindData |  |
| 4 | `NcsiFreeConnectivityStatusSet` | `0x37040` | 52 | UnwindData |  |
| 8 | `NcsiNotifySessionChange` | `0x37440` | 150 | UnwindData |  |
| 10 | `NcsiPerformReprobe` | `0x3C590` | 808 | UnwindData |  |
| 2 | `NcsiDeregisterConnectivityStatusChange` | `0x50560` | 147 | UnwindData |  |
| 3 | `NcsiDeregisterDiagnosticsInfoChange` | `0x50600` | 110 | UnwindData |  |
| 5 | `NcsiGetCaptivePortalHosts` | `0x50680` | 507 | UnwindData |  |
| 6 | `NcsiGetWebProbeConfig` | `0x50890` | 411 | UnwindData |  |
| 9 | `NcsiPerformRefresh` | `0x50A40` | 537 | UnwindData |  |
| 11 | `NcsiRegisterConnectivityStatusChange` | `0x50C60` | 210 | UnwindData |  |
| 12 | `NcsiRegisterDiagnosticsInfoChange` | `0x50D40` | 195 | UnwindData |  |
| 13 | `NcsiUpdateClientPresence` | `0x50E10` | 1,125 | UnwindData |  |
| 7 | `NcsiIdentifyUserSpecificProxies` | `0x54220` | 88 | UnwindData |  |
