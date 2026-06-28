# Binary Specification: schedprov.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\schedprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `da006f816c538f079fe91e51a182c5a98eacdeda504362b23c04d19cc0c65911`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x19C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x1A30` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1A70` | 113 | UnwindData |  |
| 3 | `DllMain` | `0x1AF0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1B50` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1BA0` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x1D20` | 150,838 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
