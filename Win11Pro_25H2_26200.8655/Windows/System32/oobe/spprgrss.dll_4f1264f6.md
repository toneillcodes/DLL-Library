# Binary Specification: spprgrss.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\oobe\spprgrss.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4f1264f6171ffbf270d91784cbd1964e370c3002308911c23d23e1e6f91658f9`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `GetProgressObject` | `0x1DE0` | 8,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `OnlineProgress` | `0x3FC0` | 185 | UnwindData |  |
| 2 | `Win32Progress` | `0x44E0` | 185 | UnwindData |  |
| 3 | `WinPEProgress` | `0x45A0` | 185 | UnwindData |  |
| 4 | `CallbackInitOnline` | `0x4660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CallbackInitWinPE` | `0x4660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CallbackInitWin32` | `0x4680` | 137 | UnwindData |  |
| 7 | `CallbackRegisterAllTasks` | `0x4710` | 25 | UnwindData |  |
| 8 | `CallbackReportEstimates` | `0x4730` | 486 | UnwindData |  |
| 9 | `CallbackTerminate` | `0x4920` | 63 | UnwindData |  |
| 11 | `ModuleInitialize` | `0x49D0` | 213 | UnwindData |  |
| 12 | `PutProgressEstimateOnBlackboard` | `0x4AB0` | 198 | UnwindData |  |
