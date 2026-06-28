# Binary Specification: UserDataTypeHelperUtil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\UserDataTypeHelperUtil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f4f76a84545c2cdb41c2538f1faf4076b434a57fb8a799d376bc0134909bb7cd`
* **Total Exported Functions:** 47

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `DuplicateCEPROPVALArrayNoAlloc` | `0x1010` | 85 | UnwindData |  |
| 18 | `DuplicateCEPROPVALArray` | `0x1240` | 769 | UnwindData |  |
| 8 | `CopyPropValue` | `0x1550` | 52 | UnwindData |  |
| 26 | `GetPropMemSize` | `0x1880` | 135 | UnwindData |  |
| 38 | `SafeStrDup` | `0x19F0` | 262 | UnwindData |  |
| 14 | `DupString` | `0x1B00` | 97 | UnwindData |  |
| 37 | `SafeLPWSTR` | `0x1CC0` | 69 | UnwindData |  |
| 36 | `ReplaceChar` | `0x1D10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ComparePropVals` | `0x1D50` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DupStringA` | `0x1FB0` | 125 | UnwindData |  |
| 46 | `UsOidToContactUdmId` | `0x2100` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CompressWhitespaceNW` | `0x21C0` | 101 | UnwindData |  |
| 30 | `MapiIdToEmailUdmId` | `0x22F0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `BytesToDigits` | `0x2460` | 207 | UnwindData |  |
| 25 | `FormatPoomIdToString` | `0x2540` | 141 | UnwindData |  |
| 5 | `ConvertUnicodeToUtf8` | `0x2650` | 532 | UnwindData |  |
| 32 | `ParsePoomIdFromString` | `0x2A00` | 92 | UnwindData |  |
| 40 | `StreamCopyTo` | `0x2A70` | 418 | UnwindData |  |
| 45 | `UsOidToCalendarUdmId` | `0x2C20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `EcUidToGlobalObjId` | `0x2C70` | 910 | UnwindData |  |
| 27 | `GetStreamSize` | `0x3010` | 316 | UnwindData |  |
| 11 | `CreateWrapFileNameStm` | `0x3160` | 213 | UnwindData |  |
| 16 | `DupStringNA` | `0x32A0` | 269 | UnwindData |  |
| 1 | `GetFilePathFromStream` | `0x4820` | 103 | UnwindData |  |
| 10 | `CreateTempFileStm` | `0x5350` | 139 | UnwindData |  |
| 12 | `CreateWrapFileStm` | `0x53F0` | 216 | UnwindData |  |
| 13 | `CreateWrapFileStreamFromDssToken` | `0x54D0` | 250 | UnwindData |  |
| 17 | `DupStringRes` | `0x5E00` | 151 | UnwindData |  |
| 35 | `RemoveLeadingAndTrailingSpace` | `0x5EA0` | 320 | UnwindData |  |
| 39 | `SplitString` | `0x5FF0` | 313 | UnwindData |  |
| 42 | `StringToBytes` | `0x6130` | 143 | UnwindData |  |
| 24 | `FindProp` | `0x6200` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ConvertUnicodeToUtf8Sz` | `0x6500` | 399 | UnwindData |  |
| 7 | `ConvertUtf8ToUnicode` | `0x66A0` | 507 | UnwindData |  |
| 22 | `EscapeURL` | `0x68B0` | 205 | UnwindData |  |
| 31 | `ParseDelimitedString` | `0x6990` | 356 | UnwindData |  |
| 9 | `CopyStream` | `0x6B80` | 234 | UnwindData |  |
| 33 | `ReadStreamContent` | `0x6C70` | 336 | UnwindData |  |
| 34 | `ReadStreamContentA` | `0x6DD0` | 305 | UnwindData |  |
| 41 | `StreamFromStringW` | `0x6F10` | 267 | UnwindData |  |
| 20 | `EcGlobalObjIdToUid` | `0x70B0` | 944 | UnwindData |  |
| 23 | `FileTimeToISO8601String` | `0x7CD0` | 197 | UnwindData |  |
| 28 | `ISO8601StringToFileTime` | `0x7DA0` | 202 | UnwindData |  |
| 29 | `ISO8601StringToSystemTime` | `0x7E70` | 432 | UnwindData |  |
| 43 | `SystemTimeToISO8601String` | `0x8030` | 388 | UnwindData |  |
| 47 | `UsOidToTaskUdmId` | `0x81C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `TrimWhiteSpaces` | `0x8240` | 214 | UnwindData |  |
