# Binary Specification: wlanpref.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wlanpref.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `beb2168fdb74201be4733e8cb6aaa6968d294ca56cf3b6a5352445b9fc9876ff`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xC200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xC220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllMain` | `0xC240` | 566 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xC480` | 93 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xC4F0` | 149,322 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
