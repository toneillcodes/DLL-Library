# Binary Specification: mxdwdrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\spool\drivers\W32X86\3\mxdwdrv.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `dffa3ffc5060910175f38ab652cdaf8b7fbfb85f3e194ce218f83e737aecf699`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x13D00` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DrvQueryDriverInfo` | `0x14160` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DrvDisableDriver` | `0x14360` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DrvEnableDriver` | `0x144B0` | 1,023,848 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
