# Binary Specification: FWUpdateLib_12.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\lms.inf_amd64_a55aa2cd52a3429d\FWUpdateLib_12.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `ac589e4b05b77398a914ca0059d104046346d21d881425d8687355a284602c30`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `FwuCheckCompatibilityFromFile` | `0x1000` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `FwuFullUpdateFromFile` | `0x1070` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `FwuFwTypeFromFile` | `0x10F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `FwuGetRecoveryImageToBuffer` | `0x1170` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `FwuPartialUpdateFromFile` | `0x1480` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `FwuPartialUpdateWithInstanceIdFromBuffer` | `0x1500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `FwuPartialUpdateWithInstanceIdFromFile` | `0x1510` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `FwuPartitionInstances` | `0x1590` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `FwuPartitionVersionFromFile` | `0x1610` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `FwuPchSkuFromFile` | `0x16A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `FwuPowerSource` | `0x1720` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `FwuProductSegmentFromFile` | `0x17B0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `FwuSaveRestorePointToFile` | `0x1830` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `FwuCheckCompatibilityFromBuffer` | `0x18D0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FwuCheckUpdateProgress` | `0x1C30` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FwuEnabledState` | `0x20D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FwuFullUpdateFromBuffer` | `0x2160` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `FwuFwType` | `0x27C0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `FwuFwTypeFromBuffer` | `0x2900` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `FwuOemId` | `0x2B00` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `FwuPartialUpdateFromBuffer` | `0x2BF0` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `FwuPartitionVendorIdFromFlash` | `0x31C0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `FwuPartitionVersionFromBuffer` | `0x3270` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `FwuPartitionVersionFromFlash` | `0x3370` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `FwuPchSku` | `0x3450` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `FwuPchSkuFromBuffer` | `0x3510` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `FwuProductSegmentFromBuffer` | `0x3740` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `FwuProductSegmentFromFlash` | `0x3930` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `FwuSaveRestorePointToBuffer` | `0x3A20` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `FwuSetEnabledState` | `0x3D70` | 484,726 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
