# Binary Specification: netdacim.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\netdacim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `88ef9fe68f13be602b7913f1494eba50745218ea4d28ef9172d1e5164aacde15`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1910` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1950` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x19D0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1A30` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1A80` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x1CA0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x1D10` | 41,968 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
