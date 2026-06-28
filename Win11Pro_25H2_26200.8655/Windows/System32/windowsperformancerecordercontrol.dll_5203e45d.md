# Binary Specification: windowsperformancerecordercontrol.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\windowsperformancerecordercontrol.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5203e45df88533dbdf24386e8741021c841ab0f4d0db95430a2b7a3a0072334b`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x7F70` | 29,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x7F70` | 29,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xF300` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xF330` | 302 | UnwindData |  |
| 5 | `WPRCControlLogging` | `0x71550` | 438 | UnwindData |  |
| 6 | `WPRCCreateInstance` | `0x71710` | 41 | UnwindData |  |
| 7 | `WPRCCreateInstanceUnderInstanceName` | `0x71740` | 879 | UnwindData |  |
| 8 | `WPRCDisableBuiltinProfiles` | `0x71AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `WPRCFormatError` | `0x71AE0` | 476 | UnwindData |  |
| 10 | `WPRCQueryBuiltInProfiles` | `0x71CD0` | 273 | UnwindData |  |
| 11 | `WPRCReleaseInstanceByName` | `0x71DF0` | 207 | UnwindData |  |
| 12 | `WPRCRemoveLogging` | `0x71ED0` | 71 | UnwindData |  |
