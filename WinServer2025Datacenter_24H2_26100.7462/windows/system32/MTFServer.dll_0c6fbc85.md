# Binary Specification: MTFServer.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MTFServer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0c6fbc85bfc30969c8b9ade8c9cc0d66d7ee0e1c8d71011bb6e084d0a7c327e6`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x9330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x9350` | 289 | UnwindData |  |
| 3 | `MTF_Close` | `0x9520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MTF_Open` | `0x9520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MTF_Deinit` | `0x9530` | 110 | UnwindData |  |
| 5 | `MTF_GetServer` | `0x95B0` | 74 | UnwindData |  |
| 6 | `MTF_IOControl` | `0x9600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MTF_Init` | `0x9610` | 562 | UnwindData |  |
| 9 | `MTF_SetPrivateMode` | `0x9850` | 179,919 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
