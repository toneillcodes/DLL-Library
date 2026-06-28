# Binary Specification: FWUpdateLib_18.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\lms.inf_amd64_a55aa2cd52a3429d\FWUpdateLib_18.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `cd8375ae0da650c6441fab79a6774d9553d98694e09b9195cf42adee724066ae`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `FwuCheckCompatibilityFromFile` | `0x1000` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `FwuFullUpdateFromFile` | `0x1070` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `FwuFwTypeFromFile` | `0x10F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `FwuPartialUpdateFromFile` | `0x1170` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `FwuPartialUpdateWithInstanceIdFromBuffer` | `0x11F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `FwuPartialUpdateWithInstanceIdFromFile` | `0x1200` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `FwuPartitionVersionFromFile` | `0x1280` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `FwuPchSkuFromFile` | `0x1310` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `FwuPowerSource` | `0x1390` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `FwuProductSegmentFromFile` | `0x1420` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `FwuSaveRestorePointToFile` | `0x14A0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `FwuCheckCompatibilityFromBuffer` | `0x15D0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FwuCheckUpdateProgress` | `0x1970` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FwuEnabledState` | `0x1DC0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FwuFullUpdateFromBuffer` | `0x1E50` | 3,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `FwuFwType` | `0x2C30` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `FwuFwTypeFromBuffer` | `0x2D20` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `FwuIsPartitionPresentInBuffer` | `0x2F20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `FwuIupsFromFlash` | `0x2F70` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `FwuIupsNumberFromFlash` | `0x3040` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `FwuOemId` | `0x30D0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `FwuPartialUpdateFromBuffer` | `0x31B0` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `FwuPartitionInstances` | `0x37B0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `FwuPartitionVendorIdFromFlash` | `0x38E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `FwuPartitionVersionFromBuffer` | `0x3980` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `FwuPartitionVersionFromFlash` | `0x3BD0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `FwuPchSku` | `0x3D00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `FwuPchSkuFromBuffer` | `0x3DC0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `FwuProductSegmentFromBuffer` | `0x4020` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `FwuProductSegmentFromFlash` | `0x4220` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `FwuSaveRestorePointToBuffer` | `0x4310` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `FwuSetEnabledState` | `0x4650` | 478,479 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
