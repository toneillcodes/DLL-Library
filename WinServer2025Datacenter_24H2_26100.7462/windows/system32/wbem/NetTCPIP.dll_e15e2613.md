# Binary Specification: NetTCPIP.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\NetTCPIP.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e15e261339c91d3666d07dc9d78f36cc652441fbf9bbd217236ee714a9e8bdb0`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x11AD0` | 346 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x11C30` | 293 | UnwindData |  |
| 3 | `DllMain` | `0x14B10` | 82 | UnwindData |  |
| 7 | `MI_Main` | `0x17AA0` | 2,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x18400` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x18450` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x184A0` | 185,024 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
