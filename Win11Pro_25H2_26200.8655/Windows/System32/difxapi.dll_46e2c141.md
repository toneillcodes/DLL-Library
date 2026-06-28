# Binary Specification: difxapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\difxapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `46e2c1416a8ec20bf0cc38e9c686d24f2f306f92d60fe7070788ab2d01fb75d0`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DIFXAPISetLogCallbackA` | `0x9510` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DIFXAPISetLogCallbackW` | `0x9540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DriverPackageGetPathA` | `0x9560` | 247 | UnwindData |  |
| 4 | `DriverPackageGetPathW` | `0x9660` | 259 | UnwindData |  |
| 5 | `DriverPackageInstallA` | `0x9770` | 416 | UnwindData |  |
| 6 | `DriverPackageInstallW` | `0x9920` | 110 | UnwindData |  |
| 7 | `DriverPackagePreinstallA` | `0x99A0` | 136 | UnwindData |  |
| 8 | `DriverPackagePreinstallW` | `0x9A30` | 106 | UnwindData |  |
| 9 | `DriverPackageUninstallA` | `0x9AA0` | 416 | UnwindData |  |
| 10 | `DriverPackageUninstallW` | `0x9C50` | 110 | UnwindData |  |
| 11 | `SetDifxLogCallbackA` | `0x9CD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SetDifxLogCallbackW` | `0x9D00` | 126,224 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
