# Binary Specification: netman.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netman.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `47a319a58e6a6bf4fad47797c8ad4d52e42fe10c5b0c7bfddab8aa76e35b2f98`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllRegisterServer` | `0x43B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllUnregisterServer` | `0x43B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `HrGetPnpDeviceStatus` | `0x43C0` | 232 | UnwindData |  |
| 4 | `ServiceMain` | `0x4650` | 58,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SvchostPushServiceGlobals` | `0x12A20` | 121,500 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
