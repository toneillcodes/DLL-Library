# Binary Specification: signdrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\signdrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dc689ffabeaa7475fa8ce15544169b832ad2999911bdbd868cec69f509c530fb`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2E30` | 93 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2EA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2ED0` | 15,139 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2ED0` | 15,139 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
