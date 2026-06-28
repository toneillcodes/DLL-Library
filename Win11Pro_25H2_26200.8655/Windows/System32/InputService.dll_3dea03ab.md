# Binary Specification: InputService.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\InputService.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3dea03abefc42c1bac6323881c44ba812690ed129b26ba997e2de3d0eb3b7411`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CreateInputMethodClient` | `0xDEB10` | 198 | UnwindData |  |
| 5 | `InitializeService` | `0xE1860` | 705 | UnwindData |  |
| 4 | `CreateKeyEventProcessor` | `0x124D00` | 160,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ServiceMain` | `0x14BF00` | 656 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x14C920` | 2,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `UninitializeService` | `0x14D410` | 264 | UnwindData |  |
