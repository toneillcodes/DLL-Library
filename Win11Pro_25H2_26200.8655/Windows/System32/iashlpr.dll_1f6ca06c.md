# Binary Specification: iashlpr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\iashlpr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1f6ca06c2f99cdc4348b3f3109cecb44bc9d70280bee357969bab0b256da763b`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AllocateAttributes` | `0x85F0` | 118 | UnwindData |  |
| 2 | `ConfigureIas` | `0x8670` | 74 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x86C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x86E0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllRegisterServer` | `0x88C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x88E0` | 33 | UnwindData |  |
| 7 | `DoRequest` | `0x8910` | 90 | UnwindData |  |
| 8 | `DoRequestAsync` | `0x8970` | 280 | UnwindData |  |
| 9 | `FreeAttributes` | `0x8A90` | 56 | UnwindData |  |
| 10 | `GetOptionIas` | `0x8AD0` | 233 | UnwindData |  |
| 11 | `InitializeIas` | `0x8BC0` | 80 | UnwindData |  |
| 12 | `MemAllocIas` | `0x8C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MemFreeIas` | `0x8C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MemReallocIas` | `0x8C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SetOptionIas` | `0x8C80` | 518 | UnwindData |  |
| 16 | `ShutdownIas` | `0x8E90` | 74 | UnwindData |  |
