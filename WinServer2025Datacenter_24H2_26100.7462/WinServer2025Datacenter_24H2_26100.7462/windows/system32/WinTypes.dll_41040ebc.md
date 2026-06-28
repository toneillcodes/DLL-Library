# Binary Specification: WinTypes.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WinTypes.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `41040ebcabee189fb7e92ae30374c2a6441570f4cbe93a3814bf7d568494c6de`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `RoCreatePropertySetSerializer` | `0x42B0` | 317 | UnwindData |  |
| 10 | `RoParseTypeName` | `0x21A60` | 93 | UnwindData |  |
| 9 | `RoIsApiContractPresent` | `0x22FE0` | 65 | UnwindData |  |
| 8 | `RoIsApiContractMajorVersionPresent` | `0x233E0` | 68 | UnwindData |  |
| 7 | `RoGetMetaDataFile` | `0x25290` | 666 | UnwindData |  |
| 11 | `RoResolveNamespace` | `0x26F60` | 884 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x30F30` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x31390` | 670 | UnwindData |  |
| 6 | `RoGetBufferMarshaler` | `0x38B80` | 154 | UnwindData |  |
| 4 | `RoCreateNonAgilePropertySet` | `0x3B670` | 167 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x3EAF0` | 403,496 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
