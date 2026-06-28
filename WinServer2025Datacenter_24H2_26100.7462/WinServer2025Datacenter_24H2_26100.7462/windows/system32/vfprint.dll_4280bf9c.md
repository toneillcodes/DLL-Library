# Binary Specification: vfprint.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vfprint.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4280bf9cdc01f19e47b7c224520bb0c8fe6433c141263bfb4dd4f71ad8925c42`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `PrintVerifierIsLayerEnabled` | `0x2A20` | 61,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetAccessViolationsCount` | `0x11BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetInvalidHandleExceptionCount` | `0x11BB0` | 4,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetPrinterHandleCount` | `0x12E10` | 56,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PrintVerifierCreatePluginInterfaceWrapper` | `0x20BE0` | 707 | UnwindData |  |
| 1 | `CreateFilterTestHook` | `0x239E0` | 256 | UnwindData |  |
