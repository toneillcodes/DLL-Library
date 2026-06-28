# Binary Specification: fsutilext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fsutilext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `91048530cabf4d7cbb084ddda10a050d8f20c1357a8ddaca283b0f8a8e4c1e5f`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `FindFirstVolumeMountPointWStub` | `0x1D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FindNextVolumeMountPointWStub` | `0x1D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FindVolumeMountPointCloseStub` | `0x1DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SetThreadUILanguageStub` | `0x1DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `SystemParametersInfoWStub` | `0x1DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CheckSonyMSWorker` | `0x1E10` | 750 | UnwindData |  |
| 2 | `DeviceInstIsRemovableWorker` | `0x2110` | 92 | UnwindData |  |
| 6 | `GetDeviceIDDiskFromDeviceIDVolumeWorker` | `0x2180` | 1,068 | UnwindData |  |
| 7 | `GetDeviceInstanceWorker` | `0x25C0` | 622 | UnwindData |  |
| 8 | `GetRemovableDeviceInstRecursWorker` | `0x2840` | 107 | UnwindData |  |
| 9 | `GetWidgetWorker` | `0x2AC0` | 274 | UnwindData |  |
| 10 | `InvalidateFveWorker` | `0x2BE0` | 1,044 | UnwindData |  |
| 11 | `SendWithSenseParseWorker` | `0x3000` | 660 | UnwindData |  |
| 14 | `WaitForUnitAndReportProgressWorker` | `0x32A0` | 545 | UnwindData |  |
