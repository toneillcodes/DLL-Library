# Binary Specification: ndfapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ndfapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3eec33bbe9e62b572a48cae6b68a3472945224ef8f585faf94d951b228e95950`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllCanUnloadNow` | `0x78F0` | 42 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x7920` | 302 | UnwindData |  |
| 9 | `DllRegisterServer` | `0x7AC0` | 296 | UnwindData |  |
| 10 | `DllUnregisterServer` | `0x7BF0` | 156 | UnwindData |  |
| 1 | `NdfRunDllDiagnoseIncident` | `0x9A90` | 52 | UnwindData |  |
| 2 | `NdfRunDllDiagnoseNetConnectionIncident` | `0x9AD0` | 304 | UnwindData |  |
| 4 | `NdfRunDllDuplicateIPDefendingSystem` | `0x9C10` | 57 | UnwindData |  |
| 5 | `NdfRunDllDuplicateIPOffendingSystem` | `0x9C50` | 96 | UnwindData |  |
| 6 | `NdfRunDllHelpTopic` | `0x9CC0` | 206 | UnwindData |  |
| 12 | `NdfCloseIncident` | `0xA800` | 150 | UnwindData |  |
| 13 | `NdfCreateConnectivityIncident` | `0xA8A0` | 268 | UnwindData |  |
| 14 | `NdfCreateDNSIncident` | `0xA9C0` | 364 | UnwindData |  |
| 15 | `NdfCreateGroupingIncident` | `0xAB40` | 808 | UnwindData |  |
| 16 | `NdfCreateInboundIncident` | `0xAE70` | 706 | UnwindData |  |
| 17 | `NdfCreateIncident` | `0xB140` | 865 | UnwindData |  |
| 18 | `NdfCreateNetConnectionIncident` | `0xB4B0` | 203 | UnwindData |  |
| 19 | `NdfCreatePnrpIncident` | `0xB590` | 521 | UnwindData |  |
| 20 | `NdfCreateSharingIncident` | `0xB7A0` | 307 | UnwindData |  |
| 21 | `NdfCreateWebIncident` | `0xB8E0` | 351 | UnwindData |  |
| 22 | `NdfCreateWebIncidentEx` | `0xBA50` | 388 | UnwindData |  |
| 23 | `NdfCreateWinSockIncident` | `0xBBE0` | 1,127 | UnwindData |  |
| 25 | `NdfExecuteDiagnosis` | `0xC050` | 301 | UnwindData |  |
| 3 | `NdfRunDllDiagnoseWithAnswerFile` | `0xF4C0` | 536 | UnwindData |  |
| 11 | `NdfCancelIncident` | `0x1C570` | 182 | UnwindData |  |
| 24 | `NdfDiagnoseIncident` | `0x1C630` | 196 | UnwindData |  |
| 26 | `NdfGetTraceFile` | `0x1C700` | 144 | UnwindData |  |
| 27 | `NdfRepairIncident` | `0x1C7A0` | 174 | UnwindData |  |
| 28 | `NdfRepairIncidentEx` | `0x1C860` | 57 | UnwindData |  |
