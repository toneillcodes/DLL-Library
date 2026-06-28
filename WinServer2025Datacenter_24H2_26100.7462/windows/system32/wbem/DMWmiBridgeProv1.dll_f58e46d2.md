# Binary Specification: DMWmiBridgeProv1.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\DMWmiBridgeProv1.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f58e46d2529651d3ecc2a03061594bc9d6aa93e528fd9872201fbc4f952cba64`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2280` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x22C0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x2340` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x23A0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x23F0` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2610` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x2670` | 619,260 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
