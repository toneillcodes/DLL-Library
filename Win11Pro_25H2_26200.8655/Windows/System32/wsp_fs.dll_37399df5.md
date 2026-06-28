# Binary Specification: wsp_fs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wsp_fs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `37399df56ffaa9e34149c03c5be18d455b2954460050dcbc513d542124c5d40d`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `PreShutdown` | `0x5230` | 25,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SetShutdownCallback` | `0x5230` | 25,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0xB660` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SmpUnload` | `0xB6C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xB710` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xB750` | 119 | UnwindData |  |
| 3 | `DllMain` | `0xB7D0` | 134 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xB860` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xB8B0` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0xBA40` | 651,440 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
