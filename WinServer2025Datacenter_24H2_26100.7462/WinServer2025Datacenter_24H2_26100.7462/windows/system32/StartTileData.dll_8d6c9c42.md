# Binary Specification: StartTileData.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\StartTileData.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8d6c9c42080a442c82c896f2d6a0541692bad74f63083263f4691bdf26a64b52`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `HasMigratedTDLData` | `0xE6B20` | 30 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x103C60` | 402 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x107010` | 69 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x156430` | 334 | UnwindData |  |
| 4 | `GetSetting` | `0x1958C0` | 656,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ProcessStartLayoutPolicy` | `0x235D30` | 223 | UnwindData |  |
| 7 | `TryMigrateTDLData` | `0x2A3D00` | 530 | UnwindData |  |
