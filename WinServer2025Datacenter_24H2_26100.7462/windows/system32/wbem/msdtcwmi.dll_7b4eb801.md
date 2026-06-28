# Binary Specification: msdtcwmi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\msdtcwmi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7b4eb8017b05a60ba764b2d38e5b5fcb21b84d38af56c659b0257fcd1ac45e4b`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x2180` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x2210` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2250` | 113 | UnwindData |  |
| 3 | `DllMain` | `0x22D0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2330` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2380` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x25A0` | 93,597 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
