# Binary Specification: ReInfo.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ReInfo.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `55ee24767413ddc182e3bc8d23bb6bff314d2bf2054001447c50f1a991008cdf`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `WinReGetConfig` | `0xB080` | 51 | UnwindData |  |
| 3 | `WinReGetTargetWindowsDirectory` | `0xB620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WinReGetTargetWindowsDirectoryEx` | `0xB640` | 169 | UnwindData |  |
| 6 | `WinReIsSystemWinRE` | `0xB6F0` | 254 | UnwindData |  |
| 1 | `WinReCloseMainOS` | `0xF460` | 233 | UnwindData |  |
| 5 | `WinReGetWindowsDirectory` | `0xF550` | 582 | UnwindData |  |
| 7 | `WinReOpenMainOS` | `0xF7A0` | 328 | UnwindData |  |
| 8 | `WinReOpenRegistryHive` | `0xF8F0` | 536 | UnwindData |  |
| 9 | `WinReSettingsDeleteFile` | `0xFB10` | 488 | UnwindData |  |
| 10 | `WinReSettingsDeleteValue` | `0xFD00` | 392 | UnwindData |  |
| 11 | `WinReSettingsFindClose` | `0xFE90` | 216 | UnwindData |  |
| 12 | `WinReSettingsFindFirstFileName` | `0xFF70` | 1,111 | UnwindData |  |
| 13 | `WinReSettingsFindFirstValueName` | `0x103D0` | 658 | UnwindData |  |
| 14 | `WinReSettingsFindNextFileName` | `0x10670` | 566 | UnwindData |  |
| 15 | `WinReSettingsFindNextValueName` | `0x108B0` | 258 | UnwindData |  |
| 16 | `WinReSettingsQueryValue` | `0x109C0` | 452 | UnwindData |  |
| 17 | `WinReSettingsRetrieveFile` | `0x10B90` | 538 | UnwindData |  |
| 18 | `WinReSettingsSetValue` | `0x10DB0` | 546 | UnwindData |  |
| 19 | `WinReSettingsStoreFile` | `0x10FE0` | 656 | UnwindData |  |
| 20 | `WinReSetupMainOS` | `0x11280` | 3,164 | UnwindData |  |
| 21 | `WinReTearDownMainOS` | `0x11EF0` | 369 | UnwindData |  |
