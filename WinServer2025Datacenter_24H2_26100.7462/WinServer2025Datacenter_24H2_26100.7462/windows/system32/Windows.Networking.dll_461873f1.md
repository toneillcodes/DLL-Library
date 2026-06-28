# Binary Specification: Windows.Networking.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Networking.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `461873f18f5ba64fe2bff403da80da60f472d9a67b17dc1a8acdac806a10ffce`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x6AEF0` | 58 | UnwindData |  |
| 3 | `DllGetActivationFactory` | `0x6AF30` | 45 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x6AF70` | 134 | UnwindData |  |
| 5 | `DllMain` | `0x6B000` | 86 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x6B060` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllUnregisterServer` | `0x6B090` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | *Ordinal Only* | `0x6B0C0` | 208 | UnwindData |  |
| 8 | `SetSocketMediaStreamingMode` | `0x6B1A0` | 107,692 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
