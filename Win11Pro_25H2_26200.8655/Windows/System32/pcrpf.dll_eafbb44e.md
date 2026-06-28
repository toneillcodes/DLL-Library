# Binary Specification: pcrpf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\pcrpf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eafbb44eb4c967c78f84399c68cce770c5dac0edaaf69c57fca90747ed50484e`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CleanupBitLockerReducedPcrProfile` | `0x14D10` | 60 | UnwindData |  |
| 2 | `NotifyFirmwareUpdateStaged` | `0x14D60` | 60 | UnwindData |  |
| 3 | `PpfCancelTransform` | `0x14DB0` | 40 | UnwindData |  |
| 4 | `PpfCreatePpfEventLogFromTcgLog` | `0x14DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PpfFinalizeTransform` | `0x14DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PpfFreePredictions` | `0x14E00` | 340 | UnwindData |  |
| 7 | `PpfGenerateFinalPcrValuesForPpfEventLog` | `0x14F60` | 206 | UnwindData |  |
| 8 | `PpfGetPredictions` | `0x15040` | 40 | UnwindData |  |
| 9 | `PpfLock` | `0x15070` | 597 | UnwindData |  |
| 10 | `PpfLogIteratorGetCurrent` | `0x152D0` | 70 | UnwindData |  |
| 11 | `PpfLogIteratorInitialize` | `0x15320` | 83 | UnwindData |  |
| 12 | `PpfLogIteratorTryGetNext` | `0x15380` | 83 | UnwindData |  |
| 13 | `PpfScheduledTaskMain` | `0x153E0` | 40 | UnwindData |  |
| 14 | `PpfStageTransform` | `0x15410` | 208 | UnwindData |  |
| 15 | `PpfUnlock` | `0x15570` | 102 | UnwindData |  |
