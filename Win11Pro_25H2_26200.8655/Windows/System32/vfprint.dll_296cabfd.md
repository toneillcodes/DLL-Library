# Binary Specification: vfprint.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vfprint.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `296cabfd69815ea33b5c8556bd4d691989176a168e576c6735d3a5cc42bc9cf9`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `PrintVerifierIsLayerEnabled` | `0x2A40` | 62,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetAccessViolationsCount` | `0x11E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetInvalidHandleExceptionCount` | `0x11E80` | 4,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetPrinterHandleCount` | `0x130F0` | 57,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PrintVerifierCreatePluginInterfaceWrapper` | `0x211E0` | 710 | UnwindData |  |
| 1 | `CreateFilterTestHook` | `0x24000` | 262 | UnwindData |  |
