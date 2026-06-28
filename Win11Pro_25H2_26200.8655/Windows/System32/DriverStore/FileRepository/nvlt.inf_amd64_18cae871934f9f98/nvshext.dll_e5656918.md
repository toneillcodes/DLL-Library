# Binary Specification: nvshext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\nvshext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e5656918397ed28717adf2d4fb2bfe621be01226a870f94a48b3c0256760dcb7`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1270` | 51 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x1370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1390` | 335 | UnwindData |  |
