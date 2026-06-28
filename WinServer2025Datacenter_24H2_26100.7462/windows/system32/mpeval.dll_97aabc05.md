# Binary Specification: mpeval.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mpeval.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `97aabc0556c27fcc02b9ab771f88d460d7047851bdd1d84dbbd1c75da22cc7be`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x12750` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x12790` | 119 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x12810` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x12860` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x12A80` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllMain` | `0x12C30` | 25,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x12C30` | 25,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MPEvalTrap` | `0x19010` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `NITS_STUB` | `0x19160` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `monitoring_platform_evaluatorFT_V1` | `0x19900` | 134,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `NITS_PRESENCE_STUB` | `0x3A830` | 0 | Indeterminate |  |
