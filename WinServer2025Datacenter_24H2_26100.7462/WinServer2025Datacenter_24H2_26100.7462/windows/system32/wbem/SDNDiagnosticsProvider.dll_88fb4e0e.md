# Binary Specification: SDNDiagnosticsProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\SDNDiagnosticsProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `88fb4e0e636f20a0f18244af2de6fac74280b46e87becda7510d31c8a7215ab7`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x24180` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x241C0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x24240` | 269 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x24360` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x243B0` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x245D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x24640` | 85,052 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
