# Binary Specification: qwave.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\qwave.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `742561ea4b6f0c5074574f5ba99078d200278601fa77c9d544ea228e324abd6e`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `ServiceMain` | `0x4B30` | 48,150 | UnwindData |  |
| 1 | `QDLHPathDiagnostics` | `0x1F0B0` | 456 | UnwindData |  |
| 2 | `QDLHStartDiagnosingPath` | `0x1F280` | 383 | UnwindData |  |
| 3 | `QOSAddSocketToFlow` | `0x1F410` | 513 | UnwindData |  |
| 4 | `QOSCancel` | `0x1F620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `QOSCloseHandle` | `0x1F640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `QOSCreateHandle` | `0x1F660` | 577 | UnwindData |  |
| 7 | `QOSEnumerateFlows` | `0x1F8B0` | 330 | UnwindData |  |
| 8 | `QOSNotifyFlow` | `0x1FA00` | 364 | UnwindData |  |
| 9 | `QOSQueryFlow` | `0x1FB80` | 364 | UnwindData |  |
| 10 | `QOSRemoveSocketFromFlow` | `0x1FD00` | 402 | UnwindData |  |
| 11 | `QOSSetFlow` | `0x1FEA0` | 368 | UnwindData |  |
| 12 | `QOSStartTrackingClient` | `0x20020` | 383 | UnwindData |  |
| 13 | `QOSStopTrackingClient` | `0x201B0` | 383 | UnwindData |  |
