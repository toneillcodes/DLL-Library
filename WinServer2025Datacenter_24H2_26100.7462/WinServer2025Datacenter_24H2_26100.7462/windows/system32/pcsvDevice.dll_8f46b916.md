# Binary Specification: pcsvDevice.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pcsvDevice.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8f46b9161c370dab5c380817e60b772ab7c9f3ee1c907ff9007da04837968118`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2850` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2890` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x2910` | 292 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2A40` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2A90` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2C20` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x2E50` | 156,287 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
