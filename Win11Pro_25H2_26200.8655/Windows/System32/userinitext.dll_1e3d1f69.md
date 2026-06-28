# Binary Specification: userinitext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\userinitext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1e3d1f69aaa1e7a19ac5668070d972985e9e6e90e67a3a2f7641edd89d9c3ac7`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateExplorerSessionKey` | `0x2110` | 328 | UnwindData |  |
| 2 | `DisplayMessageAndExitWindows` | `0x2260` | 47 | UnwindData |  |
| 3 | `ImmWorker` | `0x2300` | 118 | UnwindData |  |
| 4 | `IsSubDesktopSession` | `0x2580` | 144 | UnwindData |  |
| 5 | `IsTSAppCompatOn` | `0x2620` | 193 | UnwindData |  |
| 6 | `LoadRemoteFontsAndInitMiscWorker` | `0x2C30` | 47 | UnwindData |  |
| 7 | `PerformXForestLogonCheck` | `0x2C70` | 119 | UnwindData |  |
| 8 | `ProcesRemoteSessionInitialCommand` | `0x2CF0` | 1,511 | UnwindData |  |
| 9 | `ProcessTermSrvIniFiles` | `0x32E0` | 123 | UnwindData |  |
| 10 | `SetShellDesktopSwitchEvent` | `0x3430` | 75 | UnwindData |  |
| 11 | `SetupHotKeyForKeyboardLayout` | `0x3490` | 626 | UnwindData |  |
| 12 | `UserinitExt` | `0x3790` | 24,588 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
