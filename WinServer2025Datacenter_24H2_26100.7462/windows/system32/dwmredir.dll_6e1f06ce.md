# Binary Specification: dwmredir.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dwmredir.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6e1f06ce5ab9bf5473c605c73b78ab0d37e6ae3e18a04a6254dd5fa888ce2862`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DwmInitializePort` | `0xE080` | 36 | UnwindData |  |
| 1 | `DwmRedirectionManagerInitialize` | `0x1C1F0` | 82 | UnwindData |  |
| 2 | `DwmRedirectionManagerShutdown` | `0x1C250` | 50 | UnwindData |  |
| 3 | `DwmRegisterWindowNotificationHandler` | `0x21730` | 18,780 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
