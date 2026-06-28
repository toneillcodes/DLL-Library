# Binary Specification: NetAdapterCim.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\NetAdapterCim.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `28272240e87b03732284a402916f8b920c69d08f01494e15b3c51f559f40fa87`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x121B0` | 110 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x12230` | 192 | UnwindData |  |
| 7 | `MI_Main` | `0x12CF0` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllMain` | `0x13250` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1DC20` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1DC70` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x1DCC0` | 278,149 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
