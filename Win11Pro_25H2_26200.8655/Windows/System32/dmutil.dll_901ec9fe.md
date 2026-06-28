# Binary Specification: dmutil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dmutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `901ec9fe17e8f24442f5b06d74e70b63c313253f71f5956bcb3a381aa6be4f74`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllMain` | `0x1C70` | 143 | UnwindData |  |
| 5 | `DisplayError` | `0x1D10` | 151 | UnwindData |  |
| 6 | `DisplayErrorRgszw` | `0x1DB0` | 298 | UnwindData |  |
| 13 | `GetErrorData` | `0x1EE0` | 292 | UnwindData |  |
| 30 | `TranslateError` | `0x2010` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `FTrace` | `0x22E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `FTraceValist` | `0x2300` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `ShowMessage` | `0x2420` | 58 | UnwindData |  |
| 27 | `ShowMessageValist` | `0x2460` | 858 | UnwindData |  |
| 2 | `GetSystemVolume` | `0x27F0` | 271 | UnwindData |  |
| 3 | `AddEntryBootFileGpt` | `0x2A20` | 963 | UnwindData |  |
| 4 | `AddEntryBootFileMbr` | `0x2DF0` | 759 | UnwindData |  |
| 8 | `DmCommonNtOpenFile` | `0x30F0` | 233 | UnwindData |  |
| 12 | `FreeRgszw` | `0x31E0` | 127 | UnwindData |  |
| 14 | `GetInstallDirectoryPath` | `0x3270` | 393 | UnwindData |  |
| 16 | `LowAcquirePrivilege` | `0x3400` | 45 | UnwindData |  |
| 17 | `LowGetPartitionInfo` | `0x3440` | 139 | UnwindData |  |
| 18 | `LowNtAddBootEntry` | `0x34E0` | 1,487 | UnwindData |  |
| 19 | `LowNtReadFile` | `0x3AC0` | 128 | UnwindData |  |
| 20 | `LowNtReadOnlyAttributeOff` | `0x3B50` | 162 | UnwindData |  |
| 21 | `LowNtWriteFile` | `0x3C00` | 107 | UnwindData |  |
| 22 | `RgszwDupRgszw` | `0x3C80` | 430 | UnwindData |  |
| 23 | `RgszwFromArgs` | `0x3E40` | 30 | UnwindData |  |
| 24 | `RgszwFromValist` | `0x3E70` | 1,335 | UnwindData |  |
| 25 | `SafeLoadVdsService` | `0x43B0` | 120 | UnwindData |  |
| 28 | `SzwDupSzw` | `0x4430` | 166 | UnwindData |  |
| 29 | `SzwFromSza` | `0x44E0` | 156 | UnwindData |  |
| 1 | `CoDisableDynamicVolumes` | `0x4590` | 156 | UnwindData |  |
| 9 | `DynamicSupport` | `0x4640` | 257 | UnwindData |  |
| 15 | `IsPersonalSKU` | `0x4750` | 204 | UnwindData |  |
