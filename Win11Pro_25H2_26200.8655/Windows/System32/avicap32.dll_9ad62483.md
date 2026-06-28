# Binary Specification: avicap32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\avicap32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9ad624831aa3b90ac9443bff483e9eada5cd9ac3f517490d63ecb61d527f3997`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `capCreateCaptureWindowA` | `0x2850` | 262 | UnwindData |  |
| 3 | `capCreateCaptureWindowW` | `0x2960` | 341 | UnwindData |  |
| 4 | `capGetDriverDescriptionA` | `0x2AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `capGetDriverDescriptionW` | `0x2AD0` | 52,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AppCleanup` | `0xF8A0` | 99 | UnwindData |  |
| 6 | `videoThunk32` | `0x10F50` | 535 | UnwindData |  |
