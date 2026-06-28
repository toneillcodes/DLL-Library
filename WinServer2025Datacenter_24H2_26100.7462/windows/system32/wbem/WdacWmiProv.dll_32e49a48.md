# Binary Specification: WdacWmiProv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\WdacWmiProv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `32e49a48bb2b06c90a631e1fa2491fe095827253b134de12e9805b999e1a3f6a`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1EA0` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1EE0` | 113 | UnwindData |  |
| 3 | `DllMain` | `0x1F60` | 146 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2000` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2050` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x20A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x2110` | 53,344 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
