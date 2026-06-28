# Binary Specification: nlmcim.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\nlmcim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6a51eb8ab4927a5ffed059e39c4bc3a16004b257c9467e4ea8b143abbeee37d5`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x20D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x2160` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x21A0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x2220` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2280` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x22D0` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x24E0` | 4,111 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
