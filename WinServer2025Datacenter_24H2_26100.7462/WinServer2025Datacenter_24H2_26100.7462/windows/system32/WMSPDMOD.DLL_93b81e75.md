# Binary Specification: WMSPDMOD.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\WMSPDMOD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `93b81e7533be65937e693f6c2358c42f00b510b633304cfcdf87b479dfe3652f`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x6F770` | 217 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x6F850` | 126 | UnwindData |  |
| 1 | `CreateInstance` | `0x81FF0` | 135 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x82080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x820B0` | 238 | UnwindData |  |
