# Binary Specification: ExSMime.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ExSMime.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d6de81788ae3061a13a070050c8059a19fa07b7d73a259546e145453a5e5d9b4`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xF3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xF400` | 58 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xF480` | 90 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xF4E0` | 143,372 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
