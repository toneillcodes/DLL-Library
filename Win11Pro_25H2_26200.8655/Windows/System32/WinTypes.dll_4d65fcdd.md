# Binary Specification: WinTypes.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WinTypes.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4d65fcdd7e0900af2cccad722a866295da6723825979c317b97f6c387880e575`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `RoCreatePropertySetSerializer` | `0x42B0` | 317 | UnwindData |  |
| 10 | `RoParseTypeName` | `0x21A80` | 93 | UnwindData |  |
| 9 | `RoIsApiContractPresent` | `0x23000` | 65 | UnwindData |  |
| 8 | `RoIsApiContractMajorVersionPresent` | `0x23400` | 68 | UnwindData |  |
| 7 | `RoGetMetaDataFile` | `0x252B0` | 666 | UnwindData |  |
| 11 | `RoResolveNamespace` | `0x26F80` | 884 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x30F50` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x313B0` | 670 | UnwindData |  |
| 6 | `RoGetBufferMarshaler` | `0x38BA0` | 154 | UnwindData |  |
| 4 | `RoCreateNonAgilePropertySet` | `0x3B6A0` | 167 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x3EB20` | 403,704 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
