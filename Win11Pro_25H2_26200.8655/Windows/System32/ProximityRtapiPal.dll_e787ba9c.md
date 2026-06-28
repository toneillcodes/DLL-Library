# Binary Specification: ProximityRtapiPal.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ProximityRtapiPal.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e787ba9c7d20357113f1f0a5247eafeb66c59d151b6dfa54f56a5dda6c294d32`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `PAL_App2DeviceFindAllPeers` | `0x1AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PAL_CheckForBluetoothSupport` | `0x1AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PAL_CheckForApp2DeviceAlternateId` | `0x1B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PAL_GetCurrentProcessExplicitAppUserModelID` | `0x1B10` | 37 | UnwindData |  |
| 5 | `PAL_ParseAppUserModelId` | `0x1B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PAL_SetCurrentProcessExplicitAppUserModelID` | `0x1B50` | 11,548 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
