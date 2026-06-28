# Binary Specification: InputService.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\InputService.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `083b01d205892a59b785f22c0151aa35c261912b0941c55c15a188700788595b`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CreateInputMethodClient` | `0xE8AC0` | 198 | UnwindData |  |
| 5 | `InitializeService` | `0xEC090` | 705 | UnwindData |  |
| 4 | `CreateKeyEventProcessor` | `0x130720` | 159,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ServiceMain` | `0x1577A0` | 656 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x1581C0` | 2,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `UninitializeService` | `0x158CB0` | 264 | UnwindData |  |
