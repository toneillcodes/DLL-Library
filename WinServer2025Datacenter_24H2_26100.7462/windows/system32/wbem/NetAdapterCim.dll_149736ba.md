# Binary Specification: NetAdapterCim.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\NetAdapterCim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `149736bacf9602e6d1a5e03adfc48d8ddd736993815e9a76973c64f06431b131`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x12080` | 110 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x12100` | 192 | UnwindData |  |
| 7 | `MI_Main` | `0x12B70` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllMain` | `0x13060` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1DA10` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1DA60` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x1DAB0` | 273,333 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
