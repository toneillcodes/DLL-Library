# Binary Specification: windowsperformancerecordercontrol.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\windowsperformancerecordercontrol.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `66c8a600f0891233a97bb683f4ee1235b7dca74640dc0302784036d0c4509a36`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x7F70` | 29,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x7F70` | 29,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xF2F0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xF320` | 302 | UnwindData |  |
| 5 | `WPRCControlLogging` | `0x71540` | 438 | UnwindData |  |
| 6 | `WPRCCreateInstance` | `0x71700` | 41 | UnwindData |  |
| 7 | `WPRCCreateInstanceUnderInstanceName` | `0x71730` | 879 | UnwindData |  |
| 8 | `WPRCDisableBuiltinProfiles` | `0x71AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `WPRCFormatError` | `0x71AD0` | 476 | UnwindData |  |
| 10 | `WPRCQueryBuiltInProfiles` | `0x71CC0` | 273 | UnwindData |  |
| 11 | `WPRCReleaseInstanceByName` | `0x71DE0` | 207 | UnwindData |  |
| 12 | `WPRCRemoveLogging` | `0x71EC0` | 71 | UnwindData |  |
