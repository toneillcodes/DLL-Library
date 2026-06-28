# Binary Specification: MTFServer.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MTFServer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a2eb7a45a43c78bebcbaeb21fcf347e2f167b0a2e3cea7fe4cafd7fb1c67e0ef`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x9350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x9370` | 289 | UnwindData |  |
| 3 | `MTF_Close` | `0x9540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MTF_Open` | `0x9540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MTF_Deinit` | `0x9550` | 110 | UnwindData |  |
| 5 | `MTF_GetServer` | `0x95D0` | 74 | UnwindData |  |
| 6 | `MTF_IOControl` | `0x9620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MTF_Init` | `0x9630` | 566 | UnwindData |  |
| 9 | `MTF_SetPrivateMode` | `0x9870` | 179,919 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
