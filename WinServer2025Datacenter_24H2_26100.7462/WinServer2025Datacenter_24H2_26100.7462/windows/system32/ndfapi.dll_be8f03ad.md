# Binary Specification: ndfapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ndfapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `be8f03ad52ae88d263690ef5313774d9a3d3ddfc067aba2c8d92852210b15c43`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllCanUnloadNow` | `0x7BD0` | 42 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x7C00` | 302 | UnwindData |  |
| 9 | `DllRegisterServer` | `0x7DA0` | 296 | UnwindData |  |
| 10 | `DllUnregisterServer` | `0x7ED0` | 156 | UnwindData |  |
| 1 | `NdfRunDllDiagnoseIncident` | `0xCF00` | 52 | UnwindData |  |
| 2 | `NdfRunDllDiagnoseNetConnectionIncident` | `0xCF40` | 304 | UnwindData |  |
| 4 | `NdfRunDllDuplicateIPDefendingSystem` | `0xD080` | 57 | UnwindData |  |
| 5 | `NdfRunDllDuplicateIPOffendingSystem` | `0xD0C0` | 96 | UnwindData |  |
| 6 | `NdfRunDllHelpTopic` | `0xD130` | 206 | UnwindData |  |
| 12 | `NdfCloseIncident` | `0x11050` | 150 | UnwindData |  |
| 13 | `NdfCreateConnectivityIncident` | `0x110F0` | 268 | UnwindData |  |
| 14 | `NdfCreateDNSIncident` | `0x11210` | 364 | UnwindData |  |
| 15 | `NdfCreateGroupingIncident` | `0x11390` | 808 | UnwindData |  |
| 16 | `NdfCreateInboundIncident` | `0x116C0` | 706 | UnwindData |  |
| 17 | `NdfCreateIncident` | `0x11990` | 865 | UnwindData |  |
| 18 | `NdfCreateNetConnectionIncident` | `0x11D00` | 203 | UnwindData |  |
| 19 | `NdfCreatePnrpIncident` | `0x11DE0` | 521 | UnwindData |  |
| 20 | `NdfCreateSharingIncident` | `0x11FF0` | 307 | UnwindData |  |
| 21 | `NdfCreateWebIncident` | `0x12130` | 351 | UnwindData |  |
| 22 | `NdfCreateWebIncidentEx` | `0x122A0` | 388 | UnwindData |  |
| 23 | `NdfCreateWinSockIncident` | `0x12430` | 1,127 | UnwindData |  |
| 25 | `NdfExecuteDiagnosis` | `0x128A0` | 250 | UnwindData |  |
| 3 | `NdfRunDllDiagnoseWithAnswerFile` | `0x16370` | 536 | UnwindData |  |
| 11 | `NdfCancelIncident` | `0x23550` | 182 | UnwindData |  |
| 24 | `NdfDiagnoseIncident` | `0x23610` | 196 | UnwindData |  |
| 26 | `NdfGetTraceFile` | `0x236E0` | 144 | UnwindData |  |
| 27 | `NdfRepairIncident` | `0x23780` | 174 | UnwindData |  |
| 28 | `NdfRepairIncidentEx` | `0x23840` | 57 | UnwindData |  |
