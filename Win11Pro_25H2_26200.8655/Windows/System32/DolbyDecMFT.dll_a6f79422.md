# Binary Specification: DolbyDecMFT.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DolbyDecMFT.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a6f79422298b2008d0a2fb68cfa2b1564f155e34a11855650494a7cfe0f96cc9`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x1AB20` | 67 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1AB70` | 54 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1C460` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1C4C0` | 224 | UnwindData |  |
