# Binary Specification: qwave.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\qwave.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9a37d5279f390264ef499fa7ebdc314b6b9e505b8396cdafc0c38ae3ea607304`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `ServiceMain` | `0x4880` | 48,150 | UnwindData |  |
| 1 | `QDLHPathDiagnostics` | `0x1EE00` | 456 | UnwindData |  |
| 2 | `QDLHStartDiagnosingPath` | `0x1EFD0` | 383 | UnwindData |  |
| 3 | `QOSAddSocketToFlow` | `0x1F160` | 513 | UnwindData |  |
| 4 | `QOSCancel` | `0x1F370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `QOSCloseHandle` | `0x1F390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `QOSCreateHandle` | `0x1F3B0` | 577 | UnwindData |  |
| 7 | `QOSEnumerateFlows` | `0x1F600` | 330 | UnwindData |  |
| 8 | `QOSNotifyFlow` | `0x1F750` | 364 | UnwindData |  |
| 9 | `QOSQueryFlow` | `0x1F8D0` | 364 | UnwindData |  |
| 10 | `QOSRemoveSocketFromFlow` | `0x1FA50` | 402 | UnwindData |  |
| 11 | `QOSSetFlow` | `0x1FBF0` | 368 | UnwindData |  |
| 12 | `QOSStartTrackingClient` | `0x1FD70` | 383 | UnwindData |  |
| 13 | `QOSStopTrackingClient` | `0x1FF00` | 383 | UnwindData |  |
