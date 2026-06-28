# Binary Specification: wininitext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wininitext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `04d1e61cb6442a7b2016ab39a904bb4a22bff77cd8253b6c1625b13cf4d419db`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `WaitForWinstationShutdown` | `0x11A0` | 197 | UnwindData |  |
| 1 | `GetLoggedOnUserCount` | `0x1270` | 112 | UnwindData |  |
| 5 | `UIStartupWorker` | `0x7680` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `LaunchUmfdHostWithVirtualAccountWorker` | `0x7CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PrimaryTerminalAndHookWorker` | `0x7CE0` | 410 | UnwindData |  |
| 4 | `StartLoadingFontsWorker` | `0x7E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `WinStationSystemShutdownStartedWorker` | `0x7E90` | 9,692 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
