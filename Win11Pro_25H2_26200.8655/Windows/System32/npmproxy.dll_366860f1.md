# Binary Specification: npmproxy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\npmproxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `366860f15178411d5e06f441783e175c61c7d12f7be4fb454b0cc551c36c9d5e`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x10B0` | 73 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `LANIdRetrieveCollection` | `0x1120` | 21 | UnwindData |  |
| 6 | `LANIdFreeCollection` | `0x12F0` | 19 | UnwindData |  |
| 9 | `NlmDiagSendWlanDisconnectionDiagnostics` | `0x2060` | 290 | UnwindData |  |
| 8 | `NlmDiagSendWlanConnectionAttemptDiagnostics` | `0x2190` | 382 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x46C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x4700` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetProxyDllInfo` | `0x4740` | 11,440 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
