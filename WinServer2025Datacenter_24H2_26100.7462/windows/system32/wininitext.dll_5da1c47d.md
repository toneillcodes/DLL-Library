# Binary Specification: wininitext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wininitext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5da1c47d3b988eaa80ecf8005f8da126461fafba11f7f44a1a234fd8571812b6`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetLoggedOnUserCount` | `0x1010` | 111 | UnwindData |  |
| 6 | `WaitForWinstationShutdown` | `0x11C0` | 197 | UnwindData |  |
| 2 | `LaunchUmfdHostWithVirtualAccountWorker` | `0x22C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PrimaryTerminalAndHookWorker` | `0x22D0` | 395 | UnwindData |  |
| 4 | `StartLoadingFontsWorker` | `0x2470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `UIStartupWorker` | `0x2480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `WinStationSystemShutdownStartedWorker` | `0x2490` | 9,076 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
