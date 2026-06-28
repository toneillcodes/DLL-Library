# Binary Specification: gpprnext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\gpprnext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e4b620a203132c3c76e32442904f47afa6b2531ad05bd11cbdc6da43a7b59639`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllMain` | `0x2070` | 370 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x21F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x2200` | 338 | UnwindData |  |
| 6 | `PrinterGenerateGroupPolicy` | `0x2C60` | 415 | UnwindData |  |
| 7 | `PrinterProcessGroupPolicy` | `0x2E10` | 71 | UnwindData |  |
| 8 | `PrinterProcessGroupPolicyEx` | `0x2E60` | 359 | UnwindData |  |
